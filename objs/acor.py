import math

class ACOR():
	"""docstring for ClassName"""
	def __init__(self, draw_tools, master_dict, controller, op_type):
		self.name = "ACOR"
		self.tag = "acor"
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
			self.controller.save_json()
			# print(self.dict)
		else:
			ret =  self.addDict(event)
			if ret:
				self.controller.save_json()
				# pass

		self.controller.updateMenuLabel(self.getNextLabel(), "ACOR_Menu")
		self.draw_tools.clear_by_tag(self.tag)
		self.draw()


	def checkMasterDict(self):
		if "ACOR" not in self.dict.keys():
			self.dict["ACOR"] = 	{
									"PRE-OP":
											{
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
											},
									"POST-OP":
											{
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
									}

	def draw(self):

		# loop left and right
		for side in ["LEFT","RIGHT"]:

			isFemTop = False
			isFemBot = False
			isP1 = False
			isP2 = False

			acor_p1 = self.dict["ACOR"][self.op_type][side]["P1"]["P1"]
			acor_p2 = self.dict["ACOR"][self.op_type][side]["P2"]["P1"]

			axis_fem_top_p1 = self.dict["ACOR"][self.op_type][side]["AXIS_FEM"]["TOP"]["P1"]
			axis_fem_top_p2 = self.dict["ACOR"][self.op_type][side]["AXIS_FEM"]["TOP"]["P2"]
			axis_fem_top_m1 = self.dict["ACOR"][self.op_type][side]["AXIS_FEM"]["TOP"]["M1"]

			axis_fem_bot_p1 = self.dict["ACOR"][self.op_type][side]["AXIS_FEM"]["BOT"]["P1"]
			axis_fem_bot_p2 = self.dict["ACOR"][self.op_type][side]["AXIS_FEM"]["BOT"]["P2"]
			axis_fem_bot_m1 = self.dict["ACOR"][self.op_type][side]["AXIS_FEM"]["BOT"]["M1"]

			for item in self.dict["ACOR"][self.op_type][side]:

				item_type = self.dict["ACOR"][self.op_type][side][item]["type"]

				if item_type == "point":
					if acor_p1 != None:
						self.draw_tools.create_mypoint(acor_p1, "white", self.tag)
						isP1 = True

					if acor_p2 != None:
						self.draw_tools.create_mypoint(acor_p2, "white", self.tag)
						isP2 = True


				if item_type == "axis":
					# FEM AXIS
					# TOP
					if axis_fem_top_p1 != None:
						self.draw_tools.create_mypoint(axis_fem_top_p1, "white", self.tag)

					if axis_fem_top_p2 != None:
						self.draw_tools.create_mypoint(axis_fem_top_p2, "white", self.tag)

					if axis_fem_top_p1 != None and axis_fem_top_p2 != None:						
						# self.draw_tools.create_midpoint_line(axis_fem_top_p1, axis_fem_top_p2, axis_fem_top_m1, self.tag)
						isFemTop = True


					# BOT
					if axis_fem_bot_p1 != None:
						self.draw_tools.create_mypoint(axis_fem_bot_p1, "white", self.tag)

					if axis_fem_bot_p2 != None:
						self.draw_tools.create_mypoint(axis_fem_bot_p2, "white", self.tag)

					if axis_fem_bot_p1 != None and axis_fem_bot_p2 != None:						
						# self.draw_tools.create_midpoint_line(axis_fem_bot_p1, axis_fem_bot_p2, axis_fem_bot_m1, self.tag)
						isFemBot = True



				if isFemBot and isFemTop:
					# ankle-knee ray
					xtop, ytop, xbot, ybot = self.draw_tools.getImageCorners()

					# FEM-AXIS ray
					p_bot = self.draw_tools.line_intersection((axis_fem_top_m1, axis_fem_bot_m1),(xbot, ybot))

					U_fem, L_fem = self.draw_tools.retPointsUpDown(axis_fem_top_m1, axis_fem_bot_m1)

					self.draw_tools.create_myline(U_fem, p_bot, self.tag)



					slope, intercept = self.slope_intercept(axis_fem_bot_m1, axis_fem_top_m1)
					# print("slope")
					print(slope)

					# print("intercept")
					print(intercept)
					print(ytop)






					if isP1:
						# parallel line

						# y2-y1 = m(x2-x1)
						# y2 = 0 {top-line}
						# -y1/m = x2-x1
						# (-y1/m) + x1 = x2
						p_xtop_p1 = (-acor_p1[1] / slope) + acor_p1[0]
									
						# self.draw_tools.create_mypoint([x_val, 0], "orange", self.tag)
						self.draw_tools.create_myline(acor_p1, [p_xtop_p1,0], self.tag)					

					if isP2:
						# parallel line

						# y2-y1 = m(x2-x1)
						# y2 = 0 {top-line}
						# -y1/m = x2-x1
						# (-y1/m) + x1 = x2
						p_xtop_p2 = (-acor_p2[1] / slope) + acor_p2[0]
									
						# self.draw_tools.create_mypoint([x_val, 0], "orange", self.tag)
						self.draw_tools.create_myline(acor_p2, [p_xtop_p2,0], self.tag)




					# find L/R points for fem_axis_bot
					L_fem_axis_bot, R_fem_axis_bot = self.draw_tools.retPointsLeftRight(axis_fem_bot_p1, axis_fem_bot_p2)

					# perpendicular line
					L_per = [0,0]
					R_per = [0,0]
					dy = math.sqrt(100**2/(slope**2+1))
					dx = -slope*dy
					L_per[0] = L_fem_axis_bot[0] + dx
					L_per[1] = L_fem_axis_bot[1] + dy
					R_per[0] = R_fem_axis_bot[0] + dx
					R_per[1] = R_fem_axis_bot[1] + dy

					# self.draw_tools.create_mypoint(L_per, "orange", self.tag)
					# self.draw_tools.create_mypoint(R_per, "blue", self.tag)


					# assign L,R acor


					# use line L_per-L_fem_axis_bot and R_per-R_fem_axis_bot 
					# to find intersection
					if isP1:

						# check if its left or right
						L_acor, _ = self.draw_tools.retPointsLeftRight(axis_fem_bot_m1, acor_p1)
						_ , R_acor = self.draw_tools.retPointsLeftRight(axis_fem_bot_m1, acor_p1)
						if(acor_p1 == L_acor):
							print("point is on the left")
							L_per_int = self.draw_tools.line_intersection((L_per, L_fem_axis_bot),(acor_p1, [p_xtop_p1,0]))
							self.draw_tools.create_mypoint(L_per_int, "white", self.tag)
							self.draw_tools.create_myline(L_fem_axis_bot, L_per_int, self.tag)

						if(acor_p1 == R_acor):
							print("point is on the right")
							R_per_int = self.draw_tools.line_intersection((R_per, R_fem_axis_bot),(acor_p1, [p_xtop_p1,0]))
							self.draw_tools.create_mypoint(R_per_int, "white", self.tag)
							self.draw_tools.create_myline(R_fem_axis_bot, R_per_int, self.tag)

					if isP2:

						# check if its left or right
						L_acor, _ = self.draw_tools.retPointsLeftRight(axis_fem_bot_m1, acor_p2)
						_ , R_acor = self.draw_tools.retPointsLeftRight(axis_fem_bot_m1, acor_p2)

						if(acor_p2 == L_acor):
							print("point is on the left")
							L_per_int = self.draw_tools.line_intersection((L_per, L_fem_axis_bot),(acor_p2, [p_xtop_p2,0]))
							self.draw_tools.create_mypoint(L_per_int, "white", self.tag)
							self.draw_tools.create_myline(L_fem_axis_bot, L_per_int, self.tag)

						if(acor_p2 == R_acor):
							print("point is on the right")
							R_per_int = self.draw_tools.line_intersection((R_per, R_fem_axis_bot),(acor_p2, [p_xtop_p2,0]))
							self.draw_tools.create_mypoint(R_per_int, "white", self.tag)
							self.draw_tools.create_myline(R_fem_axis_bot, R_per_int, self.tag)

						# R_per_int = self.draw_tools.line_intersection((R_per, R_fem_axis_bot),(acor_p2, [p_xtop_p2,0]))
						# self.draw_tools.create_mypoint(R_per_int, "white", self.tag)
						# self.draw_tools.create_myline(R_fem_axis_bot, R_per_int, self.tag)


						





	def addDict(self, event):
		for item in self.dict["ACOR"][self.op_type][self.side]:
			# get item type 
			item_type = self.dict["ACOR"][self.op_type][self.side][item]["type"]

			# point only has P1
			if item_type == "point":
				# check if P1 is None				
				if self.dict["ACOR"][self.op_type][self.side][item]["P1"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["ACOR"][self.op_type][self.side][item]["P1"] = P
					return True

			# axis has two midpoints
			if item_type == "axis":
				print("axis" + item)
				# axis has a top and a bottom

				# check if P1 is None
				if self.dict["ACOR"][self.op_type][self.side][item]["TOP"]["P1"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["ACOR"][self.op_type][self.side][item]["TOP"]["P1"] = P
					return True

				# check if P2 is None				
				if self.dict["ACOR"][self.op_type][self.side][item]["TOP"]["P2"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["ACOR"][self.op_type][self.side][item]["TOP"]["P2"] = P

					M = self.draw_tools.midpoint(self.dict["ACOR"][self.op_type][self.side][item]["TOP"]["P1"], P)
					self.dict["ACOR"][self.op_type][self.side][item]["TOP"]["M1"] = M
					return True


				# check if P1 is None
				if self.dict["ACOR"][self.op_type][self.side][item]["BOT"]["P1"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["ACOR"][self.op_type][self.side][item]["BOT"]["P1"] = P
					return True

				# check if P2 is None				
				if self.dict["ACOR"][self.op_type][self.side][item]["BOT"]["P2"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["ACOR"][self.op_type][self.side][item]["BOT"]["P2"] = P

					M = self.draw_tools.midpoint(self.dict["ACOR"][self.op_type][self.side][item]["BOT"]["P1"], P)
					self.dict["ACOR"][self.op_type][self.side][item]["BOT"]["M1"] = M
					return True	

	def update_dict(self, master_dict):
		self.dict = master_dict



	def getNextLabel(self):

		if self.side != None:
			for item in self.dict["ACOR"][self.op_type][self.side]:
				# get item type 
				item_type = self.dict["ACOR"][self.op_type][self.side][item]["type"]

				# point only has P1
				if item_type == "point":
					# check if P1 is None				
					if self.dict["ACOR"][self.op_type][self.side][item]["P1"] == None:						
						return (self.side + " " + item)

				# axis has two midpoints
				if item_type == "axis":					
					# axis has a top and a bottom

					# check if P1 is None
					if self.dict["ACOR"][self.op_type][self.side][item]["TOP"]["P1"] == None:						
						return (self.side + " " + item + " P1")

					# check if P2 is None				
					if self.dict["ACOR"][self.op_type][self.side][item]["TOP"]["P2"] == None:						
						return (self.side + " " + item + " P2")


					# check if P1 is None
					if self.dict["ACOR"][self.op_type][self.side][item]["BOT"]["P1"] == None:						
						return (self.side + " " + item + " P1")

					# check if P2 is None				
					if self.dict["ACOR"][self.op_type][self.side][item]["BOT"]["P2"] == None:						
						return (self.side + " " + item + " P2")

			return (self.side + " Done")
		return None


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
			self.controller.updateMenuLabel(self.getNextLabel(), "ACOR_Menu")
			return # avoid clear,draw,json_save

		if action == "SET-RIGHT":
			self.side = "RIGHT"
			self.controller.updateMenuLabel(self.getNextLabel(), "ACOR_Menu")
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

		if action == "DEL-LEFT-P1":
			self.dict[self.name][self.op_type]["LEFT"]["P1"]["P1"] = None

		if action == "DEL-RIGHT-P1":
			self.dict[self.name][self.op_type]["RIGHT"]["P1"]["P1"] = None

		if action == "DEL-LEFT-P2":
			self.dict[self.name][self.op_type]["LEFT"]["P2"]["P1"] = None

		if action == "DEL-RIGHT-P2":
			self.dict[self.name][self.op_type]["RIGHT"]["P2"]["P1"] = None

		self.draw_tools.clear_by_tag(self.tag)
		self.draw()
		self.controller.save_json()

		self.controller.updateMenuLabel(self.getNextLabel(), "ACOR_Menu")

	def update_canvas(self, draw_tools):
		self.draw_tools = draw_tools

	def unset(self):
		# print("unset from "+self.name)
		self.draw_tools.clear_by_tag(self.tag)