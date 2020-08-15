

class UNI_FEM_VAL():
	"""docstring for ClassName"""
	def __init__(self, draw_tools, master_dict, controller, op_type):
		self.name = "UNI_FEM_VAL"
		self.tag = "uni_fem_val"
		self.draw_tools = draw_tools
		self.dict = master_dict
		self.controller = controller
		self.side = None
		self.op_type = op_type

		# check if master dictionary has values
		# if not populate the dictionary
		self.checkMasterDict()


	def click(self, event):
		# print("click from "+self.name)
		# self.draw()
		if self.side == None:
			print("please choose side")
			self.controller.warningBox("Please select a Side")
		else:
			ret =  self.addDict(event)
			if ret:				
				self.controller.save_json()
				# pass

		self.controller.updateMenuLabel(self.getNextLabel(), "UNI_FEM_VAL_Menu")
		self.draw_tools.clear_by_tag(self.tag)
		self.draw()


	# menu button clicks are routed here
	def menu_btn_click(self, action):
		print(action)
		if action == "SET-LEFT":
			self.side = "LEFT"
			self.controller.updateMenuLabel(self.getNextLabel(), "UNI_FEM_VAL_Menu")
			return # avoid clear,draw,json_save

		if action == "SET-RIGHT":
			self.side = "RIGHT"
			self.controller.updateMenuLabel(self.getNextLabel(), "UNI_FEM_VAL_Menu")
			return # avoid clear,draw,json_save

		if action == "DEL-LEFT-FEM-TOP":
			self.dict[self.name][self.op_type]["LEFT"]["AXIS_FEM"]["TOP"]["P1"] = None
			self.dict[self.name][self.op_type]["LEFT"]["AXIS_FEM"]["TOP"]["P2"] = None
			self.dict[self.name][self.op_type]["LEFT"]["AXIS_FEM"]["TOP"]["M1"] = None

		if action == "DEL-RIGHT-FEM-TOP":
			self.dict[self.name][self.op_type]["RIGHT"]["AXIS_FEM"]["TOP"]["P1"] = None
			self.dict[self.name][self.op_type]["RIGHT"]["AXIS_FEM"]["TOP"]["P2"] = None
			self.dict[self.name][self.op_type]["RIGHT"]["AXIS_FEM"]["TOP"]["M1"] = None

		if action == "DEL-LEFT-FEM-BOT":
			self.dict[self.name][self.op_type]["LEFT"]["AXIS_FEM"]["BOT"]["P1"] = None
			self.dict[self.name][self.op_type]["LEFT"]["AXIS_FEM"]["BOT"]["P2"] = None
			self.dict[self.name][self.op_type]["LEFT"]["AXIS_FEM"]["BOT"]["M1"] = None

		if action == "DEL-RIGHT-FEM-BOT":
			self.dict[self.name][self.op_type]["RIGHT"]["AXIS_FEM"]["BOT"]["P1"] = None
			self.dict[self.name][self.op_type]["RIGHT"]["AXIS_FEM"]["BOT"]["P2"] = None
			self.dict[self.name][self.op_type]["RIGHT"]["AXIS_FEM"]["BOT"]["M1"] = None

		if action == "DEL-LEFT-FEM-LINE":
			self.dict[self.name][self.op_type]["LEFT"]["FEM_JOINT_LINE"]["P1"] = None
			self.dict[self.name][self.op_type]["LEFT"]["FEM_JOINT_LINE"]["P2"] = None

		if action == "DEL-RIGHT-FEM-LINE":
			self.dict[self.name][self.op_type]["RIGHT"]["FEM_JOINT_LINE"]["P1"] = None
			self.dict[self.name][self.op_type]["RIGHT"]["FEM_JOINT_LINE"]["P2"] = None


		self.draw_tools.clear_by_tag(self.tag)
		self.draw()
		self.controller.save_json()
		
		self.controller.updateMenuLabel(self.getNextLabel(), "UNI_FEM_VAL_Menu")



	def draw(self):
		# loop left and right				
		for side in ["LEFT","RIGHT"]:

			isFemJointLine = False
			isFemTop 	= False
			isFemBot 	= False


			fem_line_p1 = self.dict["UNI_FEM_VAL"][self.op_type][side]["FEM_JOINT_LINE"]["P1"]
			fem_line_p2 = self.dict["UNI_FEM_VAL"][self.op_type][side]["FEM_JOINT_LINE"]["P2"]


			axis_fem_top_p1 = self.dict["UNI_FEM_VAL"][self.op_type][side]["AXIS_FEM"]["TOP"]["P1"]
			axis_fem_top_p2 = self.dict["UNI_FEM_VAL"][self.op_type][side]["AXIS_FEM"]["TOP"]["P2"]
			axis_fem_top_m1 = self.dict["UNI_FEM_VAL"][self.op_type][side]["AXIS_FEM"]["TOP"]["M1"]
			
			axis_fem_bot_p1 = self.dict["UNI_FEM_VAL"][self.op_type][side]["AXIS_FEM"]["BOT"]["P1"]
			axis_fem_bot_p2 = self.dict["UNI_FEM_VAL"][self.op_type][side]["AXIS_FEM"]["BOT"]["P2"]
			axis_fem_bot_m1 = self.dict["UNI_FEM_VAL"][self.op_type][side]["AXIS_FEM"]["BOT"]["M1"]

			# FEM JOINT LINE
			if fem_line_p1 != None:
				self.draw_tools.create_mypoint(fem_line_p1, "white", self.tag)

			if fem_line_p2 != None:
				self.draw_tools.create_mypoint(fem_line_p2, "white", self.tag)

			if fem_line_p1 != None and fem_line_p2 != None:
				self.draw_tools.create_myline(fem_line_p1, fem_line_p2, self.tag)
				isFemJointLine = True



			# FEM AXIS
			# TOP
			if axis_fem_top_p1 != None:
				self.draw_tools.create_mypoint(axis_fem_top_p1, "white", self.tag)

			if axis_fem_top_p2 != None:
				self.draw_tools.create_mypoint(axis_fem_top_p2, "white", self.tag)

			if axis_fem_top_p1 != None and axis_fem_top_p2 != None:				
				self.draw_tools.create_midpoint_line(axis_fem_top_p1, axis_fem_top_p2, axis_fem_top_m1, self.tag)
				isFemTop = True


			# BOT
			if axis_fem_bot_p1 != None:
				self.draw_tools.create_mypoint(axis_fem_bot_p1, "white", self.tag)

			if axis_fem_bot_p2 != None:
				self.draw_tools.create_mypoint(axis_fem_bot_p2, "white", self.tag)

			if axis_fem_bot_p1 != None and axis_fem_bot_p2 != None:				
				self.draw_tools.create_midpoint_line(axis_fem_bot_p1, axis_fem_bot_p2, axis_fem_bot_m1, self.tag)
				isFemBot = True


			if isFemJointLine and isFemTop and isFemBot:
				# axis
				U_fem_m1, D_fem_m1 = self.draw_tools.retPointsUpDown(axis_fem_top_m1, axis_fem_bot_m1)
				# line
				U_fem_p1, D_fem_p1 = self.draw_tools.retPointsUpDown(fem_line_p1, fem_line_p2)

				xtop, ytop, xbot, ybot = self.draw_tools.getImageCorners()

				# fem axis extension
				p_axis_bot = self.draw_tools.line_intersection((U_fem_m1, D_fem_m1), (xbot, ybot))
				self.draw_tools.create_myline(U_fem_m1, p_axis_bot, self.tag)

				# fem line extension
				p_line_bot = self.draw_tools.line_intersection((fem_line_p1, fem_line_p2), (xbot, ybot))
				self.draw_tools.create_myline(D_fem_p1, p_line_bot, self.tag)

				# fem-axis and fem-line intersection
				p_int = self.draw_tools.line_intersection((U_fem_m1, p_axis_bot), (D_fem_p1, p_line_bot))


				a1 = self.draw_tools.getAnglePoints(U_fem_m1, p_int, U_fem_p1)
				a2 = self.draw_tools.getAnglePoints(U_fem_p1, p_int, U_fem_m1)
				print('{0:.2f} a1 RIGHT'.format(a1))
				print('{0:.2f} a2 RIGHT'.format(a2))

				if a1 > a2:					
					angle = self.draw_tools.create_myAngle(U_fem_p1, p_int, U_fem_m1, self.tag)
				else:
					angle = self.draw_tools.create_myAngle(U_fem_m1, p_int, U_fem_p1, self.tag)
					
					
				self.draw_tools.create_mytext(U_fem_p1, '{0:.2f}'.format(angle), self.tag, x_offset=-60)

				# check if intersection point is above or below
				# if above then
				# else 
				check_U, check_D = self.draw_tools.retPointsUpDown(p_int, U_fem_m1)
				if(p_int == check_U):
					print("point is above so +ve")
				else:
					print("point is below so -ve")

			
			



	def checkMasterDict(self):
		if "UNI_FEM_VAL" not in self.dict.keys():
			self.dict["UNI_FEM_VAL"] = 	{
											"PRE-OP":{
												"LEFT":	{
															"AXIS_FEM":	{
																			"type":	"axis",
																			"TOP":	{"type":"midpoint","P1":None,"P2":None, "M1":None},
																			"BOT":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
																		},
															"FEM_JOINT_LINE":	{"type":"line","P1":None,"P2":None}
														},
												"RIGHT":{
															"AXIS_FEM":	{
																			"type":	"axis",
																			"TOP":	{"type":"midpoint","P1":None,"P2":None, "M1":None},
																			"BOT":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
																		},
															"FEM_JOINT_LINE":	{"type":"line","P1":None,"P2":None}
														}
											},
											"POST-OP":{
												"LEFT":	{
															"AXIS_FEM":	{
																			"type":	"axis",
																			"TOP":	{"type":"midpoint","P1":None,"P2":None, "M1":None},
																			"BOT":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
																		},
															"FEM_JOINT_LINE":	{"type":"line","P1":None,"P2":None}
														},
												"RIGHT":{
															"AXIS_FEM":	{
																			"type":	"axis",
																			"TOP":	{"type":"midpoint","P1":None,"P2":None, "M1":None},
																			"BOT":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
																		},
															"FEM_JOINT_LINE":	{"type":"line","P1":None,"P2":None}
														}
											}											
										}


	def addDict(self, event):
		for item in self.dict["UNI_FEM_VAL"][self.op_type][self.side]:
			# get item type 
			item_type = self.dict["UNI_FEM_VAL"][self.op_type][self.side][item]["type"]
			
			
			# axis has two midpoints
			if item_type == "axis":
				print("axis" + item)
				# axis has a top and a bottom

				# check if P1 is None
				if self.dict["UNI_FEM_VAL"][self.op_type][self.side][item]["TOP"]["P1"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["UNI_FEM_VAL"][self.op_type][self.side][item]["TOP"]["P1"] = P
					return True

				# check if P2 is None				
				if self.dict["UNI_FEM_VAL"][self.op_type][self.side][item]["TOP"]["P2"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["UNI_FEM_VAL"][self.op_type][self.side][item]["TOP"]["P2"] = P

					M = self.draw_tools.midpoint(self.dict["UNI_FEM_VAL"][self.op_type][self.side][item]["TOP"]["P1"], P)
					self.dict["UNI_FEM_VAL"][self.op_type][self.side][item]["TOP"]["M1"] = M
					return True


				# check if P1 is None
				if self.dict["UNI_FEM_VAL"][self.op_type][self.side][item]["BOT"]["P1"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["UNI_FEM_VAL"][self.op_type][self.side][item]["BOT"]["P1"] = P
					return True

				# check if P2 is None				
				if self.dict["UNI_FEM_VAL"][self.op_type][self.side][item]["BOT"]["P2"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["UNI_FEM_VAL"][self.op_type][self.side][item]["BOT"]["P2"] = P

					M = self.draw_tools.midpoint(self.dict["UNI_FEM_VAL"][self.op_type][self.side][item]["BOT"]["P1"], P)
					self.dict["UNI_FEM_VAL"][self.op_type][self.side][item]["BOT"]["M1"] = M
					return True	


			# line has P1 and P2
			if item_type == "line":

				# check if P1 is None				
				if self.dict["UNI_FEM_VAL"][self.op_type][self.side][item]["P1"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["UNI_FEM_VAL"][self.op_type][self.side][item]["P1"] = P
					return True


				# check if P2 is None				
				if self.dict["UNI_FEM_VAL"][self.op_type][self.side][item]["P2"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["UNI_FEM_VAL"][self.op_type][self.side][item]["P2"] = P
					return True

		return False									
 


	def getNextLabel(self):

		if self.side != None:
			for item in self.dict["UNI_FEM_VAL"][self.op_type][self.side]:
				# get item type 
				item_type = self.dict["UNI_FEM_VAL"][self.op_type][self.side][item]["type"]
				
				
				# axis has two midpoints
				if item_type == "axis":
					print("axis" + item)
					# axis has a top and a bottom

					# check if P1 is None
					if self.dict["UNI_FEM_VAL"][self.op_type][self.side][item]["TOP"]["P1"] == None:						
						return (self.side + " " + item + " P1")

					# check if P2 is None				
					if self.dict["UNI_FEM_VAL"][self.op_type][self.side][item]["TOP"]["P2"] == None:						
						return (self.side + " " + item + " P2")

					# check if P1 is None
					if self.dict["UNI_FEM_VAL"][self.op_type][self.side][item]["BOT"]["P1"] == None:						
						return (self.side + " " + item + " P1")

					# check if P2 is None				
					if self.dict["UNI_FEM_VAL"][self.op_type][self.side][item]["BOT"]["P2"] == None:						
						return (self.side + " " + item + " P2")


				# line has P1 and P2
				if item_type == "line":

					# check if P1 is None				
					if self.dict["UNI_FEM_VAL"][self.op_type][self.side][item]["P1"] == None:						
						return (self.side + " " + item + " P1")

					# check if P2 is None				
					if self.dict["UNI_FEM_VAL"][self.op_type][self.side][item]["P2"] == None:						
						return (self.side + " " + item + " P2")

			return (self.side + " Done")

		return None


	def update_canvas(self, draw_tools):
		self.draw_tools = draw_tools


	def update_dict(self, master_dict):
		self.dict = master_dict



	def unset(self):
		# print("unset from "+self.name)
		self.draw_tools.clear_by_tag(self.tag)