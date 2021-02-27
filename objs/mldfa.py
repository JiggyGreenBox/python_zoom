

class MLDFA():
	"""docstring for ClassName"""
	def __init__(self, draw_tools, master_dict, controller, op_type):
		self.name = "MLDFA"
		self.tag = "mldfa"
		self.menu_label = "MLDFA_Menu"
		self.draw_tools = draw_tools
		self.dict = master_dict
		self.controller = controller
		self.side = None
		self.op_type = op_type

		# check if master dictionary has values
		# if not populate the dictionary
		# self.checkMasterDict()

		self.point_size = None

	def click(self, event):
		print("click from "+self.name)

		# if self.side == None:
		# 	print("please choose side")
		# 	self.controller.warningBox("Please select a Side")
		# else:
		# 	# print(self.dict)
		# 	ret =  self.addDict(event)
		# 	if ret:
		# 		self.controller.save_json()
		# 		# pass

		# self.controller.updateMenuLabel(self.getNextLabel(), self.menu_label)
		self.draw()



	def checkMasterDict(self):
		if "MLDFA" not in self.dict.keys():
			self.dict["MLDFA"] = 	{
									"PRE-OP": 	{
												"LEFT":	{
															"FEM_JOINT_LINE":	{"type":"line","P1":None,"P2":None}
														},
												"RIGHT":	{
															"FEM_JOINT_LINE":	{"type":"line","P1":None,"P2":None}
														}
												},
									"POST-OP": 	{
												"LEFT":	{
															"FEM_JOINT_LINE":	{"type":"line","P1":None,"P2":None}
														},
												"RIGHT":	{
															"FEM_JOINT_LINE":	{"type":"line","P1":None,"P2":None}
														}
												}
									}


	def addDict(self, event):
		for item in self.dict["MLDFA"][self.op_type][self.side]:
			
			# get real coords
			P = self.draw_tools.getRealCoords(event)

			# get item type 
			item_type = self.dict["MLDFA"][self.op_type][self.side][item]["type"]

			# line has P1 and P2
			if item_type == "line":

				# check if P1 is None				
				if self.dict["MLDFA"][self.op_type][self.side][item]["P1"] == None:					
					self.dict["MLDFA"][self.op_type][self.side][item]["P1"] = P
					self.draw_tools.setHoverPointLabel("P1_MLDFA")
					self.draw_tools.setHoverPoint(P)
					self.draw_tools.setHoverBool(True)
					return True


				# check if P2 is None				
				if self.dict["MLDFA"][self.op_type][self.side][item]["P2"] == None:					
					self.dict["MLDFA"][self.op_type][self.side][item]["P2"] = P
					self.draw_tools.setHoverBool(False)
					self.draw_tools.setHoverPointLabel(None)
					return True

		return False



	def draw(self):

		self.draw_tools.clear_by_tag(self.tag)

		self.point_size = self.controller.getViewPointSize()

		# loop left and right
		for side in ["LEFT","RIGHT"]:

			isHip = False
			isKnee = False
			isMldfa = False

			hip = self.dict["MAIN"][self.op_type][side]["HIP"]["P1"]
			knee = self.dict["MAIN"][self.op_type][side]["FEM_KNEE"]["P1"]

			fem_p1 = self.dict["MAIN"][self.op_type][side]["FEM_JOINT_LINE"]["P1"]
			fem_p2 = self.dict["MAIN"][self.op_type][side]["FEM_JOINT_LINE"]["P2"]

			# ------------------------
			# FROM MLDFA
			# ------------------------
			if fem_p1 != None:
				self.draw_tools.create_mypoint(fem_p1, "orange", [self.tag, side, "P1_MLDFA"], point_thickness=self.point_size)

			if fem_p2 != None:
				self.draw_tools.create_mypoint(fem_p2, "orange", [self.tag, side, "P2_MLDFA"], point_thickness=self.point_size)

			if fem_p1 != None and fem_p2 != None:
				self.draw_tools.create_myline(fem_p1, fem_p2, [self.tag,side,"LINE_MLDFA"])
				isMldfa = True


			# ------------------------
			# FROM MAIN
			# ------------------------
			# HIP
			if hip != None:
				isHip = True
				self.draw_tools.create_mypoint(hip, "orange", [self.tag, side, "NO-DRAG"], point_thickness=self.point_size)

			# KNEE
			if knee != None:
				isKnee = True
				self.draw_tools.create_mypoint(knee, "orange", [self.tag, side, "NO-DRAG"], point_thickness=self.point_size)


			if not isMldfa:
				if isHip and isKnee:
					# hip-knee line
					self.draw_tools.create_myline(hip, knee, self.tag)
			else:
				if isHip and isKnee:
					
					xtop, ytop, xbot, ybot = self.draw_tools.getImageCorners()

					# hip-knee ray
					p_bot = self.draw_tools.line_intersection(
						(hip, knee),
						(xbot, ybot))

					self.draw_tools.create_myline(hip, p_bot, self.tag)

					# find angle ray intersection point
					p_int = self.draw_tools.line_intersection(
							(hip, p_bot),
							(fem_p1, fem_p2))


						
					L_fem, R_fem = self.draw_tools.retPointsLeftRight(fem_p1, fem_p2)
						


					if side == "LEFT":
						angle = self.draw_tools.create_myAngle(hip, p_int, R_fem, [self.tag,side,"ANGLE_MLDFA"])
						self.draw_tools.create_mytext(p_int, '{0:.2f}'.format(angle), [self.tag,side,"ANGLE_MLDFA"], x_offset=60, y_offset=-60, color="blue")

					if side == "RIGHT":
						angle = self.draw_tools.create_myAngle(L_fem, p_int, hip, [self.tag,side,"ANGLE_MLDFA"])
						self.draw_tools.create_mytext(p_int, '{0:.2f}'.format(angle), [self.tag,side,"ANGLE_MLDFA"], x_offset=-60, y_offset=-60, color="blue")


					# check if value exists
					if self.dict["EXCEL"][self.op_type][side]["mLDFA"] == None:

						self.dict["EXCEL"][self.op_type][side]["HASDATA"] 	= True
						self.dict["EXCEL"][self.op_type][side]["mLDFA"]	 	= '{0:.2f}'.format(angle)

						# save after insert
						self.controller.save_json()

			
	# def hover(self, P_mouse, P_stored, hover_label):
	# 	if hover_label == "P1_MLDFA":
	# 		self.draw_tools.clear_by_tag("hover_line")
	# 		self.draw_tools.create_myline(P_mouse, P_stored, "hover_line")

	# def regainHover(self, side):
	# 	pass

	def escapeObjFunc(self):
		self.side = None
		self.draw_tools.setHoverPointLabel(None)
		self.draw_tools.setHoverBool(False)




	# def drag_start(self, tags):
	# 	tags.remove('token')
	# 	tags.remove('current')
	# 	tags.remove(self.tag)
	# 	print(tags)
		

	# 	side = ""

	# 	# find side
	# 	if "LEFT" in tags:
	# 		side = "LEFT"
	# 	elif "RIGHT" in tags:
	# 		side = "RIGHT"


	# 	if "P1_MLDFA" in tags:
	# 		self.drag_point = self.dict["MLDFA"][self.op_type][side]["FEM_JOINT_LINE"]["P2"]
	# 		self.drag_label = "P1_MLDFA"
	# 		self.drag_side 	= side
	# 	elif "P2_MLDFA" in tags:
	# 		self.drag_point = self.dict["MLDFA"][self.op_type][side]["FEM_JOINT_LINE"]["P1"]
	# 		self.drag_label = "P2_MLDFA"
	# 		self.drag_side 	= side

	# 	else:
	# 		self.drag_point = None
	# 		self.drag_label = None
	# 		self.drag_side 	= None

	# def drag(self, P_mouse):
	# 	if self.drag_label == "P1_MLDFA" and self.drag_point != None or self.drag_label == "P2_MLDFA" and self.drag_point != None:
	# 		self.draw_tools.clear_by_tag("LINE_MLDFA")
	# 		self.draw_tools.clear_by_tag("ANGLE_MLDFA")
	# 		self.draw_tools.clear_by_tag("drag_line")
	# 		self.draw_tools.create_myline(P_mouse, self.drag_point, "drag_line")


	# def drag_stop(self, P_mouse):
	# 	self.draw_tools.clear_by_tag("drag_line")

	# 	if self.drag_label == "P1_MLDFA":
	# 		self.dict["MLDFA"][self.op_type][self.drag_side]["FEM_JOINT_LINE"]["P1"] = P_mouse
	# 		self.dict["EXCEL"][self.op_type][self.drag_side]["mLDFA"] = None 	# delete excel data from pat.json
	# 		self.dict["EXCEL"][self.op_type][self.drag_side]["aLDFA"] = None 	# delete excel data from pat.json
	# 	elif self.drag_label == "P2_MLDFA":
	# 		self.dict["MLDFA"][self.op_type][self.drag_side]["FEM_JOINT_LINE"]["P2"] = P_mouse
	# 		self.dict["EXCEL"][self.op_type][self.drag_side]["mLDFA"] = None 	# delete excel data from pat.json
	# 		self.dict["EXCEL"][self.op_type][self.drag_side]["aLDFA"] = None 	# delete excel data from pat.json

	# 	self.controller.save_json()
	# 	self.draw()
	# P1_ALDFA
	# P2_ALDFA
	# LINE_ALDFA
	# ANGLE_ALDFA

	# menu button clicks are routed here
	# def menu_btn_click(self, action):
	# 	print(action)
	# 	if action == "SET-LEFT":
	# 		self.side = "LEFT"

	# 	if action == "SET-RIGHT":
	# 		self.side = "RIGHT"



	# 	if action == "DEL-LEFT-FEM-LINE":
	# 		self.dict["MLDFA"][self.op_type]["LEFT"]["FEM_JOINT_LINE"]["P1"] = None
	# 		self.dict["MLDFA"][self.op_type]["LEFT"]["FEM_JOINT_LINE"]["P2"] = None
	# 		self.dict["EXCEL"][self.op_type]["LEFT"]["mLDFA"] = None 	# delete excel data from pat.json
	# 		self.dict["EXCEL"][self.op_type]["LEFT"]["aLDFA"] = None 	# delete excel data from pat.json
	# 		self.draw()
	# 		self.controller.save_json()

	# 	if action == "DEL-RIGHT-FEM-LINE":
	# 		self.dict["MLDFA"][self.op_type]["RIGHT"]["FEM_JOINT_LINE"]["P1"] = None
	# 		self.dict["MLDFA"][self.op_type]["RIGHT"]["FEM_JOINT_LINE"]["P2"] = None
	# 		self.dict["EXCEL"][self.op_type]["RIGHT"]["mLDFA"] = None 	# delete excel data from pat.json
	# 		self.dict["EXCEL"][self.op_type]["LEFT"]["aLDFA"] = None 	# delete excel data from pat.json
	# 		self.draw()
	# 		self.controller.save_json()

	# 	self.controller.updateMenuLabel(self.getNextLabel(), self.menu_label)



	# def getNextLabel(self):

	# 	if self.side != None:

	# 		for item in self.dict["MLDFA"][self.op_type][self.side]:
				
	# 			# get item type 
	# 			item_type = self.dict["MLDFA"][self.op_type][self.side][item]["type"]

	# 			# line has P1 and P2
	# 			if item_type == "line":

	# 				# check if P1 is None				
	# 				if self.dict["MLDFA"][self.op_type][self.side][item]["P1"] == None:						
	# 					return (self.side + " " + item + " P1")


	# 				# check if P2 is None				
	# 				if self.dict["MLDFA"][self.op_type][self.side][item]["P2"] == None:						
	# 					return (self.side + " " + item + " P2")

	# 			return (self.side + " Done")

	# 	return None


	def update_canvas(self, draw_tools):
		self.draw_tools = draw_tools

	def update_dict(self, master_dict):
		self.dict = master_dict
		
	def unset(self):
		# print("unset from "+self.name)
		self.draw_tools.clear_by_tag(self.tag)


	def drag_start(self, P_mouse):
		pass
	def drag(self, P_mouse):
		pass
	def drag_stop(self, P_mouse):
		pass
	def menu_btn_click(self, action):
		pass
	def getNextLabel(self):
		pass
	def hover(self, P_mouse, P_stored, hover_label):
		pass
	def regainHover(self, side):
		pass

	# similiar to draw but nothing is drawn on the canvas
	def updateExcelValues(self):

		# loop left and right
		for side in ["LEFT","RIGHT"]:

			isHip = False
			isKnee = False
			isMldfa = False

			hip = self.dict["MAIN"][self.op_type][side]["HIP"]["P1"]
			knee = self.dict["MAIN"][self.op_type][side]["FEM_KNEE"]["P1"]

			fem_p1 = self.dict["MAIN"][self.op_type][side]["FEM_JOINT_LINE"]["P1"]
			fem_p2 = self.dict["MAIN"][self.op_type][side]["FEM_JOINT_LINE"]["P2"]

			# ------------------------
			# FROM MLDFA
			# ------------------------			
			if fem_p1 != None and fem_p2 != None:
				isMldfa = True


			# ------------------------
			# FROM MAIN
			# ------------------------
			# HIP
			if hip != None:
				isHip = True

			# KNEE
			if knee != None:
				isKnee = True


			if isMldfa and isHip and isKnee:
									
				xtop, ytop, xbot, ybot = self.draw_tools.getImageCorners()


				# find angle ray intersection point
				p_int = self.draw_tools.line_intersection(
						(hip, knee),
						(fem_p1, fem_p2))


					
				L_fem, R_fem = self.draw_tools.retPointsLeftRight(fem_p1, fem_p2)
					


				if side == "LEFT":
					# angle = self.draw_tools.create_myAngle(hip, p_int, R_fem, [self.tag,side,"ANGLE_MLDFA"])
					angle = self.draw_tools.getAnglePoints(hip, p_int, R_fem)

				if side == "RIGHT":
					# angle = self.draw_tools.create_myAngle(L_fem, p_int, hip, [self.tag,side,"ANGLE_MLDFA"])
					angle = self.draw_tools.getAnglePoints(L_fem, p_int, hip)


				# check if value exists
				if self.dict["EXCEL"][self.op_type][side]["mLDFA"] == None:
					self.dict["EXCEL"][self.op_type][side]["HASDATA"] 	= True
					self.dict["EXCEL"][self.op_type][side]["mLDFA"]	 	= '{0:.2f}'.format(angle)
					# save after insert
					self.controller.save_json()