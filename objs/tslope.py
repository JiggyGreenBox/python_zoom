import math
from copy import deepcopy

class TSLOPE():
	"""docstring for ClassName"""
	def __init__(self, draw_tools, master_dict, controller, op_type):
		self.name = "TSLOPE"
		self.tag = "tslope"
		self.menu_label = "TSLOPE_Menu"
		self.draw_tools = draw_tools
		self.dict = master_dict
		self.controller = controller
		self.side = None
		self.op_type = op_type

		# check if master dictionary has values
		# if not populate the dictionary
		self.checkMasterDict()

		# self.tflexext = False

		self.drag_point = None
		self.drag_label = None
		self.drag_side 	= None

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
		# print(self.dict)


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


		if action == "DEL-LEFT-TIB-LINE":
			self.dict["TSLOPE"][self.op_type]["LEFT"]["TIB_JOINT_LINE"]["P1"] = None
			self.dict["TSLOPE"][self.op_type]["LEFT"]["TIB_JOINT_LINE"]["P2"] = None
			self.side = "LEFT"

		if action == "DEL-RIGHT-TIB-LINE":
			self.dict["TSLOPE"][self.op_type]["RIGHT"]["TIB_JOINT_LINE"]["P1"] = None
			self.dict["TSLOPE"][self.op_type]["RIGHT"]["TIB_JOINT_LINE"]["P2"] = None
			self.side = "RIGHT"



		if action == "DEL-LEFT-TIB-TOP":			
			self.dict["TSLOPE"][self.op_type]["LEFT"]["AXIS_TIB"]["TOP"]["P1"] = None
			self.dict["TSLOPE"][self.op_type]["LEFT"]["AXIS_TIB"]["TOP"]["P2"] = None
			self.dict["TSLOPE"][self.op_type]["LEFT"]["AXIS_TIB"]["TOP"]["M1"] = None
			self.side = "LEFT"

		if action == "DEL-RIGHT-TIB-TOP":
			self.dict["TSLOPE"][self.op_type]["RIGHT"]["AXIS_TIB"]["TOP"]["P1"] = None
			self.dict["TSLOPE"][self.op_type]["RIGHT"]["AXIS_TIB"]["TOP"]["P2"] = None
			self.dict["TSLOPE"][self.op_type]["RIGHT"]["AXIS_TIB"]["TOP"]["M1"] = None
			self.side = "RIGHT"

		if action == "DEL-LEFT-TIB-BOT":
			self.dict["TSLOPE"][self.op_type]["LEFT"]["AXIS_TIB"]["BOT"]["P1"] = None
			self.dict["TSLOPE"][self.op_type]["LEFT"]["AXIS_TIB"]["BOT"]["P2"] = None
			self.dict["TSLOPE"][self.op_type]["LEFT"]["AXIS_TIB"]["BOT"]["M1"] = None
			self.side = "LEFT"

		if action == "DEL-RIGHT-TIB-BOT":
			self.dict["TSLOPE"][self.op_type]["RIGHT"]["AXIS_TIB"]["BOT"]["P1"] = None
			self.dict["TSLOPE"][self.op_type]["RIGHT"]["AXIS_TIB"]["BOT"]["P2"] = None
			self.dict["TSLOPE"][self.op_type]["RIGHT"]["AXIS_TIB"]["BOT"]["M1"] = None
			self.side = "RIGHT"


		# delete excel data from pat.json
		self.dict["EXCEL"][self.op_type][self.side]["TSLOPE"] = None
		self.dict["EXCEL"][self.op_type][self.side]["TFLE/EXT"] = None


		self.draw()
		self.regainHover(self.side)
		self.controller.save_json()
		self.controller.updateMenuLabel(self.getNextLabel(), self.menu_label)

	
	def draw(self):

		self.draw_tools.clear_by_tag(self.tag)

		self.point_size = self.controller.getViewPointSize()

		# loop left and right
		for side in ["LEFT","RIGHT"]:

			isTibTop 	= False
			isTibBot 	= False		
			isTibP1P2 	= False

			joint_line_p1 = self.dict["TSLOPE"][self.op_type][side]["TIB_JOINT_LINE"]["P1"]
			joint_line_p2 = self.dict["TSLOPE"][self.op_type][side]["TIB_JOINT_LINE"]["P2"]

			top_axis_tib_p1 = self.dict[self.name][self.op_type][side]["AXIS_TIB"]["TOP"]["P1"]
			top_axis_tib_p2 = self.dict[self.name][self.op_type][side]["AXIS_TIB"]["TOP"]["P2"]
			top_axis_tib_m1 = self.dict[self.name][self.op_type][side]["AXIS_TIB"]["TOP"]["M1"]
			bot_axis_tib_p1 = self.dict[self.name][self.op_type][side]["AXIS_TIB"]["BOT"]["P1"]
			bot_axis_tib_p2 = self.dict[self.name][self.op_type][side]["AXIS_TIB"]["BOT"]["P2"]			
			bot_axis_tib_m1 = self.dict[self.name][self.op_type][side]["AXIS_TIB"]["BOT"]["M1"]


			if joint_line_p1 != None:
				self.draw_tools.create_mypoint(joint_line_p1, "orange", [self.tag,side,"TIB_JOINT_LINE","P1"], point_thickness=self.point_size)

			if joint_line_p2 != None:
				self.draw_tools.create_mypoint(joint_line_p2, "orange", [self.tag,side,"TIB_JOINT_LINE","P2"], point_thickness=self.point_size)

			if joint_line_p1 != None and joint_line_p2 != None:
				self.draw_tools.create_myline(joint_line_p1, joint_line_p2, [self.tag,side,"FEM_LINE"])
				isTibP1P2 = True


			# TIB AXIS
			# TOP
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
				self.draw_tools.create_midpoint_line(bot_axis_tib_p1, bot_axis_tib_p2, bot_axis_tib_m1, [self.tag,side,"BOT_AXIS_LINE"], point_thickness=self.point_size)
				isTibBot = True

			xtop, ytop, xbot, ybot = self.draw_tools.getImageCorners()

			'''
			if isTibTop and isTibBot and isTibP1P2:

				L_p1, R_p1 = self.draw_tools.retPointsLeftRight(joint_line_p1, joint_line_p2)
				U_m1, D_m1 = self.draw_tools.retPointsUpDown(top_axis_tib_m1, bot_axis_tib_m1)

				# TIB-AXIS ray
				p_top = self.draw_tools.line_intersection(
					(U_m1, D_m1),
					(xtop, ytop))
				self.draw_tools.create_myline(D_m1, p_top, self.tag)


				# intersection point
				p_int = self.draw_tools.line_intersection(
					(U_m1, D_m1),
					(joint_line_p1, joint_line_p2))				

				# find and draw angles
				if side == "LEFT":
					angle = self.draw_tools.create_myAngle(D_m1, p_int, L_p1, self.tag,radius=30)
					self.draw_tools.create_mytext(p_int, '{0:.2f}'.format(angle), self.tag, x_offset=-60, y_offset=60)

				if side == "RIGHT":
					angle = self.draw_tools.create_myAngle(R_p1, p_int, D_m1, self.tag,radius=30)
					self.draw_tools.create_mytext(p_int, '{0:.2f}'.format(angle), self.tag, x_offset=60, y_offset=60)


				# check if value exists
				if self.dict["EXCEL"][self.op_type][side]["TSLOPE"] == None:

					self.dict["EXCEL"][self.op_type][side]["HASDATA"] 	= True
					self.dict["EXCEL"][self.op_type][side]["TSLOPE"]	= '{0:.2f}'.format(angle)

					# save after insert
					self.controller.save_json()
			'''
			if isTibTop and isTibBot:


				
				U_m1, D_m1 = self.draw_tools.retPointsUpDown(top_axis_tib_m1, bot_axis_tib_m1)

				# TIB-AXIS ray
				p_top = self.draw_tools.line_intersection(
					(U_m1, D_m1),
					(xtop, ytop))
				self.draw_tools.create_myline(D_m1, p_top, self.tag)


				if isTibP1P2:
					L_p1, R_p1 = self.draw_tools.retPointsLeftRight(joint_line_p1, joint_line_p2)

					# intersection point
					p_int = self.draw_tools.line_intersection(
						(U_m1, D_m1),
						(joint_line_p1, joint_line_p2))				

					# find and draw angles
					if side == "LEFT":
						angle = self.draw_tools.create_myAngle(D_m1, p_int, L_p1, [self.tag, "TSLOPE_angle"],radius=30)
						self.draw_tools.create_mytext(p_int, '{0:.2f}'.format(angle), self.tag, color="blue", x_offset=-60, y_offset=60)

					if side == "RIGHT":
						angle = self.draw_tools.create_myAngle(R_p1, p_int, D_m1, [self.tag, "TSLOPE_angle"],radius=30)
						self.draw_tools.create_mytext(p_int, '{0:.2f}'.format(angle), self.tag, color="blue", x_offset=60, y_offset=60)


					# check if value exists
					if self.dict["EXCEL"][self.op_type][side]["TSLOPE"] == None:
						self.dict["EXCEL"][self.op_type][side]["HASDATA"] 	= True
						self.dict["EXCEL"][self.op_type][side]["TSLOPE"]	= '{0:.2f}'.format(angle)
						self.controller.save_json()

					# check T-VAR-VAL
					# if self.tflexext:
					# fem to axis intersection
					# p_int
					# self.draw_tools.create_mypoint(p_int, "orange", [self.tag, side, "NO-DRAG"], point_thickness=self.point_size)

					# find perpendicular point
					slope = self.draw_tools.slope(U_m1, D_m1)				
					dy = math.sqrt(100**2/(slope**2+1))
					dx = -slope*dy

					C = [0,0]
					C[0] = p_int[0] + dx
					C[1] = p_int[1] + dy

					tflexext_angle = -1

					if side == "RIGHT":
						R_perpend_border = self.draw_tools.line_intersection((C, p_int), (ytop, ybot))
						tflexext_angle = self.draw_tools.getSmallestAngle(R_perpend_border, p_int, R_p1)
						print('RIGHT: {0:.2f}'.format(tflexext_angle))
						self.draw_tools.create_mytext(p_int, '{0:.2f}'.format(tflexext_angle), self.tag, color="blue", x_offset=60, y_offset=-80)

					if side == "LEFT":
						L_perpend_border = self.draw_tools.line_intersection((C, p_int), (xtop, xbot))
						tflexext_angle = self.draw_tools.getSmallestAngle(L_p1, p_int, L_perpend_border)
						print('LEFT: {0:.2f}'.format(tflexext_angle))
						self.draw_tools.create_mytext(p_int, '{0:.2f}'.format(tflexext_angle), self.tag, color="blue", x_offset=60, y_offset=-80)

					# save TFLE/EXT to excel
					if tflexext_angle != -1:							
						if self.dict["EXCEL"][self.op_type][side]["TFLE/EXT"] == None:
							self.dict["EXCEL"][self.op_type][side]["HASDATA"] 	= True
							self.dict["EXCEL"][self.op_type][side]["TFLE/EXT"]	= '{0:.2f}'.format(tflexext_angle)
							self.controller.save_json()						


	def checkMasterDict(self):
		if "TSLOPE" not in self.dict.keys():
			self.dict["TSLOPE"] = 	{
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

		for item in self.dict["TSLOPE"][self.op_type][self.side]:

			# get item type 
			item_type = self.dict["TSLOPE"][self.op_type][self.side][item]["type"]

			# get the point from mouse click
			P = self.draw_tools.getRealCoords(event)
			


			# axis has two midpoints
			if item_type == "axis":
				# axis has a top and a bottom
				# TOP

				# check if P1 is None
				if self.dict["TSLOPE"][self.op_type][self.side][item]["TOP"]["P1"] == None:					
					self.dict["TSLOPE"][self.op_type][self.side][item]["TOP"]["P1"] = P
					self.draw_tools.setHoverPointLabel("P1_AXIS_TIB_TOP")
					self.draw_tools.setHoverPoint(P)
					self.draw_tools.setHoverBool(True)
					return True

				# check if P2 is None				
				if self.dict["TSLOPE"][self.op_type][self.side][item]["TOP"]["P2"] == None:					
					self.dict["TSLOPE"][self.op_type][self.side][item]["TOP"]["P2"] = P
					self.dict["TSLOPE"][self.op_type][self.side][item]["TOP"]["M1"] = self.draw_tools.midpoint(self.dict["TSLOPE"][self.op_type][self.side][item]["TOP"]["P1"], P)
					self.draw_tools.setHoverBool(False)
					self.draw_tools.setHoverPointLabel(None)
					return True

				# BOT
				# check if P1 is None
				if self.dict["TSLOPE"][self.op_type][self.side][item]["BOT"]["P1"] == None:					
					self.dict["TSLOPE"][self.op_type][self.side][item]["BOT"]["P1"] = P
					self.draw_tools.setHoverPointLabel("P1_AXIS_TIB_BOT")
					self.draw_tools.setHoverPoint(P)
					self.draw_tools.setHoverBool(True)
					return True

				# check if P2 is None				
				if self.dict["TSLOPE"][self.op_type][self.side][item]["BOT"]["P2"] == None:					
					self.dict["TSLOPE"][self.op_type][self.side][item]["BOT"]["P2"] = P
					self.dict["TSLOPE"][self.op_type][self.side][item]["BOT"]["M1"] = self.draw_tools.midpoint(self.dict["TSLOPE"][self.op_type][self.side][item]["BOT"]["P1"], P)
					self.draw_tools.setHoverBool(False)
					self.draw_tools.setHoverPointLabel(None)
					return True					


			# line has P1 and P2
			if item_type == "line":

				# check if P1 is None				
				if self.dict["TSLOPE"][self.op_type][self.side][item]["P1"] == None:					
					self.dict["TSLOPE"][self.op_type][self.side][item]["P1"] = P
					self.draw_tools.setHoverPointLabel("P1_TIB_JOINT_LINE")
					self.draw_tools.setHoverPoint(P)
					self.draw_tools.setHoverBool(True)
					return True


				# check if P2 is None				
				if self.dict["TSLOPE"][self.op_type][self.side][item]["P2"] == None:					
					self.dict["TSLOPE"][self.op_type][self.side][item]["P2"] = P
					self.draw_tools.setHoverBool(False)
					self.draw_tools.setHoverPointLabel(None)
					return True

		return False	


	def getNextLabel(self):

		if self.side != None:
			for item in self.dict["TSLOPE"][self.op_type][self.side]:
				# get item type 
				item_type = self.dict["TSLOPE"][self.op_type][self.side][item]["type"]

				
				


				# axis has two midpoints
				if item_type == "axis":				
					# axis has a top and a bottom
					# TOP

					# check if P1 is None
					if self.dict["TSLOPE"][self.op_type][self.side][item]["TOP"]["P1"] == None:						
						return (self.side + " " + item + " TOP P1")

					# check if P2 is None				
					if self.dict["TSLOPE"][self.op_type][self.side][item]["TOP"]["P2"] == None:						
						return (self.side + " " + item + " TOP P2")

					# BOT
					# check if P1 is None
					if self.dict["TSLOPE"][self.op_type][self.side][item]["BOT"]["P1"] == None:						
						return (self.side + " " + item + " BOT P1")

					# check if P2 is None				
					if self.dict["TSLOPE"][self.op_type][self.side][item]["BOT"]["P2"] == None:
						return (self.side + " " + item + " BOT P2")


				# line has P1 and P2
				if item_type == "line":

					# check if P1 is None				
					if self.dict["TSLOPE"][self.op_type][self.side][item]["P1"] == None:						
						return (self.side + " " + item + " P1")


					# check if P2 is None				
					if self.dict["TSLOPE"][self.op_type][self.side][item]["P2"] == None:						
						return (self.side + " " + item + " P2")

			return (self.side + " Done")

		return None


	def update_canvas(self, draw_tools):
		self.draw_tools = draw_tools

	def hover(self, P_mouse, P_stored, hover_label):

		# prevent auto curObject set bug
		if self.side == None:
			return


		if self.draw_hover:
			side_pre = self.side[0]+"_"
			if(	hover_label == "P0_AXIS_TIB_TOP" or
				hover_label == "P0_AXIS_TIB_BOT" or
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

			axis_fem_bot_m1 = self.dict["TSLOPE"][self.op_type][self.side]["AXIS_TIB"]["BOT"]["M1"]
			xtop, ytop, xbot, ybot = self.draw_tools.getImageCorners()

			if axis_fem_bot_m1 != None:
				# FEM-AXIS ray
				p_int = self.draw_tools.line_intersection(
					(axis_fem_bot_m1, m),
					(xtop, ytop))
				self.draw_tools.create_myline(axis_fem_bot_m1, p_int, "hover_line")


		if hover_label == "P1_AXIS_TIB_BOT":
			self.draw_tools.clear_by_tag("hover_line")
			m = self.draw_tools.midpoint(P_stored, P_mouse)
			self.draw_tools.create_midpoint_line(P_stored, P_mouse, m, "hover_line", point_thickness=self.point_size)

			axis_fem_top_m1 = self.dict["TSLOPE"][self.op_type][self.side]["AXIS_TIB"]["TOP"]["M1"]
			xtop, ytop, xbot, ybot = self.draw_tools.getImageCorners()

			if axis_fem_top_m1 != None:
				# FEM-AXIS ray
				p_int = self.draw_tools.line_intersection(
					(axis_fem_top_m1, m),
					(xtop, ytop))
				self.draw_tools.create_myline(m, p_int, "hover_line")


		if hover_label == "P1_TIB_JOINT_LINE":
			self.draw_tools.clear_by_tag("hover_line")
			self.draw_tools.create_myline(P_stored, P_mouse, "hover_line")


		# if hover_label == "P1_top":
		# 	self.draw_tools.clear_by_tag("hover_line")
		# 	m = self.draw_tools.midpoint(P_stored, P_mouse)
		# 	self.draw_tools.create_midpoint_line(P_stored, P_mouse, m, "hover_line", point_thickness=self.point_size)

		# 	axis_fem_bot_m1 = self.dict["TSLOPE"][self.op_type][self.side]["AXIS_TIB"]["BOT"]["M1"]
		# 	xtop, ytop, xbot, ybot = self.draw_tools.getImageCorners()

		# 	if axis_fem_bot_m1 != None:
		# 		# FEM-AXIS ray
		# 		p_int = self.draw_tools.line_intersection(
		# 			(axis_fem_bot_m1, m),
		# 			(xtop, ytop))
		# 		self.draw_tools.create_myline(axis_fem_bot_m1, p_int, "hover_line")

		# if hover_label == "P1_bot":
		# 	self.draw_tools.clear_by_tag("hover_line")
		# 	m = self.draw_tools.midpoint(P_stored, P_mouse)
		# 	self.draw_tools.create_midpoint_line(P_stored, P_mouse, m, "hover_line", point_thickness=self.point_size)

		# 	axis_fem_top_m1 = self.dict["TSLOPE"][self.op_type][self.side]["AXIS_TIB"]["TOP"]["M1"]
		# 	xtop, ytop, xbot, ybot = self.draw_tools.getImageCorners()

		# 	if axis_fem_top_m1 != None:
		# 		# FEM-AXIS ray
		# 		p_int = self.draw_tools.line_intersection(
		# 			(axis_fem_top_m1, m),
		# 			(xtop, ytop))
		# 		self.draw_tools.create_myline(m, p_int, "hover_line")


		# if hover_label == "P1_joint_line":
		# 	self.draw_tools.clear_by_tag("hover_line")
		# 	self.draw_tools.create_myline(P_stored, P_mouse, "hover_line")


	def regainHover(self, side):
		joint_line_p1 = self.dict["TSLOPE"][self.op_type][side]["TIB_JOINT_LINE"]["P1"]
		joint_line_p2 = self.dict["TSLOPE"][self.op_type][side]["TIB_JOINT_LINE"]["P2"]

		top_axis_tib_p1 = self.dict[self.name][self.op_type][side]["AXIS_TIB"]["TOP"]["P1"]
		top_axis_tib_p2 = self.dict[self.name][self.op_type][side]["AXIS_TIB"]["TOP"]["P2"]
		bot_axis_tib_p1 = self.dict[self.name][self.op_type][side]["AXIS_TIB"]["BOT"]["P1"]
		bot_axis_tib_p2 = self.dict[self.name][self.op_type][side]["AXIS_TIB"]["BOT"]["P2"]		


		# find if P0 hovers are required
		self.mainHoverUsingNextLabel()


		if top_axis_tib_p1 != None and top_axis_tib_p2 == None:
			self.draw_tools.setHoverPointLabel("P1_AXIS_TIB_TOP")
			self.draw_tools.setHoverPoint(top_axis_tib_p1)
			self.draw_tools.setHoverBool(True)

		if bot_axis_tib_p1 != None and bot_axis_tib_p2 == None:
			self.draw_tools.setHoverPointLabel("P1_AXIS_TIB_BOT")
			self.draw_tools.setHoverPoint(bot_axis_tib_p1)
			self.draw_tools.setHoverBool(True)

		if joint_line_p1 != None and joint_line_p2 == None:
			self.draw_tools.setHoverPointLabel("P1_TIB_JOINT_LINE")
			self.draw_tools.setHoverPoint(joint_line_p1)
			self.draw_tools.setHoverBool(True)


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
		axis_tib_top_p1 = self.dict["TSLOPE"][self.op_type][side]["AXIS_TIB"]["TOP"]["P1"]
		axis_tib_top_p2 = self.dict["TSLOPE"][self.op_type][side]["AXIS_TIB"]["TOP"]["P2"]
		axis_tib_top_m1 = self.dict["TSLOPE"][self.op_type][side]["AXIS_TIB"]["TOP"]["M1"]

		axis_tib_bot_p1 = self.dict["TSLOPE"][self.op_type][side]["AXIS_TIB"]["BOT"]["P1"]
		axis_tib_bot_p2 = self.dict["TSLOPE"][self.op_type][side]["AXIS_TIB"]["BOT"]["P2"]
		axis_tib_bot_m1 = self.dict["TSLOPE"][self.op_type][side]["AXIS_TIB"]["BOT"]["M1"]


		tib_joint_p1 = self.dict["TSLOPE"][self.op_type][side]["TIB_JOINT_LINE"]["P1"]
		tib_joint_p2 = self.dict["TSLOPE"][self.op_type][side]["TIB_JOINT_LINE"]["P2"]


		


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
				self.draw_tools.clear_by_tag("TSLOPE_angle")
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
				self.draw_tools.clear_by_tag("TSLOPE_angle")
				self.drag_point = tib_joint_p1
				self.drag_label = "P2_JOINT"
				self.drag_side 	= side


	def drag(self, P_mouse):

		if self.drag_label == "P1_JOINT" or self.drag_label == "P2_JOINT":
			if self.drag_point != None:
				self.draw_tools.clear_by_tag("FEM_LINE")
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
			self.dict["TSLOPE"][self.op_type][self.drag_side]["TIB_JOINT_LINE"]["P1"] = P_mouse
			# delete excel data from pat.json
			self.dict["EXCEL"][self.op_type][self.drag_side]["TSLOPE"] = None
			self.dict["EXCEL"][self.op_type][self.drag_side]["TFLE/EXT"] = None
			self.controller.save_json()
			self.draw()

		if self.drag_label == "P2_JOINT":
			self.dict["TSLOPE"][self.op_type][self.drag_side]["TIB_JOINT_LINE"]["P2"] = P_mouse
			# delete excel data from pat.json
			self.dict["EXCEL"][self.op_type][self.drag_side]["TSLOPE"] = None
			self.dict["EXCEL"][self.op_type][self.drag_side]["TFLE/EXT"] = None
			self.controller.save_json()
			self.draw()


		if self.drag_label == "P1_AXIS_TIB_TOP":
			self.dict["TSLOPE"][self.op_type][self.drag_side]["AXIS_TIB"]["TOP"]["P1"] = P_mouse
			self.dict["TSLOPE"][self.op_type][self.drag_side]["AXIS_TIB"]["TOP"]["M1"] = self.draw_tools.midpoint(self.drag_point, P_mouse)
			# delete excel data from pat.json
			self.dict["EXCEL"][self.op_type][self.drag_side]["TSLOPE"] = None
			self.dict["EXCEL"][self.op_type][self.drag_side]["TFLE/EXT"] = None
			self.controller.save_json()
			self.draw()

		if self.drag_label == "P2_AXIS_TIB_TOP":
			self.dict["TSLOPE"][self.op_type][self.drag_side]["AXIS_TIB"]["TOP"]["P2"] = P_mouse
			self.dict["TSLOPE"][self.op_type][self.drag_side]["AXIS_TIB"]["TOP"]["M1"] = self.draw_tools.midpoint(self.drag_point, P_mouse)
			# delete excel data from pat.json
			self.dict["EXCEL"][self.op_type][self.drag_side]["TSLOPE"] = None
			self.dict["EXCEL"][self.op_type][self.drag_side]["TFLE/EXT"] = None
			self.controller.save_json()
			self.draw()

		if self.drag_label == "P1_AXIS_TIB_BOT":
			self.dict["TSLOPE"][self.op_type][self.drag_side]["AXIS_TIB"]["BOT"]["P1"] = P_mouse
			self.dict["TSLOPE"][self.op_type][self.drag_side]["AXIS_TIB"]["BOT"]["M1"] = self.draw_tools.midpoint(self.drag_point, P_mouse)
			# delete excel data from pat.json
			self.dict["EXCEL"][self.op_type][self.drag_side]["TSLOPE"] = None
			self.dict["EXCEL"][self.op_type][self.drag_side]["TFLE/EXT"] = None
			self.controller.save_json()
			self.draw()

		if self.drag_label == "P2_AXIS_TIB_BOT":
			self.dict["TSLOPE"][self.op_type][self.drag_side]["AXIS_TIB"]["BOT"]["P2"] = P_mouse
			self.dict["TSLOPE"][self.op_type][self.drag_side]["AXIS_TIB"]["BOT"]["M1"] = self.draw_tools.midpoint(self.drag_point, P_mouse)
			# delete excel data from pat.json
			self.dict["EXCEL"][self.op_type][self.side]["TSLOPE"] = None
			self.dict["EXCEL"][self.op_type][self.side]["TFLE/EXT"] = None
			self.controller.save_json()
			self.draw()


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


	def escapeObjFunc(self):
		self.side = None
		self.draw_tools.setHoverPointLabel(None)
		self.draw_tools.setHoverBool(False)


	def mainHoverUsingNextLabel(self):
		label = self.getNextLabel()

		
		if label == "RIGHT AXIS_TIB TOP P1":
			self.side = "RIGHT"
			self.hover_text = "AXIS_TIB_TOP"
			self.draw_tools.setHoverPointLabel("P0_AXIS_TIB_TOP")
			self.draw_tools.setHoverPoint(None)
			self.draw_tools.setHoverBool(True)
		elif label == "LEFT AXIS_TIB TOP P1":
			self.side = "LEFT"
			self.hover_text = "AXIS_TIB_TOP"
			self.draw_tools.setHoverPointLabel("P0_AXIS_TIB_TOP")
			self.draw_tools.setHoverPoint(None)
			self.draw_tools.setHoverBool(True)


		if label == "RIGHT AXIS_TIB BOT P1":
			self.side = "RIGHT"
			self.hover_text = "AXIS_TIB_BOT"
			self.draw_tools.setHoverPointLabel("P0_AXIS_TIB_BOT")
			self.draw_tools.setHoverPoint(None)
			self.draw_tools.setHoverBool(True)
		elif label == "LEFT AXIS_TIB BOT P1":
			self.side = "LEFT"
			self.hover_text = "AXIS_TIB_BOT"
			self.draw_tools.setHoverPointLabel("P0_AXIS_TIB_BOT")
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


	def obj_draw_pil(self):
		print('draw PIL TSLOPE')

		# borrow from draw
		self.point_size = self.controller.getViewPointSize()

		
		# get points for drawing if both legs are available
		LL_p = deepcopy(self.dict["TSLOPE"][self.op_type]["LEFT"]["TIB_JOINT_LINE"]["P1"])
		LR_p = deepcopy(self.dict["TSLOPE"][self.op_type]["LEFT"]["TIB_JOINT_LINE"]["P2"])
		RL_p = deepcopy(self.dict["TSLOPE"][self.op_type]["RIGHT"]["TIB_JOINT_LINE"]["P1"])
		RR_p = deepcopy(self.dict["TSLOPE"][self.op_type]["RIGHT"]["TIB_JOINT_LINE"]["P2"])

		L_draw = None
		R_draw = None

		if LL_p != None and LR_p != None:
			LL_p, LR_p = self.draw_tools.retPointsLeftRight(LL_p, LR_p)

		if RL_p != None and RR_p != None:
			RL_p, RR_p = self.draw_tools.retPointsLeftRight(RL_p, RR_p)


		# uncomment for yadjusted draw points
		# if LL_p != None and RR_p != None:
		# 	# L_draw, R_draw = self.draw_tools.get_yaxis_adjusted_points(LL_p, RR_p)
		# 	# normal L/R and medical L/R bug here
		# 	# careful
		# 	R_draw, L_draw = self.draw_tools.get_yaxis_adjusted_points(LL_p, RR_p)


		# loop left and right
		for side in ["LEFT","RIGHT"]:

			isTibTop 	= False
			isTibBot 	= False		
			isTibP1P2 	= False

			joint_line_p1 = self.dict["TSLOPE"][self.op_type][side]["TIB_JOINT_LINE"]["P1"]
			joint_line_p2 = self.dict["TSLOPE"][self.op_type][side]["TIB_JOINT_LINE"]["P2"]

			top_axis_tib_m1 = self.dict[self.name][self.op_type][side]["AXIS_TIB"]["TOP"]["M1"]
			bot_axis_tib_m1 = self.dict[self.name][self.op_type][side]["AXIS_TIB"]["BOT"]["M1"]


			if joint_line_p1 != None and joint_line_p2 != None:
				isTibP1P2 = True

			if top_axis_tib_m1 != None:
				isTibTop = True

			# BOT			
			if bot_axis_tib_m1 != None:
				isTibBot = True


			if isTibTop and isTibBot and isTibP1P2:
				
				U_m1, D_m1 = self.draw_tools.retPointsUpDown(top_axis_tib_m1, bot_axis_tib_m1)

				# intersection
				p_int = self.draw_tools.line_intersection((U_m1, D_m1), (joint_line_p1, joint_line_p2))

				# join intersection to lower M1
				self.draw_tools.pil_create_mypoint(D_m1, "orange", point_thickness=self.point_size)
				self.draw_tools.pil_create_myline(p_int, D_m1)

				tslope_angle = ""
				multi_text = ""
				p_draw = None
				xoffset = 100
				yoffset = 0

				isr_val = self.dict["EXCEL"][self.op_type][side]["ISR"]
				
				

				if side == "LEFT":
					self.draw_tools.pil_create_mypoint(LL_p, "orange", point_thickness=self.point_size)
					self.draw_tools.pil_create_myline(p_int, LL_p)
					tslope_angle = self.draw_tools.pil_create_myAngle(D_m1, p_int, LL_p)

					# overwrite if isr is available
					multi_text = 'TSLOPE: {0:.2f}'.format(tslope_angle)
					if isr_val != None:
						tslope_text = 'TSLOPE: {0:.2f}'.format(tslope_angle)
						isr_text = 'ISR: {}'.format(isr_val)
						nl = "\n"
						multi_text = tslope_text + nl + isr_text

					xoffset = -1*(xoffset + self.draw_tools.pil_get_multiline_text_size(multi_text))

					# other leg data is missing if None
					if L_draw == None:
						p_draw = LL_p
					else:
						p_draw = L_draw					

				# if side == "RIGHT":
				elif side == "RIGHT":
					self.draw_tools.pil_create_mypoint(RR_p, "orange", point_thickness=self.point_size)
					self.draw_tools.pil_create_myline(p_int, RR_p)
					tslope_angle = self.draw_tools.pil_create_myAngle(RR_p, p_int, D_m1)

					# overwrite if isr is available
					multi_text = 'TSLOPE: {0:.2f}'.format(tslope_angle)
					if isr_val != None:
						tslope_text = 'TSLOPE: {0:.2f}'.format(tslope_angle)
						isr_text = 'ISR: {}'.format(isr_val)
						nl = "\n"
						multi_text = tslope_text + nl + isr_text
					

					# other leg data is missing if None
					if R_draw == None:
						p_draw = RR_p
					else:
						p_draw = R_draw


			
				# p_draw is assigned correctly, proceed				
				x1,y1,x2,y2 = self.draw_tools.pil_get_text_bbox(p_draw, multi_text, x_offset=xoffset, y_offset=yoffset)
				self.draw_tools.pil_draw_rect([x1,y1,x2,y2], padding=20)
				self.draw_tools.pil_create_multiline_text(p_draw, multi_text, x_offset=xoffset, y_offset=yoffset, color=(255,255,255,255))





				# angle = self.draw_tools.create_myAngle(D_m1, p_int, L_p1
				# angle = self.draw_tools.create_myAngle(R_p1, p_int, D_m1