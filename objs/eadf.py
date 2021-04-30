

class EADF():
	"""docstring for ClassName"""
	def __init__(self, draw_tools, master_dict, controller, op_type):
		self.name = "EADF"
		self.tag = "eadf"
		self.menu_label = "EADF_Menu"
		self.draw_tools = draw_tools
		self.dict = master_dict		
		self.controller = controller
		self.side = None
		self.op_type = op_type

		# check if master dictionary has values
		# if not populate the dictionary
		self.checkMasterDict()		

		self.point_size = None

		self.draw_labels = True
		self.draw_hover = True

		
	def checkMasterDict(self):
		if "EADF" not in self.dict.keys():
			self.dict["EADF"] = 	{
									"PRE-OP":{
											"LEFT":	{
														"EADF_LINE":	{"type":"line","P1":None,"P2":None}
													},
											"RIGHT":{
														"EADF_LINE":	{"type":"line","P1":None,"P2":None}
													}
											},

									"POST-OP":{
											"LEFT":	{
														"EADF_LINE":	{"type":"line","P1":None,"P2":None}
													},
											"RIGHT":{
														"EADF_LINE":	{"type":"line","P1":None,"P2":None}
													}
											}
									}

	def click(self, event):
		print("click from "+self.name)

		if self.side == None:
			print("please choose side")
			self.controller.warningBox("Please select a Side")
		else:
			# print(self.dict)			
			ret =  self.addDict(event)
			if ret:
				self.controller.save_json()
				# pass


		self.controller.updateMenuLabel(self.getNextLabel(), self.menu_label)		
		self.draw()



	def getNextLabel(self):	
		if self.side != None:
			for item in self.dict["EADF"][self.op_type][self.side]:
				
				# get item type 
				item_type = self.dict["EADF"][self.op_type][self.side][item]["type"]

				# line has P1 and P2
				if item_type == "line":

					# check if P1 is None				
					if self.dict["EADF"][self.op_type][self.side][item]["P1"] == None:
						return (self.side + " " + item + " P1")


					# check if P2 is None				
					if self.dict["EADF"][self.op_type][self.side][item]["P2"] == None:
						return (self.side + " " + item + " P2")

				return (self.side + " Done")
		return None

	def draw(self):

		self.draw_tools.clear_by_tag(self.tag)

		self.point_size = self.controller.getViewPointSize()

		# loop left and right
		for side in ["LEFT","RIGHT"]:

			isHip 	= False
			isKnee 	= False
			isMNSA 	= False
			isEADF 	= False

			hip 		= self.dict["MAIN"][self.op_type][side]["HIP"]["P1"]
			fem_knee 	= self.dict["MAIN"][self.op_type][side]["FEM_KNEE"]["P1"]

			mnsa_p1		= self.dict["MAIN"][self.op_type][side]["NECK_AXIS"]["P1"]
			mnsa_p2		= self.dict["MAIN"][self.op_type][side]["NECK_AXIS"]["P2"]
			mnsa_m1		= self.dict["MAIN"][self.op_type][side]["NECK_AXIS"]["M1"]

			eadf_p1 = self.dict["EADF"][self.op_type][side]["EADF_LINE"]["P1"]
			eadf_p2 = self.dict["EADF"][self.op_type][side]["EADF_LINE"]["P2"]


			# hip knee line			
			if hip != None:
				isHip = True
				self.draw_tools.create_mypoint(hip, "orange", [self.tag, side, "NO-DRAG"], point_thickness=self.point_size)			
			if fem_knee != None:
				isKnee = True
				self.draw_tools.create_mypoint(fem_knee, "orange", [self.tag, side, "NO-DRAG"], point_thickness=self.point_size)			
			if isHip and isKnee:
				self.draw_tools.create_myline(hip, fem_knee, self.tag)


			# MNSA
			if mnsa_p1 != None:
				self.draw_tools.create_mypoint(mnsa_p1, "orange", [self.tag, side, "NO-DRAG"], point_thickness=self.point_size)
			if mnsa_p2 != None:
				self.draw_tools.create_mypoint(mnsa_p2, "orange", [self.tag, side, "NO-DRAG"], point_thickness=self.point_size)
			if mnsa_p1 != None and mnsa_p2 != None:
				self.draw_tools.create_midpoint_line(mnsa_p1, mnsa_p2, mnsa_m1, [self.tag,side,"NO-DRAG"], point_thickness=self.point_size)
				isMNSA = True


			# EADF LINE
			if eadf_p1 != None:
				self.draw_tools.create_mypoint(eadf_p1, "orange", [self.tag, side, "EADF_P1"], point_thickness=self.point_size)
			if eadf_p2 != None:
				self.draw_tools.create_mypoint(eadf_p2, "orange", [self.tag, side, "EADF_P2"], point_thickness=self.point_size)
			if eadf_p1 != None and eadf_p2 != None:
				self.draw_tools.create_myline(eadf_p1, eadf_p2, [self.tag,side,"EADF_LINE"])
				isEADF = True
			if eadf_p1 != None and isKnee:
				self.draw_tools.create_myline(eadf_p1, fem_knee, [self.tag,side,"EADF_LINE"])


			# draw EADFA angle
			if isEADF and isKnee:
				eadf_top, eadf_bot = self.draw_tools.retPointsUpDown(eadf_p1, eadf_p2)
				if side == "LEFT":						
					angle = self.draw_tools.create_myAngle(fem_knee, eadf_bot, eadf_top, [self.tag,"EADF_LINE"])
				else:					
					angle = self.draw_tools.create_myAngle(eadf_top, eadf_bot, fem_knee, [self.tag,"EADF_LINE"])

				if self.draw_labels:
					self.draw_tools.create_mytext(eadf_p1, '{0:.1f}'.format(angle), self.tag, x_offset=60, color="blue")

				if self.dict["EXCEL"][self.op_type][side]["EADFA"] == None:
					self.dict["EXCEL"][self.op_type][side]["HASDATA"] 	= True
					self.dict["EXCEL"][self.op_type][side]["EADFA"]	 	= '{0:.1f}'.format(angle)
					self.controller.save_json()


			# draw neck hip ray intersecting eadf line
			if isEADF and isMNSA and isHip:

				xtop, ytop, xbot, ybot = self.draw_tools.getImageCorners()

				if side == "RIGHT":
					p_right = self.draw_tools.line_intersection(
						(mnsa_m1, hip),
						(xtop, xbot))
					self.draw_tools.create_myline(hip, p_right, [self.tag,side,"MNSA_ANGLE"])

					# find angle ray intersection point
					p_int = self.draw_tools.line_intersection(
							(hip, p_right),
							(eadf_p1, eadf_p2))
					self.draw_tools.create_mypoint(p_int, "orange", [self.tag, side, "NO-DRAG"], point_thickness=self.point_size)




				if side == "LEFT":
					p_left = self.draw_tools.line_intersection(
						(mnsa_m1, hip),
						(ytop, ybot))
					self.draw_tools.create_myline(hip, p_left, [self.tag,side,"MNSA_ANGLE"])

					# find angle ray intersection point
					p_int = self.draw_tools.line_intersection(
							(hip, p_left),
							(eadf_p1, eadf_p2))
					self.draw_tools.create_mypoint(p_int, "orange", [self.tag, side, "NO-DRAG"], point_thickness=self.point_size)


				d_fps = self.draw_tools.getDistance(p_int, eadf_p1)
				d_fds = self.draw_tools.getDistance(eadf_p1, fem_knee)

				if self.dict["EXCEL"][self.op_type][side]["EADFPS"] == None:
					self.dict["EXCEL"][self.op_type][side]["HASDATA"] 	= True
					self.dict["EXCEL"][self.op_type][side]["EADFPS"]	= '{0:.1f}'.format(d_fps)
					self.controller.save_json()

				if self.dict["EXCEL"][self.op_type][side]["EADFDS"] == None:
					self.dict["EXCEL"][self.op_type][side]["HASDATA"] 	= True
					self.dict["EXCEL"][self.op_type][side]["EADFDS"]	= '{0:.1f}'.format(d_fds)
					self.controller.save_json()





	def mainHoverUsingNextLabel(self):
		label = self.getNextLabel()

		if label == "RIGHT EADF_LINE P1":
			self.side = "RIGHT"
			self.hover_text = "EADF_P1"
			self.draw_tools.setHoverPointLabel("P0_EADF_LINE")
			self.draw_tools.setHoverPoint(None)
			self.draw_tools.setHoverBool(True)	

		if label == "LEFT EADF_LINE P1":
			self.side = "LEFT"
			self.hover_text = "EADF_P1"
			self.draw_tools.setHoverPointLabel("P0_EADF_LINE")
			self.draw_tools.setHoverPoint(None)
			self.draw_tools.setHoverBool(True)	



	def addDict(self, event):
		for item in self.dict["EADF"][self.op_type][self.side]:

			# get real coords
			P = self.draw_tools.getRealCoords(event)
			
			# get item type 
			item_type = self.dict["EADF"][self.op_type][self.side][item]["type"]

			# line has P1 and P2
			if item_type == "line":

				# check if P1 is None				
				if self.dict["EADF"][self.op_type][self.side][item]["P1"] == None:
					
					self.dict["EADF"][self.op_type][self.side][item]["P1"] = P
					self.draw_tools.setHoverPointLabel("P1_EADF")
					self.draw_tools.setHoverPoint(P)
					self.draw_tools.setHoverBool(True)
					return True


				# check if P2 is None				
				if self.dict["EADF"][self.op_type][self.side][item]["P2"] == None:					
					self.dict["EADF"][self.op_type][self.side][item]["P2"] = P
					self.draw_tools.setHoverBool(False)
					self.draw_tools.setHoverPointLabel(None)
					return True

		return False


	# menu button clicks are routed here
	def menu_btn_click(self, action):
		print(action)
		if action == "SET-LEFT":
			self.side = "LEFT"
			self.controller.updateMenuLabel(self.getNextLabel(), self.menu_label)
			self.draw()
			self.regainHover(self.side)
			return

		if action == "SET-RIGHT":
			self.side = "RIGHT"
			self.controller.updateMenuLabel(self.getNextLabel(), self.menu_label)
			self.draw()
			self.regainHover(self.side)
			return

		if action == "DEL-LEFT-EADF-LINE":
			self.dict["EADF"][self.op_type]["LEFT"]["EADF_LINE"]["P1"] = None
			self.dict["EADF"][self.op_type]["LEFT"]["EADF_LINE"]["P2"] = None
			self.side = "LEFT"
			

		if action == "DEL-RIGHT-EADF-LINE":
			self.dict["EADF"][self.op_type]["RIGHT"]["EADF_LINE"]["P1"] = None
			self.dict["EADF"][self.op_type]["RIGHT"]["EADF_LINE"]["P2"] = None
			self.side = "RIGHT"
			

		# delete excel data from pat.json
		self.dict["EXCEL"][self.op_type][self.side]["EADFA"] = None
		self.dict["EXCEL"][self.op_type][self.side]["EADFPS"] = None
		self.dict["EXCEL"][self.op_type][self.side]["EADFDS"] = None

		self.draw()
		self.regainHover(self.side)
		self.controller.save_json()
		self.controller.updateMenuLabel(self.getNextLabel(), self.menu_label)


	def drag_start(self, tags):
		tags.remove('token')
		tags.remove('current')
		tags.remove(self.tag)
		print(tags)
		
		side = ""

		# find side
		if "LEFT" in tags:
			side = "LEFT"
		elif "RIGHT" in tags:
			side = "RIGHT"


		# find item type
		if "EADF_P1" in tags:			
			self.drag_point = None
			self.drag_label = "EADF_P1"
			self.drag_side 	= side	

		if "EADF_P2" in tags:			
			self.drag_point = None
			self.drag_label = "EADF_P2"
			self.drag_side 	= side	

	def drag(self, P_mouse):
		if self.drag_label == "EADF_P1":
			self.draw_tools.clear_by_tag("drag_line")
			self.draw_tools.clear_by_tag("EADF_LINE")

			fem_knee 	= self.dict["MAIN"][self.op_type][self.drag_side]["FEM_KNEE"]["P1"]
			eadf_p2 	= self.dict["EADF"][self.op_type][self.drag_side]["EADF_LINE"]["P2"]
			if fem_knee != None:
				self.draw_tools.create_myline(P_mouse, fem_knee, "drag_line")

			if eadf_p2 != None:
				self.draw_tools.create_myline(P_mouse, eadf_p2, "drag_line")

		if self.drag_label == "EADF_P2":
			self.draw_tools.clear_by_tag("drag_line")
			self.draw_tools.clear_by_tag("EADF_LINE")
			eadf_p1 = self.dict["EADF"][self.op_type][self.drag_side]["EADF_LINE"]["P1"]

			if eadf_p1 != None:
				self.draw_tools.create_myline(P_mouse, eadf_p1, "drag_line")

	def drag_stop(self, P_mouse):
		self.draw_tools.clear_by_tag("drag_line")
		if self.drag_label == "EADF_P1":
			self.dict["EADF"][self.op_type][self.drag_side]["EADF_LINE"]["P1"] = P_mouse
			
			self.dict["EXCEL"][self.op_type][self.drag_side]["EADFA"] = None
			self.dict["EXCEL"][self.op_type][self.drag_side]["EADFPS"] = None
			self.dict["EXCEL"][self.op_type][self.drag_side]["EADFDS"] = None
			self.controller.save_json()
			self.draw()

		if self.drag_label == "EADF_P2":
			self.dict["EADF"][self.op_type][self.drag_side]["EADF_LINE"]["P2"] = P_mouse

			self.dict["EXCEL"][self.op_type][self.drag_side]["EADFA"] = None
			self.dict["EXCEL"][self.op_type][self.drag_side]["EADFPS"] = None
			self.dict["EXCEL"][self.op_type][self.drag_side]["EADFDS"] = None
			self.controller.save_json()
			self.draw()
		

	def hover(self, P_mouse, P_stored, hover_label):

		# prevent auto curObject set bug
		if self.side == None:
			return

		if self.draw_hover:
			side_pre = self.side[0]+"_"
			if	hover_label == "P0_EADF_LINE":
				self.draw_tools.clear_by_tag("hover_line")
				self.draw_tools.create_mypoint(P_mouse, "red", [self.tag, "hover_line"], hover_point=True, point_thickness=self.point_size)

				# joing P_mouse to fem_knee
				fem_knee = self.dict["MAIN"][self.op_type][self.side]["FEM_KNEE"]["P1"]
				if fem_knee != None:
					self.draw_tools.create_myline(P_mouse, fem_knee, "hover_line")

				if self.draw_labels:
					self.draw_tools.create_mytext(P_mouse,x_offset=80, mytext=(side_pre+self.hover_text), mytag=[self.tag, "hover_line"])


		if hover_label == "P1_EADF":
			self.draw_tools.clear_by_tag("hover_line")
			self.draw_tools.create_myline(P_mouse, P_stored, "hover_line")

	def regainHover(self, side):
		eadf_p1 = self.dict["EADF"][self.op_type][side]["EADF_LINE"]["P1"]
		eadf_p2 = self.dict["EADF"][self.op_type][side]["EADF_LINE"]["P2"]

		# find if P0 hovers are required
		self.mainHoverUsingNextLabel()

		if eadf_p2 == None and eadf_p1 != None:
			self.draw_tools.setHoverPointLabel("P1_EADF")
			self.draw_tools.setHoverPoint(eadf_p1)
			self.draw_tools.setHoverBool(True)

	def escapeObjFunc(self):
		self.side = None
		self.draw_tools.setHoverPointLabel(None)
		self.draw_tools.setHoverBool(False)


	def checkbox_click(self,action, val):

		print('checkbox {} val{}'.format(action,val.get()))		

		if action == "TOGGLE_LABEL":
			if val.get() == 0:
				self.draw_labels = False
			elif val.get() == 1:
				self.draw_labels = True
			self.draw()

		if action == "TOGGLE_HOVER":
			if val.get() == 0:
				self.draw_hover = False
			elif val.get() == 1:
				self.draw_hover = True
			self.draw()


	def update_canvas(self, draw_tools):
		self.draw_tools = draw_tools

	def update_dict(self, master_dict):
		self.dict = master_dict

	def unset(self):
		# print("unset from "+self.name)
		self.draw_tools.clear_by_tag(self.tag)
		self.side = None

	# similiar to draw but nothing is drawn on the canvas
	def updateExcelValues(self):
		pass
						