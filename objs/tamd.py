

class TAMD():
	"""docstring for ClassName"""
	def __init__(self, draw_tools, master_dict, controller, op_type):
		self.name = "TAMD"
		self.tag = "tamd"
		self.menu_label = "TAMD_Menu"
		self.draw_tools = draw_tools
		self.dict = master_dict
		self.controller = controller
		self.side = None
		self.op_type = op_type


	def click(self, event):
		print("click from "+self.name)		
		self.draw()

		


	def hover(self, P_mouse, P_stored, hover_label):		
		pass

	def regainHover(self, side):
		pass
	def escapeObjFunc(self):
		pass


	# def checkMasterDict(self):
	# 	if "TAMD" not in self.dict.keys():
	# 		self.dict["TAMD"] = 	{
	# 								"PRE-OP":{
	# 										"LEFT":	{
	# 													"TIB_JOINT_LINE":	{"type":"line","P1":None,"P2":None}
	# 												},
	# 										"RIGHT":{
	# 													"TIB_JOINT_LINE":	{"type":"line","P1":None,"P2":None}
	# 												}
	# 										},

	# 								"POST-OP":{
	# 										"LEFT":	{
	# 													"TIB_JOINT_LINE":	{"type":"line","P1":None,"P2":None}
	# 												},
	# 										"RIGHT":{
	# 													"TIB_JOINT_LINE":	{"type":"line","P1":None,"P2":None}
	# 												}
	# 										}
	# 								}


	def addDict(self, event):
		pass


	def draw(self):

		self.draw_tools.clear_by_tag(self.tag)
		
		# loop left and right
		for side in ["LEFT","RIGHT"]:

			isTibTop = False
			isTibBot = False
			isKnee = False
			isAnkle = False
			

			tib_top_p1 	= self.dict["MAIN"][self.op_type][side]["AXIS_TIB"]["TOP"]["P1"]
			tib_top_p2 	= self.dict["MAIN"][self.op_type][side]["AXIS_TIB"]["TOP"]["P2"]
			top_m1 		= self.dict["MAIN"][self.op_type][side]["AXIS_TIB"]["TOP"]["M1"]

			tib_bot_p1 	= self.dict["MAIN"][self.op_type][side]["AXIS_TIB"]["BOT"]["P1"]
			tib_bot_p2 	= self.dict["MAIN"][self.op_type][side]["AXIS_TIB"]["BOT"]["P2"]
			bot_m1 		= self.dict["MAIN"][self.op_type][side]["AXIS_TIB"]["BOT"]["M1"]
			


			tib_knee 	= self.dict["MAIN"][self.op_type][side]["TIB_KNEE"]["P1"]
			ankle_p1 	= self.dict["MAIN"][self.op_type][side]["ANKLE"]["P1"]
			ankle_p2 	= self.dict["MAIN"][self.op_type][side]["ANKLE"]["P2"]
			ankle_m1 	= self.dict["MAIN"][self.op_type][side]["ANKLE"]["M1"]


			# # ------------------------
			# # FROM TAMD
			# # ------------------------
			# if tib_joint_p1 != None:
			# 	self.draw_tools.create_mypoint(tib_joint_p1, "orange", [self.tag, side, "P1_TIB_JOINT_LINE"])

			# if tib_joint_p2 != None:
			# 	self.draw_tools.create_mypoint(tib_joint_p2, "orange", [self.tag, side, "P2_TIB_JOINT_LINE"])

			# if tib_joint_p1 != None and tib_joint_p2 != None:
			# 	self.draw_tools.create_myline(tib_joint_p1, tib_joint_p2, [self.tag,side,"TIB_JOINT_LINE"])
			# 	isTamd = True

			# # ------------------------
			# # FROM MAIN
			# # ------------------------
			# # TIB AXIS



			# TOP
			if tib_top_p1 != None:
				self.draw_tools.create_mypoint(tib_top_p1, "orange", [self.tag, side, "NO-DRAG"])

			if tib_top_p2 != None:
				self.draw_tools.create_mypoint(tib_top_p2, "orange", [self.tag, side, "NO-DRAG"])

			if tib_top_p1 != None and tib_top_p2 != None:				
				self.draw_tools.create_midpoint_line(tib_top_p1, tib_top_p2, top_m1, self.tag)
				isTibTop = True


			# BOT
			if tib_bot_p1 != None:
				self.draw_tools.create_mypoint(tib_bot_p1, "orange", [self.tag, side, "NO-DRAG"])

			if tib_bot_p2 != None:
				self.draw_tools.create_mypoint(tib_bot_p2, "orange", [self.tag, side, "NO-DRAG"])

			if tib_bot_p1 != None and tib_bot_p2 != None:				
				self.draw_tools.create_midpoint_line(tib_bot_p1, tib_bot_p2, bot_m1, self.tag)
				isTibBot = True


			# tib knee
			if tib_knee != None:
				self.draw_tools.create_mypoint(tib_knee, "orange", [self.tag, side, "NO-DRAG"])
				isKnee = True


			# ankle
			if ankle_p1 != None:
				self.draw_tools.create_mypoint(ankle_p1, "orange", [self.tag, side, "NO-DRAG"])

			if ankle_p2 != None:
				self.draw_tools.create_mypoint(ankle_p2, "orange", [self.tag, side, "NO-DRAG"])

			if ankle_p1 != None and ankle_p2 != None:				
				self.draw_tools.create_midpoint_line(ankle_p1, ankle_p2, ankle_m1, self.tag)
				isAnkle = True


			if isTibTop and isTibBot and isKnee and isAnkle:

				xtop, ytop, xbot, ybot = self.draw_tools.getImageCorners()

				# TIB-AXIS ray
				# p_tib = self.draw_tools.line_intersection((bot_m1, top_m1),(xtop, ytop))
				# self.draw_tools.create_myline(bot_m1, p_tib, self.tag)
				self.draw_tools.create_myline(bot_m1, top_m1, self.tag)

				# TIB-KNEE - ANKLE line
				self.draw_tools.create_myline(tib_knee, ankle_m1, self.tag)


				p_int = self.draw_tools.line_intersection((bot_m1, top_m1),(tib_knee, ankle_m1))

				angle = self.draw_tools.getSmallestAngle(top_m1, p_int, tib_knee)
				angle2 = self.draw_tools.getAnglePoints(top_m1, p_int, tib_knee)
				angle3 = self.draw_tools.getAnglePointsNeg(top_m1, p_int, tib_knee)
				print('angle1: {0:.2f}'.format(angle))
				print('angle2: {0:.2f}'.format(angle2))
				print('angle3: {0:.2f}'.format(angle3))
				self.draw_tools.create_mytext(ankle_m1, '{0:.2f}'.format(angle), [self.tag,side,"TAMD_ANGLE"], x_offset=60, y_offset=60, color="blue")



				# check if value exists
				if self.dict["EXCEL"][self.op_type][side]["TAMD"] == None:
					self.dict["EXCEL"][self.op_type][side]["HASDATA"] 	= True
					self.dict["EXCEL"][self.op_type][side]["TAMD"]	 	= '{0:.2f}'.format(angle)
					# save after insert
					self.controller.save_json()


				# # find angle ray intersection point
				# p_int = self.draw_tools.line_intersection(
				# 		(p_tib, bot_m1),
				# 		(tib_joint_p1, tib_joint_p2))

			# 	L_tib, R_tib = self.draw_tools.retPointsLeftRight(tib_joint_p1, tib_joint_p2)

			# 	if side == "RIGHT":
			# 		angle = self.draw_tools.create_myAngle(R_tib, p_int, bot_m1, [self.tag,side,"TAMD_ANGLE"])
			# 		self.draw_tools.create_mytext(p_int, '{0:.2f}'.format(angle), [self.tag,side,"TAMD_ANGLE"], x_offset=60, y_offset=60)

			# 	if side == "LEFT":
			# 		angle = self.draw_tools.create_myAngle(bot_m1, p_int, L_tib, [self.tag,side,"TAMD_ANGLE"])
			# 		self.draw_tools.create_mytext(p_int, '{0:.2f}'.format(angle), [self.tag,side,"TAMD_ANGLE"], x_offset=-60, y_offset=60)		


			# 	# check if value exists
			# 	if self.dict["EXCEL"][self.op_type][side]["TAMD"] == None:

			# 		self.dict["EXCEL"][self.op_type][side]["HASDATA"] 	= True
			# 		self.dict["EXCEL"][self.op_type][side]["TAMD"]	 	= '{0:.2f}'.format(angle)

			# 		# save after insert
			# 		self.controller.save_json()



	def drag_start(self, tags):
		pass

	def drag(self, P_mouse):
		pass

	def drag_stop(self, P_mouse):
		pass
		

	# menu button clicks are routed here
	def menu_btn_click(self, action):
		pass


	def update_canvas(self, draw_tools):
		self.draw_tools = draw_tools


	def update_dict(self, master_dict):
		self.dict = master_dict


	def unset(self):
		# print("unset from "+self.name)
		self.draw_tools.clear_by_tag(self.tag)

		