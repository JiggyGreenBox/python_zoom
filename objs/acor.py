import math

class ACOR():
	"""docstring for ClassName"""
	def __init__(self, draw_tools, master_dict, controller, op_type):
		self.name = "ACOR"
		self.tag = "acor"
		self.menu_label = "ACOR_Menu"
		self.draw_tools = draw_tools
		self.dict = master_dict
		self.controller = controller
		self.side = None
		self.op_type = op_type


		self.fem_ray_slope = {}
		self.horizontal_dx = {}
		self.horizontal_dy = {}
		self.anchor_point = {}

		# check if master dictionary has values
		# if not populate the dictionary
		self.checkMasterDict()

		self.point_size = None

		self.draw_labels = True
		self.draw_hover = True

		self.flip_left = False
		self.flip_right = False

	def click(self, event):
		# print("click from "+self.name)
		# self.draw()
		if self.side == None:
			print("please choose side")
			self.controller.warningBox("Please select a Side")
			self.controller.save_json()
			# print(self.dict)
		else:
			ret =  self.addDict(event)
			# find if P0 hovers are required
			self.mainHoverUsingNextLabel()
			if ret:
				self.controller.save_json()
				# pass

		self.controller.updateMenuLabel(self.getNextLabel(), self.menu_label)
		self.draw()


	def right_click(self, event):
		pass


	def keyRightObjFunc(self):
		print('set right')
		self.side = "RIGHT"
		self.controller.updateMenuLabel(self.getNextLabel(), self.menu_label)
		self.draw()
		self.regainHover(self.side)

	def keyLeftObjFunc(self):
		print('set left')
		self.side = "LEFT"
		self.controller.updateMenuLabel(self.getNextLabel(), self.menu_label)
		self.draw()
		self.regainHover(self.side)


	def checkMasterDict(self):
		if "ACOR" not in self.dict.keys():
			self.dict["ACOR"] = 	{
									"PRE-OP":
											{
											"LEFT":	{
														"GUIDE_FEM":	{"type":"guideline","P1":None,"P2":None},
														"P1":			{"type":"point","P1":None},
														"P2":			{"type":"point","P1":None},
														"P3":			{"type":"point","P1":None},
														"FLIP":			{"state": False}
													},
											"RIGHT":{
														"GUIDE_FEM":	{"type":"guideline","P1":None,"P2":None},
														"P1":			{"type":"point","P1":None},
														"P2":			{"type":"point","P1":None},
														"P3":			{"type":"point","P1":None},
														"FLIP":			{"state": False}
													}
											},
									"POST-OP":
											{
											"LEFT":	{
														"GUIDE_FEM":	{"type":"guideline","P1":None,"P2":None},
														"P1":			{"type":"point","P1":None},
														"P2":			{"type":"point","P1":None},
														"P3":			{"type":"point","P1":None},
														"FLIP":			{"state": False}
													},
											"RIGHT":{
														"GUIDE_FEM":	{"type":"guideline","P1":None,"P2":None},
														"P1":			{"type":"point","P1":None},
														"P2":			{"type":"point","P1":None},
														"P3":			{"type":"point","P1":None},
														"FLIP":			{"state": False}
													}
											}
									}

	def draw(self):

		self.draw_tools.clear_by_tag(self.tag)

		self.point_size = self.controller.getViewPointSize()

		# loop left and right
		for side in ["LEFT","RIGHT"]:
			
			isGuideLine = False

			isP1 = False
			isP2 = False
			isP3 = False

			acor_p1 = self.dict["ACOR"][self.op_type][side]["P1"]["P1"]
			acor_p2 = self.dict["ACOR"][self.op_type][side]["P2"]["P1"]
			acor_p3 = self.dict["ACOR"][self.op_type][side]["P3"]["P1"]

			guide_fem_p1 = self.dict["ACOR"][self.op_type][side]["GUIDE_FEM"]["P1"]
			guide_fem_p2 = self.dict["ACOR"][self.op_type][side]["GUIDE_FEM"]["P2"]

			for item in self.dict["ACOR"][self.op_type][side]:
				
				if item == "FLIP":
					continue

				item_type = self.dict["ACOR"][self.op_type][side][item]["type"]
				# print(item_type)


				if item_type == "point":

					# slope is common to P1, P2, P3
					slope = self.getFemRaySlope(side)					
					# print('slope: {}'.format(slope))

					if acor_p1 != None:
						# print("P1 Found")
						# self.draw_tools.create_mypoint(acor_p1, "orange", self.tag, point_thickness=self.point_size)
						self.draw_tools.create_mypoint(acor_p1, "orange", [self.tag, side, "P1"], point_thickness=self.point_size)

						# join the point to the top parallel to femGuideRay
						p_xtop = (-acor_p1[1] / slope) + acor_p1[0]
						self.draw_tools.create_myline(acor_p1, [p_xtop,0], [self.tag, side, "P1_line"])
						
						isP1 = True

					if acor_p2 != None:
						# print("P2 Found")
						# self.draw_tools.create_mypoint(acor_p2, "orange", self.tag, point_thickness=self.point_size)
						self.draw_tools.create_mypoint(acor_p2, "orange", [self.tag, side, "P2"], point_thickness=self.point_size)
						# join the point to the top parallel to femGuideRay
						p_xtop = (-acor_p2[1] / slope) + acor_p2[0]
						self.draw_tools.create_myline(acor_p2, [p_xtop,0], [self.tag, side, "P2_line"])
						isP2 = True

					if acor_p3 != None:
						# print("P3 Found")
						# self.draw_tools.create_mypoint(acor_p2, "orange", self.tag, point_thickness=self.point_size)
						self.draw_tools.create_mypoint(acor_p3, "orange", [self.tag, side, "P3"], point_thickness=self.point_size)

						# join the point to the top parallel to femGuideRay
						p_xtop = (-acor_p3[1] / slope) + acor_p3[0]
						self.draw_tools.create_myline(acor_p3, [p_xtop,0], [self.tag, side, "P3_line"])
						isP3 = True

					# recover state
					if self.getAnchorPoint(side) == None:
						for p in [acor_p1, acor_p2, acor_p3]:
							if p != None:
								# first point sets the anchor point
								self.routineFirstPoint(p, side)
								break
					else:
						if isP1 and isP2 and isP3:
							self.draw_tools.create_myline(acor_p1, acor_p2, [self.tag, side, "P12_baseline"])
							self.draw_tools.create_myline(acor_p2, acor_p3, [self.tag, side, "P23_baseline"])


							direction_ordered_points = self.retPointsLeftMiddleRight(acor_p1, acor_p2, acor_p3, side)
							print('{} arranged points {}'.format(side, direction_ordered_points))
							# print('acor_p1 {}',format(acor_p1))
							# print('acor_p2 {}',format(acor_p2))
							# print('acor_p3 {}',format(acor_p3))

							self.draw_tools.create_mytext(direction_ordered_points[0], y_offset=40, color="green", mytext="P1", mytag=[self.tag, side, "P_label"])
							self.draw_tools.create_mytext(direction_ordered_points[1], y_offset=40, color="blue", mytext="P2", mytag=[self.tag, side, "P_label"])
							self.draw_tools.create_mytext(direction_ordered_points[2], y_offset=40, color="blue", mytext="P3", mytag=[self.tag, side, "P_label"])

							if self.getAnchorPoint(side) != None:
								self.draw_tools.create_mytext(self.getAnchorPoint(side), y_offset=40, color="blue", mytext="X", mytag=[self.tag, side, "P_label"])


							# ACOR
							# ACOR = P1P2 / P1P3
							# P1-P2 dist
							# P1-P3 dist
							p1p2_dist = self.draw_tools.getDistance(direction_ordered_points[0],direction_ordered_points[1])
							print('p1p2 dist = {}'.format(p1p2_dist))

							p1p3_dist = self.draw_tools.getDistance(direction_ordered_points[0],direction_ordered_points[2])
							print('p1p2 dist = {}'.format(p1p3_dist))


							acor_val = p1p2_dist / p1p3_dist
							print('acor_val = {}'.format(acor_val))

							# PCOR
							# PCOR = X-P3 / P1P3
							xp3_dist = self.draw_tools.getDistance(self.getAnchorPoint(side),direction_ordered_points[2])
							print('xp3_dist = {}'.format(xp3_dist))

							pcor_val = xp3_dist / p1p3_dist
							print('pcor_val = {}'.format(pcor_val))

							m_text = 'ACOR: {0:.1f} PCOR {1:.1f}'.format(acor_val, pcor_val)
							self.draw_tools.create_mytext(direction_ordered_points[2], y_offset=50, color="blue", mytext=m_text, mytag=[self.tag, side, "P_label"])
							# self.draw_tools.create_mytext(self.getAnchorPoint(side), y_offset=-50, color="blue", mytext='ACOR {}'.format(acor_val), mytag=[self.tag, side, "P_label"])
							
							
							# check if value exists
							if self.dict["EXCEL"][self.op_type][side]["ACOR"] == None:
								self.dict["EXCEL"][self.op_type][side]["HASDATA"] 	= True
								self.dict["EXCEL"][self.op_type][side]["ACOR"]	= '{0:.1f}'.format(acor_val)								
								self.controller.save_json()

							if self.dict["EXCEL"][self.op_type][side]["PCOR"] == None:
								self.dict["EXCEL"][self.op_type][side]["HASDATA"] 	= True
								self.dict["EXCEL"][self.op_type][side]["PCOR"]	= '{0:.1f}'.format(pcor_val)								
								self.controller.save_json()




				if item_type == "guideline":

					if guide_fem_p1 != None:
						self.draw_tools.create_mypoint(guide_fem_p1, "orange", [self.tag, side, "GUIDE_FEM", "P1"], point_thickness=self.point_size)

					if guide_fem_p2 != None:
						self.draw_tools.create_mypoint(guide_fem_p2, "orange", [self.tag, side, "GUIDE_FEM", "P2"], point_thickness=self.point_size)

					if guide_fem_p1 != None and guide_fem_p2 != None:						
						# self.draw_tools.create_midpoint_line(axis_fem_top_p1, axis_fem_top_p2, axis_fem_top_m1, self.tag, point_thickness=self.point_size)
						# isFemTop = True

						p_top, p_bot = self.getFemGuideRayPoints(guide_fem_p1, guide_fem_p2)

						# recover state
						if self.getFemRaySlope(side) == None:
							
							slope = self.setFemRaySlope(guide_fem_p1, guide_fem_p2, side)
							self.setHorizontalDxDy(slope, side)
							print('NOT SET RESET slope: {}'.format(slope))

						
						self.draw_tools.create_myline(p_top, p_bot, [self.tag, side, "GUIDE_FEM", "LINE"])


	def addDict(self, event):
		for item in self.dict["ACOR"][self.op_type][self.side]:
			# get item type 
			item_type = self.dict["ACOR"][self.op_type][self.side][item]["type"]

			# guideline has P1 and P2
			if item_type == "guideline":

				# check if P1 is None				
				if self.dict["ACOR"][self.op_type][self.side][item]["P1"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.draw_tools.setHoverPoint(P)
					self.draw_tools.setHoverBool(True)
					self.draw_tools.setHoverPointLabel("GUIDE_P1")
					self.dict["ACOR"][self.op_type][self.side][item]["P1"] = P
					return True

				# check if P2 is None				
				if self.dict["ACOR"][self.op_type][self.side][item]["P2"] == None:
					P = self.draw_tools.getRealCoords(event)

					# set for hover actions
					slope = self.setFemRaySlope(self.dict["ACOR"][self.op_type][self.side][item]["P1"], P, self.side)
					self.setHorizontalDxDy(slope, self.side)

					self.draw_tools.setHoverPoint(P)
					self.draw_tools.setHoverBool(True)
					self.draw_tools.setHoverPointLabel("GUIDE_P2")
					self.dict["ACOR"][self.op_type][self.side][item]["P2"] = P
					return True


			# point only has P1
			if item_type == "point":
				# check if P1 is None				
				if self.dict["ACOR"][self.op_type][self.side][item]["P1"] == None:
					
					P = self.draw_tools.getRealCoords(event)

					# points could be deleted in any order
					# hence we must check if point is first or last
					# if first assign P1 for hover
					# if last remove hover
					# if not first and not last assign P2
					if self.isFirstPoint(self.side):

						self.draw_tools.setHoverBool(True)
						self.draw_tools.setHoverPointLabel("P1")

						self.routineFirstPoint(P, self.side)
						self.dict["ACOR"][self.op_type][self.side][item]["P1"] = P

					elif self.isLastPoint(self.side):

						self.draw_tools.setHoverBool(False)
						self.draw_tools.setHoverPointLabel(None)

						p_int = self.routineSecondThirdPoint(P)
						self.dict["ACOR"][self.op_type][self.side][item]["P1"] = p_int

					else:
						self.draw_tools.setHoverBool(True)
						self.draw_tools.setHoverPointLabel("P2")

						p_int = self.routineSecondThirdPoint(P)
						self.dict["ACOR"][self.op_type][self.side][item]["P1"] = p_int

					return True

		return False

	def update_dict(self, master_dict):
		self.dict = master_dict
		self.checkFlippedState()


	def checkFlippedState(self):
		print('checkFlippedState')


		try:
			if self.dict["ACOR"][self.op_type]["LEFT"]["FLIP"]["state"] == True:
				print('flip_left')
				self.flip_left = True
				self.controller.obj_to_menu(self.menu_label, "flip_left", True)
		except KeyError:

			flip_dict = {"state": False}
			self.dict["ACOR"][self.op_type]["LEFT"]["FLIP"] = flip_dict
			self.flip_left = True
			self.controller.obj_to_menu(self.menu_label, "flip_left", True)
			self.controller.save_json()



		try:
			if self.dict["ACOR"][self.op_type]["RIGHT"]["FLIP"]["state"] == True:
				print('flip_right')
				self.flip_right = True
				self.controller.obj_to_menu(self.menu_label, "flip_right", True)
		except KeyError:
			flip_dict = {"state": False}
			self.dict["ACOR"][self.op_type]["RIGHT"]["FLIP"] = flip_dict
			print('flip_right')
			self.flip_right = False
			self.controller.obj_to_menu(self.menu_label, "flip_right", False)
			self.controller.save_json()

			

		# if self.dict["ACOR"][self.op_type]["LEFT"]["FLIP"]["state"] == True:
		# 	print('flip_left')
		# 	self.flip_left = True
		# 	self.controller.obj_to_menu(self.menu_label, "flip_left", True)

		# if self.dict["ACOR"][self.op_type]["RIGHT"]["FLIP"]["state"] == True:
		# 	print('flip_right')
		# 	self.flip_right = True
		# 	self.controller.obj_to_menu(self.menu_label, "flip_right", True)



	def getNextLabel(self):

		if self.side != None:
			for item in self.dict["ACOR"][self.op_type][self.side]:

				if item == "FLIP":
					continue

				# get item type 
				item_type = self.dict["ACOR"][self.op_type][self.side][item]["type"]

				# point only has P1
				if item_type == "guideline":

					# check if P1 is None
					if self.dict["ACOR"][self.op_type][self.side][item]["P1"] == None:
						return (self.side + " " + item + " P1")

					# check if P2 is None				
					if self.dict["ACOR"][self.op_type][self.side][item]["P2"] == None:
						return (self.side + " " + item + " P2")

				# point only has P1
				if item_type == "point":
					# check if P1 is None				
					if self.dict["ACOR"][self.op_type][self.side][item]["P1"] == None:
						return (self.side + " " + item)

			return (self.side + " Done")
		return None


	def slope(self, point1, point2):
		x1 = point1[0]
		y1 = point1[1]
		x2 = point2[0]
		y2 = point2[1]
		return (y2-y1)/(x2-x1)


	def slope_intercept(self, point1, point2):

		x1 = point1[0]
		y1 = point1[1]
		x2 = point2[0]
		y2 = point2[1]

		a = (y2 - y1) / (x2 - x1)
		b = y1 - a * x1
		return a, b		


	# menu button clicks are routed here
	def menu_btn_click(self, action):
		print(action)		

		# print(self.dict["ACOR"][self.op_type])

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


		if action == "DEL-RIGHT-FEM-LINE":
			self.dict[self.name][self.op_type]["RIGHT"]["GUIDE_FEM"]["P1"] = None
			self.dict[self.name][self.op_type]["RIGHT"]["GUIDE_FEM"]["P2"] = None

			self.dict[self.name][self.op_type]["RIGHT"]["P1"]["P1"] = None
			self.dict[self.name][self.op_type]["RIGHT"]["P2"]["P1"] = None
			self.dict[self.name][self.op_type]["RIGHT"]["P3"]["P1"] = None

			self.side = "RIGHT"

		if action == "DEL-LEFT-FEM-LINE":
			self.dict[self.name][self.op_type]["LEFT"]["GUIDE_FEM"]["P1"] = None
			self.dict[self.name][self.op_type]["LEFT"]["GUIDE_FEM"]["P2"] = None

			self.dict[self.name][self.op_type]["LEFT"]["P1"]["P1"] = None
			self.dict[self.name][self.op_type]["LEFT"]["P2"]["P1"] = None
			self.dict[self.name][self.op_type]["LEFT"]["P3"]["P1"] = None
			
			self.side = "LEFT"


		if action == "DEL-LEFT-P1":
			self.dict[self.name][self.op_type]["LEFT"]["P1"]["P1"] = None
			self.side = "LEFT"

		if action == "DEL-RIGHT-P1":
			self.dict[self.name][self.op_type]["RIGHT"]["P1"]["P1"] = None
			self.side = "RIGHT"

		if action == "DEL-LEFT-P2":
			self.dict[self.name][self.op_type]["LEFT"]["P2"]["P1"] = None
			self.side = "LEFT"
			

		if action == "DEL-RIGHT-P2":
			self.dict[self.name][self.op_type]["RIGHT"]["P2"]["P1"] = None
			self.side = "RIGHT"		

		if action == "DEL-LEFT-P3":
			self.dict[self.name][self.op_type]["LEFT"]["P3"]["P1"] = None
			self.side = "LEFT"
			

		if action == "DEL-RIGHT-P3":
			self.dict[self.name][self.op_type]["RIGHT"]["P3"]["P1"] = None
			self.side = "RIGHT"

		
		# delete from excel pat.json
		self.dict["EXCEL"][self.op_type][self.side]["ACOR"] = None
		self.dict["EXCEL"][self.op_type][self.side]["PCOR"] = None
		self.dict["EXCEL"][self.op_type][self.side]["HASDATA"] 	= False

		# print(self.name)
		# print(self.op_type)
		# self.side = None # to reduce hover complexity		
		self.draw()
		self.regainHover(self.side)

		self.controller.save_json()
		self.controller.updateMenuLabel(self.getNextLabel(), self.menu_label)


	def hover(self, P_mouse, P_stored, hover_label):
		# prevent auto curObject set bug
		if self.side == None:
			return


		if self.draw_hover:
			side_pre = self.side[0]+"_"
			if hover_label == "P0_GUIDE_FEM":				
				self.draw_tools.clear_by_tag("hover_line")
				self.draw_tools.create_mypoint(P_mouse, "red", [self.tag, "hover_line"], hover_point=True, point_thickness=self.point_size)
				if self.draw_labels:
					self.draw_tools.create_mytext(P_mouse,x_offset=80, mytext=(side_pre+self.hover_text), mytag=[self.tag, "hover_line"])
		
	
		if hover_label == "GUIDE_P1":

			p_top, p_bot = self.getFemGuideRayPoints(P_stored, P_mouse)

			self.draw_tools.clear_by_tag("hover_line")
			self.draw_tools.create_myline(p_top, p_bot, "hover_line")

		elif hover_label == "GUIDE_P2":
			slope = self.getFemRaySlope(self.side)
			p_xtop_p1 = (-P_mouse[1] / slope) + P_mouse[0]
									
			# self.draw_tools.create_mypoint([x_val, 0], "orange", self.tag, point_thickness=self.point_size)
			self.draw_tools.clear_by_tag("hover_line")
			self.draw_tools.create_myline(P_mouse, [p_xtop_p1,0], "hover_line")

			# points perpendicular to femGuideRay
			# horizontal point
			H_point = [0,0]
			dx, dy = self.getHorizontalDxDy(self.side)
			H_point[0] = P_mouse[0] + dx
			H_point[1] = P_mouse[1] + dy
			# self.draw_tools.create_mypoint(H_point, "orange", ["hover_line"], point_thickness=self.point_size)

			# find angle ray intersection point
			p_int = self.draw_tools.line_intersection(
					(P_mouse, H_point),
					(self.dict[self.name][self.op_type][self.side]["GUIDE_FEM"]["P1"], self.dict[self.name][self.op_type][self.side]["GUIDE_FEM"]["P2"]))
			self.draw_tools.create_myline(P_mouse, p_int, "hover_line")

			self.draw_tools.create_mypoint(p_int, "orange", ["hover_line"], point_thickness=self.point_size, hover_point=True)

		elif hover_label == "P1" or hover_label == "P2":
			slope = self.getFemRaySlope(self.side)
			p_xtop_p1 = (-P_mouse[1] / slope) + P_mouse[0]
									
			# acor_p1 = self.dict["ACOR"][self.op_type][self.side]["P1"]["P1"]
			acor_p1 = self.dict["ACOR"][self.op_type][self.side]["P1"]["P1"]
			acor_p2 = self.dict["ACOR"][self.op_type][self.side]["P2"]["P1"]
			acor_p3 = self.dict["ACOR"][self.op_type][self.side]["P3"]["P1"]
			anchor_p = self.getAnchorPoint(self.side)

			# # find angle ray intersection point
			# p_int = self.draw_tools.line_intersection(
			# 		(P_mouse, [p_xtop_p1,0]),
			# 		(acor_p1, anchor_p))
			p_int = ""
			for not_null_p in [acor_p1, acor_p2, acor_p3]:
				if not_null_p != None:
					# find angle ray intersection point
					p_int = self.draw_tools.line_intersection(
							(P_mouse, [p_xtop_p1,0]),
							(not_null_p, anchor_p))



			# self.draw_tools.create_mypoint([x_val, 0], "orange", self.tag, point_thickness=self.point_size)
			if p_int != "":
				self.draw_tools.clear_by_tag("hover_line")
				self.draw_tools.create_myline(P_mouse, [p_xtop_p1,0], "hover_line")
				self.draw_tools.create_mypoint(p_int, "orange", ["hover_line"], point_thickness=self.point_size, hover_point=True)

		

	def regainHover(self, side):

		# get the count of points (P1, P2, P3)
		count = self.getPointCount(side)

		if count == 0:
			# fem ray may not exist
			if self.dict[self.name][self.op_type][side]["GUIDE_FEM"]["P1"] == None and self.dict[self.name][self.op_type][side]["GUIDE_FEM"]["P2"] == None :
				# fem ray doesnt exist
				# no lines exists
				# remove hover
				self.draw_tools.setHoverPointLabel(None)
				self.draw_tools.setHoverBool(False)
			else:
				# first point but the fem ray exists
				self.draw_tools.setHoverPointLabel("GUIDE_P2")
				self.draw_tools.setHoverBool(True)

		elif count == 1:
			self.draw_tools.setHoverPointLabel("P1")
			self.draw_tools.setHoverBool(True)

		elif count == 2:
			self.draw_tools.setHoverPointLabel("P2")
			self.draw_tools.setHoverBool(True)
		

		# find if P0 hovers are required
		self.mainHoverUsingNextLabel()


	# when drag event occurs, we need a ref to the other point(s) 
	# using tag_list we can find the current point in focus
	def set_drag_vars(self, tag_list):
		print(tag_list)



	# P1, P2, P3
	# when the first point is set need to assign anchor point
	def isFirstPoint(self, side):
		if (self.dict["ACOR"][self.op_type][side]["P1"]["P1"] == None 
			and self.dict["ACOR"][self.op_type][side]["P2"]["P1"] == None 
			and self.dict["ACOR"][self.op_type][side]["P3"]["P1"] == None):
			return True
		return False

	# P1, P2, P3	
	def isLastPoint(self, side):
		count = 0
		if self.dict["ACOR"][self.op_type][side]["P1"]["P1"] != None :
			count = count + 1
		if  self.dict["ACOR"][self.op_type][side]["P2"]["P1"] != None:
			count = count + 1
		if  self.dict["ACOR"][self.op_type][side]["P3"]["P1"] != None:
			count = count + 1
		if count == 2:
			return True
		return False

	def getPointCount(self, side):
		count = 0
		if self.dict["ACOR"][self.op_type][side]["P1"]["P1"] != None :
			count = count + 1
		if  self.dict["ACOR"][self.op_type][side]["P2"]["P1"] != None:
			count = count + 1
		if  self.dict["ACOR"][self.op_type][side]["P3"]["P1"] != None:
			count = count + 1
		return count


	def retPointsLeftMiddleRight(self, p1, p2, p3, side):
		ret_list = [None, None, None]
		# ret_list = [p1, None, p3]

		p_list = [p1, p2, p3]
		
		px_min = 0
		px_max = 0


		for p in p_list:
			# MIN
			# first pass
			if px_min == 0:
				px_min = p[0]
				ret_list[0] = p
			elif p[0] < px_min:
				px_min = p[0]
				ret_list[0] = p

			# MAX
			if p[0] > px_max:
				px_max = p[0]
				ret_list[2] = p


		# check if middle element is missing
		temp = [item for item in p_list if item not in ret_list]

		if len(temp) == 1:
			ret_list[1] = temp[0]

		# if RIGHT and flip true, flip
		# if LEFT and flip false, flip

		if side == "LEFT" and not self.flip_left:
			ret_list = ret_list[::-1]
		elif side == "RIGHT" and self.flip_right:
			ret_list = ret_list[::-1]

		return ret_list





	def mainHoverUsingNextLabel(self):
		label = self.getNextLabel()

		if label == "RIGHT GUIDE_FEM P1":
			self.side = "RIGHT"
			self.hover_text = "GUIDE_FEM P1"
			self.draw_tools.setHoverPointLabel("P0_GUIDE_FEM")
			self.draw_tools.setHoverPoint(None)
			self.draw_tools.setHoverBool(True)
		elif label == "LEFT GUIDE_FEM P1":
			self.side = "LEFT"
			self.hover_text = "GUIDE_FEM P1"
			self.draw_tools.setHoverPointLabel("P0_GUIDE_FEM")
			self.draw_tools.setHoverPoint(None)
			self.draw_tools.setHoverBool(True)




	# first point sets the anchor point
	def routineFirstPoint(self, P, side):
		dx, dy = self.getHorizontalDxDy(side)

		# anchor_point is the point where the horizontal line and the rem-guide-ray meet
		# anchor point is the intersection point of the femGuideRay and the line holding P1, P2, P3
		# anchor_helper is a helper to get 90deg
		anchor_helper = [0,0]
		anchor_helper[0] = P[0] + dx
		anchor_helper[1] = P[1] + dy

		anchor_point = self.draw_tools.line_intersection(
												(P, anchor_helper),
												(self.dict[self.name][self.op_type][side]["GUIDE_FEM"]["P1"], 
												self.dict[self.name][self.op_type][side]["GUIDE_FEM"]["P2"]))
		self.setAnchorPoint(anchor_point, side)

	# second and third point use anchor point
	def routineSecondThirdPoint(self, P):
		# if P2 or P3					
		slope = self.getFemRaySlope(self.side)

		p_xtop_p1 = (-P[1] / slope) + P[0]
		anchor_p = self.getAnchorPoint(self.side)

		acor_p1 = self.dict["ACOR"][self.op_type][self.side]["P1"]["P1"]
		acor_p2 = self.dict["ACOR"][self.op_type][self.side]["P2"]["P1"]
		acor_p3 = self.dict["ACOR"][self.op_type][self.side]["P3"]["P1"]

		for not_null_p in [acor_p1, acor_p2, acor_p3]:
			if not_null_p != None:								
				# find angle ray intersection point
				p_int = self.draw_tools.line_intersection(
						(P, [p_xtop_p1,0]),
						(not_null_p, anchor_p))
				return p_int
				break



	# for drag, hover and draw
	# fem guide P1 and P2 are supplied by the user
	# we need a ray to assure the line aligns with the back of the femur
	def getFemGuideRayPoints(self, P1, P2):
		xtop, ytop, xbot, ybot = self.draw_tools.getImageCorners()

		# find angle ray intersection point
		p_top = self.draw_tools.line_intersection(
				(P1, P2),
				(xtop, ytop))

		p_bot = self.draw_tools.line_intersection(
				(P1, P2),
				(xbot, ybot))

		return p_top, p_bot





	# for hover all calculations are with respect to 
	# FemGuideRay slope
	# so we store it once it is calculated to speed up things
	def setFemRaySlope(self, P1, P2, side):
		slope, intercept = self.slope_intercept(P1, P2)
		self.fem_ray_slope[side] = slope
		return slope

	def getFemRaySlope(self, side):
		try:
			return self.fem_ray_slope[side]
		except Exception as e:
			return None

	# set 90 deg slope dx dy
	# prevent unneccessary repaeting calculations
	def setHorizontalDxDy(self, slope, side):
		self.horizontal_dy[side] = math.sqrt(100**2/(slope**2+1))
		self.horizontal_dx[side] = -slope*self.horizontal_dy[side]

	def getHorizontalDxDy(self, side):
		try:
			return self.horizontal_dx[side], self.horizontal_dy[side]
		except Exception as e:
			return None, None
		
	# anchor point is the intersection point of the femGuideRay and the line holding P1, P2, P3
	def setAnchorPoint(self, anchor_point, side):
		self.anchor_point[side] = anchor_point

	def getAnchorPoint(self, side):
		try:
			return self.anchor_point[side]
		except Exception as e:
			return None
		
		

	def update_canvas(self, draw_tools):
		self.draw_tools = draw_tools

	def unset(self):
		print("unset from "+self.name)
		self.draw_tools.setHoverPointLabel(None)
		self.draw_tools.setHoverBool(False)
		self.draw_tools.clear_by_tag(self.tag)


	def escapeObjFunc(self):
		self.side = None
		self.draw_tools.setHoverPointLabel(None)
		self.draw_tools.setHoverBool(False)
		self.controller.updateMenuLabel("CHOOSE SIDE", self.menu_label)


	def drag_start(self, tags):
		pass		
	def drag(self, P_mouse):
		pass
	def drag_stop(self, P_mouse):
		self.draw()


	def checkbox_click(self,action, val):

		print('checkbox {} val{}'.format(action,val.get()))

		if action == "FLIP_RIGHT":
			if val.get() == 0:
				self.flip_right = False
				self.dict["ACOR"][self.op_type]["RIGHT"]["FLIP"]["state"] = False
				self.dict["EXCEL"][self.op_type]["RIGHT"]["ACOR"] = None
				self.dict["EXCEL"][self.op_type]["RIGHT"]["PCOR"] = None
				self.controller.save_json()
			elif val.get() == 1:
				self.flip_right = True
				print(self.dict["ACOR"][self.op_type]["RIGHT"]["FLIP"])
				self.dict["ACOR"][self.op_type]["RIGHT"]["FLIP"]["state"] = True
				self.dict["EXCEL"][self.op_type]["RIGHT"]["ACOR"] = None
				self.dict["EXCEL"][self.op_type]["RIGHT"]["PCOR"] = None
				self.controller.save_json()
			self.draw()

		if action == "FLIP_LEFT":
			if val.get() == 0:
				self.flip_left = False
				self.dict["ACOR"][self.op_type]["LEFT"]["FLIP"]["state"] = False
				self.dict["EXCEL"][self.op_type]["LEFT"]["ACOR"] = None
				self.dict["EXCEL"][self.op_type]["LEFT"]["PCOR"] = None
				self.controller.save_json()
			elif val.get() == 1:
				self.flip_left = True
				print(self.dict["ACOR"][self.op_type]["LEFT"]["FLIP"])
				self.dict["ACOR"][self.op_type]["LEFT"]["FLIP"]["state"] = True
				self.dict["EXCEL"][self.op_type]["LEFT"]["ACOR"] = None
				self.dict["EXCEL"][self.op_type]["LEFT"]["PCOR"] = None
				self.controller.save_json()
			self.draw()

