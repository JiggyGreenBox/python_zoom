

class ALPHA():
	"""docstring for ClassName"""
	def __init__(self, draw_tools, master_dict, controller, op_type):
		self.name = "ALPHA"
		self.tag = "alpha"
		self.menu_label = "ALPHA_Menu"
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
		self.drag_label = None


	def checkMasterDict(self):
		if "ALPHA" not in self.dict.keys():
			self.dict["ALPHA"] = 	{
									"PRE-OP":{
											"LEFT":	{
														"FEM_JOINT_LINE":	{"type":"line","P1":None,"P2":None}
													},
											"RIGHT":{
														"FEM_JOINT_LINE":	{"type":"line","P1":None,"P2":None}
													}
											},

									"POST-OP":{
											"LEFT":	{
														"FEM_JOINT_LINE":	{"type":"line","P1":None,"P2":None}
													},
											"RIGHT":{
														"FEM_JOINT_LINE":	{"type":"line","P1":None,"P2":None}
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
			# find if P0 hovers are required
			self.mainHoverUsingNextLabel()
			if ret:
				self.controller.save_json()
				# pass


		self.controller.updateMenuLabel(self.getNextLabel(), self.menu_label)
		self.draw()

	def draw(self):

		self.draw_tools.clear_by_tag(self.tag)

		self.point_size = self.controller.getViewPointSize()

		# loop left and right				
		for side in ["LEFT","RIGHT"]:

			isFemJointLine = False
			isFemTop 	= False
			isFemBot 	= False


			fem_line_p1 = self.dict["ALPHA"][self.op_type][side]["FEM_JOINT_LINE"]["P1"]
			fem_line_p2 = self.dict["ALPHA"][self.op_type][side]["FEM_JOINT_LINE"]["P2"]


			axis_fem_top_p1 = self.dict["UNI_FEM_VAL"][self.op_type][side]["AXIS_FEM"]["TOP"]["P1"]
			axis_fem_top_p2 = self.dict["UNI_FEM_VAL"][self.op_type][side]["AXIS_FEM"]["TOP"]["P2"]
			axis_fem_top_m1 = self.dict["UNI_FEM_VAL"][self.op_type][side]["AXIS_FEM"]["TOP"]["M1"]
			
			axis_fem_bot_p1 = self.dict["UNI_FEM_VAL"][self.op_type][side]["AXIS_FEM"]["BOT"]["P1"]
			axis_fem_bot_p2 = self.dict["UNI_FEM_VAL"][self.op_type][side]["AXIS_FEM"]["BOT"]["P2"]
			axis_fem_bot_m1 = self.dict["UNI_FEM_VAL"][self.op_type][side]["AXIS_FEM"]["BOT"]["M1"]

			# FEM JOINT LINE
			if fem_line_p1 != None:
				self.draw_tools.create_mypoint(fem_line_p1, "orange", [self.tag,side,"FEM_JOINT_LINE","P1"], point_thickness=self.point_size)

			if fem_line_p2 != None:
				self.draw_tools.create_mypoint(fem_line_p2, "orange", [self.tag,side,"FEM_JOINT_LINE","P2"], point_thickness=self.point_size)

			if fem_line_p1 != None and fem_line_p2 != None:
				self.draw_tools.create_myline(fem_line_p1, fem_line_p2, [self.tag,side,"FEM_LINE"])
				isFemJointLine = True



			# FEM AXIS
			# TOP
			if axis_fem_top_p1 != None:
				self.draw_tools.create_mypoint(axis_fem_top_p1, "orange", [self.tag,side,"NO-DRAG"], point_thickness=self.point_size)

			if axis_fem_top_p2 != None:
				self.draw_tools.create_mypoint(axis_fem_top_p2, "orange", [self.tag,side,"NO-DRAG"], point_thickness=self.point_size)

			if axis_fem_top_p1 != None and axis_fem_top_p2 != None:				
				self.draw_tools.create_midpoint_line(axis_fem_top_p1, axis_fem_top_p2, axis_fem_top_m1, [self.tag,side,"NO-DRAG"], point_thickness=self.point_size)
				isFemTop = True


			# BOT
			if axis_fem_bot_p1 != None:
				self.draw_tools.create_mypoint(axis_fem_bot_p1, "orange", [self.tag,side,"NO-DRAG"], point_thickness=self.point_size)

			if axis_fem_bot_p2 != None:
				self.draw_tools.create_mypoint(axis_fem_bot_p2, "orange", [self.tag,side,"NO-DRAG"], point_thickness=self.point_size)

			if axis_fem_bot_p1 != None and axis_fem_bot_p2 != None:				
				self.draw_tools.create_midpoint_line(axis_fem_bot_p1, axis_fem_bot_p2, axis_fem_bot_m1, [self.tag,side,"NO-DRAG"], point_thickness=self.point_size)
				isFemBot = True

			# if isFemJointLine and isFemTop and isFemBot:
			if isFemTop and isFemBot:
				# axis
				U_fem_m1, D_fem_m1 = self.draw_tools.retPointsUpDown(axis_fem_top_m1, axis_fem_bot_m1)
				

				xtop, ytop, xbot, ybot = self.draw_tools.getImageCorners()

				# fem axis extension
				p_axis_bot = self.draw_tools.line_intersection((U_fem_m1, D_fem_m1), (xbot, ybot))
				self.draw_tools.create_myline(U_fem_m1, p_axis_bot, self.tag)

				


				if isFemJointLine:

					# find angle ray intersection point
					p_int = self.draw_tools.line_intersection(
							(U_fem_m1, D_fem_m1),
							(fem_line_p1, fem_line_p2))


					L_fem, R_fem = self.draw_tools.retPointsLeftRight(fem_line_p1, fem_line_p2)

					if side == "RIGHT":
						angle = self.draw_tools.create_myAngle(U_fem_m1, p_int, R_fem, [self.tag,side,"ALPHA_ANGLE"])
						if self.draw_labels:
							self.draw_tools.create_mytext(p_int, '{0:.2f}'.format(angle), [self.tag,side,"ALPHA_ANGLE"], x_offset=60, y_offset=-60, color="blue")

					if side == "LEFT":
						angle = self.draw_tools.create_myAngle(L_fem, p_int, U_fem_m1, [self.tag,side,"ALPHA_ANGLE"])
						if self.draw_labels:
							self.draw_tools.create_mytext(p_int, '{0:.2f}'.format(angle), [self.tag,side,"ALPHA_ANGLE"], x_offset=-60, y_offset=-60, color="blue")


	def addDict(self, event):
		for item in self.dict["ALPHA"][self.op_type][self.side]:

			# get real coords
			P = self.draw_tools.getRealCoords(event)
			
			# get item type 
			item_type = self.dict["ALPHA"][self.op_type][self.side][item]["type"]

			# line has P1 and P2
			if item_type == "line":

				# check if P1 is None				
				if self.dict["ALPHA"][self.op_type][self.side][item]["P1"] == None:
					
					self.dict["ALPHA"][self.op_type][self.side][item]["P1"] = P
					self.draw_tools.setHoverPointLabel("P1_ALPHA")
					self.draw_tools.setHoverPoint(P)
					self.draw_tools.setHoverBool(True)
					return True


				# check if P2 is None				
				if self.dict["ALPHA"][self.op_type][self.side][item]["P2"] == None:					
					self.dict["ALPHA"][self.op_type][self.side][item]["P2"] = P
					self.draw_tools.setHoverBool(False)
					self.draw_tools.setHoverPointLabel(None)
					return True

		return False


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

		# dissallow drag from other objects
		if "NO-DRAG" in tags:
			self.drag_point = None
			self.drag_label = "NO-DRAG"
			self.drag_side 	= None


	
		if "P1" in tags:
			self.drag_point = self.dict["ALPHA"][self.op_type][side]["FEM_JOINT_LINE"]["P2"]
			self.drag_label = "P1_FEM_JOINT_LINE"
			self.drag_side 	= side
		elif "P2" in tags:
			self.drag_point = self.dict["ALPHA"][self.op_type][side]["FEM_JOINT_LINE"]["P1"]
			self.drag_label = "P2_FEM_JOINT_LINE"
			self.drag_side 	= side		

	def drag(self, P_mouse):
		if self.drag_label == "P1_FEM_JOINT_LINE" and self.drag_point != None or self.drag_label == "P2_FEM_JOINT_LINE" and self.drag_point != None:
			self.draw_tools.clear_by_tag("FEM_LINE")
			self.draw_tools.clear_by_tag("ALPHA_ANGLE")
			self.draw_tools.clear_by_tag("drag_line")
			self.draw_tools.create_myline(P_mouse, self.drag_point, "drag_line")

	def drag_stop(self, P_mouse):
		self.draw_tools.clear_by_tag("drag_line")

		if self.drag_label == "P1_FEM_JOINT_LINE":
			self.dict["ALPHA"][self.op_type][self.drag_side]["FEM_JOINT_LINE"]["P1"] = P_mouse

		elif self.drag_label == "P2_FEM_JOINT_LINE":
			self.dict["ALPHA"][self.op_type][self.drag_side]["FEM_JOINT_LINE"]["P2"] = P_mouse

		self.controller.save_json()
		self.draw()		

	def hover(self, P_mouse, P_stored, hover_label):

		# prevent auto curObject set bug
		if self.side == None:
			return

		if self.draw_hover:
			side_pre = self.side[0]+"_"
			if hover_label == "P0_FEM_JOINT_LINE":
				self.draw_tools.clear_by_tag("hover_line")
				self.draw_tools.create_mypoint(P_mouse, "red", [self.tag, "hover_line"], hover_point=True, point_thickness=self.point_size)
				if self.draw_labels:
					self.draw_tools.create_mytext(P_mouse,x_offset=80, mytext=(side_pre+self.hover_text), mytag=[self.tag, "hover_line"])

		if hover_label == "P1_ALPHA":
			self.draw_tools.clear_by_tag("hover_line")			
			self.draw_tools.create_myline(P_stored, P_mouse, "hover_line")
	
	def escapeObjFunc(self):
		self.side = None
		self.draw_tools.setHoverPointLabel(None)
		self.draw_tools.setHoverBool(False)


	def getNextLabel(self):
		if self.side != None:
			for item in self.dict["ALPHA"][self.op_type][self.side]:
				
				# get item type 
				item_type = self.dict["ALPHA"][self.op_type][self.side][item]["type"]

				# line has P1 and P2
				if item_type == "line":

					# check if P1 is None				
					if self.dict["ALPHA"][self.op_type][self.side][item]["P1"] == None:
						return (self.side + " " + item + " P1")


					# check if P2 is None				
					if self.dict["ALPHA"][self.op_type][self.side][item]["P2"] == None:
						return (self.side + " " + item + " P2")

				return (self.side + " Done")
		return None


	# menu button clicks are routed here
	def menu_btn_click(self, action):
		print(action)
		if action == "SET-LEFT":
			self.side = "LEFT"

		if action == "SET-RIGHT":
			self.side = "RIGHT"

		if action == "DEL-LEFT-FEM-LINE":
			self.side = "LEFT"
			self.dict["ALPHA"][self.op_type]["LEFT"]["FEM_JOINT_LINE"]["P1"] = None
			self.dict["ALPHA"][self.op_type]["LEFT"]["FEM_JOINT_LINE"]["P2"] = None			
			self.controller.save_json()

		if action == "DEL-RIGHT-FEM-LINE":
			self.side = "RIGHT"
			self.dict["ALPHA"][self.op_type]["RIGHT"]["FEM_JOINT_LINE"]["P1"] = None
			self.dict["ALPHA"][self.op_type]["RIGHT"]["FEM_JOINT_LINE"]["P2"] = None			
			self.controller.save_json()

		self.draw()
		self.regainHover(self.side)
		self.controller.updateMenuLabel(self.getNextLabel(), self.menu_label)


	def update_canvas(self, draw_tools):
		self.draw_tools = draw_tools


	def update_dict(self, master_dict):
		self.dict = master_dict


	def unset(self):
		# print("unset from "+self.name)
		self.draw_tools.clear_by_tag(self.tag)
	

	def regainHover(self, side):
		p1_fem_joint_line = self.dict["ALPHA"][self.op_type][side]["FEM_JOINT_LINE"]["P1"]
		p2_fem_joint_line = self.dict["ALPHA"][self.op_type][side]["FEM_JOINT_LINE"]["P2"]

		# find if P0 hovers are required
		self.mainHoverUsingNextLabel()

		if p1_fem_joint_line != None and p2_fem_joint_line == None:
			self.draw_tools.setHoverPointLabel("P1_FEM_JOINT_LINE")
			self.draw_tools.setHoverPoint(p1_fem_joint_line)
			self.draw_tools.setHoverBool(True)

	# similiar to draw but nothing is drawn on the canvas
	def updateExcelValues(self):
		pass


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

	def mainHoverUsingNextLabel(self):
		label = self.getNextLabel()

		if label == "RIGHT FEM_JOINT_LINE P1":
			self.side = "RIGHT"
			self.hover_text = "FEM_JOINT_LINE"
			self.draw_tools.setHoverPointLabel("P0_FEM_JOINT_LINE")
			self.draw_tools.setHoverPoint(None)
			self.draw_tools.setHoverBool(True)
		elif label == "LEFT FEM_JOINT_LINE P1":
			self.side = "LEFT"
			self.hover_text = "FEM_JOINT_LINE"
			self.draw_tools.setHoverPointLabel("P0_FEM_JOINT_LINE")
			self.draw_tools.setHoverPoint(None)
			self.draw_tools.setHoverBool(True)


	def obj_draw_pil(self):
		print('draw PIL ALPHA')

		self.point_size = self.controller.getViewPointSize()

		# loop left and right				
		for side in ["LEFT","RIGHT"]:

			isFemJointLine 	= False
			isFemTop 		= False
			isFemBot 		= False


			fem_line_p1 = self.dict["ALPHA"][self.op_type][side]["FEM_JOINT_LINE"]["P1"]
			fem_line_p2 = self.dict["ALPHA"][self.op_type][side]["FEM_JOINT_LINE"]["P2"]

			axis_fem_top_m1 = self.dict["UNI_FEM_VAL"][self.op_type][side]["AXIS_FEM"]["TOP"]["M1"]
			axis_fem_bot_m1 = self.dict["UNI_FEM_VAL"][self.op_type][side]["AXIS_FEM"]["BOT"]["M1"]


			if fem_line_p1 != None and fem_line_p2 != None:
				isFemJointLine = True



			# FEM AXIS
			# TOP
			if axis_fem_top_m1 != None:			
				isFemTop = True
			# BOT
			if axis_fem_bot_m1 != None:
				isFemBot = True


			# if isFemJointLine and isFemTop and isFemBot:
			if isFemTop and isFemBot and isFemJointLine:

				# axis
				U_fem_m1, D_fem_m1 = self.draw_tools.retPointsUpDown(axis_fem_top_m1, axis_fem_bot_m1)

				# find angle ray intersection point
				p_int = self.draw_tools.line_intersection((U_fem_m1, D_fem_m1),(fem_line_p1, fem_line_p2))

				self.draw_tools.pil_create_myline(p_int, U_fem_m1)
				self.draw_tools.pil_create_mypoint(U_fem_m1, "orange", point_thickness=self.point_size)


				L_fem, R_fem = self.draw_tools.retPointsLeftRight(fem_line_p1, fem_line_p2)


				multi_text = ""
				p_draw = None
				xoffset = 120
				yoffset = -100

				if side == "RIGHT":
					alpha_angle = self.draw_tools.pil_create_myAngle(U_fem_m1, p_int, R_fem)
					multi_text = 'ALPHA: {0:.2f}'.format(alpha_angle)
					self.draw_tools.pil_create_myline(p_int, R_fem)
					self.draw_tools.pil_create_mypoint(R_fem, "orange", point_thickness=self.point_size)
					p_draw = R_fem

				if side == "LEFT":
					alpha_angle = self.draw_tools.pil_create_myAngle(L_fem, p_int, U_fem_m1)
					multi_text = 'ALPHA: {0:.2f}'.format(alpha_angle)
					xoffset = -1*(xoffset + self.draw_tools.pil_get_multiline_text_size(multi_text))
					self.draw_tools.pil_create_myline(p_int, L_fem)
					self.draw_tools.pil_create_mypoint(L_fem, "orange", point_thickness=self.point_size)
					p_draw = L_fem


				# p_draw is assigned correctly, proceed
				x1,y1,x2,y2 = self.draw_tools.pil_get_text_bbox(p_draw, multi_text, x_offset=xoffset, y_offset=yoffset)
				self.draw_tools.pil_draw_rect([x1,y1,x2,y2], padding=20)
				self.draw_tools.pil_create_multiline_text(p_draw, multi_text, x_offset=xoffset, y_offset=yoffset, color=(255,255,255,255))
		