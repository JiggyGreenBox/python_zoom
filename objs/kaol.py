import math

class KAOL():
	"""docstring for ClassName"""
	def __init__(self, draw_tools, master_dict, controller):
		self.name = "KAOL"
		self.tag = "kaol"
		self.draw_tools = draw_tools
		self.dict = master_dict		

		
	def click(self, event):
		print("click from "+self.name)
		# self.draw() 

		# print(self.slope((0,0),(10,10)))



	def slope(self, point1, point2):
		x1 = point1[0]
		y1 = point1[1]
		x2 = point2[0]
		y2 = point2[1]
		return (y2-y1)/(x2-x1)


	def draw(self):

		# loop left and right
		for side in ["LEFT","RIGHT"]:

			isTamd = False			

			tib_joint_p1 = self.dict["TAMD"][side]["TIB_JOINT_LINE"]["P1"]
			tib_joint_p2 = self.dict["TAMD"][side]["TIB_JOINT_LINE"]["P2"]
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
			# ANKLE
			if ankle_p1 != None and ankle_p2 != None:
				
				self.draw_tools.create_mypoint(ankle_p1, "white", self.tag)
				self.draw_tools.create_mypoint(ankle_p2, "white", self.tag)
				self.draw_tools.create_midpoint_line(ankle_p1, ankle_p2, ankle_m1, self.tag)



				# =============CLEAN UP==================================
				slope = self.slope(ankle_p1, ankle_p2)

				C = [0,0]
				# D = p1

				dy = math.sqrt(100**2/(slope**2+1))
				dx = -slope*dy
				# print("DX"+str(dx))
				# print("DY"+str(dy))
				C[0] = ankle_m1[0] + dx
				C[1] = ankle_m1[1] + dy
				# D[0] = m1[0] - dx
				# D[1] = m1[1] - dy

				print(C)
				# print(D)

				self.draw_tools.create_mypoint(C, "white", self.tag)
				# self.draw_tools.create_mypoint(D, "white", self.tag)

				# self.draw_tools.create_myline(C, D, self.tag)

				if isTamd:

					xtop, ytop, xbot, ybot = self.draw_tools.getImageCorners()

					# hip-knee ray
					p_top = self.draw_tools.line_intersection((ankle_m1, C),(xtop, ytop))
					self.draw_tools.create_myline(ankle_m1, p_top, self.tag)


					# find angle ray intersection point
					p_int = self.draw_tools.line_intersection((ankle_m1, p_top),(tib_joint_p1, tib_joint_p2))

					L_tib, R_tib = self.draw_tools.retPointsLeftRight(tib_joint_p1, tib_joint_p2)

					if side == "LEFT":
						angle = self.draw_tools.create_myAngle(ankle_m1, p_int, L_tib, self.tag)
						self.draw_tools.create_mytext(p_int, '{0:.2f}'.format(angle), self.tag, x_offset=60, y_offset=-60)

					if side == "RIGHT":
						angle = self.draw_tools.create_myAngle(R_tib, p_int, ankle_m1, self.tag)
						self.draw_tools.create_mytext(p_int, '{0:.2f}'.format(angle), self.tag, x_offset=-60, y_offset=-60)


	def update_canvas(self, draw_tools):
		self.draw_tools = draw_tools


	def update_dict(self, master_dict):
		self.dict = master_dict


	def unset(self):
		# print("unset from "+self.name)
		self.draw_tools.clear_by_tag(self.tag)	