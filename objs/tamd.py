

class TAMD():
	"""docstring for ClassName"""
	def __init__(self, draw_tools, master_dict, controller):
		self.name = "TAMD"
		self.tag = "tamd"
		self.draw_tools = draw_tools
		self.dict = master_dict
		self.controller = controller
		self.side = None

		# check if master dictionary has values
		# if not populate the dictionary
		self.checkMasterDict()

	def click(self, event):
		print("click from "+self.name)

		if self.side == None:
			print("please choose side")
			self.controller.warningBox("Please select a Side")
		else:
			pass
			# print(self.dict)
			ret =  self.addDict(event)
			if ret:
				pass
			else:
				print(self.dict)			
		self.draw()

	def checkMasterDict(self):
		if "TAMD" not in self.dict.keys():
			self.dict["TAMD"] = 	{
									"LEFT":	{
												"TIB_JOINT_LINE":	{"type":"line","P1":None,"P2":None}
											},
									"RIGHT":	{
												"TIB_JOINT_LINE":	{"type":"line","P1":None,"P2":None}
											}
									}


	def addDict(self, event):
		for item in self.dict["TAMD"][self.side]:
			
			# get item type 
			item_type = self.dict["TAMD"][self.side][item]["type"]

			# line has P1 and P2
			if item_type == "line":

				# check if P1 is None				
				if self.dict["TAMD"][self.side][item]["P1"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["TAMD"][self.side][item]["P1"] = P
					return True


				# check if P2 is None				
				if self.dict["TAMD"][self.side][item]["P2"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["TAMD"][self.side][item]["P2"] = P
					return True

		return False


	def draw(self):

		# loop left and right
		for side in ["LEFT","RIGHT"]:

			isTibTop = False
			isTibBot = False
			isTamd = False


			# ------------------------
			# FROM TAMD
			# ------------------------
			if self.dict["TAMD"][side]["TIB_JOINT_LINE"]["P1"] != None:
				self.draw_tools.create_mypoint(self.dict["TAMD"][side]["TIB_JOINT_LINE"]["P1"], "white", self.tag)

			if self.dict["TAMD"][side]["TIB_JOINT_LINE"]["P2"] != None:
				self.draw_tools.create_mypoint(self.dict["TAMD"][side]["TIB_JOINT_LINE"]["P2"], "white", self.tag)

			if self.dict["TAMD"][side]["TIB_JOINT_LINE"]["P1"] != None and self.dict["TAMD"][side]["TIB_JOINT_LINE"]["P2"] != None:
				self.draw_tools.create_myline(self.dict["TAMD"][side]["TIB_JOINT_LINE"]["P1"], self.dict["TAMD"][side]["TIB_JOINT_LINE"]["P2"], self.tag)
				isTamd = True

			# ------------------------
			# FROM MAIN
			# ------------------------
			# TIB AXIS
			# TOP
			if self.dict["MAIN"][side]["AXIS_TIB"]["TOP"]["P1"] != None:
				self.draw_tools.create_mypoint(self.dict["MAIN"][side]["AXIS_TIB"]["TOP"]["P1"], "white", self.tag)

			if self.dict["MAIN"][side]["AXIS_TIB"]["TOP"]["P2"] != None:
				self.draw_tools.create_mypoint(self.dict["MAIN"][side]["AXIS_TIB"]["TOP"]["P2"], "white", self.tag)

			if self.dict["MAIN"][side]["AXIS_TIB"]["TOP"]["P1"] != None and self.dict["MAIN"][side]["AXIS_TIB"]["TOP"]["P2"] != None:
				p1 = self.dict["MAIN"][side]["AXIS_TIB"]["TOP"]["P1"]
				p2 = self.dict["MAIN"][side]["AXIS_TIB"]["TOP"]["P2"]
				m1 = self.dict["MAIN"][side]["AXIS_TIB"]["TOP"]["M1"]
				self.draw_tools.create_midpoint_line(p1, p2, m1, self.tag)
				isTibTop = True


			# BOT
			if self.dict["MAIN"][side]["AXIS_TIB"]["BOT"]["P1"] != None:
				self.draw_tools.create_mypoint(self.dict["MAIN"][side]["AXIS_TIB"]["BOT"]["P1"], "white", self.tag)

			if self.dict["MAIN"][side]["AXIS_TIB"]["BOT"]["P2"] != None:
				self.draw_tools.create_mypoint(self.dict["MAIN"][side]["AXIS_TIB"]["BOT"]["P2"], "white", self.tag)

			if self.dict["MAIN"][side]["AXIS_TIB"]["BOT"]["P1"] != None and self.dict["MAIN"][side]["AXIS_TIB"]["BOT"]["P2"] != None:
				p1 = self.dict["MAIN"][side]["AXIS_TIB"]["BOT"]["P1"]
				p2 = self.dict["MAIN"][side]["AXIS_TIB"]["BOT"]["P2"]
				m1 = self.dict["MAIN"][side]["AXIS_TIB"]["BOT"]["M1"]
				self.draw_tools.create_midpoint_line(p1, p2, m1, self.tag)
				isTibBot = True


			if isTibTop and isTibBot and isTamd:

				xtop, ytop, xbot, ybot = self.draw_tools.getImageCorners()
				# TIB-AXIS ray
				p_tib = self.draw_tools.line_intersection(
					(self.dict["MAIN"][side]["AXIS_TIB"]["BOT"]["M1"], self.dict["MAIN"][side]["AXIS_TIB"]["TOP"]["M1"]),
					(xtop, ytop))

				self.draw_tools.create_myline(self.dict["MAIN"][side]["AXIS_TIB"]["BOT"]["M1"], p_tib, self.tag)



	# menu button clicks are routed here
	def menu_btn_click(self, action):
		print(action)
		if action == "SET-LEFT":
			self.side = "LEFT"

		if action == "SET-RIGHT":
			self.side = "RIGHT"


	def update_canvas(self, draw_tools):
		self.draw_tools = draw_tools

	def unset(self):
		print("unset from "+self.name)
		self.draw_tools.clear_by_tag(self.tag)