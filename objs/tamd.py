

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

			tib_joint_p1 = self.dict["TAMD"][side]["TIB_JOINT_LINE"]["P1"]
			tib_joint_p2 = self.dict["TAMD"][side]["TIB_JOINT_LINE"]["P2"]

			tib_top_p1 = self.dict["MAIN"][side]["AXIS_TIB"]["TOP"]["P1"]
			tib_top_p2 = self.dict["MAIN"][side]["AXIS_TIB"]["TOP"]["P2"]

			tib_bot_p1 = self.dict["MAIN"][side]["AXIS_TIB"]["BOT"]["P1"]
			tib_bot_p2 = self.dict["MAIN"][side]["AXIS_TIB"]["BOT"]["P2"]

			bot_m1 = self.dict["MAIN"][side]["AXIS_TIB"]["BOT"]["M1"]
			top_m1 = self.dict["MAIN"][side]["AXIS_TIB"]["TOP"]["M1"]


			# ------------------------
			# FROM TAMD
			# ------------------------
			if tib_joint_p1 != None:
				self.draw_tools.create_mypoint(tib_joint_p1, "white", self.tag)

			if tib_joint_p2 != None:
				self.draw_tools.create_mypoint(tib_joint_p2, "white", self.tag)

			if tib_joint_p1 != None and tib_joint_p2 != None:
				self.draw_tools.create_myline(tib_joint_p1, tib_joint_p2, self.tag)
				isTamd = True

			# ------------------------
			# FROM MAIN
			# ------------------------
			# TIB AXIS
			# TOP
			if tib_top_p1 != None:
				self.draw_tools.create_mypoint(tib_top_p1, "white", self.tag)

			if tib_top_p2 != None:
				self.draw_tools.create_mypoint(tib_top_p2, "white", self.tag)

			if tib_top_p1 != None and tib_top_p2 != None:				
				self.draw_tools.create_midpoint_line(tib_top_p1, tib_top_p2, top_m1, self.tag)
				isTibTop = True


			# BOT
			if tib_bot_p1 != None:
				self.draw_tools.create_mypoint(tib_bot_p1, "white", self.tag)

			if tib_bot_p2 != None:
				self.draw_tools.create_mypoint(tib_bot_p2, "white", self.tag)

			if tib_bot_p1 != None and tib_bot_p2 != None:				
				self.draw_tools.create_midpoint_line(tib_bot_p1, tib_bot_p2, bot_m1, self.tag)
				isTibBot = True


			if isTibTop and isTibBot and isTamd:

				xtop, ytop, xbot, ybot = self.draw_tools.getImageCorners()
				# TIB-AXIS ray
				p_tib = self.draw_tools.line_intersection(
					(bot_m1, top_m1),
					(xtop, ytop))

				self.draw_tools.create_myline(bot_m1, p_tib, self.tag)

				# find angle ray intersection point
				p_int = self.draw_tools.line_intersection(
						(p_tib, bot_m1),
						(tib_joint_p1, tib_joint_p2))


				if side == "LEFT":
					angle = self.draw_tools.create_myAngle(tib_joint_p2, p_int, bot_m1, self.tag)
					self.draw_tools.create_mytext(p_int, '{0:.2f}'.format(angle), self.tag, x_offset=60, y_offset=60)

				if side == "RIGHT":
					angle = self.draw_tools.create_myAngle(bot_m1, p_int, tib_joint_p1, self.tag)
					self.draw_tools.create_mytext(p_int, '{0:.2f}'.format(angle), self.tag, x_offset=-60, y_offset=60)		



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