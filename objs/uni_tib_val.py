

class UNI_TIB_VAL():
	"""docstring for ClassName"""
	def __init__(self, draw_tools, master_dict, controller):
		self.name = "UNI_TIB_VAL"
		self.tag = "uni_tib_val"
		self.draw_tools = draw_tools
		self.dict = master_dict
		self.controller = controller
		self.side = None

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
			if not ret:
				print("dict full")
			# print(self.side)

		self.draw()
		print(self.dict)


	# menu button clicks are routed here
	def menu_btn_click(self, action):
		print(action)
		if action == "SET-LEFT":
			self.side = "LEFT"

		if action == "SET-RIGHT":
			self.side = "RIGHT"			



	def draw(self):
		# loop left and right				
		for side in ["LEFT","RIGHT"]:

			isFemJointLine = False
			isFemTop 	= False
			isFemBot 	= False


			fem_joint_p1 = self.dict[self.name][side]["FEM_JOINT_LINE"]["P1"]
			fem_joint_p2 = self.dict[self.name][side]["FEM_JOINT_LINE"]["P2"]


			# FEM JOINT LINE
			if fem_joint_p1 != None:
				self.draw_tools.create_mypoint(fem_joint_p1, "white", self.tag)

			if fem_joint_p2 != None:
				self.draw_tools.create_mypoint(fem_joint_p2, "white", self.tag)

			if fem_joint_p1 != None and fem_joint_p2 != None:
				self.draw_tools.create_myline(fem_joint_p1, fem_joint_p2, self.tag)
				isFemJointLine = True


			# FEM AXIS
			# TOP
			top_axis_tib_p1 = self.dict[self.name][side]["AXIS_TIB"]["TOP"]["P1"]
			top_axis_tib_p2 = self.dict[self.name][side]["AXIS_TIB"]["TOP"]["P2"]
			bot_axis_tib_p1 = self.dict[self.name][side]["AXIS_TIB"]["BOT"]["P1"]
			bot_axis_tib_p2 = self.dict[self.name][side]["AXIS_TIB"]["BOT"]["P2"]

			if top_axis_tib_p1 != None:
				self.draw_tools.create_mypoint(top_axis_tib_p1, "white", self.tag)

			if top_axis_tib_p2 != None:
				self.draw_tools.create_mypoint(top_axis_tib_p2, "white", self.tag)

			if top_axis_tib_p1 != None and top_axis_tib_p2 != None:				
				m1 = self.dict["UNI_TIB_VAL"][side]["AXIS_TIB"]["TOP"]["M1"]
				self.draw_tools.create_midpoint_line(top_axis_tib_p1, top_axis_tib_p2, m1, self.tag)
				isFemTop = True


			# BOT
			if bot_axis_tib_p1 != None:
				self.draw_tools.create_mypoint(bot_axis_tib_p1, "white", self.tag)

			if bot_axis_tib_p2 != None:
				self.draw_tools.create_mypoint(bot_axis_tib_p2, "white", self.tag)

			if bot_axis_tib_p1 != None and bot_axis_tib_p2 != None:				
				m1 = self.dict["UNI_TIB_VAL"][side]["AXIS_TIB"]["TOP"]["M1"]
				self.draw_tools.create_midpoint_line(bot_axis_tib_p1, bot_axis_tib_p2, m1, self.tag)
				isFemBot = True



	def checkMasterDict(self):
		if "UNI_TIB_VAL" not in self.dict.keys():
			self.dict["UNI_TIB_VAL"] = 	{
									"LEFT":	{
												"AXIS_TIB":	{
																"type":	"axis",
																"TOP":	{"type":"midpoint","P1":None,"P2":None, "M1":None},
																"BOT":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
															},
												"FEM_JOINT_LINE":	{"type":"line","P1":None,"P2":None}
											},
									"RIGHT":	{
												"AXIS_TIB":	{
																"type":	"axis",
																"TOP":	{"type":"midpoint","P1":None,"P2":None, "M1":None},
																"BOT":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
															},
												"FEM_JOINT_LINE":	{"type":"line","P1":None,"P2":None}
											}
									}


	def addDict(self, event):
		for item in self.dict["UNI_TIB_VAL"][self.side]:
			# get item type 
			item_type = self.dict["UNI_TIB_VAL"][self.side][item]["type"]
			
			
			# axis has two midpoints
			if item_type == "axis":
				print("axis" + item)
				# axis has a top and a bottom

				# check if P1 is None
				if self.dict["UNI_TIB_VAL"][self.side][item]["TOP"]["P1"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["UNI_TIB_VAL"][self.side][item]["TOP"]["P1"] = P
					return True

				# check if P2 is None				
				if self.dict["UNI_TIB_VAL"][self.side][item]["TOP"]["P2"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["UNI_TIB_VAL"][self.side][item]["TOP"]["P2"] = P

					M = self.draw_tools.midpoint(self.dict["UNI_TIB_VAL"][self.side][item]["TOP"]["P1"], P)
					self.dict["UNI_TIB_VAL"][self.side][item]["TOP"]["M1"] = M
					return True


				# check if P1 is None
				if self.dict["UNI_TIB_VAL"][self.side][item]["BOT"]["P1"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["UNI_TIB_VAL"][self.side][item]["BOT"]["P1"] = P
					return True

				# check if P2 is None				
				if self.dict["UNI_TIB_VAL"][self.side][item]["BOT"]["P2"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["UNI_TIB_VAL"][self.side][item]["BOT"]["P2"] = P

					M = self.draw_tools.midpoint(self.dict["UNI_TIB_VAL"][self.side][item]["BOT"]["P1"], P)
					self.dict["UNI_TIB_VAL"][self.side][item]["BOT"]["M1"] = M
					return True	


			# line has P1 and P2
			if item_type == "line":

				# check if P1 is None				
				if self.dict["UNI_TIB_VAL"][self.side][item]["P1"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["UNI_TIB_VAL"][self.side][item]["P1"] = P
					return True


				# check if P2 is None				
				if self.dict["UNI_TIB_VAL"][self.side][item]["P2"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["UNI_TIB_VAL"][self.side][item]["P2"] = P
					return True

		return False									
 

	def update_canvas(self, draw_tools):
		self.draw_tools = draw_tools

	def unset(self):
		print("unset from "+self.name)
		self.draw_tools.clear_by_tag(self.tag)