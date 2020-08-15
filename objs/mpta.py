

class MPTA():
	"""docstring for ClassName"""
	def __init__(self, draw_tools, master_dict, controller, op_type):
		self.name = "MPTA"
		self.tag = "mpta"
		self.draw_tools = draw_tools
		self.dict = master_dict
		self.controller = controller
		self.side = None
		self.op_type = op_type

	def click(self, event):
		print("click from "+self.name)

	def draw(self):

		# loop left and right
		for side in ["LEFT","RIGHT"]:

			isKnee = False			
			isTamd = False

			tib_joint_p1 = self.dict["TAMD"][self.op_type][side]["TIB_JOINT_LINE"]["P1"]
			tib_joint_p2 = self.dict["TAMD"][self.op_type][side]["TIB_JOINT_LINE"]["P2"]

			knee = self.dict["MAIN"][self.op_type][side]["KNEE"]["P1"]

			ankle_p1 = self.dict["MAIN"][self.op_type][side]["ANKLE"]["P1"]
			ankle_p2 = self.dict["MAIN"][self.op_type][side]["ANKLE"]["P2"]
			ankle_m1 = self.dict["MAIN"][self.op_type][side]["ANKLE"]["M1"]


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


					L_tib, R_tib = self.draw_tools.retPointsLeftRight(tib_joint_p1, tib_joint_p2)

					if side == "RIGHT":
						angle = self.draw_tools.create_myAngle(R_tib, p_int, ankle_m1, self.tag)
						self.draw_tools.create_mytext(p_int, '{0:.2f}'.format(angle), self.tag, x_offset=60, y_offset=60)

					if side == "LEFT":
						angle = self.draw_tools.create_myAngle(ankle_m1, p_int, L_tib, self.tag)
						self.draw_tools.create_mytext(p_int, '{0:.2f}'.format(angle), self.tag, x_offset=-60, y_offset=60)


					# check if value exists
					if self.dict["EXCEL"][self.op_type][side]["MPTA"] == None:

						self.dict["EXCEL"][self.op_type][side]["HASDATA"] 	= True
						self.dict["EXCEL"][self.op_type][side]["MPTA"]	 	= '{0:.2f}'.format(angle)

						# save after insert
						self.controller.save_json()


	def update_canvas(self, draw_tools):
		self.draw_tools = draw_tools


	def update_dict(self, master_dict):
		self.dict = master_dict


	def unset(self):
		# print("unset from "+self.name)
		self.draw_tools.clear_by_tag(self.tag)	

		