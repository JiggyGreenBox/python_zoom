

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

			tib_joint_p1 = self.dict["TAMD"][side]["TIB_JOINT_LINE"]["P1"]
			tib_joint_p2 = self.dict["TAMD"][side]["TIB_JOINT_LINE"]["P2"]

			knee = self.dict["MAIN"][side]["KNEE"]["P1"]

			ankle_p1 = self.dict["MAIN"][side]["ANKLE"]["P1"]
			ankle_p2 = self.dict["MAIN"][side]["ANKLE"]["P2"]
			ankle_m1 = self.dict["MAIN"][side]["ANKLE"]["M1"]


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
			# KNEE
			if knee != None:
				isKnee = True
				self.draw_tools.create_mypoint(knee, "white", self.tag)


			# ANKLE
			if ankle_p1 != None and ankle_p2 != None:
				
				self.draw_tools.create_mypoint(ankle_p1, "white", self.tag)
				self.draw_tools.create_mypoint(ankle_p2, "white", self.tag)
				self.draw_tools.create_midpoint_line(ankle_p1, ankle_p2, ankle_m1, self.tag)

				if isTamd and isKnee:

					# ankle-knee ray
					xtop, ytop, xbot, ybot = self.draw_tools.getImageCorners()
					p_top = self.draw_tools.line_intersection((ankle_m1, knee), (xtop, ytop))
					self.draw_tools.create_myline(ankle_m1, p_top, self.tag)

						# find angle ray intersection point
					p_int = self.draw_tools.line_intersection(
							(p_top, ankle_m1),
							(tib_joint_p1, tib_joint_p2))


					if side == "LEFT":
						angle = self.draw_tools.create_myAngle(tib_joint_p2, p_int, ankle_m1, self.tag)
						self.draw_tools.create_mytext(p_int, '{0:.2f}'.format(angle), self.tag, x_offset=60, y_offset=60)

					if side == "RIGHT":
						angle = self.draw_tools.create_myAngle(ankle_m1, p_int, tib_joint_p1, self.tag)
						self.draw_tools.create_mytext(p_int, '{0:.2f}'.format(angle), self.tag, x_offset=-60, y_offset=60)

	def update_canvas(self, draw_tools):
		self.draw_tools = draw_tools


	def update_dict(self, master_dict):
		self.dict = master_dict


	def unset(self):
		# print("unset from "+self.name)
		self.draw_tools.clear_by_tag(self.tag)	