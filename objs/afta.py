

class AFTA():
	"""docstring for ClassName"""
	def __init__(self, draw_tools, master_dict, controller):
		self.name = "AFTA"
		self.tag = "afta"
		self.draw_tools = draw_tools
		self.dict = master_dict

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
			if self.dict["MAIN"][side]["AXIS_FEM"]["TOP"]["P1"] != None:
				self.draw_tools.create_mypoint(self.dict["MAIN"][side]["AXIS_FEM"]["TOP"]["P1"], "white", self.tag)

			if self.dict["MAIN"][side]["AXIS_FEM"]["TOP"]["P2"] != None:
				self.draw_tools.create_mypoint(self.dict["MAIN"][side]["AXIS_FEM"]["TOP"]["P2"], "white", self.tag)

			if self.dict["MAIN"][side]["AXIS_FEM"]["TOP"]["P1"] != None and self.dict["MAIN"][side]["AXIS_FEM"]["TOP"]["P2"] != None:
				p1 = self.dict["MAIN"][side]["AXIS_FEM"]["TOP"]["P1"]
				p2 = self.dict["MAIN"][side]["AXIS_FEM"]["TOP"]["P2"]
				m1 = self.dict["MAIN"][side]["AXIS_FEM"]["TOP"]["M1"]
				self.draw_tools.create_midpoint_line(p1, p2, m1, self.tag)
				isFemTop = True


			# BOT
			if self.dict["MAIN"][side]["AXIS_FEM"]["BOT"]["P1"] != None:
				self.draw_tools.create_mypoint(self.dict["MAIN"][side]["AXIS_FEM"]["BOT"]["P1"], "white", self.tag)

			if self.dict["MAIN"][side]["AXIS_FEM"]["BOT"]["P2"] != None:
				self.draw_tools.create_mypoint(self.dict["MAIN"][side]["AXIS_FEM"]["BOT"]["P2"], "white", self.tag)

			if self.dict["MAIN"][side]["AXIS_FEM"]["BOT"]["P1"] != None and self.dict["MAIN"][side]["AXIS_FEM"]["BOT"]["P2"] != None:
				p1 = self.dict["MAIN"][side]["AXIS_FEM"]["BOT"]["P1"]
				p2 = self.dict["MAIN"][side]["AXIS_FEM"]["BOT"]["P2"]
				m1 = self.dict["MAIN"][side]["AXIS_FEM"]["BOT"]["M1"]
				self.draw_tools.create_midpoint_line(p1, p2, m1, self.tag)
				isFemBot = True


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




			xtop, ytop, xbot, ybot = self.draw_tools.getImageCorners()

			if isFemBot and isFemTop:
				
				# FEM-AXIS ray
				p_fem = self.draw_tools.line_intersection(
					(self.dict["MAIN"][side]["AXIS_FEM"]["BOT"]["M1"], self.dict["MAIN"][side]["AXIS_FEM"]["TOP"]["M1"]),
					(xbot, ybot))

				self.draw_tools.create_myline(self.dict["MAIN"][side]["AXIS_FEM"]["TOP"]["M1"], p_fem, self.tag)

			if isTibTop and isTibBot:

				# TIB-AXIS ray
				p_tib = self.draw_tools.line_intersection(
					(self.dict["MAIN"][side]["AXIS_TIB"]["BOT"]["M1"], self.dict["MAIN"][side]["AXIS_TIB"]["TOP"]["M1"]),
					(xtop, ytop))

				self.draw_tools.create_myline(self.dict["MAIN"][side]["AXIS_TIB"]["BOT"]["M1"], p_tib, self.tag)


	def update_canvas(self, draw_tools):
		self.draw_tools = draw_tools
		print("updated canvas from" + self.tag)

	def unset(self):
		print("unset from "+self.name)
		self.draw_tools.clear_by_tag(self.tag)
