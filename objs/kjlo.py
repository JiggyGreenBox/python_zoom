import math

class KJLO():
	"""docstring for ClassName"""
	def __init__(self, draw_tools, master_dict, controller):
		self.name = "KJLO"
		self.tag = "kjlo"
		self.draw_tools = draw_tools
		self.dict = master_dict		

		
	def click(self, event):
		print("click from "+self.name)
		# self.draw() 

		print(self.slope((0,0),(10,10)))



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
				self.draw_tools.create_midpoint_line(ankle_p1, ankle_p1, ankle_m1, self.tag)

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

			# not in left right loop
			L_tib_joint_p1 = self.dict["TAMD"]["LEFT"]["TIB_JOINT_LINE"]["P1"]
			L_tib_joint_p2 = self.dict["TAMD"]["LEFT"]["TIB_JOINT_LINE"]["P2"]
			R_tib_joint_p1 = self.dict["TAMD"]["RIGHT"]["TIB_JOINT_LINE"]["P1"]
			R_tib_joint_p2 = self.dict["TAMD"]["RIGHT"]["TIB_JOINT_LINE"]["P2"]




			# find points on edges
			if L_tib_joint_p1 != None and L_tib_joint_p2 != None:
				L_tib_joint_L_limit = self.draw_tools.line_intersection((L_tib_joint_p1, L_tib_joint_p2),(xtop, xbot))
				L_tib_joint_R_limit = self.draw_tools.line_intersection((L_tib_joint_p1, L_tib_joint_p2),(ytop, ybot))

				# intersection points
				p_int_L = self.draw_tools.line_intersection((p_top_L, p_left),(L_tib_joint_L_limit, L_tib_joint_R_limit))

				# draw angles
				L_angle = self.draw_tools.create_myAngle(p_left, p_int_L, L_tib_joint_L_limit, self.tag)
				self.draw_tools.create_mytext(p_int_L, '{0:.2f}'.format(L_angle), self.tag, x_offset=-60, y_offset=-60)

			if R_tib_joint_p1 != None and R_tib_joint_p2 != None:
				R_tib_joint_L_limit = self.draw_tools.line_intersection((R_tib_joint_p1, R_tib_joint_p2),(xtop, xbot))
				R_tib_joint_R_limit = self.draw_tools.line_intersection((R_tib_joint_p1, R_tib_joint_p2),(ytop, ybot))

				# intersection points
				p_int_R = self.draw_tools.line_intersection((p_top_R, p_right),(R_tib_joint_L_limit, R_tib_joint_R_limit))
				
				# draw angles
				R_angle = self.draw_tools.create_myAngle(R_tib_joint_R_limit, p_int_R, p_right, self.tag)
				self.draw_tools.create_mytext(p_int_R, '{0:.2f}'.format(R_angle), self.tag, x_offset=60, y_offset=-60)


	def update_canvas(self, draw_tools):
		self.draw_tools = draw_tools


	def update_dict(self, master_dict):
		self.dict = master_dict


	def unset(self):
		# print("unset from "+self.name)
		self.draw_tools.clear_by_tag(self.tag)		
	

						