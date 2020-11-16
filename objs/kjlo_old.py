import math

class KJLO():
	"""docstring for ClassName"""
	def __init__(self, draw_tools, master_dict, controller, op_type):
		self.name = "KJLO"
		self.tag = "kjlo"
		self.draw_tools = draw_tools
		self.dict = master_dict
		self.controller = controller
		self.op_type = op_type

		
	def click(self, event):
		print("click from "+self.name)
		self.draw() 

		# print(self.slope((0,0),(10,10)))



	def slope(self, point1, point2):
		x1 = point1[0]
		y1 = point1[1]
		x2 = point2[0]
		y2 = point2[1]
		return (y2-y1)/(x2-x1)


	def draw(self):

		self.draw_tools.clear_by_tag(self.tag)

		isLeftAnkle = False
		isRightAnkle = False

		# loop left and right
		for side in ["LEFT","RIGHT"]:

			isTamd = False

			# tib_joint_p1 = self.dict["TAMD"][self.op_type][side]["TIB_JOINT_LINE"]["P1"]
			# tib_joint_p2 = self.dict["TAMD"][self.op_type][side]["TIB_JOINT_LINE"]["P2"]
			tib_joint_p1 = self.dict["MPTA"][self.op_type][side]["TIB_JOINT_LINE"]["P1"]
			tib_joint_p2 = self.dict["MPTA"][self.op_type][side]["TIB_JOINT_LINE"]["P2"]

			ankle_p1 = self.dict["MAIN"][self.op_type][side]["ANKLE"]["P1"]
			ankle_p2 = self.dict["MAIN"][self.op_type][side]["ANKLE"]["P2"]
			ankle_m1 = self.dict["MAIN"][self.op_type][side]["ANKLE"]["M1"]

			# ------------------------
			# FROM TAMD
			# ------------------------
			if tib_joint_p1 != None:
				self.draw_tools.create_mypoint(tib_joint_p1, "orange", [self.tag, side, "NO-DRAG"])

			if tib_joint_p2 != None:
				self.draw_tools.create_mypoint(tib_joint_p2, "orange", [self.tag, side, "NO-DRAG"])

			if tib_joint_p1 != None and tib_joint_p2 != None:
				self.draw_tools.create_myline(tib_joint_p1, tib_joint_p2, self.tag)
				isTamd = True


			# ------------------------
			# FROM MAIN
			# ------------------------			
			# ANKLE
			if ankle_p1 != None and ankle_p2 != None:
				
				self.draw_tools.create_mypoint(ankle_p1, "orange", [self.tag, side, "NO-DRAG"])
				self.draw_tools.create_mypoint(ankle_p2, "orange", [self.tag, side, "NO-DRAG"])
				self.draw_tools.create_midpoint_line(ankle_p1, ankle_p2, ankle_m1, self.tag)

				if side == "RIGHT":
					isRightAnkle = True

				if side == "LEFT":
					isLeftAnkle = True



		if isLeftAnkle and isRightAnkle:
			L_ankle = self.dict["MAIN"][self.op_type]["LEFT"]["ANKLE"]["M1"]
			R_ankle = self.dict["MAIN"][self.op_type]["RIGHT"]["ANKLE"]["M1"]

			# join ankles
			self.draw_tools.create_myline(L_ankle, R_ankle, self.tag)

			slope = self.slope(L_ankle, R_ankle)

			# points perpendicular to LR-ankle-line
			L = [0,0]
			R = [0,0]
			# D = p1

			dy = math.sqrt(100**2/(slope**2+1))
			dx = -slope*dy
			# print("DX"+str(dx))
			# print("DY"+str(dy))
			L[0] = L_ankle[0] + dx
			L[1] = L_ankle[1] + dy

			R[0] = R_ankle[0] + dx
			R[1] = R_ankle[1] + dy

			# self.draw_tools.create_mypoint(L, "orange", [self.tag, side, "NO-DRAG"])
			# self.draw_tools.create_mypoint(R, "orange", [self.tag, side, "NO-DRAG"])

			xtop, ytop, xbot, ybot = self.draw_tools.getImageCorners()

			# hip-knee ray
			p_top_L = self.draw_tools.line_intersection(
				(L_ankle, L),
				(xtop, ytop))

			p_top_R = self.draw_tools.line_intersection(
				(R_ankle, R),
				(xtop, ytop))

			self.draw_tools.create_myline(L_ankle, p_top_L, self.tag)
			self.draw_tools.create_myline(R_ankle, p_top_R, self.tag)

			# not in left right loop
			# L_tib_joint_p1 = self.dict["TAMD"][self.op_type]["LEFT"]["TIB_JOINT_LINE"]["P1"]
			# L_tib_joint_p2 = self.dict["TAMD"][self.op_type]["LEFT"]["TIB_JOINT_LINE"]["P2"]
			# R_tib_joint_p1 = self.dict["TAMD"][self.op_type]["RIGHT"]["TIB_JOINT_LINE"]["P1"]
			# R_tib_joint_p2 = self.dict["TAMD"][self.op_type]["RIGHT"]["TIB_JOINT_LINE"]["P2"]

			L_tib_joint_p1 = self.dict["MPTA"][self.op_type]["LEFT"]["TIB_JOINT_LINE"]["P1"]
			L_tib_joint_p2 = self.dict["MPTA"][self.op_type]["LEFT"]["TIB_JOINT_LINE"]["P2"]
			R_tib_joint_p1 = self.dict["MPTA"][self.op_type]["RIGHT"]["TIB_JOINT_LINE"]["P1"]
			R_tib_joint_p2 = self.dict["MPTA"][self.op_type]["RIGHT"]["TIB_JOINT_LINE"]["P2"]




			# find points on edges
			if L_tib_joint_p1 != None and L_tib_joint_p2 != None:
				L_tib_joint_L_limit = self.draw_tools.line_intersection((L_tib_joint_p1, L_tib_joint_p2),(xtop, xbot))
				L_tib_joint_R_limit = self.draw_tools.line_intersection((L_tib_joint_p1, L_tib_joint_p2),(ytop, ybot))

				# intersection points
				p_int_L = self.draw_tools.line_intersection((p_top_L, L_ankle),(L_tib_joint_L_limit, L_tib_joint_R_limit))

				# find LR points
				LL_tib, LR_tib = self.draw_tools.retPointsLeftRight(L_tib_joint_p1, L_tib_joint_p2)

				# draw angles
				L_angle = self.draw_tools.create_myAngle(LR_tib, p_int_L, L_ankle, self.tag)
				self.draw_tools.create_mytext(p_int_L, '{0:.2f}'.format(L_angle), self.tag, x_offset=-60, y_offset=-60)

				# check if value exists
				if self.dict["EXCEL"][self.op_type]["LEFT"]["KJLO"] == None:
					# print("enter left")

					self.dict["EXCEL"][self.op_type]["LEFT"]["HASDATA"] 	= True
					self.dict["EXCEL"][self.op_type]["LEFT"]["KJLO"]	 	= '{0:.2f}'.format(L_angle)

					# save after insert
					self.controller.save_json()	


			if R_tib_joint_p1 != None and R_tib_joint_p2 != None:
				R_tib_joint_L_limit = self.draw_tools.line_intersection((R_tib_joint_p1, R_tib_joint_p2),(xtop, xbot))
				R_tib_joint_R_limit = self.draw_tools.line_intersection((R_tib_joint_p1, R_tib_joint_p2),(ytop, ybot))

				# intersection points
				p_int_R = self.draw_tools.line_intersection((p_top_R, R_ankle),(R_tib_joint_L_limit, R_tib_joint_R_limit))

				# find LR points
				RL_tib, RR_tib = self.draw_tools.retPointsLeftRight(R_tib_joint_p1, R_tib_joint_p2)
				
				# draw angles
				R_angle = self.draw_tools.create_myAngle(R_ankle, p_int_R, RL_tib, self.tag)
				self.draw_tools.create_mytext(p_int_R, '{0:.2f}'.format(R_angle), self.tag, x_offset=60, y_offset=-60)

				# check if value exists
				if self.dict["EXCEL"][self.op_type]["RIGHT"]["KJLO"] == None:
					# print("enter right")

					self.dict["EXCEL"][self.op_type]["RIGHT"]["HASDATA"] 	= True
					self.dict["EXCEL"][self.op_type]["RIGHT"]["KJLO"]	 	= '{0:.2f}'.format(R_angle)

					# save after insert
					self.controller.save_json()	



	def drag_start(self, tags):
		pass		
	def drag(self, P_mouse):
		pass
	def drag_stop(self, P_mouse):
		self.draw()
	def hover(self, P_mouse, P_stored, hover_label):
		pass
	def regainHover(self, side):
		pass
	def escapeObjFunc(self):
		pass


	def update_canvas(self, draw_tools):
		self.draw_tools = draw_tools


	def update_dict(self, master_dict):
		self.dict = master_dict


	def unset(self):
		# print("unset from "+self.name)
		self.draw_tools.clear_by_tag(self.tag)		
	

						