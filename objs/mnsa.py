import json

class MNSA():
	"""docstring for ClassName"""
	def __init__(self, draw_tools, master_dict, controller, op_type):
		self.name = "MNSA"
		self.tag = "mnsa"
		self.menu_label = "MNSA_Menu"
		self.draw_tools = draw_tools
		self.dict = master_dict
		self.controller = controller
		self.side = None
		self.op_type = op_type

		# check if master dictionary has values
		# if not populate the dictionary
		self.checkMasterDict()



	def checkMasterDict(self):
		if "MNSA" not in self.dict.keys():
			self.dict["MNSA"] = 	{
										"PRE-OP":{
												"LEFT":	{
															"NECK_AXIS":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
														},
												"RIGHT":	{
															"NECK_AXIS":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
														}
										},
										"POST-OP":{
												"LEFT":	{
															"NECK_AXIS":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
														},
												"RIGHT":	{
															"NECK_AXIS":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
														}
										}
									}

	def click(self, event):
		print("click from "+self.name)

		

		if self.side == None:
			print("please choose side")
			self.controller.warningBox("Please select a Side")
		else:
			print(self.dict)
			ret =  self.addDict(event)
			if ret:										
				self.controller.save_json()
				# pass

		self.controller.updateMenuLabel(self.getNextLabel(), self.menu_label)		
		self.draw()





	def addDict(self, event):
		for item in self.dict["MNSA"][self.op_type][self.side]:
			
			# get real coords
			P = self.draw_tools.getRealCoords(event)

			# get item type 
			item_type = self.dict["MNSA"][self.op_type][self.side][item]["type"]

			# point has P1 and P2, M1 is calculated
			if item_type == "midpoint":

				# check if P1 is None				
				if self.dict["MNSA"][self.op_type][self.side][item]["P1"] == None:
					
					self.dict["MNSA"][self.op_type][self.side][item]["P1"] = P

					self.draw_tools.setHoverPointLabel("P1_MNSA")
					self.draw_tools.setHoverPoint(P)
					self.draw_tools.setHoverBool(True)

					return True


				# check if P2 is None				
				if self.dict["MNSA"][self.op_type][self.side][item]["P2"] == None:					
					self.dict["MNSA"][self.op_type][self.side][item]["P2"] = P
					M = self.draw_tools.midpoint(self.dict["MNSA"][self.op_type][self.side][item]["P1"], P)
					self.dict["MNSA"][self.op_type][self.side][item]["M1"] = M
					self.draw_tools.setHoverBool(False)
					self.draw_tools.setHoverPointLabel(None)
					return True
		return False



	def draw(self):

		self.draw_tools.clear_by_tag(self.tag)

		# check if dictionary exists
		if "MAIN" not in self.dict.keys():
			return

		# loop left and right
		for side in ["LEFT","RIGHT"]:
			
			isNeck 		= False
			isFemTop 	= False
			isFemBot 	= False

			# ------------------------
			# FROM MNSA
			# ------------------------
			if self.dict["MNSA"][self.op_type][side]["NECK_AXIS"]["P1"] != None:
				self.draw_tools.create_mypoint(self.dict["MNSA"][self.op_type][side]["NECK_AXIS"]["P1"], "white", [self.tag, side, "P1_NECK_AXIS"])

			if self.dict["MNSA"][self.op_type][side]["NECK_AXIS"]["P2"] != None:
				self.draw_tools.create_mypoint(self.dict["MNSA"][self.op_type][side]["NECK_AXIS"]["P2"], "white", [self.tag, side, "P2_NECK_AXIS"])

			if self.dict["MNSA"][self.op_type][side]["NECK_AXIS"]["P1"] != None and self.dict["MNSA"][self.op_type][side]["NECK_AXIS"]["P2"] != None:
				p1 = self.dict["MNSA"][self.op_type][side]["NECK_AXIS"]["P1"]
				p2 = self.dict["MNSA"][self.op_type][side]["NECK_AXIS"]["P2"]
				m1 = self.dict["MNSA"][self.op_type][side]["NECK_AXIS"]["M1"]
				self.draw_tools.create_midpoint_line(p1, p2, m1, [self.tag,side,"NECK_AXIS_LINE"])
				isNeck = True



			# ------------------------
			# FROM MAIN
			# ------------------------
			# HIP
			if self.dict["MAIN"][self.op_type][side]["HIP"]["P1"] != None:				
				self.draw_tools.create_mypoint(self.dict["MAIN"][self.op_type][side]["HIP"]["P1"], "white", [self.tag, side, "NO-DRAG"])


			# FEM AXIS
			# TOP
			if self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["TOP"]["P1"] != None:
				self.draw_tools.create_mypoint(self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["TOP"]["P1"], "white", [self.tag, side, "NO-DRAG"])

			if self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["TOP"]["P2"] != None:
				self.draw_tools.create_mypoint(self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["TOP"]["P2"], "white", [self.tag, side, "NO-DRAG"])

			if self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["TOP"]["P1"] != None and self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["TOP"]["P2"] != None:
				p1 = self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["TOP"]["P1"]
				p2 = self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["TOP"]["P2"]
				m1 = self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["TOP"]["M1"]
				self.draw_tools.create_midpoint_line(p1, p2, m1, self.tag)
				isFemTop = True


			# BOT
			if self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["BOT"]["P1"] != None:
				self.draw_tools.create_mypoint(self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["BOT"]["P1"], "white", [self.tag, side, "NO-DRAG"])

			if self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["BOT"]["P2"] != None:
				self.draw_tools.create_mypoint(self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["BOT"]["P2"], "white", [self.tag, side, "NO-DRAG"])

			if self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["BOT"]["P1"] != None and self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["BOT"]["P2"] != None:
				p1 = self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["BOT"]["P1"]
				p2 = self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["BOT"]["P2"]
				m1 = self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["BOT"]["M1"]
				self.draw_tools.create_midpoint_line(p1, p2, m1, self.tag)
				isFemBot = True

			'''
			if isNeck and isFemBot and isFemTop:
				
				xtop, ytop, xbot, ybot = self.draw_tools.getImageCorners()

				fem_bot_m1 	= self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["BOT"]["M1"]
				fem_top_m1 	= self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["TOP"]["M1"]

				neck_m1 	= self.dict["MNSA"][self.op_type][side]["NECK_AXIS"]["M1"]
				hip 		= self.dict["MAIN"][self.op_type][side]["HIP"]["P1"]

				# FEM-AXIS ray
				p_top = self.draw_tools.line_intersection(
					(fem_bot_m1, fem_top_m1),
					(xtop, ytop))
				self.draw_tools.create_myline(fem_bot_m1, p_top, self.tag)


				# NECK-SHAFT ray
				if side == "RIGHT":
					p_right = self.draw_tools.line_intersection(
						(neck_m1, hip),
						(xtop, xbot))
					self.draw_tools.create_myline(hip, p_right, self.tag)

					# find angle ray intersection point
					p_int = self.draw_tools.line_intersection(
							(hip, p_right),
							(fem_bot_m1, p_top))

					angle = self.draw_tools.create_myAngle(hip, p_int, fem_bot_m1, self.tag)
					self.draw_tools.create_mytext(p_int, '{0:.2f}'.format(angle), self.tag, x_offset=60)




				if side == "LEFT":
					p_left = self.draw_tools.line_intersection(
						(neck_m1, hip),
						(ytop, ybot))
					self.draw_tools.create_myline(hip, p_left, self.tag)

					# find angle ray intersection point
					p_int = self.draw_tools.line_intersection(
							(hip, p_left),
							(fem_bot_m1, p_top))

					angle = self.draw_tools.create_myAngle(fem_bot_m1, p_int, hip, self.tag)
					self.draw_tools.create_mytext(p_int, '{0:.2f}'.format(angle), self.tag, x_offset=60)



				# check if value exists
				if self.dict["EXCEL"][self.op_type][side]["MNSA"] == None:

					self.dict["EXCEL"][self.op_type][side]["HASDATA"] 	= True
					self.dict["EXCEL"][self.op_type][side]["MNSA"]	 	= '{0:.2f}'.format(angle)

					# save after insert
					self.controller.save_json()

			'''
			if isFemBot and isFemTop:
				
				xtop, ytop, xbot, ybot = self.draw_tools.getImageCorners()

				fem_bot_m1 	= self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["BOT"]["M1"]
				fem_top_m1 	= self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["TOP"]["M1"]

				neck_m1 	= self.dict["MNSA"][self.op_type][side]["NECK_AXIS"]["M1"]
				hip 		= self.dict["MAIN"][self.op_type][side]["HIP"]["P1"]

				# FEM-AXIS ray
				p_top = self.draw_tools.line_intersection(
					(fem_bot_m1, fem_top_m1),
					(xtop, ytop))
				self.draw_tools.create_myline(fem_bot_m1, p_top, self.tag)

				if isNeck:
					# NECK-SHAFT ray
					if side == "RIGHT":
						p_right = self.draw_tools.line_intersection(
							(neck_m1, hip),
							(xtop, xbot))
						self.draw_tools.create_myline(hip, p_right, [self.tag,side,"MNSA_ANGLE"])

						# find angle ray intersection point
						p_int = self.draw_tools.line_intersection(
								(hip, p_right),
								(fem_bot_m1, p_top))

						angle = self.draw_tools.create_myAngle(hip, p_int, fem_bot_m1, [self.tag,side,"MNSA_ANGLE"])
						self.draw_tools.create_mytext(p_int, '{0:.2f}'.format(angle), [self.tag,side,"MNSA_ANGLE"], x_offset=60)




					if side == "LEFT":
						p_left = self.draw_tools.line_intersection(
							(neck_m1, hip),
							(ytop, ybot))
						self.draw_tools.create_myline(hip, p_left, [self.tag,side,"MNSA_ANGLE"])

						# find angle ray intersection point
						p_int = self.draw_tools.line_intersection(
								(hip, p_left),
								(fem_bot_m1, p_top))

						angle = self.draw_tools.create_myAngle(fem_bot_m1, p_int, hip, [self.tag,side,"MNSA_ANGLE"])
						self.draw_tools.create_mytext(p_int, '{0:.2f}'.format(angle), [self.tag,side,"MNSA_ANGLE"], x_offset=60)



					# check if value exists
					if self.dict["EXCEL"][self.op_type][side]["MNSA"] == None:

						self.dict["EXCEL"][self.op_type][side]["HASDATA"] 	= True
						self.dict["EXCEL"][self.op_type][side]["MNSA"]	 	= '{0:.2f}'.format(angle)

						# save after insert
						self.controller.save_json()


	def hover(self, P_mouse, P_stored, hover_label):
		if hover_label == "P1_MNSA":
			self.draw_tools.clear_by_tag("hover_line")
			m = self.draw_tools.midpoint(P_stored, P_mouse)
			self.draw_tools.create_midpoint_line(P_stored, P_mouse, m, "hover_line")

			if self.side != None and self.dict["MAIN"][self.op_type][self.side]["HIP"]["P1"] != None:

				hip = self.dict["MAIN"][self.op_type][self.side]["HIP"]["P1"]
				fem_bot_m1 	= self.dict["MAIN"][self.op_type][self.side]["AXIS_FEM"]["BOT"]["M1"]
				fem_top_m1 	= self.dict["MAIN"][self.op_type][self.side]["AXIS_FEM"]["TOP"]["M1"]

				xtop, ytop, xbot, ybot = self.draw_tools.getImageCorners()

				# neck_m1
				# fem_bot_m1
				# p_top

				if self.side == "RIGHT":
					p_right = self.draw_tools.line_intersection(
						(m, hip),
						(xtop, xbot))
					self.draw_tools.create_myline(hip, p_right, "hover_line")

					# find angle ray intersection point
					p_int = self.draw_tools.line_intersection(
							(hip, m),
							(fem_bot_m1, fem_top_m1))

					angle = self.draw_tools.create_myAngle(hip, p_int, fem_bot_m1, "hover_line")
					self.draw_tools.create_mytext(p_int, '{0:.2f}'.format(angle), "hover_line", x_offset=60)




				if self.side == "LEFT":
					p_left = self.draw_tools.line_intersection(
						(m, hip),
						(ytop, ybot))
					self.draw_tools.create_myline(hip, p_left, "hover_line")

					# find angle ray intersection point
					p_int = self.draw_tools.line_intersection(
							(hip, p_left),
							(fem_bot_m1, fem_top_m1))

					angle = self.draw_tools.create_myAngle(fem_bot_m1, p_int, hip, "hover_line")
					self.draw_tools.create_mytext(p_int, '{0:.2f}'.format(angle), "hover_line", x_offset=60)

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


		if "P1_NECK_AXIS" in tags:
			self.drag_point = self.dict["MNSA"][self.op_type][side]["NECK_AXIS"]["P2"]
			self.drag_label = "P1_NECK_AXIS"
			self.drag_side 	= side
		elif "P2_NECK_AXIS" in tags:
			self.drag_point = self.dict["MNSA"][self.op_type][side]["NECK_AXIS"]["P1"]
			self.drag_label = "P2_NECK_AXIS"
			self.drag_side 	= side

		else:
			self.drag_point = None
			self.drag_label = None
			self.drag_side 	= None
		

			
	def drag(self, P_mouse):
		# NECK_AXIS_LINE
		if self.drag_label == "P1_NECK_AXIS" and self.drag_point != None or self.drag_label == "P2_NECK_AXIS" and self.drag_point != None:
			self.draw_tools.clear_by_tag("NECK_AXIS_LINE")
			self.draw_tools.clear_by_tag("MNSA_ANGLE")
			self.draw_tools.clear_by_tag("drag_line")
			m = self.draw_tools.midpoint(self.drag_point, P_mouse)
			self.draw_tools.create_midpoint_line(self.drag_point, P_mouse, m, "drag_line")


			if self.drag_side != None and self.dict["MAIN"][self.op_type][self.drag_side]["HIP"]["P1"] != None:

				hip = self.dict["MAIN"][self.op_type][self.drag_side]["HIP"]["P1"]
				fem_bot_m1 	= self.dict["MAIN"][self.op_type][self.drag_side]["AXIS_FEM"]["BOT"]["M1"]
				fem_top_m1 	= self.dict["MAIN"][self.op_type][self.drag_side]["AXIS_FEM"]["TOP"]["M1"]

				xtop, ytop, xbot, ybot = self.draw_tools.getImageCorners()

				# neck_m1
				# fem_bot_m1
				# p_top

				if self.drag_side == "RIGHT":
					p_right = self.draw_tools.line_intersection(
						(m, hip),
						(xtop, xbot))
					self.draw_tools.create_myline(hip, p_right, "drag_line")
					# find angle ray intersection point
					p_int = self.draw_tools.line_intersection(
							(hip, m),
							(fem_bot_m1, fem_top_m1))
					angle = self.draw_tools.create_myAngle(hip, p_int, fem_bot_m1, "drag_line")
					self.draw_tools.create_mytext(p_int, '{0:.2f}'.format(angle), "drag_line", x_offset=60)


				if self.drag_side == "LEFT":
					p_left = self.draw_tools.line_intersection(
						(m, hip),
						(ytop, ybot))
					self.draw_tools.create_myline(hip, p_left, "drag_line")
					# find angle ray intersection point
					p_int = self.draw_tools.line_intersection(
							(hip, p_left),
							(fem_bot_m1, fem_top_m1))
					angle = self.draw_tools.create_myAngle(fem_bot_m1, p_int, hip, "drag_line")
					self.draw_tools.create_mytext(p_int, '{0:.2f}'.format(angle), "drag_line", x_offset=60)


	def drag_stop(self, P_mouse):
		self.draw_tools.clear_by_tag("drag_line")

		if self.drag_label == "P1_NECK_AXIS":
			self.dict["MNSA"][self.op_type][self.drag_side]["NECK_AXIS"]["P1"] = P_mouse
			self.dict["MNSA"][self.op_type][self.drag_side]["NECK_AXIS"]["M1"] = self.draw_tools.midpoint(self.drag_point, P_mouse)
		elif self.drag_label == "P2_NECK_AXIS":
			self.dict["MNSA"][self.op_type][self.drag_side]["NECK_AXIS"]["P2"] = P_mouse
			self.dict["MNSA"][self.op_type][self.drag_side]["NECK_AXIS"]["M1"] = self.draw_tools.midpoint(self.drag_point, P_mouse)

		self.controller.save_json()
		self.draw()
	

	# menu button clicks are routed here
	def menu_btn_click(self, action):
		print(action)
		if action == "SET-LEFT":
			self.side = "LEFT"

		if action == "SET-RIGHT":
			self.side = "RIGHT"

		if action == "DEL-LEFT-NECK-AXIS":
			self.dict["MNSA"][self.op_type]["LEFT"]["NECK_AXIS"]["P1"] = None
			self.dict["MNSA"][self.op_type]["LEFT"]["NECK_AXIS"]["P2"] = None
			self.dict["MNSA"][self.op_type]["LEFT"]["NECK_AXIS"]["M1"] = None

			self.draw_tools.clear_by_tag(self.tag)
			self.draw()
			self.controller.save_json()

		if action == "DEL-RIGHT-NECK-AXIS":
			self.dict["MNSA"][self.op_type]["RIGHT"]["NECK_AXIS"]["P1"] = None
			self.dict["MNSA"][self.op_type]["RIGHT"]["NECK_AXIS"]["P2"] = None
			self.dict["MNSA"][self.op_type]["RIGHT"]["NECK_AXIS"]["M1"] = None



			self.draw_tools.clear_by_tag(self.tag)
			self.draw()
			self.controller.save_json()

		self.controller.updateMenuLabel(self.getNextLabel(), self.menu_label)

	def update_canvas(self, draw_tools):
		self.draw_tools = draw_tools


	def update_dict(self, master_dict):
		self.dict = master_dict



	def getNextLabel(self):

		if self.side != None:
			
			for item in self.dict["MNSA"][self.op_type][self.side]:

				# get item type 
				item_type = self.dict["MNSA"][self.op_type][self.side][item]["type"]


				# point has P1 and P2, M1 is calculated
				if item_type == "midpoint":

					# check if P1 is None				
					if self.dict["MNSA"][self.op_type][self.side][item]["P1"] == None:
						return (self.side + " " + item + " P1")


					# check if P2 is None				
					if self.dict["MNSA"][self.op_type][self.side][item]["P2"] == None:
						return (self.side + " " + item + " P2")

			return (self.side + " Done")

		return None

 
	def unset(self):
		# print("unset from "+self.name)
		self.draw_tools.clear_by_tag(self.tag)
		self.side = None
