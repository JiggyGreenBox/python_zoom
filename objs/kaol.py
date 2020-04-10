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

		isLeftAnkle = False
		isRightAnkle = False

		# loop left and right
		for side in ["LEFT","RIGHT"]:

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
			# ANKLE
			if self.dict["MAIN"][side]["ANKLE"]["P1"] != None and self.dict["MAIN"][side]["ANKLE"]["P2"] != None:


				p1 = self.dict["MAIN"][side]["ANKLE"]["P1"]
				p2 = self.dict["MAIN"][side]["ANKLE"]["P2"]
				m1 = self.dict["MAIN"][side]["ANKLE"]["M1"]
				self.draw_tools.create_mypoint(p1, "white", self.tag)
				self.draw_tools.create_mypoint(p2, "white", self.tag)
				self.draw_tools.create_midpoint_line(p1, p2, m1, self.tag)

				if side == "RIGHT":
					isRightAnkle = True

				if side == "LEFT":
					isLeftAnkle = True

		if isLeftAnkle and isRightAnkle:
			p_left = self.dict["MAIN"]["LEFT"]["ANKLE"]["M1"]
			p_right = self.dict["MAIN"]["RIGHT"]["ANKLE"]["M1"]

			self.draw_tools.create_myline(p_left, p_right, self.tag)

			slope = self.slope(p_left, p_right)


			L = [0,0]
			R = [0,0]
			# D = p1

			dy = math.sqrt(100**2/(slope**2+1))
			dx = -slope*dy
			# print("DX"+str(dx))
			# print("DY"+str(dy))
			L[0] = p_left[0] + dx
			L[1] = p_left[1] + dy

			R[0] = p_right[0] + dx
			R[1] = p_right[1] + dy

			self.draw_tools.create_mypoint(L, "white", self.tag)
			self.draw_tools.create_mypoint(R, "white", self.tag)

			xtop, ytop, xbot, ybot = self.draw_tools.getImageCorners()

			# hip-knee ray
			p_top_L = self.draw_tools.line_intersection(
				(p_left, L),
				(xtop, ytop))

			p_top_R = self.draw_tools.line_intersection(
				(p_right, R),
				(xtop, ytop))

			self.draw_tools.create_myline(p_left, p_top_L, self.tag)
			self.draw_tools.create_myline(p_right, p_top_R, self.tag)


	def update_canvas(self, draw_tools):
		self.draw_tools = draw_tools

	def unset(self):
		print("unset from "+self.name)
		self.draw_tools.clear_by_tag(self.tag)		

						