

class BETA():
	"""docstring for ClassName"""
	def __init__(self, draw_tools, master_dict, controller, op_type):
		self.name = "BETA"
		self.tag = "beta"
		self.menu_label = "BETA_Menu"
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
		if "BETA" not in self.dict.keys():
			self.dict["BETA"] = 	{
									"PRE-OP":{
											"LEFT":	{
														"AXIS_TIB":	{
																		"type":	"axis",
																		"TOP":	{"type":"midpoint","P1":None,"P2":None, "M1":None},
																		"BOT":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
																	},
														"TIB_JOINT_LINE":	{"type":"line","P1":None,"P2":None}
													},
											"RIGHT":	{
														"AXIS_TIB":	{
																		"type":	"axis",
																		"TOP":	{"type":"midpoint","P1":None,"P2":None, "M1":None},
																		"BOT":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
																	},
														"TIB_JOINT_LINE":	{"type":"line","P1":None,"P2":None}
													}
										},
										"POST-OP":{
											"LEFT":	{
														"AXIS_TIB":	{
																		"type":	"axis",
																		"TOP":	{"type":"midpoint","P1":None,"P2":None, "M1":None},
																		"BOT":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
																	},
														"TIB_JOINT_LINE":	{"type":"line","P1":None,"P2":None}
													},
											"RIGHT":	{
														"AXIS_TIB":	{
																		"type":	"axis",
																		"TOP":	{"type":"midpoint","P1":None,"P2":None, "M1":None},
																		"BOT":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
																	},
														"TIB_JOINT_LINE":	{"type":"line","P1":None,"P2":None}
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


	def draw(self):

		self.draw_tools.clear_by_tag(self.tag)

		self.point_size = self.controller.getViewPointSize()

		# loop left and right
		for side in ["LEFT","RIGHT"]:
			isTibJointLine = False
			isTibTop 	= False
			isTibBot 	= False

			# TIB JOINT LINE
			tib_joint_p1 = self.dict[self.name][self.op_type][side]["TIB_JOINT_LINE"]["P1"]
			tib_joint_p2 = self.dict[self.name][self.op_type][side]["TIB_JOINT_LINE"]["P2"]


			# TIB JOINT LINE
			if tib_joint_p1 != None:
				self.draw_tools.create_mypoint(tib_joint_p1, "orange", [self.tag,side,"TIB_JOINT_LINE","P1"], point_thickness=self.point_size)

			if tib_joint_p2 != None:
				self.draw_tools.create_mypoint(tib_joint_p2, "orange", [self.tag,side,"TIB_JOINT_LINE","P2"], point_thickness=self.point_size)

			if tib_joint_p1 != None and tib_joint_p2 != None:
				self.draw_tools.create_myline(tib_joint_p1, tib_joint_p2, [self.tag,side,"TIB_LINE"])
				isTibJointLine = True


			# TIB AXIS
			# TOP
			top_axis_tib_p1 = self.dict[self.name][self.op_type][side]["AXIS_TIB"]["TOP"]["P1"]
			top_axis_tib_p2 = self.dict[self.name][self.op_type][side]["AXIS_TIB"]["TOP"]["P2"]
			top_axis_tib_m1 = self.dict[self.name][self.op_type][side]["AXIS_TIB"]["TOP"]["M1"]
			# BOT
			bot_axis_tib_p1 = self.dict[self.name][self.op_type][side]["AXIS_TIB"]["BOT"]["P1"]
			bot_axis_tib_p2 = self.dict[self.name][self.op_type][side]["AXIS_TIB"]["BOT"]["P2"]			
			bot_axis_tib_m1 = self.dict[self.name][self.op_type][side]["AXIS_TIB"]["BOT"]["M1"]


			if top_axis_tib_p1 != None:
				self.draw_tools.create_mypoint(top_axis_tib_p1, "orange", [self.tag,side,"NO-DRAG"], point_thickness=self.point_size)

			if top_axis_tib_p2 != None:
				self.draw_tools.create_mypoint(top_axis_tib_p2, "orange", [self.tag,side,"NO-DRAG"], point_thickness=self.point_size)

			if top_axis_tib_p1 != None and top_axis_tib_p2 != None:				
				
				self.draw_tools.create_midpoint_line(top_axis_tib_p1, top_axis_tib_p2, top_axis_tib_m1, [self.tag,side,"NO-DRAG"], point_thickness=self.point_size)
				isTibTop = True


			# BOT
			if bot_axis_tib_p1 != None:
				self.draw_tools.create_mypoint(bot_axis_tib_p1, "orange", [self.tag,side,"NO-DRAG"], point_thickness=self.point_size)

			if bot_axis_tib_p2 != None:
				self.draw_tools.create_mypoint(bot_axis_tib_p2, "orange", [self.tag,side,"NO-DRAG"], point_thickness=self.point_size)

			if bot_axis_tib_p1 != None and bot_axis_tib_p2 != None:				
				# m1 = self.dict["UNI_TIB_VAL"][self.op_type][side]["AXIS_TIB"]["TOP"]["M1"]
				self.draw_tools.create_midpoint_line(bot_axis_tib_p1, bot_axis_tib_p2, bot_axis_tib_m1, [self.tag,side,"BOT_AXIS_LINE"], point_thickness=self.point_size)
				isTibBot = True


			# if isFemJointLine and isFemTop and isFemBot:
			if isTibTop and isTibBot:
				# axis
				U_tib_m1, D_tib_m1 = self.draw_tools.retPointsUpDown(top_axis_tib_m1, bot_axis_tib_m1)
				

				xtop, ytop, xbot, ybot = self.draw_tools.getImageCorners()

				# fem axis extension
				p_axis_bot = self.draw_tools.line_intersection((U_tib_m1, D_tib_m1), (xtop, ytop))
				self.draw_tools.create_myline(D_tib_m1, p_axis_bot, self.tag)

				if isTibJointLine:

					# find angle ray intersection point
					p_int = self.draw_tools.line_intersection(
							(U_tib_m1, D_tib_m1),
							(tib_joint_p1, tib_joint_p2))

					L_tib, R_tib = self.draw_tools.retPointsLeftRight(tib_joint_p1, tib_joint_p2)

					if side == "RIGHT":
						angle = self.draw_tools.create_myAngle(R_tib, p_int, D_tib_m1, [self.tag,side,"BETA_ANGLE"])
						if self.draw_labels:
							self.draw_tools.create_mytext(p_int, '{0:.1f}'.format(angle), [self.tag,side,"BETA_ANGLE"], x_offset=60, y_offset=60, color="blue")

					if side == "LEFT":
						angle = self.draw_tools.create_myAngle(D_tib_m1, p_int, L_tib, [self.tag,side,"BETA_ANGLE"])
						if self.draw_labels:
							self.draw_tools.create_mytext(p_int, '{0:.1f}'.format(angle), [self.tag,side,"BETA_ANGLE"], x_offset=-60, y_offset=60, color="blue")


		


	def addDict(self, event):
		for item in self.dict["BETA"][self.op_type][self.side]:

			# get real coords
			P = self.draw_tools.getRealCoords(event)
			
			# get item type 
			item_type = self.dict["BETA"][self.op_type][self.side][item]["type"]

			# axis has two midpoints
			if item_type == "axis":
				print("axis" + item)
				# axis has a top and a bottom

				# check if P1 is None
				if self.dict["BETA"][self.op_type][self.side][item]["TOP"]["P1"] == None:					
					self.dict["BETA"][self.op_type][self.side][item]["TOP"]["P1"] = P
					self.draw_tools.setHoverPointLabel("P1_"+item+"_TOP")
					self.draw_tools.setHoverPoint(P)
					self.draw_tools.setHoverBool(True)
					return True

				# check if P2 is None				
				if self.dict["BETA"][self.op_type][self.side][item]["TOP"]["P2"] == None:					
					self.dict["BETA"][self.op_type][self.side][item]["TOP"]["P2"] = P
					M = self.draw_tools.midpoint(self.dict["BETA"][self.op_type][self.side][item]["TOP"]["P1"], P)
					self.dict["BETA"][self.op_type][self.side][item]["TOP"]["M1"] = M
					self.draw_tools.setHoverBool(False)
					self.draw_tools.setHoverPointLabel(None)
					return True


				# check if P1 is None
				if self.dict["BETA"][self.op_type][self.side][item]["BOT"]["P1"] == None:					
					self.dict["BETA"][self.op_type][self.side][item]["BOT"]["P1"] = P
					self.draw_tools.setHoverPointLabel("P1_"+item+"_BOT")
					self.draw_tools.setHoverPoint(P)
					self.draw_tools.setHoverBool(True)
					return True

				# check if P2 is None				
				if self.dict["BETA"][self.op_type][self.side][item]["BOT"]["P2"] == None:					
					self.dict["BETA"][self.op_type][self.side][item]["BOT"]["P2"] = P
					M = self.draw_tools.midpoint(self.dict["BETA"][self.op_type][self.side][item]["BOT"]["P1"], P)
					self.dict["BETA"][self.op_type][self.side][item]["BOT"]["M1"] = M
					self.draw_tools.setHoverBool(False)
					self.draw_tools.setHoverPointLabel(None)
					return True	

			# line has P1 and P2
			if item_type == "line":

				# check if P1 is None				
				if self.dict["BETA"][self.op_type][self.side][item]["P1"] == None:
					
					self.dict["BETA"][self.op_type][self.side][item]["P1"] = P
					self.draw_tools.setHoverPointLabel("P1_BETA")
					self.draw_tools.setHoverPoint(P)
					self.draw_tools.setHoverBool(True)
					return True


				# check if P2 is None				
				if self.dict["BETA"][self.op_type][self.side][item]["P2"] == None:					
					self.dict["BETA"][self.op_type][self.side][item]["P2"] = P
					self.draw_tools.setHoverBool(False)
					self.draw_tools.setHoverPointLabel(None)
					return True

		return False


	# def drag_start(self, tags):
	# 	tags.remove('token')
	# 	tags.remove('current')
	# 	tags.remove(self.tag)
	# 	print(tags)
		

	# 	side = ""

	# 	# find side
	# 	if "LEFT" in tags:
	# 		side = "LEFT"
	# 	elif "RIGHT" in tags:
	# 		side = "RIGHT"

	# 	if "P1_TIB_JOINT_LINE" in tags:
	# 		self.drag_point = self.dict["MPTA"][self.op_type][side]["TIB_JOINT_LINE"]["P2"]
	# 		self.drag_label = "P1_TIB_JOINT_LINE"
	# 		self.drag_side 	= side
	# 	elif "P2_TIB_JOINT_LINE" in tags:
	# 		self.drag_point = self.dict["MPTA"][self.op_type][side]["TIB_JOINT_LINE"]["P1"]
	# 		self.drag_label = "P2_TIB_JOINT_LINE"
	# 		self.drag_side 	= side

	# 	else:
	# 		self.drag_point = None
	# 		self.drag_label = None
	# 		self.drag_side 	= None

	# def drag(self, P_mouse):
	# 	if self.drag_label == "P1_TIB_JOINT_LINE" and self.drag_point != None or self.drag_label == "P2_TIB_JOINT_LINE" and self.drag_point != None:
	# 		self.draw_tools.clear_by_tag("TIB_JOINT_LINE")
	# 		self.draw_tools.clear_by_tag("MPTA_ANGLE")
	# 		self.draw_tools.clear_by_tag("drag_line")
	# 		self.draw_tools.create_myline(P_mouse, self.drag_point, "drag_line")

	# def drag_stop(self, P_mouse):
	# 	self.draw_tools.clear_by_tag("drag_line")

	# 	if self.drag_label == "P1_TIB_JOINT_LINE":
	# 		self.dict["MPTA"][self.op_type][self.drag_side]["TIB_JOINT_LINE"]["P1"] = P_mouse
	# 		self.dict["EXCEL"][self.op_type][self.drag_side]["MPTA"] = None 	# delete excel data from pat.json

	# 	elif self.drag_label == "P2_TIB_JOINT_LINE":
	# 		self.dict["MPTA"][self.op_type][self.drag_side]["TIB_JOINT_LINE"]["P2"] = P_mouse
	# 		self.dict["EXCEL"][self.op_type][self.drag_side]["MPTA"] = None 	# delete excel data from pat.json

	# 	self.controller.save_json()
	# 	self.draw()		

	def hover(self, P_mouse, P_stored, hover_label):

		# prevent auto curObject set bug
		if self.side == None:
			return

		if self.draw_hover:
			side_pre = self.side[0]+"_"
			if(	hover_label == "P0_AXIS_TIB" or
				hover_label == "P0_TIB_JOINT_LINE"
				):
				self.draw_tools.clear_by_tag("hover_line")
				self.draw_tools.create_mypoint(P_mouse, "red", [self.tag, "hover_line"], hover_point=True, point_thickness=self.point_size)
				if self.draw_labels:
					self.draw_tools.create_mytext(P_mouse,x_offset=80, mytext=(side_pre+self.hover_text), mytag=[self.tag, "hover_line"])

		if hover_label == "P1_BETA":
			self.draw_tools.clear_by_tag("hover_line")
			self.draw_tools.create_myline(P_mouse, P_stored, "hover_line")


		if hover_label == "P1_AXIS_TIB_TOP":
			self.draw_tools.clear_by_tag("hover_line")
			m = self.draw_tools.midpoint(P_stored, P_mouse)
			self.draw_tools.create_midpoint_line(P_stored, P_mouse, m, "hover_line", point_thickness=self.point_size)

			bot_axis_tib_m1 = self.dict[self.name][self.op_type][self.side]["AXIS_TIB"]["BOT"]["M1"]

			if bot_axis_tib_m1 != None:
				# join center points of axes
				xtop, ytop, xbot, ybot = self.draw_tools.getImageCorners()
				U_m1, D_m1 = self.draw_tools.retPointsUpDown(m, bot_axis_tib_m1)
				p_top = self.draw_tools.line_intersection((D_m1, U_m1), (xtop, ytop))
				self.draw_tools.create_myline(D_m1, p_top, "hover_line")


		if hover_label == "P1_AXIS_TIB_BOT":
			self.draw_tools.clear_by_tag("hover_line")
			m = self.draw_tools.midpoint(P_stored, P_mouse)
			self.draw_tools.create_midpoint_line(P_stored, P_mouse, m, "hover_line", point_thickness=self.point_size)

			top_axis_tib_m1 = self.dict[self.name][self.op_type][self.side]["AXIS_TIB"]["TOP"]["M1"]

			if top_axis_tib_m1 != None:				
				# join center points of axes
				xtop, ytop, xbot, ybot = self.draw_tools.getImageCorners()
				U_m1, D_m1 = self.draw_tools.retPointsUpDown(top_axis_tib_m1, m)
				p_top = self.draw_tools.line_intersection((D_m1, U_m1), (xtop, ytop))
				self.draw_tools.create_myline(D_m1, p_top, "hover_line")
	
	def escapeObjFunc(self):
		self.side = None
		self.draw_tools.setHoverPointLabel(None)
		self.draw_tools.setHoverBool(False)
		self.controller.updateMenuLabel("CHOOSE SIDE", self.menu_label)


	def getNextLabel(self):
		if self.side != None:
			for item in self.dict["BETA"][self.op_type][self.side]:
				
				# get item type 
				item_type = self.dict["BETA"][self.op_type][self.side][item]["type"]

				# axis has two midpoints
				if item_type == "axis":
					print("axis" + item)
					# axis has a top and a bottom

					# check if P1 is None
					if self.dict["BETA"][self.op_type][self.side][item]["TOP"]["P1"] == None:						
						return (self.side + " " + item + " P1")

					# check if P2 is None				
					if self.dict["BETA"][self.op_type][self.side][item]["TOP"]["P2"] == None:						
						return (self.side + " " + item + " P2")


					# check if P1 is None
					if self.dict["BETA"][self.op_type][self.side][item]["BOT"]["P1"] == None:						
						return (self.side + " " + item + " P1")

					# check if P2 is None				
					if self.dict["BETA"][self.op_type][self.side][item]["BOT"]["P2"] == None:						
						return (self.side + " " + item + " P2")

				# line has P1 and P2
				if item_type == "line":

					# check if P1 is None				
					if self.dict["BETA"][self.op_type][self.side][item]["P1"] == None:
						return (self.side + " " + item + " P1")


					# check if P2 is None				
					if self.dict["BETA"][self.op_type][self.side][item]["P2"] == None:
						return (self.side + " " + item + " P2")

			return (self.side + " Done")
		return None


	# menu button clicks are routed here
	def menu_btn_click(self, action):
		print(action)
		if action == "SET-LEFT":
			self.side = "LEFT"
			self.draw()
			self.regainHover(self.side)
			self.controller.updateMenuLabel(self.getNextLabel(), self.menu_label)
			return # avoid json_save

		if action == "SET-RIGHT":
			self.side = "RIGHT"
			self.draw()
			self.regainHover(self.side)
			self.controller.updateMenuLabel(self.getNextLabel(), self.menu_label)
			return # avoid json_save

		if action == "DEL-LEFT-TIB-LINE":
			self.side = "LEFT"
			self.dict["BETA"][self.op_type]["LEFT"]["TIB_JOINT_LINE"]["P1"] = None
			self.dict["BETA"][self.op_type]["LEFT"]["TIB_JOINT_LINE"]["P2"] = None			
		if action == "DEL-RIGHT-TIB-LINE":
			self.side = "RIGHT"
			self.dict["BETA"][self.op_type]["RIGHT"]["TIB_JOINT_LINE"]["P1"] = None
			self.dict["BETA"][self.op_type]["RIGHT"]["TIB_JOINT_LINE"]["P2"] = None						


		if action == "DEL-LEFT-TIB-TOP":			
			self.dict["BETA"][self.op_type]["LEFT"]["AXIS_TIB"]["TOP"]["P1"] = None
			self.dict["BETA"][self.op_type]["LEFT"]["AXIS_TIB"]["TOP"]["P2"] = None
			self.dict["BETA"][self.op_type]["LEFT"]["AXIS_TIB"]["TOP"]["M1"] = None
			self.side = "LEFT"
		if action == "DEL-RIGHT-TIB-TOP":
			self.dict["BETA"][self.op_type]["RIGHT"]["AXIS_TIB"]["TOP"]["P1"] = None
			self.dict["BETA"][self.op_type]["RIGHT"]["AXIS_TIB"]["TOP"]["P2"] = None
			self.dict["BETA"][self.op_type]["RIGHT"]["AXIS_TIB"]["TOP"]["M1"] = None
			self.side = "RIGHT"


		if action == "DEL-LEFT-TIB-BOT":
			self.dict["BETA"][self.op_type]["LEFT"]["AXIS_TIB"]["BOT"]["P1"] = None
			self.dict["BETA"][self.op_type]["LEFT"]["AXIS_TIB"]["BOT"]["P2"] = None
			self.dict["BETA"][self.op_type]["LEFT"]["AXIS_TIB"]["BOT"]["M1"] = None
			self.side = "LEFT"
		if action == "DEL-RIGHT-TIB-BOT":
			self.dict["BETA"][self.op_type]["RIGHT"]["AXIS_TIB"]["BOT"]["P1"] = None
			self.dict["BETA"][self.op_type]["RIGHT"]["AXIS_TIB"]["BOT"]["P2"] = None
			self.dict["BETA"][self.op_type]["RIGHT"]["AXIS_TIB"]["BOT"]["M1"] = None
			self.side = "RIGHT"

		self.draw()
		self.regainHover(self.side)
		self.controller.save_json()
		self.controller.updateMenuLabel(self.getNextLabel(), self.menu_label)


	def update_canvas(self, draw_tools):
		self.draw_tools = draw_tools


	def update_dict(self, master_dict):
		self.dict = master_dict


	def unset(self):
		# print("unset from "+self.name)
		self.draw_tools.clear_by_tag(self.tag)


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
			self.drag_point = self.dict["BETA"][self.op_type][side]["TIB_JOINT_LINE"]["P2"]
			self.drag_label = "P1_TIB_JOINT_LINE"
			self.drag_side 	= side
		elif "P2" in tags:
			self.drag_point = self.dict["BETA"][self.op_type][side]["TIB_JOINT_LINE"]["P1"]
			self.drag_label = "P2_TIB_JOINT_LINE"
			self.drag_side 	= side

	def drag(self, P_mouse):
		if self.drag_label == "P1_TIB_JOINT_LINE" and self.drag_point != None or self.drag_label == "P2_TIB_JOINT_LINE" and self.drag_point != None:
			self.draw_tools.clear_by_tag("TIB_LINE")
			self.draw_tools.clear_by_tag("BETA_ANGLE")
			self.draw_tools.clear_by_tag("drag_line")
			self.draw_tools.create_myline(P_mouse, self.drag_point, "drag_line")

	def drag_stop(self, P_mouse):
		self.draw_tools.clear_by_tag("drag_line")

		if self.drag_label == "P1_TIB_JOINT_LINE":
			self.dict["BETA"][self.op_type][self.drag_side]["TIB_JOINT_LINE"]["P1"] = P_mouse

		elif self.drag_label == "P2_TIB_JOINT_LINE":
			self.dict["BETA"][self.op_type][self.drag_side]["TIB_JOINT_LINE"]["P2"] = P_mouse

		self.controller.save_json()
		self.draw()

	def regainHover(self, side):

		p1_axis_tib_top = self.dict["BETA"][self.op_type][side]["AXIS_TIB"]["TOP"]["P1"]
		p2_axis_tib_top = self.dict["BETA"][self.op_type][side]["AXIS_TIB"]["TOP"]["P2"]
		p1_axis_tib_bot = self.dict["BETA"][self.op_type][side]["AXIS_TIB"]["BOT"]["P1"]
		p2_axis_tib_bot = self.dict["BETA"][self.op_type][side]["AXIS_TIB"]["BOT"]["P2"]

		p1_tib_joint_line = self.dict["BETA"][self.op_type][side]["TIB_JOINT_LINE"]["P1"]
		p2_tib_joint_line = self.dict["BETA"][self.op_type][side]["TIB_JOINT_LINE"]["P2"]

		# find if P0 hovers are required
		self.mainHoverUsingNextLabel()

		if p1_axis_tib_top != None and p2_axis_tib_top == None:
			self.draw_tools.setHoverPointLabel("P1_AXIS_TIB_TOP")
			self.draw_tools.setHoverPoint(p1_axis_tib_top)
			self.draw_tools.setHoverBool(True)

		if p1_axis_tib_bot != None and p2_axis_tib_bot == None:
			self.draw_tools.setHoverPointLabel("P1_AXIS_TIB_BOT")
			self.draw_tools.setHoverPoint(p1_axis_tib_bot)
			self.draw_tools.setHoverBool(True)

		if p1_tib_joint_line != None and p2_tib_joint_line == None:
			self.draw_tools.setHoverPointLabel("P1_BETA")
			self.draw_tools.setHoverPoint(p1_tib_joint_line)
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

		if label == "RIGHT AXIS_TIB P1":
			self.side = "RIGHT"
			self.hover_text = "AXIS_TIB"
			self.draw_tools.setHoverPointLabel("P0_AXIS_TIB")
			self.draw_tools.setHoverPoint(None)
			self.draw_tools.setHoverBool(True)
		elif label == "LEFT AXIS_TIB P1":
			self.side = "LEFT"
			self.hover_text = "AXIS_TIB"
			self.draw_tools.setHoverPointLabel("P0_AXIS_TIB")
			self.draw_tools.setHoverPoint(None)
			self.draw_tools.setHoverBool(True)

		elif label == "RIGHT TIB_JOINT_LINE P1":
			self.side = "RIGHT"
			self.hover_text = "TIB_JOINT_LINE"
			self.draw_tools.setHoverPointLabel("P0_TIB_JOINT_LINE")
			self.draw_tools.setHoverPoint(None)
			self.draw_tools.setHoverBool(True)
		elif label == "LEFT TIB_JOINT_LINE P1":
			self.side = "LEFT"
			self.hover_text = "TIB_JOINT_LINE"
			self.draw_tools.setHoverPointLabel("P0_TIB_JOINT_LINE")
			self.draw_tools.setHoverPoint(None)
			self.draw_tools.setHoverBool(True)


	def obj_draw_pil(self):
		print('draw PIL BETA')

		self.point_size = self.controller.getViewPointSize()

		# loop left and right
		for side in ["LEFT","RIGHT"]:
			isTibJointLine = False
			isTibTop 	= False
			isTibBot 	= False

			
			tib_joint_p1 = self.dict[self.name][self.op_type][side]["TIB_JOINT_LINE"]["P1"]
			tib_joint_p2 = self.dict[self.name][self.op_type][side]["TIB_JOINT_LINE"]["P2"]

			top_axis_tib_m1 = self.dict["UNI_TIB_VAL"][self.op_type][side]["AXIS_TIB"]["TOP"]["M1"]
			bot_axis_tib_m1 = self.dict["UNI_TIB_VAL"][self.op_type][side]["AXIS_TIB"]["BOT"]["M1"]


			# TIB JOINT LINE
			if tib_joint_p1 != None and tib_joint_p2 != None:
				isTibJointLine = True

			# TIB AXIS
			# TOP
			if top_axis_tib_m1 != None:				
				isTibTop = True
			# BOT
			if bot_axis_tib_m1 != None:
				isTibBot = True


			# if isFemJointLine and isFemTop and isFemBot:
			if isTibTop and isTibBot and isTibJointLine:
				# axis
				U_tib_m1, D_tib_m1 = self.draw_tools.retPointsUpDown(top_axis_tib_m1, bot_axis_tib_m1)
				
				# find angle ray intersection point
				p_int = self.draw_tools.line_intersection((U_tib_m1, D_tib_m1),(tib_joint_p1, tib_joint_p2))

				L_tib, R_tib = self.draw_tools.retPointsLeftRight(tib_joint_p1, tib_joint_p2)


				self.draw_tools.pil_create_myline(p_int, D_tib_m1)
				self.draw_tools.pil_create_mypoint(D_tib_m1, "orange", point_thickness=self.point_size)

				multi_text = ""
				p_draw = None
				xoffset = 120
				yoffset = 100

				if side == "RIGHT":
					beta_angle = self.draw_tools.pil_create_myAngle(R_tib, p_int, D_tib_m1)
					multi_text = 'BETA: {0:.1f}'.format(beta_angle)
					self.draw_tools.pil_create_myline(p_int, R_tib)
					self.draw_tools.pil_create_mypoint(R_tib, "orange", point_thickness=self.point_size)
					p_draw = R_tib

				if side == "LEFT":
					beta_angle = self.draw_tools.pil_create_myAngle(D_tib_m1, p_int, L_tib)
					multi_text = 'BETA: {0:.1f}'.format(beta_angle)
					xoffset = -1*(xoffset + self.draw_tools.pil_get_multiline_text_size(multi_text))
					self.draw_tools.pil_create_myline(p_int, L_tib)
					self.draw_tools.pil_create_mypoint(L_tib, "orange", point_thickness=self.point_size)
					p_draw = L_tib

				# p_draw is assigned correctly, proceed
				x1,y1,x2,y2 = self.draw_tools.pil_get_text_bbox(p_draw, multi_text, x_offset=xoffset, y_offset=yoffset)
				self.draw_tools.pil_draw_rect([x1,y1,x2,y2], padding=20)
				self.draw_tools.pil_create_multiline_text(p_draw, multi_text, x_offset=xoffset, y_offset=yoffset, color=(255,255,255,255))
	