

class ACOR():
	"""docstring for ClassName"""
	def __init__(self, draw_tools, master_dict, controller):
		self.name = "ACOR"
		self.tag = "acor"
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
				print(self.dict["ACOR"])
			# print(self.side)

		self.draw()
		# print(self.dict)


	def checkMasterDict(self):
		if "ACOR" not in self.dict.keys():
			self.dict["ACOR"] = 	{
									"LEFT":	{
												
												"AXIS_FEM":	{
																"type":	"axis",
																"TOP":	{"type":"midpoint","P1":None,"P2":None, "M1":None},
																"BOT":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
															},
												"P1":		{"type":"point","P1":None},
												"P2":		{"type":"point","P1":None}
											},
									"RIGHT":	{
												"AXIS_FEM":	{
																"type":	"axis",
																"TOP":	{"type":"midpoint","P1":None,"P2":None, "M1":None},
																"BOT":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
															},
												"P1":		{"type":"point","P1":None},
												"P2":		{"type":"point","P1":None}
											}
									}

	def draw(self):

		# loop left and right
		for side in ["LEFT","RIGHT"]:

			isFemTop = False
			isFemBot = False
			isP1 = False
			isP2 = False

			for item in self.dict["ACOR"][side]:

				item_type = self.dict["ACOR"][side][item]["type"]

				if item_type == "point":
					if self.dict["ACOR"][side]["P1"]["P1"] != None:
						self.draw_tools.create_mypoint(self.dict["ACOR"][side]["P1"]["P1"], "white", self.tag)
						isP1 = True

					if self.dict["ACOR"][side]["P2"]["P1"] != None:
						self.draw_tools.create_mypoint(self.dict["ACOR"][side]["P2"]["P1"], "white", self.tag)
						isP2 = True


				if item_type == "axis":
					# FEM AXIS
					# TOP
					if self.dict["ACOR"][side]["AXIS_FEM"]["TOP"]["P1"] != None:
						self.draw_tools.create_mypoint(self.dict["ACOR"][side]["AXIS_FEM"]["TOP"]["P1"], "white", self.tag)

					if self.dict["ACOR"][side]["AXIS_FEM"]["TOP"]["P2"] != None:
						self.draw_tools.create_mypoint(self.dict["ACOR"][side]["AXIS_FEM"]["TOP"]["P2"], "white", self.tag)

					if self.dict["ACOR"][side]["AXIS_FEM"]["TOP"]["P1"] != None and self.dict["ACOR"][side]["AXIS_FEM"]["TOP"]["P2"] != None:
						p1 = self.dict["ACOR"][side]["AXIS_FEM"]["TOP"]["P1"]
						p2 = self.dict["ACOR"][side]["AXIS_FEM"]["TOP"]["P2"]
						m1 = self.dict["ACOR"][side]["AXIS_FEM"]["TOP"]["M1"]
						self.draw_tools.create_midpoint_line(p1, p2, m1, self.tag)
						isFemTop = True


					# BOT
					if self.dict["ACOR"][side]["AXIS_FEM"]["BOT"]["P1"] != None:
						self.draw_tools.create_mypoint(self.dict["ACOR"][side]["AXIS_FEM"]["BOT"]["P1"], "white", self.tag)

					if self.dict["ACOR"][side]["AXIS_FEM"]["BOT"]["P2"] != None:
						self.draw_tools.create_mypoint(self.dict["ACOR"][side]["AXIS_FEM"]["BOT"]["P2"], "white", self.tag)

					if self.dict["ACOR"][side]["AXIS_FEM"]["BOT"]["P1"] != None and self.dict["ACOR"][side]["AXIS_FEM"]["BOT"]["P2"] != None:
						p1 = self.dict["ACOR"][side]["AXIS_FEM"]["BOT"]["P1"]
						p2 = self.dict["ACOR"][side]["AXIS_FEM"]["BOT"]["P2"]
						m1 = self.dict["ACOR"][side]["AXIS_FEM"]["BOT"]["M1"]
						self.draw_tools.create_midpoint_line(p1, p2, m1, self.tag)
						isFemBot = True



				if isFemBot and isFemTop:
					# ankle-knee ray
					xtop, ytop, xbot, ybot = self.draw_tools.getImageCorners()

					# FEM-AXIS ray
					p_fem = self.draw_tools.line_intersection(
						(self.dict["ACOR"][side]["AXIS_FEM"]["BOT"]["M1"], self.dict["ACOR"][side]["AXIS_FEM"]["TOP"]["M1"]),
						(xbot, ybot))

					self.draw_tools.create_myline(self.dict["ACOR"][side]["AXIS_FEM"]["TOP"]["M1"], p_fem, self.tag)



					slope, intercept = self.slope_intercept(self.dict["ACOR"][side]["AXIS_FEM"]["BOT"]["M1"],self.dict["ACOR"][side]["AXIS_FEM"]["TOP"]["M1"])
					# print("slope")
					print(slope)

					# print("intercept")
					print(intercept)
					print(ytop)

					if isP1:						
						P1_t = self.dict["ACOR"][side]["P1"]["P1"]

						p_xtop_p1 = (-P1_t[1] / slope) + P1_t[0]
										
						# self.draw_tools.create_mypoint([x_val, 0], "orange", self.tag)
						self.draw_tools.create_myline(self.dict["ACOR"][side]["P1"]["P1"], [p_xtop_p1,0], self.tag)

					if isP2:						
						P2_t = self.dict["ACOR"][side]["P2"]["P1"]

						p_xtop_p2 = (-P2_t[1] / slope) + P2_t[0]
										
						# self.draw_tools.create_mypoint([x_val, 0], "orange", self.tag)
						self.draw_tools.create_myline(self.dict["ACOR"][side]["P2"]["P1"], [p_xtop_p2,0], self.tag)





	def addDict(self, event):
		for item in self.dict["ACOR"][self.side]:
			# get item type 
			item_type = self.dict["ACOR"][self.side][item]["type"]

			# point only has P1
			if item_type == "point":
				# check if P1 is None				
				if self.dict["ACOR"][self.side][item]["P1"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["ACOR"][self.side][item]["P1"] = P
					return True

			# axis has two midpoints
			if item_type == "axis":
				print("axis" + item)
				# axis has a top and a bottom

				# check if P1 is None
				if self.dict["ACOR"][self.side][item]["TOP"]["P1"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["ACOR"][self.side][item]["TOP"]["P1"] = P
					return True

				# check if P2 is None				
				if self.dict["ACOR"][self.side][item]["TOP"]["P2"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["ACOR"][self.side][item]["TOP"]["P2"] = P

					M = self.draw_tools.midpoint(self.dict["ACOR"][self.side][item]["TOP"]["P1"], P)
					self.dict["ACOR"][self.side][item]["TOP"]["M1"] = M
					return True


				# check if P1 is None
				if self.dict["ACOR"][self.side][item]["BOT"]["P1"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["ACOR"][self.side][item]["BOT"]["P1"] = P
					return True

				# check if P2 is None				
				if self.dict["ACOR"][self.side][item]["BOT"]["P2"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["ACOR"][self.side][item]["BOT"]["P2"] = P

					M = self.draw_tools.midpoint(self.dict["ACOR"][self.side][item]["BOT"]["P1"], P)
					self.dict["ACOR"][self.side][item]["BOT"]["M1"] = M
					return True	




	def slope(self, point1, point2):
		x1 = point1[0]
		y1 = point1[1]
		x2 = point2[0]
		y2 = point2[1]
		return (y2-y1)/(x2-x1)


	def slope_intercept(self, point1, point2):

		x1 = point1[0]
		y1 = point1[1]
		x2 = point2[0]
		y2 = point2[1]

		a = (y2 - y1) / (x2 - x1)
		b = y1 - a * x1
		return a, b		


	# menu button clicks are routed here
	def menu_btn_click(self, action):
		print(action)
		if action == "SET-LEFT":
			self.side = "LEFT"

		if action == "SET-RIGHT":
			self.side = "RIGHT"

	def unset(self):
		print("unset from "+self.name)
		self.draw_tools.clear_by_tag(self.tag)