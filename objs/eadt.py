

class EADT():
	"""docstring for ClassName"""
	def __init__(self, draw_tools, master_dict, controller, op_type):
		self.name = "EADT"
		self.tag = "eadt"
		self.menu_label = "EADT_Menu"
		self.draw_tools = draw_tools
		self.dict = master_dict		
		self.controller = controller
		self.side = None
		self.op_type = op_type

		# check if master dictionary has values
		# if not populate the dictionary
		self.checkMasterDict()		

		self.drag_label = None

		self.point_size = None
		self.draw_labels = True
		self.draw_hover = True

		
	def checkMasterDict(self):
		if "EADT" not in self.dict.keys():
			self.dict["EADT"] = 	{
									"PRE-OP":{
											"LEFT":	{
														"EADT_P1":	{"type":"point", "P1":None}
													},
											"RIGHT":{
														"EADT_P1":	{"type":"point", "P1":None}
													}
											},

									"POST-OP":{
											"LEFT":	{
														"EADT_P1":	{"type":"point", "P1":None}
													},
											"RIGHT":{
														"EADT_P1":	{"type":"point", "P1":None}
													}
											},
									}

	def click(self, event):
		print("click from "+self.name)

		if self.side == None:
			print("please choose side")
			self.controller.warningBox("Please select a Side")
		else:
			# print(self.dict)			
			ret =  self.addDict(event)
			# find if P0 hovers are required
			self.mainHoverUsingNextLabel()
			if ret:
				self.controller.save_json()
				# pass


		self.controller.updateMenuLabel(self.getNextLabel(), self.menu_label)		
		self.draw()


	def right_click(self, event):
		pass

	def keyRightObjFunc(self):
		print('set right')
		self.side = "RIGHT"
		self.controller.updateMenuLabel(self.getNextLabel(), self.menu_label)
		self.draw()
		self.regainHover(self.side)

	def keyLeftObjFunc(self):
		print('set left')
		self.side = "LEFT"
		self.controller.updateMenuLabel(self.getNextLabel(), self.menu_label)
		self.draw()
		self.regainHover(self.side)


	def getNextLabel(self):	
		if self.side != None:
			for item in self.dict["EADT"][self.op_type][self.side]:
				
				# get item type 
				item_type = self.dict["EADT"][self.op_type][self.side][item]["type"]

				# point has P1
				if item_type == "point":

					# check if P1 is None				
					if self.dict["EADT"][self.op_type][self.side][item]["P1"] == None:
						return (self.side + " " + item)					

				return (self.side + " Done")
		return None

	def draw(self):

		self.draw_tools.clear_by_tag(self.tag)

		self.point_size = self.controller.getViewPointSize()

		# loop left and right
		for side in ["LEFT","RIGHT"]:

			isKnee 	= False
			isAnkle = False
			isEADT 	= False

			tib_knee 	= self.dict["MAIN"][self.op_type][side]["TIB_KNEE"]["P1"]
			ankle_m1 	= self.dict["MAIN"][self.op_type][side]["ANKLE"]["M1"]
			eadt_p1 	= self.dict["EADT"][self.op_type][side]["EADT_P1"]["P1"]


			
			if tib_knee != None:
				isKnee = True
				self.draw_tools.create_mypoint(tib_knee, "orange", [self.tag, side, "NO-DRAG"], point_thickness=self.point_size)

			if ankle_m1 != None:
				isAnkle = True
				self.draw_tools.create_mypoint(ankle_m1, "orange", [self.tag, side, "NO-DRAG"], point_thickness=self.point_size)
		
			# EADT POINT
			if eadt_p1 != None:
				self.draw_tools.create_mypoint(eadt_p1, "orange", [self.tag, side, "EADT_P1"], point_thickness=self.point_size)			
				isEADT = True


			if isAnkle and isKnee and isEADT==False:
				self.draw_tools.create_myline(ankle_m1, tib_knee, self.tag)

			if isEADT and isAnkle and isKnee:
				self.draw_tools.create_myline(eadt_p1, tib_knee, [self.tag,side,"EADT_LINE"])
				self.draw_tools.create_myline(eadt_p1, ankle_m1, [self.tag,side,"EADT_LINE"])

				if side == "LEFT":						
					angle = self.draw_tools.create_myAngle(ankle_m1, eadt_p1, tib_knee, [self.tag,"EADT_LINE"])
				else:
					angle = self.draw_tools.create_myAngle(tib_knee, eadt_p1, ankle_m1, [self.tag,"EADT_LINE"])

				if self.draw_labels:
					self.draw_tools.create_mytext(eadt_p1, '{0:.1f}'.format(angle), self.tag, x_offset=60, color="blue")
			


				if self.dict["EXCEL"][self.op_type][side]["EADTA"] == None:
					self.dict["EXCEL"][self.op_type][side]["HASDATA"] 	= True
					self.dict["EXCEL"][self.op_type][side]["EADTA"]	 	= '{0:.1f}'.format(angle)
					self.controller.save_json()

				d_tps = self.draw_tools.getDistance(eadt_p1, tib_knee)
				d_tds = self.draw_tools.getDistance(eadt_p1, ankle_m1)

				if self.dict["EXCEL"][self.op_type][side]["EADTPS"] == None:
					self.dict["EXCEL"][self.op_type][side]["HASDATA"] 	= True
					self.dict["EXCEL"][self.op_type][side]["EADTPS"]	= '{0:.1f}'.format(d_tps)
					self.controller.save_json()

				if self.dict["EXCEL"][self.op_type][side]["EADTDS"] == None:
					self.dict["EXCEL"][self.op_type][side]["HASDATA"] 	= True
					self.dict["EXCEL"][self.op_type][side]["EADTDS"]	= '{0:.1f}'.format(d_tds)
					self.controller.save_json()




	def mainHoverUsingNextLabel(self):
		label = self.getNextLabel()

		if label == "RIGHT EADT_P1":
			self.side = "RIGHT"
			self.hover_text = "EADT_P1"
			self.draw_tools.setHoverPointLabel("P0_EADT_P1")
			self.draw_tools.setHoverPoint(None)
			self.draw_tools.setHoverBool(True)	

		if label == "LEFT EADT_P1":
			self.side = "LEFT"
			self.hover_text = "EADT_P1"
			self.draw_tools.setHoverPointLabel("P0_EADT_P1")
			self.draw_tools.setHoverPoint(None)
			self.draw_tools.setHoverBool(True)	



	def addDict(self, event):

		for item in self.dict["EADT"][self.op_type][self.side]:

			# get real coords
			P = self.draw_tools.getRealCoords(event)
			
			# get item type 
			item_type = self.dict["EADT"][self.op_type][self.side][item]["type"]

			# line has P1 and P2
			if item_type == "point":

				# check if P1 is None				
				if self.dict["EADT"][self.op_type][self.side][item]["P1"] == None:
					
					self.dict["EADT"][self.op_type][self.side][item]["P1"] = P
					self.draw_tools.setHoverBool(False)
					self.draw_tools.setHoverPointLabel(None)
					return True				

		return False


	# menu button clicks are routed here
	def menu_btn_click(self, action):
		print(action)		
		if action == "SET-LEFT":
			self.side = "LEFT"			
			self.draw()
			self.regainHover(self.side)
			self.controller.updateMenuLabel(self.getNextLabel(), self.menu_label)
			return

		if action == "SET-RIGHT":
			self.side = "RIGHT"			
			self.draw()
			self.regainHover(self.side)
			self.controller.updateMenuLabel(self.getNextLabel(), self.menu_label)
			return

		if action == "DEL-LEFT-EADT-P1":
			self.dict["EADT"][self.op_type]["LEFT"]["EADT_P1"]["P1"] = None
			self.side = "LEFT"			

		if action == "DEL-RIGHT-EADT-P1":
			self.dict["EADT"][self.op_type]["RIGHT"]["EADT_P1"]["P1"] = None
			self.side = "RIGHT"


		self.dict["EXCEL"][self.op_type][self.side]["EADTA"]	= None
		self.dict["EXCEL"][self.op_type][self.side]["EADTPS"]	= None
		self.dict["EXCEL"][self.op_type][self.side]["EADTDS"]	= None
		self.dict["EXCEL"][self.op_type][self.side]["HASDATA"] 	= False

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
		if "EADT_P1" in tags:			
			self.drag_point = None
			self.drag_label = "EADT_P1"
			self.drag_side 	= side
				
	def drag(self, P_mouse):
		if self.drag_label == "EADT_P1":
			self.draw_tools.clear_by_tag("drag_line")
			self.draw_tools.clear_by_tag("EADT_LINE")

			tib_knee 	= self.dict["MAIN"][self.op_type][self.drag_side]["TIB_KNEE"]["P1"]
			ankle_m1 	= self.dict["MAIN"][self.op_type][self.drag_side]["ANKLE"]["M1"]
			if tib_knee != None and ankle_m1 != None:					
				self.draw_tools.create_myline(P_mouse, tib_knee, "drag_line")
				self.draw_tools.create_myline(P_mouse, ankle_m1, "drag_line")

	def drag_stop(self, P_mouse):
		self.draw_tools.clear_by_tag("drag_line")
		if self.drag_label == "EADT_P1":
			self.dict["EADT"][self.op_type][self.drag_side]["EADT_P1"]["P1"] = P_mouse
			
			self.dict["EXCEL"][self.op_type][self.drag_side]["EADTA"]	= None
			self.dict["EXCEL"][self.op_type][self.drag_side]["EADTPS"]	= None
			self.dict["EXCEL"][self.op_type][self.drag_side]["EADTDS"]	= None
			self.controller.save_json()
			self.draw()

	def hover(self, P_mouse, P_stored, hover_label):
		

		# prevent auto curObject set bug
		if self.side == None:
			return

		if self.draw_hover:
			side_pre = self.side[0]+"_"
			if	hover_label == "P0_EADT_P1":
				self.draw_tools.clear_by_tag("hover_line")
				self.draw_tools.create_mypoint(P_mouse, "red", [self.tag, "hover_line"], hover_point=True, point_thickness=self.point_size)

				# joing P_mouse to fem_knee
				tib_knee 	= self.dict["MAIN"][self.op_type][self.side]["TIB_KNEE"]["P1"]
				ankle_m1 	= self.dict["MAIN"][self.op_type][self.side]["ANKLE"]["M1"]
				if tib_knee != None and ankle_m1 != None:					
					self.draw_tools.create_myline(P_mouse, tib_knee, "hover_line")
					self.draw_tools.create_myline(P_mouse, ankle_m1, "hover_line")

				if self.draw_labels:
					self.draw_tools.create_mytext(P_mouse,x_offset=80, mytext=(side_pre+self.hover_text), mytag=[self.tag, "hover_line"])


		# if hover_label == "P1_EADF":
		# 	self.draw_tools.clear_by_tag("hover_line")
		# 	self.draw_tools.create_myline(P_mouse, P_stored, "hover_line")

	def regainHover(self, side):
		
		# eadf_p1 = self.dict["EADF"][self.op_type][side]["EADF_LINE"]["P1"]
		# eadf_p2 = self.dict["EADF"][self.op_type][side]["EADF_LINE"]["P2"]

		# find if P0 hovers are required
		self.mainHoverUsingNextLabel()

		# if eadf_p2 == None and eadf_p1 != None:
		# 	self.draw_tools.setHoverPointLabel("P1_EADF")
		# 	self.draw_tools.setHoverPoint(eadf_p1)
		# 	self.draw_tools.setHoverBool(True)

	def escapeObjFunc(self):
		self.side = None
		self.draw_tools.setHoverPointLabel(None)
		self.draw_tools.setHoverBool(False)
		self.controller.updateMenuLabel("CHOOSE SIDE", self.menu_label)


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
		print('update EADT')


		# loop left and right
		for side in ["LEFT","RIGHT"]:

			isKnee 	= False
			isAnkle = False
			isEADT 	= False

			tib_knee 	= self.dict["MAIN"][self.op_type][side]["TIB_KNEE"]["P1"]
			ankle_m1 	= self.dict["MAIN"][self.op_type][side]["ANKLE"]["M1"]
			eadt_p1 	= self.dict["EADT"][self.op_type][side]["EADT_P1"]["P1"]


			
			if tib_knee != None:
				isKnee = True

			if ankle_m1 != None:
				isAnkle = True
		
			# EADT POINT
			if eadt_p1 != None:
				isEADT = True


			if isEADT and isAnkle and isKnee:

				if side == "LEFT":						
					# angle = self.draw_tools.create_myAngle(ankle_m1, eadt_p1, tib_knee, [self.tag,"EADT_LINE"])
					angle = self.draw_tools.getAnglePoints(ankle_m1, eadt_p1, tib_knee)
				else:
					# angle = self.draw_tools.create_myAngle(tib_knee, eadt_p1, ankle_m1, [self.tag,"EADT_LINE"])
					angle = self.draw_tools.getAnglePoints(tib_knee, eadt_p1, ankle_m1)

				
				if self.dict["EXCEL"][self.op_type][side]["EADTA"] == None:
					self.dict["EXCEL"][self.op_type][side]["HASDATA"] 	= True
					self.dict["EXCEL"][self.op_type][side]["EADTA"]	 	= '{0:.1f}'.format(angle)
					self.controller.save_json()

				d_tps = self.draw_tools.getDistance(eadt_p1, tib_knee)
				d_tds = self.draw_tools.getDistance(eadt_p1, ankle_m1)

				if self.dict["EXCEL"][self.op_type][side]["EADTPS"] == None:
					self.dict["EXCEL"][self.op_type][side]["HASDATA"] 	= True
					self.dict["EXCEL"][self.op_type][side]["EADTPS"]	= '{0:.1f}'.format(d_tps)
					self.controller.save_json()

				if self.dict["EXCEL"][self.op_type][side]["EADTDS"] == None:
					self.dict["EXCEL"][self.op_type][side]["HASDATA"] 	= True
					self.dict["EXCEL"][self.op_type][side]["EADTDS"]	= '{0:.1f}'.format(d_tds)
					self.controller.save_json()
						