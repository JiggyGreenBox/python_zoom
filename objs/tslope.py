

class TSLOPE():
	"""docstring for ClassName"""
	def __init__(self, draw_tools, master_dict, controller):
		self.name = "TSLOPE"
		self.tag = "tslope"
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
				# print("dict full")
				print(self.dict)
			# print(self.side)

		self.draw()
		# print(self.dict)


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

			isTibTop 	= False
			isTibBot 	= False			


			if self.dict["TSLOPE"][side]["TIB_JOINT_LINE"]["P1"] != None:
				self.draw_tools.create_mypoint(self.dict["TSLOPE"][side]["TIB_JOINT_LINE"]["P1"], "white", self.tag)

			if self.dict["TSLOPE"][side]["TIB_JOINT_LINE"]["P2"] != None:
				self.draw_tools.create_mypoint(self.dict["TSLOPE"][side]["TIB_JOINT_LINE"]["P2"], "white", self.tag)

			if self.dict["TSLOPE"][side]["TIB_JOINT_LINE"]["P1"] != None and self.dict["TSLOPE"][side]["TIB_JOINT_LINE"]["P2"] != None:
				self.draw_tools.create_myline(self.dict["TSLOPE"][side]["TIB_JOINT_LINE"]["P1"], self.dict["TSLOPE"][side]["TIB_JOINT_LINE"]["P2"], self.tag)


			# TIB AXIS
			# TOP
			if self.dict["TSLOPE"][side]["AXIS_TIB"]["TOP"]["P1"] != None:
				self.draw_tools.create_mypoint(self.dict["TSLOPE"][side]["AXIS_TIB"]["TOP"]["P1"], "white", self.tag)

			if self.dict["TSLOPE"][side]["AXIS_TIB"]["TOP"]["P2"] != None:
				self.draw_tools.create_mypoint(self.dict["TSLOPE"][side]["AXIS_TIB"]["TOP"]["P2"], "white", self.tag)

			if self.dict["TSLOPE"][side]["AXIS_TIB"]["TOP"]["P1"] != None and self.dict["TSLOPE"][side]["AXIS_TIB"]["TOP"]["P2"] != None:
				p1 = self.dict["TSLOPE"][side]["AXIS_TIB"]["TOP"]["P1"]
				p2 = self.dict["TSLOPE"][side]["AXIS_TIB"]["TOP"]["P2"]
				m1 = self.dict["TSLOPE"][side]["AXIS_TIB"]["TOP"]["M1"]
				self.draw_tools.create_midpoint_line(p1, p2, m1, self.tag)
				isTibTop = True


			# BOT
			if self.dict["TSLOPE"][side]["AXIS_TIB"]["BOT"]["P1"] != None:
				self.draw_tools.create_mypoint(self.dict["TSLOPE"][side]["AXIS_TIB"]["BOT"]["P1"], "white", self.tag)

			if self.dict["TSLOPE"][side]["AXIS_TIB"]["BOT"]["P2"] != None:
				self.draw_tools.create_mypoint(self.dict["TSLOPE"][side]["AXIS_TIB"]["BOT"]["P2"], "white", self.tag)

			if self.dict["TSLOPE"][side]["AXIS_TIB"]["BOT"]["P1"] != None and self.dict["TSLOPE"][side]["AXIS_TIB"]["BOT"]["P2"] != None:
				p1 = self.dict["TSLOPE"][side]["AXIS_TIB"]["BOT"]["P1"]
				p2 = self.dict["TSLOPE"][side]["AXIS_TIB"]["BOT"]["P2"]
				m1 = self.dict["TSLOPE"][side]["AXIS_TIB"]["BOT"]["M1"]
				self.draw_tools.create_midpoint_line(p1, p2, m1, self.tag)
				isTibBot = True

			xtop, ytop, xbot, ybot = self.draw_tools.getImageCorners()

			if isTibTop and isTibBot:
				# TIB-AXIS ray
				p_tib = self.draw_tools.line_intersection(
					(self.dict["TSLOPE"][side]["AXIS_TIB"]["BOT"]["M1"], self.dict["TSLOPE"][side]["AXIS_TIB"]["TOP"]["M1"]),
					(xtop, ytop))
				self.draw_tools.create_myline(self.dict["TSLOPE"][side]["AXIS_TIB"]["BOT"]["M1"], p_tib, self.tag)





	def checkMasterDict(self):
		if "TSLOPE" not in self.dict.keys():
			self.dict["TSLOPE"] = 	{
									"LEFT":	{
												"TIB_JOINT_LINE":	{"type":"line","P1":None,"P2":None},
												"AXIS_TIB":	{
																"type":	"axis",
																"TOP":	{"type":"midpoint","P1":None,"P2":None, "M1":None},
																"BOT":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
															}
											},
									"RIGHT":	{
												"TIB_JOINT_LINE":	{"type":"line","P1":None,"P2":None},
												"AXIS_TIB":	{
																"type":	"axis",
																"TOP":	{"type":"midpoint","P1":None,"P2":None, "M1":None},
																"BOT":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
															}
											}
									}



	def addDict(self, event):

		for item in self.dict["TSLOPE"][self.side]:
			# get item type 
			item_type = self.dict["TSLOPE"][self.side][item]["type"]

			
			# line has P1 and P2
			if item_type == "line":

				# check if P1 is None				
				if self.dict["TSLOPE"][self.side][item]["P1"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["TSLOPE"][self.side][item]["P1"] = P
					return True


				# check if P2 is None				
				if self.dict["TSLOPE"][self.side][item]["P2"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["TSLOPE"][self.side][item]["P2"] = P
					return True


			# axis has two midpoints
			if item_type == "axis":				
				# axis has a top and a bottom
				# TOP

				# check if P1 is None
				if self.dict["TSLOPE"][self.side][item]["TOP"]["P1"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["TSLOPE"][self.side][item]["TOP"]["P1"] = P
					return True

				# check if P2 is None				
				if self.dict["TSLOPE"][self.side][item]["TOP"]["P2"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["TSLOPE"][self.side][item]["TOP"]["P2"] = P

					M = self.draw_tools.midpoint(self.dict["TSLOPE"][self.side][item]["TOP"]["P1"], P)
					self.dict["TSLOPE"][self.side][item]["TOP"]["M1"] = M
					return True

				# BOT
				# check if P1 is None
				if self.dict["TSLOPE"][self.side][item]["BOT"]["P1"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["TSLOPE"][self.side][item]["BOT"]["P1"] = P
					return True

				# check if P2 is None				
				if self.dict["TSLOPE"][self.side][item]["BOT"]["P2"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["TSLOPE"][self.side][item]["BOT"]["P2"] = P

					M = self.draw_tools.midpoint(self.dict["TSLOPE"][self.side][item]["BOT"]["P1"], P)
					self.dict["TSLOPE"][self.side][item]["BOT"]["M1"] = M
					return True					

		return False	


	def update_canvas(self, draw_tools):
		self.draw_tools = draw_tools


	def unset(self):
		print("unset from "+self.name)
		self.draw_tools.clear_by_tag(self.tag)