

class MPTA():
	"""docstring for ClassName"""
	def __init__(self, draw_tools, master_dict, controller):
		self.name = "MPTA"
		self.tag = "mpta"
		self.draw_tools = draw_tools
		self.dict = master_dict
		self.controller = controller
		self.side = None

	def click(self, event):
		print("click from "+self.name)

	def draw(self):

		# loop left and right
		for side in ["LEFT","RIGHT"]:

			isKnee = False			
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
			# KNEE
			if self.dict["MAIN"][side]["KNEE"]["P1"] != None:
				isKnee = True
				self.draw_tools.create_mypoint(self.dict["MAIN"][side]["KNEE"]["P1"], "white", self.tag)


			# ANKLE
			if self.dict["MAIN"][side]["ANKLE"]["P1"] != None and self.dict["MAIN"][side]["ANKLE"]["P2"] != None:


				p1 = self.dict["MAIN"][side]["ANKLE"]["P1"]
				p2 = self.dict["MAIN"][side]["ANKLE"]["P2"]
				m1 = self.dict["MAIN"][side]["ANKLE"]["M1"]
				self.draw_tools.create_mypoint(p1, "white", self.tag)
				self.draw_tools.create_mypoint(p2, "white", self.tag)
				self.draw_tools.create_midpoint_line(p1, p2, m1, self.tag)

				if isTamd and isKnee:

					# ankle-knee ray
					xtop, ytop, xbot, ybot = self.draw_tools.getImageCorners()
					p_top = self.draw_tools.line_intersection((m1, self.dict["MAIN"][side]["KNEE"]["P1"]), (xtop, ytop))
					self.draw_tools.create_myline(m1, p_top, self.tag)					

	def update_canvas(self, draw_tools):
		self.draw_tools = draw_tools

	def unset(self):
		print("unset from "+self.name)
		self.draw_tools.clear_by_tag(self.tag)	