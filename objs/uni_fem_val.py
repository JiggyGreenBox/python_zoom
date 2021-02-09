

class UNI_FEM_VAL():
	"""docstring for ClassName"""
	def __init__(self, draw_tools, master_dict, controller, op_type):
		self.name = "UNI_FEM_VAL"
		self.tag = "uni_fem_val"
		self.menu_label = "UNI_FEM_VAL_Menu"
		self.draw_tools = draw_tools
		self.dict = master_dict
		self.controller = controller
		self.side = None
		self.op_type = op_type

		# check if master dictionary has values
		# if not populate the dictionary
		self.checkMasterDict()

		self.point_size = None


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


	# menu button clicks are routed here
	def menu_btn_click(self, action):
		print(action)
		if action == "SET-LEFT":
			self.side = "LEFT"
			self.controller.updateMenuLabel(self.getNextLabel(), self.menu_label)
			return # avoid clear,draw,json_save

		if action == "SET-RIGHT":
			self.side = "RIGHT"
			self.controller.updateMenuLabel(self.getNextLabel(), self.menu_label)
			return # avoid clear,draw,json_save

		if action == "DEL-LEFT-FEM-TOP":
			self.dict[self.name][self.op_type]["LEFT"]["AXIS_FEM"]["TOP"]["P1"] = None
			self.dict[self.name][self.op_type]["LEFT"]["AXIS_FEM"]["TOP"]["P2"] = None
			self.dict[self.name][self.op_type]["LEFT"]["AXIS_FEM"]["TOP"]["M1"] = None
			self.side = "LEFT"

		if action == "DEL-RIGHT-FEM-TOP":
			self.dict[self.name][self.op_type]["RIGHT"]["AXIS_FEM"]["TOP"]["P1"] = None
			self.dict[self.name][self.op_type]["RIGHT"]["AXIS_FEM"]["TOP"]["P2"] = None
			self.dict[self.name][self.op_type]["RIGHT"]["AXIS_FEM"]["TOP"]["M1"] = None
			self.side = "RIGHT"

		if action == "DEL-LEFT-FEM-BOT":
			self.dict[self.name][self.op_type]["LEFT"]["AXIS_FEM"]["BOT"]["P1"] = None
			self.dict[self.name][self.op_type]["LEFT"]["AXIS_FEM"]["BOT"]["P2"] = None
			self.dict[self.name][self.op_type]["LEFT"]["AXIS_FEM"]["BOT"]["M1"] = None
			self.side = "LEFT"

		if action == "DEL-RIGHT-FEM-BOT":
			self.dict[self.name][self.op_type]["RIGHT"]["AXIS_FEM"]["BOT"]["P1"] = None
			self.dict[self.name][self.op_type]["RIGHT"]["AXIS_FEM"]["BOT"]["P2"] = None
			self.dict[self.name][self.op_type]["RIGHT"]["AXIS_FEM"]["BOT"]["M1"] = None
			self.side = "RIGHT"

		if action == "DEL-LEFT-FEM-LINE":
			self.dict[self.name][self.op_type]["LEFT"]["FEM_JOINT_LINE"]["P1"] = None
			self.dict[self.name][self.op_type]["LEFT"]["FEM_JOINT_LINE"]["P2"] = None
			self.side = "LEFT"

		if action == "DEL-RIGHT-FEM-LINE":
			self.dict[self.name][self.op_type]["RIGHT"]["FEM_JOINT_LINE"]["P1"] = None
			self.dict[self.name][self.op_type]["RIGHT"]["FEM_JOINT_LINE"]["P2"] = None
			self.side = "RIGHT"


		# delete excel data from pat.json
		self.dict["EXCEL"][self.op_type][self.side]["FVAR/VAL"] = None
		
		self.draw()
		self.controller.save_json()
		
		self.controller.updateMenuLabel(self.getNextLabel(), self.menu_label)



	def draw(self):

		self.draw_tools.clear_by_tag(self.tag)

		self.point_size = self.controller.getViewPointSize()

		# loop left and right				
		for side in ["LEFT","RIGHT"]:

			isFemJointLine = False
			isFemTop 	= False
			isFemBot 	= False


			fem_line_p1 = self.dict["UNI_FEM_VAL"][self.op_type][side]["FEM_JOINT_LINE"]["P1"]
			fem_line_p2 = self.dict["UNI_FEM_VAL"][self.op_type][side]["FEM_JOINT_LINE"]["P2"]


			axis_fem_top_p1 = self.dict["UNI_FEM_VAL"][self.op_type][side]["AXIS_FEM"]["TOP"]["P1"]
			axis_fem_top_p2 = self.dict["UNI_FEM_VAL"][self.op_type][side]["AXIS_FEM"]["TOP"]["P2"]
			axis_fem_top_m1 = self.dict["UNI_FEM_VAL"][self.op_type][side]["AXIS_FEM"]["TOP"]["M1"]
			
			axis_fem_bot_p1 = self.dict["UNI_FEM_VAL"][self.op_type][side]["AXIS_FEM"]["BOT"]["P1"]
			axis_fem_bot_p2 = self.dict["UNI_FEM_VAL"][self.op_type][side]["AXIS_FEM"]["BOT"]["P2"]
			axis_fem_bot_m1 = self.dict["UNI_FEM_VAL"][self.op_type][side]["AXIS_FEM"]["BOT"]["M1"]

			# FEM JOINT LINE
			if fem_line_p1 != None:
				self.draw_tools.create_mypoint(fem_line_p1, "orange", [self.tag,side,"FEM_JOINT_LINE","P1"], point_thickness=self.point_size)

			if fem_line_p2 != None:
				self.draw_tools.create_mypoint(fem_line_p2, "orange", [self.tag,side,"FEM_JOINT_LINE","P2"], point_thickness=self.point_size)

			if fem_line_p1 != None and fem_line_p2 != None:
				self.draw_tools.create_myline(fem_line_p1, fem_line_p2, [self.tag,side,"FEM_LINE"])
				isFemJointLine = True



			# FEM AXIS
			# TOP
			if axis_fem_top_p1 != None:
				self.draw_tools.create_mypoint(axis_fem_top_p1, "orange", [self.tag,side,"AXIS_FEM","TOP","P1"], point_thickness=self.point_size)

			if axis_fem_top_p2 != None:
				self.draw_tools.create_mypoint(axis_fem_top_p2, "orange", [self.tag,side,"AXIS_FEM","TOP","P2"], point_thickness=self.point_size)

			if axis_fem_top_p1 != None and axis_fem_top_p2 != None:				
				self.draw_tools.create_midpoint_line(axis_fem_top_p1, axis_fem_top_p2, axis_fem_top_m1, [self.tag,side,"TOP_AXIS_LINE"], point_thickness=self.point_size)
				isFemTop = True


			# BOT
			if axis_fem_bot_p1 != None:
				self.draw_tools.create_mypoint(axis_fem_bot_p1, "orange", [self.tag,side,"AXIS_FEM","BOT","P1"], point_thickness=self.point_size)

			if axis_fem_bot_p2 != None:
				self.draw_tools.create_mypoint(axis_fem_bot_p2, "orange", [self.tag,side,"AXIS_FEM","BOT","P2"], point_thickness=self.point_size)

			if axis_fem_bot_p1 != None and axis_fem_bot_p2 != None:				
				self.draw_tools.create_midpoint_line(axis_fem_bot_p1, axis_fem_bot_p2, axis_fem_bot_m1, [self.tag,side,"BOT_AXIS_LINE"], point_thickness=self.point_size)
				isFemBot = True

			# if isFemJointLine and isFemTop and isFemBot:
			if isFemTop and isFemBot:
				# axis
				U_fem_m1, D_fem_m1 = self.draw_tools.retPointsUpDown(axis_fem_top_m1, axis_fem_bot_m1)
				

				xtop, ytop, xbot, ybot = self.draw_tools.getImageCorners()

				# fem axis extension
				p_axis_bot = self.draw_tools.line_intersection((U_fem_m1, D_fem_m1), (xbot, ybot))
				self.draw_tools.create_myline(U_fem_m1, p_axis_bot, self.tag)

				


				if isFemJointLine:

					# line
					U_fem_p1, D_fem_p1 = self.draw_tools.retPointsUpDown(fem_line_p1, fem_line_p2)

					# fem line extension
					p_line_bot = self.draw_tools.line_intersection((fem_line_p1, fem_line_p2), (xbot, ybot))
					self.draw_tools.create_myline(D_fem_p1, p_line_bot, [self.tag,"FEM_LINE"])

					# fem-axis and fem-line intersection
					p_int = self.draw_tools.line_intersection((U_fem_m1, p_axis_bot), (D_fem_p1, p_line_bot))


					a1 = self.draw_tools.getAnglePoints(U_fem_m1, p_int, U_fem_p1)
					a2 = self.draw_tools.getAnglePoints(U_fem_p1, p_int, U_fem_m1)
					print('{0:.2f} a1 RIGHT'.format(a1))
					print('{0:.2f} a2 RIGHT'.format(a2))

					if a1 > a2:					
						angle = self.draw_tools.create_myAngle(U_fem_p1, p_int, U_fem_m1, self.tag)
					else:
						angle = self.draw_tools.create_myAngle(U_fem_m1, p_int, U_fem_p1, self.tag)
						
						
					

					# check if intersection point is above or below
					# if above then
					# else 
					check_U, check_D = self.draw_tools.retPointsUpDown(p_int, U_fem_m1)
					if(p_int == check_U):
						print('{} point is above so +ve'.format(side))
					else:
						angle = angle * -1
						print('{} point is below so -ve'.format(side))

					self.draw_tools.create_mytext(U_fem_p1, '{0:.2f}'.format(angle), self.tag, y_offset=-60, color="blue")

					# F-VAR-VAL
					if self.dict["EXCEL"][self.op_type][side]["FVAR/VAL"] == None:
						self.dict["EXCEL"][self.op_type][side]["HASDATA"] 	= True
						self.dict["EXCEL"][self.op_type][side]["FVAR/VAL"]	= '{0:.2f}'.format(angle)
						self.controller.save_json()
					

			
			



	def checkMasterDict(self):
		if "UNI_FEM_VAL" not in self.dict.keys():
			self.dict["UNI_FEM_VAL"] = 	{
											"PRE-OP":{
												"LEFT":	{
															"AXIS_FEM":	{
																			"type":	"axis",
																			"TOP":	{"type":"midpoint","P1":None,"P2":None, "M1":None},
																			"BOT":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
																		},
															"FEM_JOINT_LINE":	{"type":"line","P1":None,"P2":None}
														},
												"RIGHT":{
															"AXIS_FEM":	{
																			"type":	"axis",
																			"TOP":	{"type":"midpoint","P1":None,"P2":None, "M1":None},
																			"BOT":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
																		},
															"FEM_JOINT_LINE":	{"type":"line","P1":None,"P2":None}
														}
											},
											"POST-OP":{
												"LEFT":	{
															"AXIS_FEM":	{
																			"type":	"axis",
																			"TOP":	{"type":"midpoint","P1":None,"P2":None, "M1":None},
																			"BOT":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
																		},
															"FEM_JOINT_LINE":	{"type":"line","P1":None,"P2":None}
														},
												"RIGHT":{
															"AXIS_FEM":	{
																			"type":	"axis",
																			"TOP":	{"type":"midpoint","P1":None,"P2":None, "M1":None},
																			"BOT":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
																		},
															"FEM_JOINT_LINE":	{"type":"line","P1":None,"P2":None}
														}
											}											
										}


	def addDict(self, event):
		for item in self.dict["UNI_FEM_VAL"][self.op_type][self.side]:

			# get real coords
			P = self.draw_tools.getRealCoords(event)

			# get item type 
			item_type = self.dict["UNI_FEM_VAL"][self.op_type][self.side][item]["type"]
			

			# axis has two midpoints
			if item_type == "axis":
				print("axis" + item)
				# axis has a top and a bottom

				# check if P1 is None
				if self.dict["UNI_FEM_VAL"][self.op_type][self.side][item]["TOP"]["P1"] == None:					
					self.dict["UNI_FEM_VAL"][self.op_type][self.side][item]["TOP"]["P1"] = P
					self.draw_tools.setHoverPointLabel("P1_"+item+"_TOP")
					self.draw_tools.setHoverPoint(P)
					self.draw_tools.setHoverBool(True)
					return True

				# check if P2 is None				
				if self.dict["UNI_FEM_VAL"][self.op_type][self.side][item]["TOP"]["P2"] == None:					
					self.dict["UNI_FEM_VAL"][self.op_type][self.side][item]["TOP"]["P2"] = P
					M = self.draw_tools.midpoint(self.dict["UNI_FEM_VAL"][self.op_type][self.side][item]["TOP"]["P1"], P)
					self.dict["UNI_FEM_VAL"][self.op_type][self.side][item]["TOP"]["M1"] = M
					self.draw_tools.setHoverBool(False)
					self.draw_tools.setHoverPointLabel(None)
					return True


				# check if P1 is None
				if self.dict["UNI_FEM_VAL"][self.op_type][self.side][item]["BOT"]["P1"] == None:					
					self.dict["UNI_FEM_VAL"][self.op_type][self.side][item]["BOT"]["P1"] = P
					self.draw_tools.setHoverPointLabel("P1_"+item+"_BOT")
					self.draw_tools.setHoverPoint(P)
					self.draw_tools.setHoverBool(True)
					return True

				# check if P2 is None				
				if self.dict["UNI_FEM_VAL"][self.op_type][self.side][item]["BOT"]["P2"] == None:					
					self.dict["UNI_FEM_VAL"][self.op_type][self.side][item]["BOT"]["P2"] = P
					M = self.draw_tools.midpoint(self.dict["UNI_FEM_VAL"][self.op_type][self.side][item]["BOT"]["P1"], P)
					self.dict["UNI_FEM_VAL"][self.op_type][self.side][item]["BOT"]["M1"] = M
					self.draw_tools.setHoverBool(False)
					self.draw_tools.setHoverPointLabel(None)
					return True	


			# line has P1 and P2
			if item_type == "line":

				# check if P1 is None				
				if self.dict["UNI_FEM_VAL"][self.op_type][self.side][item]["P1"] == None:					
					self.dict["UNI_FEM_VAL"][self.op_type][self.side][item]["P1"] = P
					self.draw_tools.setHoverPointLabel("P1_"+item)
					self.draw_tools.setHoverPoint(P)
					self.draw_tools.setHoverBool(True)
					return True


				# check if P2 is None				
				if self.dict["UNI_FEM_VAL"][self.op_type][self.side][item]["P2"] == None:					
					self.dict["UNI_FEM_VAL"][self.op_type][self.side][item]["P2"] = P
					self.draw_tools.setHoverBool(False)
					self.draw_tools.setHoverPointLabel(None)
					return True

		return False									
 


	def getNextLabel(self):

		if self.side != None:
			for item in self.dict["UNI_FEM_VAL"][self.op_type][self.side]:
				# get item type 
				item_type = self.dict["UNI_FEM_VAL"][self.op_type][self.side][item]["type"]
				
				
				# axis has two midpoints
				if item_type == "axis":
					print("axis" + item)
					# axis has a top and a bottom

					# check if P1 is None
					if self.dict["UNI_FEM_VAL"][self.op_type][self.side][item]["TOP"]["P1"] == None:						
						return (self.side + " " + item + " P1")

					# check if P2 is None				
					if self.dict["UNI_FEM_VAL"][self.op_type][self.side][item]["TOP"]["P2"] == None:						
						return (self.side + " " + item + " P2")

					# check if P1 is None
					if self.dict["UNI_FEM_VAL"][self.op_type][self.side][item]["BOT"]["P1"] == None:						
						return (self.side + " " + item + " P1")

					# check if P2 is None				
					if self.dict["UNI_FEM_VAL"][self.op_type][self.side][item]["BOT"]["P2"] == None:						
						return (self.side + " " + item + " P2")


				# line has P1 and P2
				if item_type == "line":

					# check if P1 is None				
					if self.dict["UNI_FEM_VAL"][self.op_type][self.side][item]["P1"] == None:						
						return (self.side + " " + item + " P1")

					# check if P2 is None				
					if self.dict["UNI_FEM_VAL"][self.op_type][self.side][item]["P2"] == None:						
						return (self.side + " " + item + " P2")

			return (self.side + " Done")

		return None


	def hover(self, P_mouse, P_stored, hover_label):

		if hover_label == "P1_AXIS_FEM_TOP":
			self.draw_tools.clear_by_tag("hover_line")
			m = self.draw_tools.midpoint(P_stored, P_mouse)
			self.draw_tools.create_midpoint_line(P_stored, P_mouse, m, "hover_line", point_thickness=self.point_size)

			# bot_axis_tib_m1 = self.dict[self.name][self.op_type][self.side]["AXIS_FEM"]["BOT"]["M1"]
			axis_fem_bot_m1 = self.dict["UNI_FEM_VAL"][self.op_type][self.side]["AXIS_FEM"]["BOT"]["M1"]

			if axis_fem_bot_m1 != None:
				# join center points of axes
				xtop, ytop, xbot, ybot = self.draw_tools.getImageCorners()
				U_m1, D_m1 = self.draw_tools.retPointsUpDown(m, axis_fem_bot_m1)
				p_top = self.draw_tools.line_intersection((D_m1, U_m1), (xbot, ybot))
				self.draw_tools.create_myline(U_m1, p_top, "hover_line")


		if hover_label == "P1_AXIS_FEM_BOT":
			self.draw_tools.clear_by_tag("hover_line")
			m = self.draw_tools.midpoint(P_stored, P_mouse)
			self.draw_tools.create_midpoint_line(P_stored, P_mouse, m, "hover_line", point_thickness=self.point_size)

			axis_fem_top_m1 = self.dict["UNI_FEM_VAL"][self.op_type][self.side]["AXIS_FEM"]["TOP"]["M1"]

			if axis_fem_top_m1 != None:				
				# join center points of axes
				xtop, ytop, xbot, ybot = self.draw_tools.getImageCorners()
				U_m1, D_m1 = self.draw_tools.retPointsUpDown(axis_fem_top_m1, m)
				p_top = self.draw_tools.line_intersection((D_m1, U_m1), (xbot, ybot))
				self.draw_tools.create_myline(U_m1, p_top, "hover_line")

		if hover_label == "P1_FEM_JOINT_LINE":
			self.draw_tools.clear_by_tag("hover_line")			
			self.draw_tools.create_myline(P_stored, P_mouse, "hover_line")

	def regainHover(self, side):
		pass

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
		axis_fem_top_p1 = self.dict["UNI_FEM_VAL"][self.op_type][side]["AXIS_FEM"]["TOP"]["P1"]
		axis_fem_top_p2 = self.dict["UNI_FEM_VAL"][self.op_type][side]["AXIS_FEM"]["TOP"]["P2"]		

		axis_fem_bot_p1 = self.dict["UNI_FEM_VAL"][self.op_type][side]["AXIS_FEM"]["BOT"]["P1"]
		axis_fem_bot_p2 = self.dict["UNI_FEM_VAL"][self.op_type][side]["AXIS_FEM"]["BOT"]["P2"]		


		fem_joint_p1 = self.dict["UNI_FEM_VAL"][self.op_type][side]["FEM_JOINT_LINE"]["P1"]
		fem_joint_p2 = self.dict["UNI_FEM_VAL"][self.op_type][side]["FEM_JOINT_LINE"]["P2"]


		# find item type
		if "AXIS_FEM" in tags:
			item = "AXIS_FEM"

			# axis has top and bot
			if "TOP" in tags:
				topbot = "TOP"
			elif "BOT" in tags:
				topbot = "BOT"

		elif "FEM_JOINT_LINE" in tags:
			item = "FEM_JOINT_LINE"


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

			elif item == "FEM_JOINT_LINE":
				# self.draw_tools.clear_by_tag("TSLOPE_angle")
				self.drag_point = fem_joint_p2
				self.drag_label = "P1_JOINT"
				self.drag_side 	= side


		elif "P2" in tags:
			if item == "AXIS_FEM":
				if topbot == "TOP":
					self.drag_point = axis_fem_top_p1
					self.drag_label = "P2_AXIS_FEM_TOP"
					self.drag_side 	= side

				elif topbot == "BOT":
					self.drag_point = axis_fem_bot_p1
					self.drag_label = "P2_AXIS_FEM_BOT"
					self.drag_side 	= side

			elif item == "FEM_JOINT_LINE":
				# self.draw_tools.clear_by_tag("TSLOPE_angle")
				self.drag_point = fem_joint_p1
				self.drag_label = "P2_JOINT"
				self.drag_side 	= side

			
	def drag(self, P_mouse):

		if self.drag_label == "P1_JOINT" or self.drag_label == "P2_JOINT":
			if self.drag_point != None:
				self.draw_tools.clear_by_tag("FEM_LINE")
				self.draw_tools.clear_by_tag("drag_line")
				self.draw_tools.create_myline(self.drag_point, P_mouse, "drag_line")


		if self.drag_label == "P1_AXIS_FEM_TOP" or self.drag_label == "P2_AXIS_FEM_TOP":
			if self.drag_point != None:
				self.draw_tools.clear_by_tag("TOP_AXIS_LINE")
				self.draw_tools.clear_by_tag("drag_line")
				m = self.draw_tools.midpoint(self.drag_point, P_mouse)
				self.draw_tools.create_midpoint_line(self.drag_point, P_mouse, m, "drag_line", point_thickness=self.point_size)

		if self.drag_label == "P1_AXIS_FEM_BOT" or self.drag_label == "P2_AXIS_FEM_BOT":
			if self.drag_point != None:
				self.draw_tools.clear_by_tag("BOT_AXIS_LINE")
				self.draw_tools.clear_by_tag("drag_line")
				m = self.draw_tools.midpoint(self.drag_point, P_mouse)
				self.draw_tools.create_midpoint_line(self.drag_point, P_mouse, m, "drag_line", point_thickness=self.point_size)
	def drag_stop(self, P_mouse):
		self.draw_tools.clear_by_tag("drag_line")

		# FEM JOINT LINE
		if self.drag_label == "P1_JOINT":
			self.dict["UNI_FEM_VAL"][self.op_type][self.drag_side]["FEM_JOINT_LINE"]["P1"] = P_mouse
			self.dict["EXCEL"][self.op_type][self.drag_side]["FVAR/VAL"] = None
			self.controller.save_json()
			self.draw()

		if self.drag_label == "P2_JOINT":
			self.dict["UNI_FEM_VAL"][self.op_type][self.drag_side]["FEM_JOINT_LINE"]["P2"] = P_mouse
			self.dict["EXCEL"][self.op_type][self.drag_side]["FVAR/VAL"] = None
			self.controller.save_json()
			self.draw()


		if self.drag_label == "P1_AXIS_FEM_TOP":
			self.dict["UNI_FEM_VAL"][self.op_type][self.drag_side]["AXIS_FEM"]["TOP"]["P1"] = P_mouse
			self.dict["UNI_FEM_VAL"][self.op_type][self.drag_side]["AXIS_FEM"]["TOP"]["M1"] = self.draw_tools.midpoint(self.drag_point, P_mouse)
			self.dict["EXCEL"][self.op_type][self.drag_side]["FVAR/VAL"] = None
			self.controller.save_json()
			self.draw()

		if self.drag_label == "P2_AXIS_FEM_TOP":
			self.dict["UNI_FEM_VAL"][self.op_type][self.drag_side]["AXIS_FEM"]["TOP"]["P2"] = P_mouse
			self.dict["UNI_FEM_VAL"][self.op_type][self.drag_side]["AXIS_FEM"]["TOP"]["M1"] = self.draw_tools.midpoint(self.drag_point, P_mouse)
			self.dict["EXCEL"][self.op_type][self.drag_side]["FVAR/VAL"] = None
			self.controller.save_json()
			self.draw()

		if self.drag_label == "P1_AXIS_FEM_BOT":
			self.dict["UNI_FEM_VAL"][self.op_type][self.drag_side]["AXIS_FEM"]["BOT"]["P1"] = P_mouse
			self.dict["UNI_FEM_VAL"][self.op_type][self.drag_side]["AXIS_FEM"]["BOT"]["M1"] = self.draw_tools.midpoint(self.drag_point, P_mouse)
			self.dict["EXCEL"][self.op_type][self.drag_side]["FVAR/VAL"] = None
			self.controller.save_json()
			self.draw()

		if self.drag_label == "P2_AXIS_FEM_BOT":
			self.dict["UNI_FEM_VAL"][self.op_type][self.drag_side]["AXIS_FEM"]["BOT"]["P2"] = P_mouse
			self.dict["UNI_FEM_VAL"][self.op_type][self.drag_side]["AXIS_FEM"]["BOT"]["M1"] = self.draw_tools.midpoint(self.drag_point, P_mouse)
			self.dict["EXCEL"][self.op_type][self.drag_side]["FVAR/VAL"] = None
			self.controller.save_json()
			self.draw()


	def update_canvas(self, draw_tools):
		self.draw_tools = draw_tools


	def update_dict(self, master_dict):
		self.dict = master_dict



	def unset(self):
		# print("unset from "+self.name)
		self.draw_tools.clear_by_tag(self.tag)