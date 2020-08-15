

class AFTA():
	"""docstring for ClassName"""
	def __init__(self, draw_tools, master_dict, controller, op_type):
		self.name = "AFTA"
		self.tag = "afta"
		self.draw_tools = draw_tools
		self.dict = master_dict
		self.op_type = op_type
		self.controller = controller

	def click(self, event):
		print("click from "+self.name)

	def draw(self):

		# loop left and right
		for side in ["LEFT","RIGHT"]:

			isFemTop 	= False
			isFemBot 	= False

			isTibTop 	= False
			isTibBot 	= False

			# FEM AXIS
			# TOP
			if self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["TOP"]["P1"] != None:
				self.draw_tools.create_mypoint(self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["TOP"]["P1"], "white", self.tag)

			if self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["TOP"]["P2"] != None:
				self.draw_tools.create_mypoint(self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["TOP"]["P2"], "white", self.tag)

			if self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["TOP"]["P1"] != None and self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["TOP"]["P2"] != None:
				p1 = self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["TOP"]["P1"]
				p2 = self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["TOP"]["P2"]
				m1 = self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["TOP"]["M1"]
				self.draw_tools.create_midpoint_line(p1, p2, m1, self.tag)
				isFemTop = True


			# BOT
			if self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["BOT"]["P1"] != None:
				self.draw_tools.create_mypoint(self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["BOT"]["P1"], "white", self.tag)

			if self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["BOT"]["P2"] != None:
				self.draw_tools.create_mypoint(self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["BOT"]["P2"], "white", self.tag)

			if self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["BOT"]["P1"] != None and self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["BOT"]["P2"] != None:
				p1 = self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["BOT"]["P1"]
				p2 = self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["BOT"]["P2"]
				m1 = self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["BOT"]["M1"]
				self.draw_tools.create_midpoint_line(p1, p2, m1, self.tag)
				isFemBot = True


			# TIB AXIS
			# TOP
			if self.dict["MAIN"][self.op_type][side]["AXIS_TIB"]["TOP"]["P1"] != None:
				self.draw_tools.create_mypoint(self.dict["MAIN"][self.op_type][side]["AXIS_TIB"]["TOP"]["P1"], "white", self.tag)

			if self.dict["MAIN"][self.op_type][side]["AXIS_TIB"]["TOP"]["P2"] != None:
				self.draw_tools.create_mypoint(self.dict["MAIN"][self.op_type][side]["AXIS_TIB"]["TOP"]["P2"], "white", self.tag)

			if self.dict["MAIN"][self.op_type][side]["AXIS_TIB"]["TOP"]["P1"] != None and self.dict["MAIN"][self.op_type][side]["AXIS_TIB"]["TOP"]["P2"] != None:
				p1 = self.dict["MAIN"][self.op_type][side]["AXIS_TIB"]["TOP"]["P1"]
				p2 = self.dict["MAIN"][self.op_type][side]["AXIS_TIB"]["TOP"]["P2"]
				m1 = self.dict["MAIN"][self.op_type][side]["AXIS_TIB"]["TOP"]["M1"]
				self.draw_tools.create_midpoint_line(p1, p2, m1, self.tag)
				isTibTop = True


			# BOT
			if self.dict["MAIN"][self.op_type][side]["AXIS_TIB"]["BOT"]["P1"] != None:
				self.draw_tools.create_mypoint(self.dict["MAIN"][self.op_type][side]["AXIS_TIB"]["BOT"]["P1"], "white", self.tag)

			if self.dict["MAIN"][self.op_type][side]["AXIS_TIB"]["BOT"]["P2"] != None:
				self.draw_tools.create_mypoint(self.dict["MAIN"][self.op_type][side]["AXIS_TIB"]["BOT"]["P2"], "white", self.tag)

			if self.dict["MAIN"][self.op_type][side]["AXIS_TIB"]["BOT"]["P1"] != None and self.dict["MAIN"][self.op_type][side]["AXIS_TIB"]["BOT"]["P2"] != None:
				p1 = self.dict["MAIN"][self.op_type][side]["AXIS_TIB"]["BOT"]["P1"]
				p2 = self.dict["MAIN"][self.op_type][side]["AXIS_TIB"]["BOT"]["P2"]
				m1 = self.dict["MAIN"][self.op_type][side]["AXIS_TIB"]["BOT"]["M1"]
				self.draw_tools.create_midpoint_line(p1, p2, m1, self.tag)
				isTibBot = True




			xtop, ytop, xbot, ybot = self.draw_tools.getImageCorners()

			if isFemBot and isFemTop:
				
				# FEM-AXIS ray
				p_fem = self.draw_tools.line_intersection(
					(self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["BOT"]["M1"], self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["TOP"]["M1"]),
					(xbot, ybot))

				self.draw_tools.create_myline(self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["TOP"]["M1"], p_fem, self.tag)

			if isTibTop and isTibBot:

				# TIB-AXIS ray
				p_tib = self.draw_tools.line_intersection(
					(self.dict["MAIN"][self.op_type][side]["AXIS_TIB"]["BOT"]["M1"], self.dict["MAIN"][self.op_type][side]["AXIS_TIB"]["TOP"]["M1"]),
					(xtop, ytop))

				self.draw_tools.create_myline(self.dict["MAIN"][self.op_type][side]["AXIS_TIB"]["BOT"]["M1"], p_tib, self.tag)


			if isFemBot and isFemTop and isTibTop and isTibBot:
				p_int = self.draw_tools.line_intersection((self.dict["MAIN"][self.op_type][side]["AXIS_TIB"]["BOT"]["M1"], self.dict["MAIN"][self.op_type][side]["AXIS_TIB"]["TOP"]["M1"]),
					(self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["BOT"]["M1"], self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["TOP"]["M1"]))


				a1 = self.draw_tools.getAnglePoints(self.dict["MAIN"][self.op_type][side]["AXIS_TIB"]["TOP"]["M1"], p_int, self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["BOT"]["M1"])
				a2 = self.draw_tools.getAnglePoints(self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["BOT"]["M1"], p_int, self.dict["MAIN"][self.op_type][side]["AXIS_TIB"]["TOP"]["M1"])
				print('{0:.2f} a1 RIGHT'.format(a1))
				print('{0:.2f} a2 RIGHT'.format(a2))

				if a1 < a2:					
					angle = self.draw_tools.create_myAngle(self.dict["MAIN"][self.op_type][side]["AXIS_TIB"]["TOP"]["M1"], p_int, self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["BOT"]["M1"], self.tag)
				else:
					angle = self.draw_tools.create_myAngle(self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["BOT"]["M1"], p_int, self.dict["MAIN"][self.op_type][side]["AXIS_TIB"]["TOP"]["M1"], self.tag)

				self.draw_tools.create_mytext(p_int, '{0:.2f}'.format(angle), self.tag, x_offset=-60)


				# check if value exists
				if self.dict["EXCEL"][self.op_type][side]["aFTA"] == None:

					self.dict["EXCEL"][self.op_type][side]["HASDATA"] 	= True
					self.dict["EXCEL"][self.op_type][side]["aFTA"]	 	= '{0:.2f}'.format(angle)

					# save after insert
					self.controller.save_json()


	def update_canvas(self, draw_tools):
		self.draw_tools = draw_tools
		print("updated canvas from" + self.tag)

	def update_dict(self, master_dict):
		self.dict = master_dict

	def unset(self):
		# print("unset from "+self.name)
		self.draw_tools.clear_by_tag(self.tag)
