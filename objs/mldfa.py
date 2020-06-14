

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

			fem_joint_p1 = self.dict["ALDFA"][side]["FEM_JOINT_LINE"]["P1"]
			fem_joint_p2 = self.dict["ALDFA"][side]["FEM_JOINT_LINE"]["P2"]

			fem_top_p1 = self.dict["MAIN"][side]["AXIS_FEM"]["TOP"]["P1"]
			fem_top_p2 = self.dict["MAIN"][side]["AXIS_FEM"]["TOP"]["P2"]

			fem_bot_p1 = self.dict["MAIN"][side]["AXIS_FEM"]["BOT"]["P1"]
			fem_bot_p2 = self.dict["MAIN"][side]["AXIS_FEM"]["BOT"]["P2"]


			bot_m1 = self.dict["MAIN"][side]["AXIS_FEM"]["BOT"]["M1"]
			top_m1 = self.dict["MAIN"][side]["AXIS_FEM"]["TOP"]["M1"]


			# ------------------------
			# FROM ALDFA
			# ------------------------
			if fem_joint_p1 != None:
				self.draw_tools.create_mypoint(fem_joint_p1, "white", self.tag)

			if fem_joint_p2 != None:
				self.draw_tools.create_mypoint(fem_joint_p2, "white", self.tag)

			if fem_joint_p1 != None and fem_joint_p2 != None:
				self.draw_tools.create_myline(fem_joint_p1, fem_joint_p2, self.tag)
				isAldfa = True



			# ------------------------
			# FROM MAIN
			# ------------------------
			# FEM AXIS
			# TOP
			if fem_top_p1 != None:
				self.draw_tools.create_mypoint(fem_top_p1, "white", self.tag)

			if fem_top_p2 != None:
				self.draw_tools.create_mypoint(fem_top_p2, "white", self.tag)

			if fem_top_p1 != None and fem_top_p2 != None:								
				self.draw_tools.create_midpoint_line(fem_top_p1, fem_top_p2, top_m1, self.tag)
				isFemTop = True


			# BOT
			if fem_bot_p1 != None:
				self.draw_tools.create_mypoint(fem_bot_p1, "white", self.tag)

			if fem_bot_p2 != None:
				self.draw_tools.create_mypoint(fem_bot_p2, "white", self.tag)

			if fem_bot_p1 != None and fem_bot_p2 != None:								
				self.draw_tools.create_midpoint_line(fem_bot_p1, fem_bot_p2, bot_m1, self.tag)
				isFemBot = True


			if isAldfa and isFemBot and isFemTop:

				# fem ray
				xtop, ytop, xbot, ybot = self.draw_tools.getImageCorners()

				p_bot = self.draw_tools.line_intersection(
						(top_m1, bot_m1),
						(xbot, ybot))
				self.draw_tools.create_myline(top_m1, p_bot, self.tag)

				# find angle ray intersection point
				p_int = self.draw_tools.line_intersection(
						(top_m1, p_bot),
						(fem_joint_p1, fem_joint_p2))


				L_fem, R_fem = self.draw_tools.retPointsLeftRight(fem_joint_p1, fem_joint_p2)

				if side == "LEFT":
					angle = self.draw_tools.create_myAngle(top_m1, p_int, R_fem, self.tag)
					self.draw_tools.create_mytext(p_int, '{0:.2f}'.format(angle), self.tag, x_offset=60, y_offset=-60)

				if side == "RIGHT":
					angle = self.draw_tools.create_myAngle(L_fem, p_int, top_m1, self.tag)
					self.draw_tools.create_mytext(p_int, '{0:.2f}'.format(angle), self.tag, x_offset=-60, y_offset=-60)				


	def update_canvas(self, draw_tools):
		self.draw_tools = draw_tools

	def update_dict(self, master_dict):
		self.dict = master_dict

	def unset(self):
		# print("unset from "+self.name)
		self.draw_tools.clear_by_tag(self.tag)
