

class MLDFA():
	"""docstring for ClassName"""
	def __init__(self, draw_tools, master_dict, controller):
		self.name = "MLDFA"
		self.tag = "mldfa"
		self.draw_tools = draw_tools
		self.dict = master_dict
		self.controller = controller
		self.side = None
		
	def click(self, event):
		print("click from "+self.name)


	def draw(self):

		# loop left and right
		for side in ["LEFT","RIGHT"]:

			isFemTop = False
			isFemBot = False
			isAldfa = False



			# ------------------------
			# FROM ALDFA
			# ------------------------
			if self.dict["ALDFA"][side]["FEM_JOINT_LINE"]["P1"] != None:
				self.draw_tools.create_mypoint(self.dict["ALDFA"][side]["FEM_JOINT_LINE"]["P1"], "white", self.tag)

			if self.dict["ALDFA"][side]["FEM_JOINT_LINE"]["P2"] != None:
				self.draw_tools.create_mypoint(self.dict["ALDFA"][side]["FEM_JOINT_LINE"]["P2"], "white", self.tag)

			if self.dict["ALDFA"][side]["FEM_JOINT_LINE"]["P1"] != None and self.dict["ALDFA"][side]["FEM_JOINT_LINE"]["P2"] != None:
				self.draw_tools.create_myline(self.dict["ALDFA"][side]["FEM_JOINT_LINE"]["P1"], self.dict["ALDFA"][side]["FEM_JOINT_LINE"]["P2"], self.tag)
				isAldfa = True



			# ------------------------
			# FROM MAIN
			# ------------------------
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


			if isAldfa and isFemBot and isFemTop:

				# fem ray
				xtop, ytop, xbot, ybot = self.draw_tools.getImageCorners()

				p_bot = self.draw_tools.line_intersection(
						(self.dict["MAIN"][side]["AXIS_FEM"]["TOP"]["M1"], self.dict["MAIN"][side]["AXIS_FEM"]["BOT"]["M1"]),
						(xbot, ybot))
				self.draw_tools.create_myline(self.dict["MAIN"][side]["AXIS_FEM"]["TOP"]["M1"], p_bot, self.tag)


	def update_canvas(self, draw_tools):
		self.draw_tools = draw_tools

	def unset(self):
		print("unset from "+self.name)
		self.draw_tools.clear_by_tag(self.tag)
