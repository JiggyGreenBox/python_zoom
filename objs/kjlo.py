import math

class KJLO():
	"""docstring for ClassName"""
	def __init__(self, draw_tools, master_dict, controller, op_type):
		self.name = "KJLO"
		self.tag = "kjlo"
		self.menu_label = "KJLO_Menu"
		self.draw_tools = draw_tools
		self.dict = master_dict
		self.controller = controller
		self.side = None
		self.op_type = op_type

		# check if master dictionary has values
		# if not populate the dictionary
		self.checkMasterDict()

		self.point_size = None

	def checkMasterDict(self):
		if "KJLO" not in self.dict.keys():
			self.dict["KJLO"] = 	{
									"PRE-OP": 	{
												"LEFT":	{
															"JOINT_LINE":	{"type":"line","P1":None,"P2":None}
														},
												"RIGHT":	{
															"JOINT_LINE":	{"type":"line","P1":None,"P2":None}
														}
												},
									"POST-OP": 	{
												"LEFT":	{
															"JOINT_LINE":	{"type":"line","P1":None,"P2":None}
														},
												"RIGHT":	{
															"JOINT_LINE":	{"type":"line","P1":None,"P2":None}
														}
												}
									}
		
	def click(self, event):
		print("click from "+self.name)

		if self.side == None:
			print("please choose side")
			self.controller.warningBox("Please select a Side")
		else:
			# print(self.dict)
			ret =  self.addDict(event)
			if ret:
				self.controller.save_json()
				# pass

		self.controller.updateMenuLabel(self.getNextLabel(), self.menu_label)
		self.draw()


	def slope(self, point1, point2):
		x1 = point1[0]
		y1 = point1[1]
		x2 = point2[0]
		y2 = point2[1]
		return (y2-y1)/(x2-x1)

	def addDict(self, event):
		for item in self.dict["KJLO"][self.op_type][self.side]:
			
			# get real coords
			P = self.draw_tools.getRealCoords(event)

			# get item type 
			item_type = self.dict["KJLO"][self.op_type][self.side][item]["type"]

			# line has P1 and P2
			if item_type == "line":

				# check if P1 is None				
				if self.dict["KJLO"][self.op_type][self.side][item]["P1"] == None:					
					self.dict["KJLO"][self.op_type][self.side][item]["P1"] = P
					self.draw_tools.setHoverPointLabel("P1_KJLO")
					self.draw_tools.setHoverPoint(P)
					self.draw_tools.setHoverBool(True)
					return True


				# check if P2 is None				
				if self.dict["KJLO"][self.op_type][self.side][item]["P2"] == None:					
					self.dict["KJLO"][self.op_type][self.side][item]["P2"] = P
					self.draw_tools.setHoverBool(False)
					self.draw_tools.setHoverPointLabel(None)
					return True

		return False


	def draw(self):

		self.draw_tools.clear_by_tag(self.tag)

		self.point_size = self.controller.getViewPointSize()

		isLeftAnkle = False
		isRightAnkle = False

		# loop left and right
		for side in ["LEFT","RIGHT"]:

			isJointLine = False

			# tib_joint_p1 = self.dict["TAMD"][self.op_type][side]["TIB_JOINT_LINE"]["P1"]
			# tib_joint_p2 = self.dict["TAMD"][self.op_type][side]["TIB_JOINT_LINE"]["P2"]
			# tib_joint_p1 = self.dict["MPTA"][self.op_type][side]["TIB_JOINT_LINE"]["P1"]
			# tib_joint_p2 = self.dict["MPTA"][self.op_type][side]["TIB_JOINT_LINE"]["P2"]

			joint_p1 = self.dict["KJLO"][self.op_type][side]["JOINT_LINE"]["P1"]
			joint_p2 = self.dict["KJLO"][self.op_type][side]["JOINT_LINE"]["P2"]

			ankle_p1 = self.dict["MAIN"][self.op_type][side]["ANKLE"]["P1"]
			ankle_p2 = self.dict["MAIN"][self.op_type][side]["ANKLE"]["P2"]
			ankle_m1 = self.dict["MAIN"][self.op_type][side]["ANKLE"]["M1"]

			# ------------------------
			# FROM KJLO
			# ------------------------
			if joint_p1 != None:
				self.draw_tools.create_mypoint(joint_p1, "orange", [self.tag, side, "P1_JOINT_LINE"], point_thickness=self.point_size)

			if joint_p2 != None:
				self.draw_tools.create_mypoint(joint_p2, "orange", [self.tag, side, "P2_JOINT_LINE"], point_thickness=self.point_size)

			if joint_p1 != None and joint_p2 != None:
				self.draw_tools.create_myline(joint_p1, joint_p2, [self.tag,side,"LINE_KJLO"])
				isJointLine = True


			# ------------------------
			# FROM MAIN
			# ------------------------			
			# ANKLE
			if ankle_p1 != None and ankle_p2 != None:
				
				self.draw_tools.create_mypoint(ankle_p1, "orange", [self.tag, side, "NO-DRAG"], point_thickness=self.point_size)
				self.draw_tools.create_mypoint(ankle_p2, "orange", [self.tag, side, "NO-DRAG"], point_thickness=self.point_size)
				self.draw_tools.create_midpoint_line(ankle_p1, ankle_p2, ankle_m1, self.tag, point_thickness=self.point_size)

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

			# L_tib_joint_p1 = self.dict["MPTA"][self.op_type]["LEFT"]["TIB_JOINT_LINE"]["P1"]
			# L_tib_joint_p2 = self.dict["MPTA"][self.op_type]["LEFT"]["TIB_JOINT_LINE"]["P2"]
			# R_tib_joint_p1 = self.dict["MPTA"][self.op_type]["RIGHT"]["TIB_JOINT_LINE"]["P1"]
			# R_tib_joint_p2 = self.dict["MPTA"][self.op_type]["RIGHT"]["TIB_JOINT_LINE"]["P2"]

			L_tib_joint_p1 = self.dict["KJLO"][self.op_type]["LEFT"]["JOINT_LINE"]["P1"]
			L_tib_joint_p2 = self.dict["KJLO"][self.op_type]["LEFT"]["JOINT_LINE"]["P2"]
			R_tib_joint_p1 = self.dict["KJLO"][self.op_type]["RIGHT"]["JOINT_LINE"]["P1"]
			R_tib_joint_p2 = self.dict["KJLO"][self.op_type]["RIGHT"]["JOINT_LINE"]["P2"]




			# find points on edges
			if L_tib_joint_p1 != None and L_tib_joint_p2 != None:
				L_tib_joint_L_limit = self.draw_tools.line_intersection((L_tib_joint_p1, L_tib_joint_p2),(xtop, xbot))
				L_tib_joint_R_limit = self.draw_tools.line_intersection((L_tib_joint_p1, L_tib_joint_p2),(ytop, ybot))

				# intersection points
				p_int_L = self.draw_tools.line_intersection((p_top_L, L_ankle),(L_tib_joint_L_limit, L_tib_joint_R_limit))

				# find LR points
				LL_tib, LR_tib = self.draw_tools.retPointsLeftRight(L_tib_joint_p1, L_tib_joint_p2)

				# draw angles
				L_angle = self.draw_tools.create_myAngle(LR_tib, p_int_L, L_ankle, [self.tag,"ANGLE_KJLO"])
				self.draw_tools.create_mytext(p_int_L, '{0:.2f}'.format(L_angle), [self.tag,"ANGLE_KJLO"], x_offset=-60, y_offset=-60, color="blue")

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
				R_angle = self.draw_tools.create_myAngle(R_ankle, p_int_R, RL_tib, [self.tag,"ANGLE_KJLO"])
				self.draw_tools.create_mytext(p_int_R, '{0:.2f}'.format(R_angle), [self.tag,"ANGLE_KJLO"], x_offset=60, y_offset=-60, color="blue")

				# check if value exists
				if self.dict["EXCEL"][self.op_type]["RIGHT"]["KJLO"] == None:
					# print("enter right")

					self.dict["EXCEL"][self.op_type]["RIGHT"]["HASDATA"] 	= True
					self.dict["EXCEL"][self.op_type]["RIGHT"]["KJLO"]	 	= '{0:.2f}'.format(R_angle)

					# save after insert
					self.controller.save_json()	



	def drag_start(self, tags):
		tags.remove('token')
		tags.remove('current')
		tags.remove(self.tag)
		print(tags)
		

		side = ""

		# find side
		if "LEFT" in tags:
			side = "LEFT"
		elif "RIGHT" in tags:
			side = "RIGHT"


		if "P1_JOINT_LINE" in tags:
			self.drag_point = self.dict["KJLO"][self.op_type][side]["JOINT_LINE"]["P2"]
			self.drag_label = "P1_JOINT_LINE"
			self.drag_side 	= side
		elif "P2_JOINT_LINE" in tags:
			self.drag_point = self.dict["KJLO"][self.op_type][side]["JOINT_LINE"]["P1"]
			self.drag_label = "P2_JOINT_LINE"
			self.drag_side 	= side

		else:
			self.drag_point = None
			self.drag_label = None
			self.drag_side 	= None

	def drag(self, P_mouse):
		if self.drag_label == "P1_JOINT_LINE" and self.drag_point != None or self.drag_label == "P2_JOINT_LINE" and self.drag_point != None:
			self.draw_tools.clear_by_tag("LINE_KJLO")
			self.draw_tools.clear_by_tag("ANGLE_KJLO")			
			self.draw_tools.clear_by_tag("drag_line")
			self.draw_tools.create_myline(P_mouse, self.drag_point, "drag_line")

	def drag_stop(self, P_mouse):
		self.draw_tools.clear_by_tag("drag_line")

		if self.drag_label == "P1_JOINT_LINE":			
			self.dict["KJLO"][self.op_type][self.drag_side]["JOINT_LINE"]["P1"] = P_mouse
			self.dict["EXCEL"][self.op_type][self.drag_side]["KJLO"] = None 	# delete excel data from pat.json
			self.dict["EXCEL"][self.op_type][self.drag_side]["KAOL"] = None 	# delete excel data from pat.json
		elif self.drag_label == "P2_JOINT_LINE":
			self.dict["KJLO"][self.op_type][self.drag_side]["JOINT_LINE"]["P2"] = P_mouse
			self.dict["EXCEL"][self.op_type][self.drag_side]["KJLO"] = None 	# delete excel data from pat.json
			self.dict["EXCEL"][self.op_type][self.drag_side]["KAOL"] = None 	# delete excel data from pat.json

		self.controller.save_json()
		self.draw()

	def hover(self, P_mouse, P_stored, hover_label):
		if hover_label == "P1_KJLO":
			self.draw_tools.clear_by_tag("hover_line")
			self.draw_tools.create_myline(P_mouse, P_stored, "hover_line")

	def regainHover(self, side):
		pass

	def escapeObjFunc(self):
		self.side = None
		self.draw_tools.setHoverPointLabel(None)
		self.draw_tools.setHoverBool(False)


	# menu button clicks are routed here
	def menu_btn_click(self, action):
		print(action)
		if action == "SET-LEFT":
			self.side = "LEFT"

		if action == "SET-RIGHT":
			self.side = "RIGHT"



		if action == "DEL-LEFT-JOINT-LINE":
			self.dict["KJLO"][self.op_type]["LEFT"]["JOINT_LINE"]["P1"] = None
			self.dict["KJLO"][self.op_type]["LEFT"]["JOINT_LINE"]["P2"] = None
			self.dict["EXCEL"][self.op_type]["LEFT"]["KJLO"] = None 	# delete excel data from pat.json
			self.dict["EXCEL"][self.op_type]["LEFT"]["KAOL"] = None 	# delete excel data from pat.json
			self.draw()
			self.controller.save_json()

		if action == "DEL-RIGHT-JOINT-LINE":
			self.dict["KJLO"][self.op_type]["RIGHT"]["JOINT_LINE"]["P1"] = None
			self.dict["KJLO"][self.op_type]["RIGHT"]["JOINT_LINE"]["P2"] = None
			self.dict["EXCEL"][self.op_type]["RIGHT"]["KJLO"] = None 	# delete excel data from pat.json
			self.dict["EXCEL"][self.op_type]["RIGHT"]["KAOL"] = None 	# delete excel data from pat.json
			self.draw()
			self.controller.save_json()

		self.controller.updateMenuLabel(self.getNextLabel(), self.menu_label)



	def getNextLabel(self):

		if self.side != None:

			for item in self.dict["KJLO"][self.op_type][self.side]:
				
				# get item type 
				item_type = self.dict["KJLO"][self.op_type][self.side][item]["type"]

				# line has P1 and P2
				if item_type == "line":

					# check if P1 is None				
					if self.dict["KJLO"][self.op_type][self.side][item]["P1"] == None:						
						return (self.side + " " + item + " P1")


					# check if P2 is None				
					if self.dict["KJLO"][self.op_type][self.side][item]["P2"] == None:						
						return (self.side + " " + item + " P2")

				return (self.side + " Done")

		return None


	def update_canvas(self, draw_tools):
		self.draw_tools = draw_tools


	def update_dict(self, master_dict):
		self.dict = master_dict


	def unset(self):
		# print("unset from "+self.name)
		self.draw_tools.clear_by_tag(self.tag)		
	

						