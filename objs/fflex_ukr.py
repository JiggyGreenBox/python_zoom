

class FFLEX_UKR():
	"""docstring for ClassName"""
	def __init__(self, draw_tools, master_dict, controller, op_type):
		self.name = "FFLEX_UKR"
		self.tag = "fflex_ukr"
		self.menu_label = "FFLEX_UKR_Menu"
		self.draw_tools = draw_tools
		self.dict = master_dict
		self.controller = controller
		self.side = None
		self.op_type = op_type

		# check if master dictionary has values
		# if not populate the dictionary
		self.checkMasterDict()

		self.drag_point = None
		self.drag_label = None
		self.drag_side 	= None



	def click(self, event):
		# print("click from "+self.name)
		# self.draw()
		if self.side == None:
			print("please choose side")
			self.controller.warningBox("Please select a Side")
		else:
			ret =  self.addDict(event)			
			if ret:
				self.controller.save_json()
				# pass

		self.controller.updateMenuLabel(self.getNextLabel(), self.menu_label)		
		self.draw()
		# print(self.dict)


	# menu button clicks are routed here
	def menu_btn_click(self, action):
		print(action)
		if action == "SET-LEFT":
			self.side = "LEFT"
			self.controller.updateMenuLabel(self.getNextLabel(), self.menu_label)
			self.draw()
			self.regainHover(self.side)
			return # avoid clear,draw,json_save

		if action == "SET-RIGHT":
			self.side = "RIGHT"
			self.controller.updateMenuLabel(self.getNextLabel(), self.menu_label)
			self.draw()
			self.regainHover(self.side)
			return # avoid clear,draw,json_save


		
		if action == "DEL-LEFT-FEM-TOP":			
			self.dict["FFLEX_UKR"][self.op_type]["LEFT"]["AXIS_FEM"]["TOP"]["P1"] = None
			self.dict["FFLEX_UKR"][self.op_type]["LEFT"]["AXIS_FEM"]["TOP"]["P2"] = None
			self.dict["FFLEX_UKR"][self.op_type]["LEFT"]["AXIS_FEM"]["TOP"]["M1"] = None
			self.side = "LEFT"
		if action == "DEL-RIGHT-FEM-TOP":
			self.dict["FFLEX_UKR"][self.op_type]["RIGHT"]["AXIS_FEM"]["TOP"]["P1"] = None
			self.dict["FFLEX_UKR"][self.op_type]["RIGHT"]["AXIS_FEM"]["TOP"]["P2"] = None
			self.dict["FFLEX_UKR"][self.op_type]["RIGHT"]["AXIS_FEM"]["TOP"]["M1"] = None
			self.side = "RIGHT"
		if action == "DEL-LEFT-FEM-BOT":
			self.dict["FFLEX_UKR"][self.op_type]["LEFT"]["AXIS_FEM"]["BOT"]["P1"] = None
			self.dict["FFLEX_UKR"][self.op_type]["LEFT"]["AXIS_FEM"]["BOT"]["P2"] = None
			self.dict["FFLEX_UKR"][self.op_type]["LEFT"]["AXIS_FEM"]["BOT"]["M1"] = None
			self.side = "LEFT"
		if action == "DEL-RIGHT-FEM-BOT":
			self.dict["FFLEX_UKR"][self.op_type]["RIGHT"]["AXIS_FEM"]["BOT"]["P1"] = None
			self.dict["FFLEX_UKR"][self.op_type]["RIGHT"]["AXIS_FEM"]["BOT"]["P2"] = None
			self.dict["FFLEX_UKR"][self.op_type]["RIGHT"]["AXIS_FEM"]["BOT"]["M1"] = None
			self.side = "RIGHT"



		if action == "DEL-RIGHT-PEG-TOP":
			self.dict["FFLEX_UKR"][self.op_type]["RIGHT"]["AXIS_PEG"]["TOP"]["P1"] = None
			self.dict["FFLEX_UKR"][self.op_type]["RIGHT"]["AXIS_PEG"]["TOP"]["P2"] = None
			self.dict["FFLEX_UKR"][self.op_type]["RIGHT"]["AXIS_PEG"]["TOP"]["M1"] = None
			self.side = "RIGHT"
		if action == "DEL-LEFT-PEG-TOP":
			self.dict["FFLEX_UKR"][self.op_type]["LEFT"]["AXIS_PEG"]["TOP"]["P1"] = None
			self.dict["FFLEX_UKR"][self.op_type]["LEFT"]["AXIS_PEG"]["TOP"]["P2"] = None
			self.dict["FFLEX_UKR"][self.op_type]["LEFT"]["AXIS_PEG"]["TOP"]["M1"] = None
			self.side = "LEFT"
		if action == "DEL-RIGHT-PEG-BOT":
			self.dict["FFLEX_UKR"][self.op_type]["RIGHT"]["AXIS_PEG"]["BOT"]["P1"] = None
			self.dict["FFLEX_UKR"][self.op_type]["RIGHT"]["AXIS_PEG"]["BOT"]["P2"] = None
			self.dict["FFLEX_UKR"][self.op_type]["RIGHT"]["AXIS_PEG"]["BOT"]["M1"] = None
			self.side = "RIGHT"
		if action == "DEL-LEFT-PEG-BOT":
			self.dict["FFLEX_UKR"][self.op_type]["LEFT"]["AXIS_PEG"]["BOT"]["P1"] = None
			self.dict["FFLEX_UKR"][self.op_type]["LEFT"]["AXIS_PEG"]["BOT"]["P2"] = None
			self.dict["FFLEX_UKR"][self.op_type]["LEFT"]["AXIS_PEG"]["BOT"]["M1"] = None
			self.side = "LEFT"
				
		
		# delete excel data from pat.json
		self.dict["EXCEL"][self.op_type][self.side]["FFLEX"] = None
		self.dict["EXCEL"][self.op_type][self.side]["FFLE/EXT"] = None

		self.draw()		
		self.regainHover(self.side)

		self.controller.save_json()
		self.controller.updateMenuLabel(self.getNextLabel(), self.menu_label)

	
	def draw(self):
		
		
		self.draw_tools.clear_by_tag(self.tag)

		# loop left and right
		for side in ["LEFT","RIGHT"]:

			isFemTop 	= False
			isFemBot 	= False
			isPegTop 	= False
			isPegBot 	= False

		# 	joint_line_p1 = self.dict["TSLOPE"][self.op_type][side]["TIB_JOINT_LINE"]["P1"]
		# 	joint_line_p2 = self.dict["TSLOPE"][self.op_type][side]["TIB_JOINT_LINE"]["P2"]

			axis_fem_top_p1 = self.dict["FFLEX_UKR"][self.op_type][side]["AXIS_FEM"]["TOP"]["P1"]
			axis_fem_top_p2 = self.dict["FFLEX_UKR"][self.op_type][side]["AXIS_FEM"]["TOP"]["P2"]
			axis_fem_top_m1 = self.dict["FFLEX_UKR"][self.op_type][side]["AXIS_FEM"]["TOP"]["M1"]

			axis_fem_bot_p1 = self.dict["FFLEX_UKR"][self.op_type][side]["AXIS_FEM"]["BOT"]["P1"]
			axis_fem_bot_p2 = self.dict["FFLEX_UKR"][self.op_type][side]["AXIS_FEM"]["BOT"]["P2"]
			axis_fem_bot_m1 = self.dict["FFLEX_UKR"][self.op_type][side]["AXIS_FEM"]["BOT"]["M1"]


			axis_peg_top_p1 = self.dict["FFLEX_UKR"][self.op_type][side]["AXIS_PEG"]["TOP"]["P1"]
			axis_peg_top_p2 = self.dict["FFLEX_UKR"][self.op_type][side]["AXIS_PEG"]["TOP"]["P2"]
			axis_peg_top_m1 = self.dict["FFLEX_UKR"][self.op_type][side]["AXIS_PEG"]["TOP"]["M1"]

			axis_peg_bot_p1 = self.dict["FFLEX_UKR"][self.op_type][side]["AXIS_PEG"]["BOT"]["P1"]
			axis_peg_bot_p2 = self.dict["FFLEX_UKR"][self.op_type][side]["AXIS_PEG"]["BOT"]["P2"]
			axis_peg_bot_m1 = self.dict["FFLEX_UKR"][self.op_type][side]["AXIS_PEG"]["BOT"]["M1"]

		


			# FEM AXIS
			# TOP
			if axis_fem_top_p1 != None:
				self.draw_tools.create_mypoint(axis_fem_top_p1, "orange", [self.tag,side,"AXIS_FEM","TOP","P1"])

			if axis_fem_top_p2 != None:
				self.draw_tools.create_mypoint(axis_fem_top_p2, "orange", [self.tag,side,"AXIS_FEM","TOP","P2"])

			if axis_fem_top_p1 != None and axis_fem_top_p2 != None:				
				self.draw_tools.create_midpoint_line(axis_fem_top_p1, axis_fem_top_p2, axis_fem_top_m1, [self.tag,side,"TOP_AXIS_LINE"])
				isFemTop = True
				

			# BOT
			if axis_fem_bot_p1 != None:
				self.draw_tools.create_mypoint(axis_fem_bot_p1, "orange", [self.tag,side,"AXIS_FEM","BOT","P1"])

			if axis_fem_bot_p2 != None:
				self.draw_tools.create_mypoint(axis_fem_bot_p2, "orange", [self.tag,side,"AXIS_FEM","BOT","P2"])

			if axis_fem_bot_p1 != None and axis_fem_bot_p2 != None:				
				self.draw_tools.create_midpoint_line(axis_fem_bot_p1, axis_fem_bot_p2, axis_fem_bot_m1, [self.tag,"BOT_AXIS_LINE"])
				isFemBot = True



			# PEG AXIS
			# TOP
			if axis_peg_top_p1 != None:
				self.draw_tools.create_mypoint(axis_peg_top_p1, "orange", [self.tag,side,"AXIS_PEG","TOP","P1"])

			if axis_peg_top_p2 != None:
				self.draw_tools.create_mypoint(axis_peg_top_p2, "orange", [self.tag,side,"AXIS_PEG","TOP","P2"])

			if axis_peg_top_p1 != None and axis_peg_top_p2 != None:				
				self.draw_tools.create_midpoint_line(axis_peg_top_p1, axis_peg_top_p2, axis_peg_top_m1, [self.tag,side,"TOP_AXIS_LINE"])
				isPegTop = True
				

			# BOT
			if axis_peg_bot_p1 != None:
				self.draw_tools.create_mypoint(axis_peg_bot_p1, "orange", [self.tag,side,"AXIS_PEG","BOT","P1"])

			if axis_peg_bot_p2 != None:
				self.draw_tools.create_mypoint(axis_peg_bot_p2, "orange", [self.tag,side,"AXIS_PEG","BOT","P2"])

			if axis_peg_bot_p1 != None and axis_peg_bot_p2 != None:				
				self.draw_tools.create_midpoint_line(axis_peg_bot_p1, axis_peg_bot_p2, axis_peg_bot_m1, [self.tag,"BOT_AXIS_LINE"])
				isPegBot = True






			xtop, ytop, xbot, ybot = self.draw_tools.getImageCorners()

			# draw the axis
			if isFemTop and isFemBot:			 

				
				U_m1, D_m1 = self.draw_tools.retPointsUpDown(axis_fem_top_m1, axis_fem_bot_m1)

				# TIB-AXIS ray
				p_bot = self.draw_tools.line_intersection((U_m1, D_m1),(xbot, ybot))
				p_top = self.draw_tools.line_intersection((U_m1, D_m1),(xtop, ytop))				
				self.draw_tools.create_myline(p_top, p_bot, [self.tag])


				if isPegTop and isPegBot:
					U_peg_m1, D_peg_m1 = self.draw_tools.retPointsUpDown(axis_peg_top_m1, axis_peg_bot_m1)

					peg_bot = self.draw_tools.line_intersection((U_peg_m1, D_peg_m1),(xbot, ybot))
					peg_top = self.draw_tools.line_intersection((U_peg_m1, D_peg_m1),(xtop, ytop))
					self.draw_tools.create_myline(peg_bot, peg_top, [self.tag])

					p_int = self.draw_tools.line_intersection((U_peg_m1, D_peg_m1),(U_m1, D_m1))

					angle = self.draw_tools.getSmallestAngle(D_peg_m1, p_int, D_m1)
					
					fflex = 0
					fflex_ext = 0

					# intersection point is above
					# FLEXTION
					# positive value
					# for eg: if flextion is 2deg then FFLEX:90-2, FFLEX-EXT:2
					if(self.draw_tools.retIsPointUp(p_int,D_peg_m1)):
						fflex 		= angle
						fflex_ext 	= 90-angle
						self.draw_tools.create_mytext(axis_peg_bot_p2, '{0:.2f}'.format(angle), [self.tag,"PTILT_ANGLE"], y_offset=60, color="blue")
						self.draw_tools.create_mytext(axis_peg_bot_p2, '{0:.2f}'.format(90-angle), [self.tag,"PTILT_ANGLE"], y_offset=120, color="blue")
					# intersection point is below
					# EXTENTION
					# negative value
					# angle = -1*angle
					# for eg: if flextion is 7deg then, FFLEX-EXT:-(7), FFLEX:90-(-7)=97, 
					else:
						angle = angle*-1
						fflex 		= angle
						fflex_ext 	= 90-angle
						self.draw_tools.create_mytext(axis_peg_bot_p2, '{0:.2f}'.format(angle), [self.tag,"PTILT_ANGLE"], y_offset=60, color="blue")
						self.draw_tools.create_mytext(axis_peg_bot_p2, '{0:.2f}'.format(90-angle), [self.tag,"PTILT_ANGLE"], y_offset=120, color="blue")
						
					# save to excel
					if fflex != 0 and fflex_ext != 0:
						if self.dict["EXCEL"][self.op_type][side]["FFLEX"] == None:
							self.dict["EXCEL"][self.op_type][side]["HASDATA"] 	= True
							self.dict["EXCEL"][self.op_type][side]["FFLEX"]	= '{0:.2f}'.format(fflex)								
							self.controller.save_json() 


						if self.dict["EXCEL"][self.op_type][side]["FFLE/EXT"] == None:
							self.dict["EXCEL"][self.op_type][side]["HASDATA"] 	= True
							self.dict["EXCEL"][self.op_type][side]["FFLE/EXT"]	= '{0:.2f}'.format(fflex_ext)								
							self.controller.save_json()






				# if isFemJoint:

				# 	L_p1, R_p1 = self.draw_tools.retPointsLeftRight(fem_joint_p1, fem_joint_p2)

				# 	# intersection point
				# 	p_int = self.draw_tools.line_intersection(
				# 		(U_m1, D_m1),
				# 		(fem_joint_p1, fem_joint_p2))				

				# 	# find and draw angles
				# 	if side == "LEFT":
				# 		angle = self.draw_tools.create_myAngle(L_p1, p_int, D_m1, [self.tag, "FFLEX_angle"], radius=30)
				# 		self.draw_tools.create_mytext(p_int, '{0:.2f}'.format(angle), self.tag, x_offset=-30, y_offset=60, color="blue")

				# 	if side == "RIGHT":
				# 		angle = self.draw_tools.create_myAngle(D_m1, p_int, R_p1, [self.tag, "FFLEX_angle"],radius=30)
				# 		self.draw_tools.create_mytext(p_int, '{0:.2f}'.format(angle), self.tag, x_offset=30, y_offset=60, color="blue")


					# # check if value exists
					# if self.dict["EXCEL"][self.op_type][side]["TSLOPE"] == None:

					# 	self.dict["EXCEL"][self.op_type][side]["HASDATA"] 	= True
					# 	self.dict["EXCEL"][self.op_type][side]["TSLOPE"]	= '{0:.2f}'.format(angle)

					# 	# save after insert
					# 	self.controller.save_json()
					


	def hover(self, P_mouse, P_stored, hover_label):

		if hover_label == "P1_top":
			self.draw_tools.clear_by_tag("hover_line")
			m = self.draw_tools.midpoint(P_stored, P_mouse)
			self.draw_tools.create_midpoint_line(P_stored, P_mouse, m, "hover_line")

			axis_fem_bot_m1 = self.dict["FFLEX_UKR"][self.op_type][self.side]["AXIS_FEM"]["BOT"]["M1"]
			xtop, ytop, xbot, ybot = self.draw_tools.getImageCorners()

			if axis_fem_bot_m1 != None:
				# FEM-AXIS ray
				p_int = self.draw_tools.line_intersection(
					(axis_fem_bot_m1, m),
					(xbot, ybot))
				self.draw_tools.create_myline(m, p_int, "hover_line")


		if hover_label == "P1_bot":
			self.draw_tools.clear_by_tag("hover_line")
			m = self.draw_tools.midpoint(P_stored, P_mouse)
			self.draw_tools.create_midpoint_line(P_stored, P_mouse, m, "hover_line")

			axis_fem_top_m1 = self.dict["FFLEX_UKR"][self.op_type][self.side]["AXIS_FEM"]["TOP"]["M1"]
			xtop, ytop, xbot, ybot = self.draw_tools.getImageCorners()

			if axis_fem_top_m1 != None:
				# FEM-AXIS ray
				p_int = self.draw_tools.line_intersection(
					(axis_fem_top_m1, m),
					(xbot, ybot))
				self.draw_tools.create_myline(axis_fem_top_m1, p_int, "hover_line")


		if hover_label == "P1_fem":
			self.draw_tools.clear_by_tag("hover_line")
			self.draw_tools.create_myline(P_stored, P_mouse, "hover_line")

		# peg hover
		# top
		if hover_label == "P1_peg_top":
			self.draw_tools.clear_by_tag("hover_line")
			m = self.draw_tools.midpoint(P_stored, P_mouse)
			self.draw_tools.create_midpoint_line(P_stored, P_mouse, m, "hover_line")
		# bot
		if hover_label == "P1_peg_bot":
			self.draw_tools.clear_by_tag("hover_line")
			m = self.draw_tools.midpoint(P_stored, P_mouse)
			self.draw_tools.create_midpoint_line(P_stored, P_mouse, m, "hover_line")

	def regainHover(self, side):
		pass
		'''
		axis_fem_top_p1 = self.dict["FFLEX_UKR"][self.op_type][side]["AXIS_FEM"]["TOP"]["P1"]
		axis_fem_top_p2 = self.dict["FFLEX_UKR"][self.op_type][side]["AXIS_FEM"]["TOP"]["P2"]
		axis_fem_top_m1 = self.dict["FFLEX_UKR"][self.op_type][side]["AXIS_FEM"]["TOP"]["M1"]

		axis_fem_bot_p1 = self.dict["FFLEX_UKR"][self.op_type][side]["AXIS_FEM"]["BOT"]["P1"]
		axis_fem_bot_p2 = self.dict["FFLEX_UKR"][self.op_type][side]["AXIS_FEM"]["BOT"]["P2"]
		axis_fem_bot_m1 = self.dict["FFLEX_UKR"][self.op_type][side]["AXIS_FEM"]["BOT"]["M1"]


		fem_joint_p1 = self.dict["FFLEX_UKR"][self.op_type][side]["FEM_JOINT_LINE"]["P1"]
		fem_joint_p2 = self.dict["FFLEX_UKR"][self.op_type][side]["FEM_JOINT_LINE"]["P2"]

		# if top p1 and not p2
		if axis_fem_top_p1 != None and axis_fem_top_p2 == None:
			self.draw_tools.setHoverPointLabel("P1_top")
			self.draw_tools.setHoverPoint(axis_fem_top_p1)
			self.draw_tools.setHoverBool(True)

		# if bot p1 and not p2
		if axis_fem_bot_p1 != None and axis_fem_bot_p2 == None:
			self.draw_tools.setHoverPointLabel("P1_bot")
			self.draw_tools.setHoverPoint(axis_fem_bot_p1)
			self.draw_tools.setHoverBool(True)

		# if fem p1 and not p2
		if fem_joint_p1 != None and fem_joint_p2 == None:
			self.draw_tools.setHoverPointLabel("P1_fem")
			self.draw_tools.setHoverPoint(fem_joint_p1)
			self.draw_tools.setHoverBool(True)
		'''



	def checkMasterDict(self):
		if "FFLEX_UKR" not in self.dict.keys():
			self.dict["FFLEX_UKR"] = 	{
										"POST-OP":{
												"LEFT":	{
															"AXIS_FEM":	{
																			"type":	"axis",
																			"TOP":	{"type":"midpoint","P1":None,"P2":None, "M1":None},
																			"BOT":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
																		},
															"AXIS_PEG":	{
																			"type":	"axis",
																			"TOP":	{"type":"midpoint","P1":None,"P2":None, "M1":None},
																			"BOT":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
																		}															
														},
												"RIGHT":{
															"AXIS_FEM":	{
																			"type":	"axis",
																			"TOP":	{"type":"midpoint","P1":None,"P2":None, "M1":None},
																			"BOT":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
																		},
															"AXIS_PEG":	{
																			"type":	"axis",
																			"TOP":	{"type":"midpoint","P1":None,"P2":None, "M1":None},
																			"BOT":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
																		}
														}
												}
									}



	def addDict(self, event):

		for item in self.dict["FFLEX_UKR"][self.op_type][self.side]:

			print(item)

			# get the point from mouse click
			P = self.draw_tools.getRealCoords(event)

			# get item type 
			item_type = self.dict["FFLEX_UKR"][self.op_type][self.side][item]["type"]

			# axis has top and bottom
			if item_type == "axis":

				axis_fem_top_p1 = self.dict["FFLEX_UKR"][self.op_type][self.side]["AXIS_FEM"]["TOP"]["P1"]
				axis_fem_top_p2 = self.dict["FFLEX_UKR"][self.op_type][self.side]["AXIS_FEM"]["TOP"]["P2"]
				axis_fem_top_m1 = self.dict["FFLEX_UKR"][self.op_type][self.side]["AXIS_FEM"]["TOP"]["M1"]

				axis_fem_bot_p1 = self.dict["FFLEX_UKR"][self.op_type][self.side]["AXIS_FEM"]["BOT"]["P1"]
				axis_fem_bot_p2 = self.dict["FFLEX_UKR"][self.op_type][self.side]["AXIS_FEM"]["BOT"]["P2"]
				axis_fem_bot_m1 = self.dict["FFLEX_UKR"][self.op_type][self.side]["AXIS_FEM"]["BOT"]["M1"]


				axis_peg_top_p1 = self.dict["FFLEX_UKR"][self.op_type][self.side]["AXIS_PEG"]["TOP"]["P1"]
				axis_peg_top_p2 = self.dict["FFLEX_UKR"][self.op_type][self.side]["AXIS_PEG"]["TOP"]["P2"]
				axis_peg_top_m1 = self.dict["FFLEX_UKR"][self.op_type][self.side]["AXIS_PEG"]["TOP"]["M1"]

				axis_peg_bot_p1 = self.dict["FFLEX_UKR"][self.op_type][self.side]["AXIS_PEG"]["BOT"]["P1"]
				axis_peg_bot_p2 = self.dict["FFLEX_UKR"][self.op_type][self.side]["AXIS_PEG"]["BOT"]["P2"]
				axis_peg_bot_m1 = self.dict["FFLEX_UKR"][self.op_type][self.side]["AXIS_PEG"]["BOT"]["M1"]


				# FEM TOP
				# check if P1 is None
				if axis_fem_top_p1 == None:
					# axis_fem_top_p1 = P					
					self.dict["FFLEX_UKR"][self.op_type][self.side]["AXIS_FEM"]["TOP"]["P1"] = P
					self.draw_tools.setHoverPointLabel("P1_top")
					self.draw_tools.setHoverPoint(P)
					self.draw_tools.setHoverBool(True)
					return True

				# check if P2 is None
				if axis_fem_top_p2 == None:
					self.dict["FFLEX_UKR"][self.op_type][self.side]["AXIS_FEM"]["TOP"]["M1"] = self.draw_tools.midpoint(self.dict["FFLEX_UKR"][self.op_type][self.side]["AXIS_FEM"]["TOP"]["P1"], P)
					self.dict["FFLEX_UKR"][self.op_type][self.side]["AXIS_FEM"]["TOP"]["P2"] = P
					self.draw_tools.setHoverBool(False)
					self.draw_tools.setHoverPointLabel(None)
					return True

				# FEM BOT
				# check if P1 is None
				if axis_fem_bot_p1 == None:
					self.dict["FFLEX_UKR"][self.op_type][self.side]["AXIS_FEM"]["BOT"]["P1"] = P
					self.draw_tools.setHoverPointLabel("P1_bot")
					self.draw_tools.setHoverPoint(P)
					self.draw_tools.setHoverBool(True)
					return True

				# check if P2 is None
				if axis_fem_bot_p2 == None:
					self.dict["FFLEX_UKR"][self.op_type][self.side]["AXIS_FEM"]["BOT"]["M1"] = self.draw_tools.midpoint(self.dict["FFLEX_UKR"][self.op_type][self.side]["AXIS_FEM"]["BOT"]["P1"], P)
					self.dict["FFLEX_UKR"][self.op_type][self.side]["AXIS_FEM"]["BOT"]["P2"] = P
					self.draw_tools.setHoverBool(False)
					self.draw_tools.setHoverPointLabel(None)
					return True



				# PEG TOP
				# check if P1 is None
				if axis_peg_top_p1 == None:
					# axis_fem_top_p1 = P					
					self.dict["FFLEX_UKR"][self.op_type][self.side]["AXIS_PEG"]["TOP"]["P1"] = P
					self.draw_tools.setHoverPointLabel("P1_peg_top")
					self.draw_tools.setHoverPoint(P)
					self.draw_tools.setHoverBool(True)
					return True

				# check if P2 is None
				if axis_peg_top_p2 == None:
					self.dict["FFLEX_UKR"][self.op_type][self.side]["AXIS_PEG"]["TOP"]["M1"] = self.draw_tools.midpoint(self.dict["FFLEX_UKR"][self.op_type][self.side]["AXIS_PEG"]["TOP"]["P1"], P)
					self.dict["FFLEX_UKR"][self.op_type][self.side]["AXIS_PEG"]["TOP"]["P2"] = P
					self.draw_tools.setHoverBool(False)
					self.draw_tools.setHoverPointLabel(None)
					return True

				# PEG BOT
				# check if P1 is None
				if axis_peg_bot_p1 == None:
					self.dict["FFLEX_UKR"][self.op_type][self.side]["AXIS_PEG"]["BOT"]["P1"] = P
					self.draw_tools.setHoverPointLabel("P1_peg_bot")
					self.draw_tools.setHoverPoint(P)
					self.draw_tools.setHoverBool(True)
					return True

				# check if P2 is None
				if axis_peg_bot_p2 == None:
					self.dict["FFLEX_UKR"][self.op_type][self.side]["AXIS_PEG"]["BOT"]["M1"] = self.draw_tools.midpoint(self.dict["FFLEX_UKR"][self.op_type][self.side]["AXIS_PEG"]["BOT"]["P1"], P)
					self.dict["FFLEX_UKR"][self.op_type][self.side]["AXIS_PEG"]["BOT"]["P2"] = P
					self.draw_tools.setHoverBool(False)
					self.draw_tools.setHoverPointLabel(None)
					return True


			

		return False	


	def getNextLabel(self):

		if self.side != None:
			for item in self.dict["FFLEX_UKR"][self.op_type][self.side]:
				# get item type 
				item_type = self.dict["FFLEX_UKR"][self.op_type][self.side][item]["type"]

				# axis has two midpoints
				if item_type == "axis":
					# axis has a top and a bottom

					# check if P1 is None
					if self.dict["FFLEX_UKR"][self.op_type][self.side]["AXIS_FEM"]["TOP"]["P1"] == None:
						return (self.side + " " + "FEM TOP" + " P1")
					# check if P2 is None
					if self.dict["FFLEX_UKR"][self.op_type][self.side]["AXIS_FEM"]["TOP"]["P2"] == None:
						return (self.side + " " + "FEM TOP" + " P2")
					# check if P1 is None
					if self.dict["FFLEX_UKR"][self.op_type][self.side]["AXIS_FEM"]["BOT"]["P1"] == None:
						return (self.side + " " + "FEM BOT" + " P1")
					# check if P2 is None
					if self.dict["FFLEX_UKR"][self.op_type][self.side]["AXIS_FEM"]["BOT"]["P2"] == None:
						return (self.side + " " + "FEM BOT" + " P2")



					# check if P1 is None
					if self.dict["FFLEX_UKR"][self.op_type][self.side]["AXIS_PEG"]["TOP"]["P1"] == None:
						return (self.side + " " + "PEG TOP" + " P1")
					# check if P2 is None
					if self.dict["FFLEX_UKR"][self.op_type][self.side]["AXIS_PEG"]["TOP"]["P2"] == None:
						return (self.side + " " + "PEG TOP" + " P2")
					# check if P1 is None
					if self.dict["FFLEX_UKR"][self.op_type][self.side]["AXIS_PEG"]["BOT"]["P1"] == None:
						return (self.side + " " + "PEG BOT" + " P1")
					# check if P2 is None
					if self.dict["FFLEX_UKR"][self.op_type][self.side]["AXIS_PEG"]["BOT"]["P2"] == None:
						return (self.side + " " + "PEG BOT" + " P2")



			return (self.side + " Done")
		return None

	
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
		axis_fem_top_p1 = self.dict["FFLEX_UKR"][self.op_type][side]["AXIS_FEM"]["TOP"]["P1"]
		axis_fem_top_p2 = self.dict["FFLEX_UKR"][self.op_type][side]["AXIS_FEM"]["TOP"]["P2"]
		axis_fem_top_m1 = self.dict["FFLEX_UKR"][self.op_type][side]["AXIS_FEM"]["TOP"]["M1"]

		axis_fem_bot_p1 = self.dict["FFLEX_UKR"][self.op_type][side]["AXIS_FEM"]["BOT"]["P1"]
		axis_fem_bot_p2 = self.dict["FFLEX_UKR"][self.op_type][side]["AXIS_FEM"]["BOT"]["P2"]
		axis_fem_bot_m1 = self.dict["FFLEX_UKR"][self.op_type][side]["AXIS_FEM"]["BOT"]["M1"]


		axis_peg_top_p1 = self.dict["FFLEX_UKR"][self.op_type][side]["AXIS_PEG"]["TOP"]["P1"]
		axis_peg_top_p2 = self.dict["FFLEX_UKR"][self.op_type][side]["AXIS_PEG"]["TOP"]["P2"]
		axis_peg_top_m1 = self.dict["FFLEX_UKR"][self.op_type][side]["AXIS_PEG"]["TOP"]["M1"]

		axis_peg_bot_p1 = self.dict["FFLEX_UKR"][self.op_type][side]["AXIS_PEG"]["BOT"]["P1"]
		axis_peg_bot_p2 = self.dict["FFLEX_UKR"][self.op_type][side]["AXIS_PEG"]["BOT"]["P2"]
		axis_peg_bot_m1 = self.dict["FFLEX_UKR"][self.op_type][side]["AXIS_PEG"]["BOT"]["M1"]
		

		
		# find item type
		if "AXIS_FEM" in tags:
			item = "AXIS_FEM"

			# axis has top and bot
			if "TOP" in tags:
				topbot = "TOP"
			elif "BOT" in tags:
				topbot = "BOT"

		elif "AXIS_PEG" in tags:
			item = "AXIS_PEG"

			# axis has top and bot
			if "TOP" in tags:
				topbot = "TOP"
			elif "BOT" in tags:
				topbot = "BOT"


		if "P1" in tags:
			if item == "AXIS_FEM":
				if topbot == "TOP":
					self.drag_point = axis_fem_top_p2
					self.drag_label = "P1_AXIS_FEM_TOP"
					self.drag_side 	= side

				elif topbot == "BOT":
					self.drag_point = axis_fem_bot_p2
					self.drag_label = "P1_AXIS_FEM_BOT"
					self.drag_side 	= side

			elif item == "AXIS_PEG":
				if topbot == "TOP":
					self.drag_point = axis_peg_top_p2
					self.drag_label = "P1_AXIS_PEG_TOP"
					self.drag_side 	= side

				elif topbot == "BOT":
					self.drag_point = axis_peg_bot_p2
					self.drag_label = "P1_AXIS_PEG_BOT"
					self.drag_side 	= side


		if "P2" in tags:
			if item == "AXIS_FEM":
				if topbot == "TOP":
					self.drag_point = axis_fem_top_p1
					self.drag_label = "P2_AXIS_FEM_TOP"
					self.drag_side 	= side

				elif topbot == "BOT":
					self.drag_point = axis_fem_bot_p1
					self.drag_label = "P2_AXIS_FEM_BOT"
					self.drag_side 	= side

			elif item == "AXIS_PEG":
				if topbot == "TOP":
					self.drag_point = axis_peg_top_p1
					self.drag_label = "P2_AXIS_PEG_TOP"
					self.drag_side 	= side

				elif topbot == "BOT":
					self.drag_point = axis_peg_bot_p1
					self.drag_label = "P2_AXIS_PEG_BOT"
					self.drag_side 	= side


	def drag(self, P_mouse):

		if self.drag_label == "P1_AXIS_FEM_TOP" or self.drag_label == "P2_AXIS_FEM_TOP":
			if self.drag_point != None:
				self.draw_tools.clear_by_tag("TOP_AXIS_LINE")
				self.draw_tools.clear_by_tag("drag_line")
				m = self.draw_tools.midpoint(self.drag_point, P_mouse)
				self.draw_tools.create_midpoint_line(self.drag_point, P_mouse, m, "drag_line")

		if self.drag_label == "P1_AXIS_FEM_BOT" or self.drag_label == "P2_AXIS_FEM_BOT":
			if self.drag_point != None:
				self.draw_tools.clear_by_tag("BOT_AXIS_LINE")
				self.draw_tools.clear_by_tag("drag_line")
				m = self.draw_tools.midpoint(self.drag_point, P_mouse)
				self.draw_tools.create_midpoint_line(self.drag_point, P_mouse, m, "drag_line")

		if self.drag_label == "P1_AXIS_PEG_TOP" or self.drag_label == "P2_AXIS_PEG_TOP":
			if self.drag_point != None:
				self.draw_tools.clear_by_tag("TOP_AXIS_LINE")
				self.draw_tools.clear_by_tag("drag_line")
				m = self.draw_tools.midpoint(self.drag_point, P_mouse)
				self.draw_tools.create_midpoint_line(self.drag_point, P_mouse, m, "drag_line")

		if self.drag_label == "P1_AXIS_PEG_BOT" or self.drag_label == "P2_AXIS_PEG_BOT":
			if self.drag_point != None:
				self.draw_tools.clear_by_tag("BOT_AXIS_LINE")
				self.draw_tools.clear_by_tag("drag_line")
				m = self.draw_tools.midpoint(self.drag_point, P_mouse)
				self.draw_tools.create_midpoint_line(self.drag_point, P_mouse, m, "drag_line")


	def drag_stop(self, P_mouse):
		self.draw_tools.clear_by_tag("drag_line")


		if self.drag_label == "P1_AXIS_FEM_TOP":
			self.dict["FFLEX_UKR"][self.op_type][self.drag_side]["AXIS_FEM"]["TOP"]["P1"] = P_mouse
			self.dict["FFLEX_UKR"][self.op_type][self.drag_side]["AXIS_FEM"]["TOP"]["M1"] = self.draw_tools.midpoint(self.drag_point, P_mouse)
			# delete excel data from pat.json
			self.dict["EXCEL"][self.op_type][self.drag_side]["FFLEX"] = None
			self.dict["EXCEL"][self.op_type][self.drag_side]["FFLE/EXT"] = None
			self.controller.save_json()
			self.draw()

		if self.drag_label == "P2_AXIS_FEM_TOP":
			self.dict["FFLEX_UKR"][self.op_type][self.drag_side]["AXIS_FEM"]["TOP"]["P2"] = P_mouse
			self.dict["FFLEX_UKR"][self.op_type][self.drag_side]["AXIS_FEM"]["TOP"]["M1"] = self.draw_tools.midpoint(self.drag_point, P_mouse)
			# delete excel data from pat.json
			self.dict["EXCEL"][self.op_type][self.drag_side]["FFLEX"] = None
			self.dict["EXCEL"][self.op_type][self.drag_side]["FFLE/EXT"] = None
			self.controller.save_json()
			self.draw()

		if self.drag_label == "P1_AXIS_FEM_BOT":
			self.dict["FFLEX_UKR"][self.op_type][self.drag_side]["AXIS_FEM"]["BOT"]["P1"] = P_mouse
			self.dict["FFLEX_UKR"][self.op_type][self.drag_side]["AXIS_FEM"]["BOT"]["M1"] = self.draw_tools.midpoint(self.drag_point, P_mouse)
			# delete excel data from pat.json
			self.dict["EXCEL"][self.op_type][self.drag_side]["FFLEX"] = None
			self.dict["EXCEL"][self.op_type][self.drag_side]["FFLE/EXT"] = None
			self.controller.save_json()
			self.draw()

		if self.drag_label == "P2_AXIS_FEM_BOT":
			self.dict["FFLEX_UKR"][self.op_type][self.drag_side]["AXIS_FEM"]["BOT"]["P2"] = P_mouse
			self.dict["FFLEX_UKR"][self.op_type][self.drag_side]["AXIS_FEM"]["BOT"]["M1"] = self.draw_tools.midpoint(self.drag_point, P_mouse)
			# delete excel data from pat.json
			self.dict["EXCEL"][self.op_type][self.drag_side]["FFLEX"] = None
			self.dict["EXCEL"][self.op_type][self.drag_side]["FFLE/EXT"] = None
			self.controller.save_json()
			self.draw()

		if self.drag_label == "P1_AXIS_PEG_TOP":
			self.dict["FFLEX_UKR"][self.op_type][self.drag_side]["AXIS_PEG"]["TOP"]["P1"] = P_mouse
			self.dict["FFLEX_UKR"][self.op_type][self.drag_side]["AXIS_PEG"]["TOP"]["M1"] = self.draw_tools.midpoint(self.drag_point, P_mouse)
			# delete excel data from pat.json
			self.dict["EXCEL"][self.op_type][self.drag_side]["FFLEX"] = None
			self.dict["EXCEL"][self.op_type][self.drag_side]["FFLE/EXT"] = None
			self.controller.save_json()
			self.draw()

		if self.drag_label == "P2_AXIS_PEG_TOP":
			self.dict["FFLEX_UKR"][self.op_type][self.drag_side]["AXIS_PEG"]["TOP"]["P2"] = P_mouse
			self.dict["FFLEX_UKR"][self.op_type][self.drag_side]["AXIS_PEG"]["TOP"]["M1"] = self.draw_tools.midpoint(self.drag_point, P_mouse)
			# delete excel data from pat.json
			self.dict["EXCEL"][self.op_type][self.drag_side]["FFLEX"] = None
			self.dict["EXCEL"][self.op_type][self.drag_side]["FFLE/EXT"] = None
			self.controller.save_json()
			self.draw()

		if self.drag_label == "P1_AXIS_PEG_BOT":
			self.dict["FFLEX_UKR"][self.op_type][self.drag_side]["AXIS_PEG"]["BOT"]["P1"] = P_mouse
			self.dict["FFLEX_UKR"][self.op_type][self.drag_side]["AXIS_PEG"]["BOT"]["M1"] = self.draw_tools.midpoint(self.drag_point, P_mouse)
			# delete excel data from pat.json
			self.dict["EXCEL"][self.op_type][self.drag_side]["FFLEX"] = None
			self.dict["EXCEL"][self.op_type][self.drag_side]["FFLE/EXT"] = None
			self.controller.save_json()
			self.draw()

		if self.drag_label == "P2_AXIS_PEG_BOT":
			self.dict["FFLEX_UKR"][self.op_type][self.drag_side]["AXIS_PEG"]["BOT"]["P2"] = P_mouse
			self.dict["FFLEX_UKR"][self.op_type][self.drag_side]["AXIS_PEG"]["BOT"]["M1"] = self.draw_tools.midpoint(self.drag_point, P_mouse)
			# delete excel data from pat.json
			self.dict["EXCEL"][self.op_type][self.drag_side]["FFLEX"] = None
			self.dict["EXCEL"][self.op_type][self.drag_side]["FFLE/EXT"] = None
			self.controller.save_json()
			self.draw()


	def update_canvas(self, draw_tools):
		self.draw_tools = draw_tools


	def update_dict(self, master_dict):
		self.dict = master_dict


	def unset(self):
		# print("unset from "+self.name)
		self.draw_tools.clear_by_tag(self.tag)




	# def drag_start(self, tags):
	# 	pass
	# def drag(self, P_mouse):
	# 	pass
	# def drag_stop(self, P_mouse):
	# 	pass


		