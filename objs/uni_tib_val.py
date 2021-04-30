import math

class UNI_TIB_VAL():
	"""docstring for ClassName"""
	def __init__(self, draw_tools, master_dict, controller, op_type):
		self.name = "UNI_TIB_VAL"
		self.tag = "uni_tib_val"
		self.menu_label = "UNI_TIB_VAL_Menu"
		self.draw_tools = draw_tools
		self.dict = master_dict
		self.controller = controller
		self.side = None
		self.op_type = op_type

		# check if master dictionary has values
		# if not populate the dictionary
		self.checkMasterDict()

		self.point_size = None

		self.draw_labels = True
		self.draw_hover = True


	def click(self, event):
		# print("click from "+self.name)
		# self.draw()
		if self.side == None:
			print("please choose side")
			self.controller.warningBox("Please select a Side")
		else:
			ret =  self.addDict(event)
			# find if P0 hovers are required
			self.mainHoverUsingNextLabel()
			if ret:				
				self.controller.save_json()
				# pass

		self.controller.updateMenuLabel(self.getNextLabel(), self.menu_label)		
		self.draw()


	# menu button clicks are routed here
	def menu_btn_click(self, action):
		print(action)
		if action == "SET-LEFT":
			self.side = "LEFT"
			self.draw()
			self.regainHover(self.side)
			self.controller.updateMenuLabel(self.getNextLabel(), self.menu_label)
			return # avoid clear,draw,json_save

		if action == "SET-RIGHT":
			self.side = "RIGHT"
			self.draw()
			self.regainHover(self.side)
			self.controller.updateMenuLabel(self.getNextLabel(), self.menu_label)
			return # avoid clear,draw,json_save

		if action == "DEL-LEFT-FEM-LINE":
			self.dict["UNI_TIB_VAL"][self.op_type]["LEFT"]["TIB_JOINT_LINE"]["P1"] = None
			self.dict["UNI_TIB_VAL"][self.op_type]["LEFT"]["TIB_JOINT_LINE"]["P2"] = None
			self.side = "LEFT"

		if action == "DEL-RIGHT-FEM-LINE":
			self.dict["UNI_TIB_VAL"][self.op_type]["RIGHT"]["TIB_JOINT_LINE"]["P1"] = None
			self.dict["UNI_TIB_VAL"][self.op_type]["RIGHT"]["TIB_JOINT_LINE"]["P2"] = None
			self.side = "RIGHT"

		if action == "DEL-LEFT-TIB-TOP":			
			self.dict["UNI_TIB_VAL"][self.op_type]["LEFT"]["AXIS_TIB"]["TOP"]["P1"] = None
			self.dict["UNI_TIB_VAL"][self.op_type]["LEFT"]["AXIS_TIB"]["TOP"]["P2"] = None
			self.dict["UNI_TIB_VAL"][self.op_type]["LEFT"]["AXIS_TIB"]["TOP"]["M1"] = None
			self.side = "LEFT"

		if action == "DEL-RIGHT-TIB-TOP":
			self.dict["UNI_TIB_VAL"][self.op_type]["RIGHT"]["AXIS_TIB"]["TOP"]["P1"] = None
			self.dict["UNI_TIB_VAL"][self.op_type]["RIGHT"]["AXIS_TIB"]["TOP"]["P2"] = None
			self.dict["UNI_TIB_VAL"][self.op_type]["RIGHT"]["AXIS_TIB"]["TOP"]["M1"] = None
			self.side = "RIGHT"

		if action == "DEL-LEFT-TIB-BOT":
			self.dict["UNI_TIB_VAL"][self.op_type]["LEFT"]["AXIS_TIB"]["BOT"]["P1"] = None
			self.dict["UNI_TIB_VAL"][self.op_type]["LEFT"]["AXIS_TIB"]["BOT"]["P2"] = None
			self.dict["UNI_TIB_VAL"][self.op_type]["LEFT"]["AXIS_TIB"]["BOT"]["M1"] = None
			self.side = "LEFT"

		if action == "DEL-RIGHT-TIB-BOT":
			self.dict["UNI_TIB_VAL"][self.op_type]["RIGHT"]["AXIS_TIB"]["BOT"]["P1"] = None
			self.dict["UNI_TIB_VAL"][self.op_type]["RIGHT"]["AXIS_TIB"]["BOT"]["P2"] = None
			self.dict["UNI_TIB_VAL"][self.op_type]["RIGHT"]["AXIS_TIB"]["BOT"]["M1"] = None
			self.side = "RIGHT"

		# delete excel data from pat.json
		self.dict["EXCEL"][self.op_type][self.side]["TVAR/VAL"] = None

		self.draw()
		self.regainHover(self.side)
		self.controller.save_json()
		self.controller.updateMenuLabel(self.getNextLabel(), self.menu_label)	




	def draw(self):

		self.draw_tools.clear_by_tag(self.tag)

		self.point_size = self.controller.getViewPointSize()
		
		# loop left and right				
		for side in ["LEFT","RIGHT"]:

			isTibJointLine = False
			isTibTop 	= False
			isTibBot 	= False

			# TIB JOINT LINE
			tib_joint_p1 = self.dict[self.name][self.op_type][side]["TIB_JOINT_LINE"]["P1"]
			tib_joint_p2 = self.dict[self.name][self.op_type][side]["TIB_JOINT_LINE"]["P2"]


			# TIB JOINT LINE
			if tib_joint_p1 != None:
				self.draw_tools.create_mypoint(tib_joint_p1, "orange", [self.tag,side,"TIB_JOINT_LINE","P1"], point_thickness=self.point_size)

			if tib_joint_p2 != None:
				self.draw_tools.create_mypoint(tib_joint_p2, "orange", [self.tag,side,"TIB_JOINT_LINE","P2"], point_thickness=self.point_size)

			if tib_joint_p1 != None and tib_joint_p2 != None:
				self.draw_tools.create_myline(tib_joint_p1, tib_joint_p2, [self.tag,side,"TIB_LINE"])
				isTibJointLine = True


			# TIB AXIS
			# TOP
			top_axis_tib_p1 = self.dict[self.name][self.op_type][side]["AXIS_TIB"]["TOP"]["P1"]
			top_axis_tib_p2 = self.dict[self.name][self.op_type][side]["AXIS_TIB"]["TOP"]["P2"]
			top_axis_tib_m1 = self.dict[self.name][self.op_type][side]["AXIS_TIB"]["TOP"]["M1"]
			# BOT
			bot_axis_tib_p1 = self.dict[self.name][self.op_type][side]["AXIS_TIB"]["BOT"]["P1"]
			bot_axis_tib_p2 = self.dict[self.name][self.op_type][side]["AXIS_TIB"]["BOT"]["P2"]			
			bot_axis_tib_m1 = self.dict[self.name][self.op_type][side]["AXIS_TIB"]["BOT"]["M1"]


			if top_axis_tib_p1 != None:
				self.draw_tools.create_mypoint(top_axis_tib_p1, "orange", [self.tag,side,"AXIS_TIB","TOP","P1"], point_thickness=self.point_size)

			if top_axis_tib_p2 != None:
				self.draw_tools.create_mypoint(top_axis_tib_p2, "orange", [self.tag,side,"AXIS_TIB","TOP","P2"], point_thickness=self.point_size)

			if top_axis_tib_p1 != None and top_axis_tib_p2 != None:				
				
				self.draw_tools.create_midpoint_line(top_axis_tib_p1, top_axis_tib_p2, top_axis_tib_m1, [self.tag,side,"TOP_AXIS_LINE"], point_thickness=self.point_size)
				isTibTop = True


			# BOT
			if bot_axis_tib_p1 != None:
				self.draw_tools.create_mypoint(bot_axis_tib_p1, "orange", [self.tag,side,"AXIS_TIB","BOT","P1"], point_thickness=self.point_size)

			if bot_axis_tib_p2 != None:
				self.draw_tools.create_mypoint(bot_axis_tib_p2, "orange", [self.tag,side,"AXIS_TIB","BOT","P2"], point_thickness=self.point_size)

			if bot_axis_tib_p1 != None and bot_axis_tib_p2 != None:				
				# m1 = self.dict["UNI_TIB_VAL"][self.op_type][side]["AXIS_TIB"]["TOP"]["M1"]
				self.draw_tools.create_midpoint_line(bot_axis_tib_p1, bot_axis_tib_p2, bot_axis_tib_m1, [self.tag,side,"BOT_AXIS_LINE"], point_thickness=self.point_size)
				isTibBot = True

			# if isFemJointLine and isFemTop and isFemBot:
			if isTibTop and isTibBot:

				xtop, ytop, xbot, ybot = self.draw_tools.getImageCorners()

				# join center points of axes, and extend till the top of the frame
				U_m1, D_m1 = self.draw_tools.retPointsUpDown(top_axis_tib_m1, bot_axis_tib_m1)
				
				p_top = self.draw_tools.line_intersection((D_m1, U_m1), (xtop, ytop))
				self.draw_tools.create_myline(D_m1, p_top, self.tag)


				if isTibJointLine:

					TibP_L, TibP_R = self.draw_tools.retPointsLeftRight(tib_joint_p1, tib_joint_p2)

					p_int = self.draw_tools.line_intersection((tib_joint_p1, tib_joint_p2), (p_top, D_m1))

					# find angle between tibjointline and tib axis
					# if less than 90
						# T-FLEX-EXT = angle-90
							# 80-90 = -10 negative value VARUS							
					# else if more than 90
						# T-FLEX-EXT = angle-90
							# 110 - 90 = 20 keep positive value (VALGUS)

					if side == "LEFT":
						tib_line_axis_angle = self.draw_tools.getSmallestAngle(TibP_L, p_int, D_m1)						
					else:
						tib_line_axis_angle = self.draw_tools.getSmallestAngle(TibP_R, p_int, D_m1)

					# print('{0:.1f} tib_line_axis_angle'.format(tib_line_axis_angle))
					tflexext = (tib_line_axis_angle-90)*-1
					# tflexext = tib_line_axis_angle-90
					# if tib_line_axis_angle > 90:
					# 	tflexext = tib_line_axis_angle-90
					# else:
					# 	tflexext = tib_line_axis_angle-90



					# print info
					
					if side == "LEFT":
						self.draw_tools.create_mytext(TibP_L, '{0:.1f}'.format(tflexext), self.tag, y_offset=-80, color="blue")
						self.draw_tools.create_mytext(TibP_L, '{0:.1f}'.format(tib_line_axis_angle), self.tag, y_offset=80, color="blue")
					else:
						self.draw_tools.create_mytext(TibP_R, '{0:.1f}'.format(tflexext), self.tag, y_offset=-80, color="blue")
						self.draw_tools.create_mytext(TibP_R, '{0:.1f}'.format(tib_line_axis_angle), self.tag, y_offset=80, color="blue")


					# save to excel
					# T-VAR-VAL
					if self.dict["EXCEL"][self.op_type][side]["TVAR/VAL"] == None:
						self.dict["EXCEL"][self.op_type][side]["HASDATA"] 	= True
						self.dict["EXCEL"][self.op_type][side]["TVAR/VAL"]	= '{0:.1f}'.format(tflexext)
						self.controller.save_json()					



					'''
					# fem to axis intersection
					p_int = self.draw_tools.line_intersection((tib_joint_p1, tib_joint_p2), (p_top, D_m1))
					self.draw_tools.create_mypoint(p_int, "orange", [self.tag, side, "NO-DRAG"], point_thickness=self.point_size)

					# find parallel point
					# slope = self.slope(U_m1, D_m1)
					slope = self.draw_tools.slope(U_m1, D_m1)
					dy = math.sqrt(100**2/(slope**2+1))
					dx = -slope*dy

					C = [0,0]
					C[0] = p_int[0] + dx
					C[1] = p_int[1] + dy

					# self.draw_tools.create_mypoint(C, "orange", [self.tag, side, "NO-DRAG"], point_thickness=self.point_size)

					# find L R point
					L_fem, R_fem = self.draw_tools.retPointsLeftRight(tib_joint_p1, tib_joint_p2)

					if side == "LEFT":
						L_p_border = self.draw_tools.line_intersection((C, p_int), (ytop, ybot))
						self.draw_tools.create_myline(L_p_border, p_int, self.tag)

						a1 = self.draw_tools.getAnglePoints(L_p_border, p_int, R_fem)
						a2 = self.draw_tools.getAnglePoints(R_fem, p_int, L_p_border)
						print('{0:.1f} a1 left'.format(a1))
						print('{0:.1f} a2 left'.format(a2))

						if a1 > a2:						
							angle = self.draw_tools.create_myAngle(R_fem, p_int, L_p_border, self.tag)
						else:
							angle = self.draw_tools.create_myAngle(L_p_border, p_int, R_fem, self.tag)
						self.draw_tools.create_mytext(R_fem, '{0:.1f}'.format(angle), self.tag, x_offset=60)



					if side == "RIGHT":
						R_p_border = self.draw_tools.line_intersection((C, p_int), (xtop, xbot))
						self.draw_tools.create_myline(R_p_border, p_int, self.tag)


						a1 = self.draw_tools.getAnglePoints(R_p_border, p_int, L_fem)
						a2 = self.draw_tools.getAnglePoints(L_fem, p_int, R_p_border)
						print('{0:.1f} a1 RIGHT'.format(a1))
						print('{0:.1f} a2 RIGHT'.format(a2))

						if a1 > a2:						
							angle = self.draw_tools.create_myAngle(L_fem, p_int, R_p_border, self.tag)
						else:
							angle = self.draw_tools.create_myAngle(R_p_border, p_int, L_fem, self.tag)
							
						self.draw_tools.create_mytext(L_fem, '{0:.1f}'.format(angle), self.tag, x_offset=-60)
					'''




	def checkMasterDict(self):
		if "UNI_TIB_VAL" not in self.dict.keys():
			self.dict["UNI_TIB_VAL"] = 	{
										"PRE-OP":{
											"LEFT":	{
														"AXIS_TIB":	{
																		"type":	"axis",
																		"TOP":	{"type":"midpoint","P1":None,"P2":None, "M1":None},
																		"BOT":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
																	},
														"TIB_JOINT_LINE":	{"type":"line","P1":None,"P2":None}
													},
											"RIGHT":	{
														"AXIS_TIB":	{
																		"type":	"axis",
																		"TOP":	{"type":"midpoint","P1":None,"P2":None, "M1":None},
																		"BOT":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
																	},
														"TIB_JOINT_LINE":	{"type":"line","P1":None,"P2":None}
													}
										},
										"POST-OP":{
											"LEFT":	{
														"AXIS_TIB":	{
																		"type":	"axis",
																		"TOP":	{"type":"midpoint","P1":None,"P2":None, "M1":None},
																		"BOT":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
																	},
														"TIB_JOINT_LINE":	{"type":"line","P1":None,"P2":None}
													},
											"RIGHT":	{
														"AXIS_TIB":	{
																		"type":	"axis",
																		"TOP":	{"type":"midpoint","P1":None,"P2":None, "M1":None},
																		"BOT":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
																	},
														"TIB_JOINT_LINE":	{"type":"line","P1":None,"P2":None}
													}
										}
									}


	def addDict(self, event):
		for item in self.dict["UNI_TIB_VAL"][self.op_type][self.side]:

			# get real coords
			P = self.draw_tools.getRealCoords(event)

			# get item type 
			item_type = self.dict["UNI_TIB_VAL"][self.op_type][self.side][item]["type"]
			
			
			# axis has two midpoints
			if item_type == "axis":
				print("axis" + item)
				# axis has a top and a bottom

				# check if P1 is None
				if self.dict["UNI_TIB_VAL"][self.op_type][self.side][item]["TOP"]["P1"] == None:					
					self.dict["UNI_TIB_VAL"][self.op_type][self.side][item]["TOP"]["P1"] = P
					self.draw_tools.setHoverPointLabel("P1_"+item+"_TOP")
					self.draw_tools.setHoverPoint(P)
					self.draw_tools.setHoverBool(True)
					return True

				# check if P2 is None				
				if self.dict["UNI_TIB_VAL"][self.op_type][self.side][item]["TOP"]["P2"] == None:					
					self.dict["UNI_TIB_VAL"][self.op_type][self.side][item]["TOP"]["P2"] = P
					M = self.draw_tools.midpoint(self.dict["UNI_TIB_VAL"][self.op_type][self.side][item]["TOP"]["P1"], P)
					self.dict["UNI_TIB_VAL"][self.op_type][self.side][item]["TOP"]["M1"] = M
					self.draw_tools.setHoverBool(False)
					self.draw_tools.setHoverPointLabel(None)
					return True


				# check if P1 is None
				if self.dict["UNI_TIB_VAL"][self.op_type][self.side][item]["BOT"]["P1"] == None:					
					self.dict["UNI_TIB_VAL"][self.op_type][self.side][item]["BOT"]["P1"] = P
					self.draw_tools.setHoverPointLabel("P1_"+item+"_BOT")
					self.draw_tools.setHoverPoint(P)
					self.draw_tools.setHoverBool(True)
					return True

				# check if P2 is None				
				if self.dict["UNI_TIB_VAL"][self.op_type][self.side][item]["BOT"]["P2"] == None:					
					self.dict["UNI_TIB_VAL"][self.op_type][self.side][item]["BOT"]["P2"] = P
					M = self.draw_tools.midpoint(self.dict["UNI_TIB_VAL"][self.op_type][self.side][item]["BOT"]["P1"], P)
					self.dict["UNI_TIB_VAL"][self.op_type][self.side][item]["BOT"]["M1"] = M
					self.draw_tools.setHoverBool(False)
					self.draw_tools.setHoverPointLabel(None)
					return True	


			# line has P1 and P2
			if item_type == "line":

				# check if P1 is None				
				if self.dict["UNI_TIB_VAL"][self.op_type][self.side][item]["P1"] == None:
					self.dict["UNI_TIB_VAL"][self.op_type][self.side][item]["P1"] = P
					self.draw_tools.setHoverPointLabel("P1_"+item)
					self.draw_tools.setHoverPoint(P)
					self.draw_tools.setHoverBool(True)
					return True


				# check if P2 is None				
				if self.dict["UNI_TIB_VAL"][self.op_type][self.side][item]["P2"] == None:
					self.dict["UNI_TIB_VAL"][self.op_type][self.side][item]["P2"] = P
					self.draw_tools.setHoverBool(False)
					self.draw_tools.setHoverPointLabel(None)
					return True

		return False									
 

	def getNextLabel(self):
		if self.side != None:
			for item in self.dict["UNI_TIB_VAL"][self.op_type][self.side]:
				# get item type 
				item_type = self.dict["UNI_TIB_VAL"][self.op_type][self.side][item]["type"]
				
				
				# axis has two midpoints
				if item_type == "axis":
					print("axis" + item)
					# axis has a top and a bottom

					# check if P1 is None
					if self.dict["UNI_TIB_VAL"][self.op_type][self.side][item]["TOP"]["P1"] == None:						
						return (self.side + " " + item + " P1")

					# check if P2 is None				
					if self.dict["UNI_TIB_VAL"][self.op_type][self.side][item]["TOP"]["P2"] == None:						
						return (self.side + " " + item + " P2")


					# check if P1 is None
					if self.dict["UNI_TIB_VAL"][self.op_type][self.side][item]["BOT"]["P1"] == None:						
						return (self.side + " " + item + " P1")

					# check if P2 is None				
					if self.dict["UNI_TIB_VAL"][self.op_type][self.side][item]["BOT"]["P2"] == None:						
						return (self.side + " " + item + " P2")


				# line has P1 and P2
				if item_type == "line":

					# check if P1 is None				
					if self.dict["UNI_TIB_VAL"][self.op_type][self.side][item]["P1"] == None:						
						return (self.side + " " + item + " P1")


					# check if P2 is None				
					if self.dict["UNI_TIB_VAL"][self.op_type][self.side][item]["P2"] == None:
						return (self.side + " " + item + " P2")


			return (self.side + " Done")
		return None


	def hover(self, P_mouse, P_stored, hover_label):
		
		# prevent auto curObject set bug
		if self.side == None:
			return

		if self.draw_hover:
			side_pre = self.side[0]+"_"
			if(	hover_label == "P0_AXIS_TIB" or
				hover_label == "P0_TIB_JOINT_LINE"
				):
				self.draw_tools.clear_by_tag("hover_line")
				self.draw_tools.create_mypoint(P_mouse, "red", [self.tag, "hover_line"], hover_point=True, point_thickness=self.point_size)
				if self.draw_labels:
					self.draw_tools.create_mytext(P_mouse,x_offset=80, mytext=(side_pre+self.hover_text), mytag=[self.tag, "hover_line"])

		if hover_label == "P1_AXIS_TIB_TOP":
			self.draw_tools.clear_by_tag("hover_line")
			m = self.draw_tools.midpoint(P_stored, P_mouse)
			self.draw_tools.create_midpoint_line(P_stored, P_mouse, m, "hover_line", point_thickness=self.point_size)

			bot_axis_tib_m1 = self.dict[self.name][self.op_type][self.side]["AXIS_TIB"]["BOT"]["M1"]

			if bot_axis_tib_m1 != None:
				# join center points of axes
				xtop, ytop, xbot, ybot = self.draw_tools.getImageCorners()
				U_m1, D_m1 = self.draw_tools.retPointsUpDown(m, bot_axis_tib_m1)
				p_top = self.draw_tools.line_intersection((D_m1, U_m1), (xtop, ytop))
				self.draw_tools.create_myline(D_m1, p_top, "hover_line")


		if hover_label == "P1_AXIS_TIB_BOT":
			self.draw_tools.clear_by_tag("hover_line")
			m = self.draw_tools.midpoint(P_stored, P_mouse)
			self.draw_tools.create_midpoint_line(P_stored, P_mouse, m, "hover_line", point_thickness=self.point_size)

			top_axis_tib_m1 = self.dict[self.name][self.op_type][self.side]["AXIS_TIB"]["TOP"]["M1"]

			if top_axis_tib_m1 != None:				
				# join center points of axes
				xtop, ytop, xbot, ybot = self.draw_tools.getImageCorners()
				U_m1, D_m1 = self.draw_tools.retPointsUpDown(top_axis_tib_m1, m)
				p_top = self.draw_tools.line_intersection((D_m1, U_m1), (xtop, ytop))
				self.draw_tools.create_myline(D_m1, p_top, "hover_line")

		# P1_AXIS_TIB_TOP

		# P1_AXIS_TIB_BOT

		# P1_FEM_JOINT_LINE
		if hover_label == "P1_TIB_JOINT_LINE":
			self.draw_tools.clear_by_tag("hover_line")			
			self.draw_tools.create_myline(P_stored, P_mouse, "hover_line")

	def regainHover(self, side):
		p1_axis_tib_top = self.dict["UNI_TIB_VAL"][self.op_type][side]["AXIS_TIB"]["TOP"]["P1"]
		p2_axis_tib_top = self.dict["UNI_TIB_VAL"][self.op_type][side]["AXIS_TIB"]["TOP"]["P2"]
		p1_axis_tib_bot = self.dict["UNI_TIB_VAL"][self.op_type][side]["AXIS_TIB"]["BOT"]["P1"]
		p2_axis_tib_bot = self.dict["UNI_TIB_VAL"][self.op_type][side]["AXIS_TIB"]["BOT"]["P2"]

		p1_tib_joint_line = self.dict["UNI_TIB_VAL"][self.op_type][side]["TIB_JOINT_LINE"]["P1"]
		p2_tib_joint_line = self.dict["UNI_TIB_VAL"][self.op_type][side]["TIB_JOINT_LINE"]["P2"]

		# find if P0 hovers are required
		self.mainHoverUsingNextLabel()

		if p1_axis_tib_top != None and p2_axis_tib_top == None:
			self.draw_tools.setHoverPointLabel("P1_AXIS_TIB_TOP")
			self.draw_tools.setHoverPoint(p1_axis_tib_top)
			self.draw_tools.setHoverBool(True)

		if p1_axis_tib_bot != None and p2_axis_tib_bot == None:
			self.draw_tools.setHoverPointLabel("P1_AXIS_TIB_BOT")
			self.draw_tools.setHoverPoint(p1_axis_tib_bot)
			self.draw_tools.setHoverBool(True)
		if p1_tib_joint_line != None and p2_tib_joint_line == None:
			self.draw_tools.setHoverPointLabel("P1_TIB_JOINT_LINE")
			self.draw_tools.setHoverPoint(p1_tib_joint_line)
			self.draw_tools.setHoverBool(True)

	def escapeObjFunc(self):
		self.side = None
		self.draw_tools.setHoverPointLabel(None)
		self.draw_tools.setHoverBool(False)


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

		# vars for code readability
		axis_tib_top_p1 = self.dict["UNI_TIB_VAL"][self.op_type][side]["AXIS_TIB"]["TOP"]["P1"]
		axis_tib_top_p2 = self.dict["UNI_TIB_VAL"][self.op_type][side]["AXIS_TIB"]["TOP"]["P2"]
		axis_tib_top_m1 = self.dict["UNI_TIB_VAL"][self.op_type][side]["AXIS_TIB"]["TOP"]["M1"]

		axis_tib_bot_p1 = self.dict["UNI_TIB_VAL"][self.op_type][side]["AXIS_TIB"]["BOT"]["P1"]
		axis_tib_bot_p2 = self.dict["UNI_TIB_VAL"][self.op_type][side]["AXIS_TIB"]["BOT"]["P2"]
		axis_tib_bot_m1 = self.dict["UNI_TIB_VAL"][self.op_type][side]["AXIS_TIB"]["BOT"]["M1"]


		tib_joint_p1 = self.dict["UNI_TIB_VAL"][self.op_type][side]["TIB_JOINT_LINE"]["P1"]
		tib_joint_p2 = self.dict["UNI_TIB_VAL"][self.op_type][side]["TIB_JOINT_LINE"]["P2"]

		# find item type
		if "AXIS_TIB" in tags:
			item = "AXIS_TIB"

			# axis has top and bot
			if "TOP" in tags:
				topbot = "TOP"
			elif "BOT" in tags:
				topbot = "BOT"

		elif "TIB_JOINT_LINE" in tags:
			item = "TIB_JOINT_LINE"


		if "P1" in tags:
			if item == "AXIS_TIB":
				if topbot == "TOP":
					self.drag_point = axis_tib_top_p2
					self.drag_label = "P1_AXIS_TIB_TOP"
					self.drag_side 	= side

				elif topbot == "BOT":
					self.drag_point = axis_tib_bot_p2
					self.drag_label = "P1_AXIS_TIB_BOT"
					self.drag_side 	= side

			elif item == "TIB_JOINT_LINE":
				# self.draw_tools.clear_by_tag("UNI_TIB_VAL_angle")
				self.drag_point = tib_joint_p2
				self.drag_label = "P1_JOINT"
				self.drag_side 	= side


		if "P2" in tags:
			if item == "AXIS_TIB":
				if topbot == "TOP":
					self.drag_point = axis_tib_top_p1
					self.drag_label = "P2_AXIS_TIB_TOP"
					self.drag_side 	= side

				elif topbot == "BOT":
					self.drag_point = axis_tib_bot_p1
					self.drag_label = "P2_AXIS_TIB_BOT"
					self.drag_side 	= side

			elif item == "TIB_JOINT_LINE":
				self.draw_tools.clear_by_tag("UNI_TIB_VAL_angle")
				self.drag_point = tib_joint_p1
				self.drag_label = "P2_JOINT"
				self.drag_side 	= side

	def drag(self, P_mouse):
		if self.drag_label == "P1_JOINT" or self.drag_label == "P2_JOINT":
			if self.drag_point != None:
				self.draw_tools.clear_by_tag("TIB_LINE")
				self.draw_tools.clear_by_tag("drag_line")
				self.draw_tools.create_myline(self.drag_point, P_mouse, "drag_line")


		if self.drag_label == "P1_AXIS_TIB_TOP" or self.drag_label == "P2_AXIS_TIB_TOP":
			if self.drag_point != None:
				self.draw_tools.clear_by_tag("TOP_AXIS_LINE")
				self.draw_tools.clear_by_tag("drag_line")
				m = self.draw_tools.midpoint(self.drag_point, P_mouse)
				self.draw_tools.create_midpoint_line(self.drag_point, P_mouse, m, "drag_line", point_thickness=self.point_size)

		if self.drag_label == "P1_AXIS_TIB_BOT" or self.drag_label == "P2_AXIS_TIB_BOT":
			if self.drag_point != None:
				self.draw_tools.clear_by_tag("BOT_AXIS_LINE")
				self.draw_tools.clear_by_tag("drag_line")
				m = self.draw_tools.midpoint(self.drag_point, P_mouse)
				self.draw_tools.create_midpoint_line(self.drag_point, P_mouse, m, "drag_line", point_thickness=self.point_size)

	def drag_stop(self, P_mouse):
		self.draw_tools.clear_by_tag("drag_line")

		# FEM JOINT LINE
		if self.drag_label == "P1_JOINT":
			self.dict["UNI_TIB_VAL"][self.op_type][self.drag_side]["TIB_JOINT_LINE"]["P1"] = P_mouse
			self.dict["EXCEL"][self.op_type][self.drag_side]["TVAR/VAL"] = None
			self.controller.save_json()
			self.draw()

		if self.drag_label == "P2_JOINT":
			self.dict["UNI_TIB_VAL"][self.op_type][self.drag_side]["TIB_JOINT_LINE"]["P2"] = P_mouse
			self.dict["EXCEL"][self.op_type][self.drag_side]["TVAR/VAL"] = None
			self.controller.save_json()
			self.draw()


		if self.drag_label == "P1_AXIS_TIB_TOP":
			self.dict["UNI_TIB_VAL"][self.op_type][self.drag_side]["AXIS_TIB"]["TOP"]["P1"] = P_mouse
			self.dict["UNI_TIB_VAL"][self.op_type][self.drag_side]["AXIS_TIB"]["TOP"]["M1"] = self.draw_tools.midpoint(self.drag_point, P_mouse)
			self.dict["EXCEL"][self.op_type][self.drag_side]["TVAR/VAL"] = None
			self.controller.save_json()
			self.draw()

		if self.drag_label == "P2_AXIS_TIB_TOP":
			self.dict["UNI_TIB_VAL"][self.op_type][self.drag_side]["AXIS_TIB"]["TOP"]["P2"] = P_mouse
			self.dict["UNI_TIB_VAL"][self.op_type][self.drag_side]["AXIS_TIB"]["TOP"]["M1"] = self.draw_tools.midpoint(self.drag_point, P_mouse)
			self.dict["EXCEL"][self.op_type][self.drag_side]["TVAR/VAL"] = None
			self.controller.save_json()
			self.draw()

		if self.drag_label == "P1_AXIS_TIB_BOT":
			self.dict["UNI_TIB_VAL"][self.op_type][self.drag_side]["AXIS_TIB"]["BOT"]["P1"] = P_mouse
			self.dict["UNI_TIB_VAL"][self.op_type][self.drag_side]["AXIS_TIB"]["BOT"]["M1"] = self.draw_tools.midpoint(self.drag_point, P_mouse)
			self.dict["EXCEL"][self.op_type][self.drag_side]["TVAR/VAL"] = None
			self.controller.save_json()
			self.draw()

		if self.drag_label == "P2_AXIS_TIB_BOT":
			self.dict["UNI_TIB_VAL"][self.op_type][self.drag_side]["AXIS_TIB"]["BOT"]["P2"] = P_mouse
			self.dict["UNI_TIB_VAL"][self.op_type][self.drag_side]["AXIS_TIB"]["BOT"]["M1"] = self.draw_tools.midpoint(self.drag_point, P_mouse)
			self.dict["EXCEL"][self.op_type][self.drag_side]["TVAR/VAL"] = None
			self.controller.save_json()
			self.draw()


	def update_canvas(self, draw_tools):
		self.draw_tools = draw_tools


	def update_dict(self, master_dict):
		self.dict = master_dict


	def unset(self):
		# print("unset from "+self.name)
		self.draw_tools.clear_by_tag(self.tag)


	def checkbox_click(self,action, val):
		print('checkbox {} val{}'.format(action,val.get()))

		if action == "TOGGLE_LABEL":
			if val.get() == 0:
				self.draw_labels = False
			elif val.get() == 1:
				self.draw_labels = True
			self.draw()

		if action == "TOGGLE_HOVER":
			if val.get() == 0:
				self.draw_hover = False
			elif val.get() == 1:
				self.draw_hover = True
			self.draw()


	def mainHoverUsingNextLabel(self):
		label = self.getNextLabel()

		
		if label == "RIGHT AXIS_TIB P1":
			self.side = "RIGHT"
			self.hover_text = "AXIS_TIB"
			self.draw_tools.setHoverPointLabel("P0_AXIS_TIB")
			self.draw_tools.setHoverPoint(None)
			self.draw_tools.setHoverBool(True)
		elif label == "LEFT AXIS_TIB P1":
			self.side = "LEFT"
			self.hover_text = "AXIS_TIB"
			self.draw_tools.setHoverPointLabel("P0_AXIS_TIB")
			self.draw_tools.setHoverPoint(None)
			self.draw_tools.setHoverBool(True)

		elif label == "RIGHT TIB_JOINT_LINE P1":
			self.side = "RIGHT"
			self.hover_text = "TIB_JOINT_LINE"
			self.draw_tools.setHoverPointLabel("P0_TIB_JOINT_LINE")
			self.draw_tools.setHoverPoint(None)
			self.draw_tools.setHoverBool(True)
		elif label == "LEFT TIB_JOINT_LINE P1":
			self.side = "LEFT"
			self.hover_text = "TIB_JOINT_LINE"
			self.draw_tools.setHoverPointLabel("P0_TIB_JOINT_LINE")
			self.draw_tools.setHoverPoint(None)
			self.draw_tools.setHoverBool(True)