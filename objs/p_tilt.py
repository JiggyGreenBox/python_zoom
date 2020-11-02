

class P_TILT():
	"""docstring for ClassName"""
	def __init__(self, draw_tools, master_dict, controller, op_type):
		self.name = "P_TILT"
		self.tag = "p_tilt"
		self.draw_tools = draw_tools
		self.dict = master_dict
		self.controller = controller
		self.side = None
		self.op_type = op_type

		# check if master dictionary has values
		# if not populate the dictionary
		self.checkMasterDict()		

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

		self.controller.updateMenuLabel(self.getNextLabel(), "P_TILT_Menu")
		self.draw_tools.clear_by_tag(self.tag)
		self.draw()


	# menu button clicks are routed here
	def menu_btn_click(self, action):
		print(action)
		if action == "SET-LEFT":
			self.side = "LEFT"
			self.controller.updateMenuLabel(self.getNextLabel(), "P_TILT_Menu")
			self.draw()
			self.regainHover(self.side)
			return

		if action == "SET-RIGHT":
			self.side = "RIGHT"
			self.controller.updateMenuLabel(self.getNextLabel(), "P_TILT_Menu")
			self.draw()
			self.regainHover(self.side)
			return


		if action == "DEL-LEFT-P1":			
			self.dict["P_TILT"][self.op_type]["LEFT"]["P1P2_LINE"]["P1"] = None
			self.side = "LEFT"

		if action == "DEL-RIGHT-P1":			
			self.dict["P_TILT"][self.op_type]["RIGHT"]["P1P2_LINE"]["P1"] = None
			self.side = "RIGHT"

		if action == "DEL-LEFT-P2":
			self.dict["P_TILT"][self.op_type]["LEFT"]["P1P2_LINE"]["P2"] = None
			self.side = "LEFT"

		if action == "DEL-RIGHT-P2":
			self.dict["P_TILT"][self.op_type]["RIGHT"]["P1P2_LINE"]["P2"] = None
			self.side = "RIGHT"


		if action == "DEL-LEFT-P3":			
			self.dict["P_TILT"][self.op_type]["LEFT"]["P3P4_LINE"]["P1"] = None
			self.side = "LEFT"

		if action == "DEL-RIGHT-P3":			
			self.dict["P_TILT"][self.op_type]["RIGHT"]["P3P4_LINE"]["P1"] = None
			self.side = "RIGHT"

		if action == "DEL-LEFT-P4":
			self.dict["P_TILT"][self.op_type]["LEFT"]["P3P4_LINE"]["P2"] = None
			self.side = "LEFT"

		if action == "DEL-RIGHT-P4":
			self.dict["P_TILT"][self.op_type]["RIGHT"]["P3P4_LINE"]["P2"] = None
			self.side = "RIGHT"

		
		self.draw()
		self.regainHover(self.side)
		self.controller.save_json()
		self.controller.updateMenuLabel(self.getNextLabel(), "P_TILT_Menu")

	
	def draw(self):

		self.draw_tools.clear_by_tag(self.tag)

		# loop left and right
		for side in ["LEFT","RIGHT"]:

			p1 = self.dict["P_TILT"][self.op_type][side]["P1P2_LINE"]["P1"]
			p2 = self.dict["P_TILT"][self.op_type][side]["P1P2_LINE"]["P2"]
			p3 = self.dict["P_TILT"][self.op_type][side]["P3P4_LINE"]["P1"]
			p4 = self.dict["P_TILT"][self.op_type][side]["P3P4_LINE"]["P2"]



			if p1 != None:
				self.draw_tools.create_mypoint(p1, "white", [self.tag,side,"P1P2_LINE","P1"])

			if p2 != None:
				self.draw_tools.create_mypoint(p2, "white", [self.tag,side,"P1P2_LINE","P2"])

			if p1 != None and p2 != None:
				self.draw_tools.create_myline(p1, p2, [self.tag,side,"P1P2_LINE","P1P2_LINE_LINE"])



			if p3 != None:
				self.draw_tools.create_mypoint(p3, "white", [self.tag,side,"P3P4_LINE","P1"])

			if p4 != None:
				self.draw_tools.create_mypoint(p4, "white", [self.tag,side,"P3P4_LINE","P2"])

			if p3 != None and p4 != None:
				self.draw_tools.create_myline(p3, p4, [self.tag,side,"P3P4_LINE","P3P4_LINE_LINE"])
			

			if p1 != None and p2 != None and p3 != None and p4 != None:
				
				U_p, D_p = self.draw_tools.retPointsUpDown(p3, p4)
				L_p, R_p = self.draw_tools.retPointsLeftRight(p1, p2)
				p_int = self.draw_tools.line_intersection((U_p, D_p), (L_p, R_p))


				if side == "LEFT":
					angle = self.draw_tools.create_myAngle(U_p, p_int, R_p, [self.tag,"PTILT_ANGLE"])
				else:
					angle = self.draw_tools.create_myAngle(L_p, p_int, U_p, [self.tag,"PTILT_ANGLE"])

				self.draw_tools.create_mytext(p_int, '{0:.2f}'.format(angle), [self.tag,"PTILT_ANGLE"], y_offset=60, color="blue")


			# if p1!=None and p2!=None:
			# 	self.draw_tools.create_myline(p1, p2, self.tag)

			# 	try:
			# 		sa_p1 = self.dict["SA"][self.op_type][side]["P1"]["P1"]				
			# 		sa_p3 = self.dict["SA"][self.op_type][side]["P3"]["P1"]

			# 		self.draw_tools.create_mypoint(sa_p1, "white", [self.tag])
			# 		self.draw_tools.create_mypoint(sa_p3, "white", [self.tag])
			# 		self.draw_tools.create_myline(sa_p1, sa_p3, [self.tag])
					

			# 		# get left and right points
			# 		L_sa, R_sa = self.draw_tools.retPointsLeftRight(sa_p1, sa_p3)
			# 		L_p, R_p = self.draw_tools.retPointsLeftRight(p1, p2)
			# 		p_int = self.draw_tools.line_intersection((sa_p1, sa_p3), (p1, p2))

			# 		# self.draw_tools.create_mypoint(p_int, "white", self.tag)

			# 		if side == "LEFT":
			# 			angle = self.draw_tools.create_myAngle(L_sa, p_int, L_p, [self.tag])
			# 		else:
			# 			angle = self.draw_tools.create_myAngle(R_p, p_int, R_sa, [self.tag])

			# 		self.draw_tools.create_mytext(p_int, '{0:.2f}'.format(angle), [self.tag], y_offset=60)

			# 		# check if value exists
			# 		if self.dict["EXCEL"][self.op_type][side]["PTILT"] == None:

			# 			self.dict["EXCEL"][self.op_type][side]["HASDATA"] 	= True
			# 			self.dict["EXCEL"][self.op_type][side]["PTILT"]	 	= '{0:.2f}'.format(angle)

			# 			# save after insert
			# 			self.controller.save_json()




			# 	except Exception as e:
			# 		print(e)
				
				
	def checkMasterDict(self):
		if "P_TILT" not in self.dict.keys():
			'''
			self.dict["P_TILT"] = 	{
										"PRE-OP":{
												"LEFT":	{
															"P1":		{"type":"point","P1":None},
															"P2":		{"type":"point","P1":None}																
														},
												"RIGHT":	{
															"P1":		{"type":"point","P1":None},
															"P2":		{"type":"point","P1":None}
														}
										},
										"POST-OP":{
												"LEFT":	{
															"P1":		{"type":"point","P1":None},
															"P2":		{"type":"point","P1":None}																
														},
												"RIGHT":	{
															"P1":		{"type":"point","P1":None},
															"P2":		{"type":"point","P1":None}
														}
										}
									}
			'''
			self.dict["P_TILT"] = 	{
										"PRE-OP":{
												"LEFT":	{
															"P1P2_LINE":	{"type":"line","P1":None,"P2":None},
															"P3P4_LINE":	{"type":"line","P1":None,"P2":None}
																										
														},
												"RIGHT":	{
															"P1P2_LINE":	{"type":"line","P1":None,"P2":None},
															"P3P4_LINE":	{"type":"line","P1":None,"P2":None}
														}
										},
										"POST-OP":{
												"LEFT":	{
															"P1P2_LINE":	{"type":"line","P1":None,"P2":None},
															"P3P4_LINE":	{"type":"line","P1":None,"P2":None}
														},
												"RIGHT":	{
															"P1P2_LINE":	{"type":"line","P1":None,"P2":None},
															"P3P4_LINE":	{"type":"line","P1":None,"P2":None}
														}
										}
									}



	def addDict(self, event):

		for item in self.dict["P_TILT"][self.op_type][self.side]:
			# get item type 
			item_type = self.dict["P_TILT"][self.op_type][self.side][item]["type"]

			P = self.draw_tools.getRealCoords(event)

			p1 = self.dict["P_TILT"][self.op_type][self.side]["P1P2_LINE"]["P1"]
			p2 = self.dict["P_TILT"][self.op_type][self.side]["P1P2_LINE"]["P2"]
			p3 = self.dict["P_TILT"][self.op_type][self.side]["P3P4_LINE"]["P1"]
			p4 = self.dict["P_TILT"][self.op_type][self.side]["P3P4_LINE"]["P2"]

			# point only has P1
			if item_type == "line":
				# check if P1 is None				
				if p1 == None:
					self.dict["P_TILT"][self.op_type][self.side]["P1P2_LINE"]["P1"] = P

					if p2 == None:
						self.draw_tools.setHoverPointLabel("P1")
						self.draw_tools.setHoverPoint(P)
						self.draw_tools.setHoverBool(True)
					elif p2 != None:
						self.draw_tools.setHoverBool(False)
						self.draw_tools.setHoverPointLabel(None)
					return True

				if p2 == None:
					self.dict["P_TILT"][self.op_type][self.side]["P1P2_LINE"]["P2"] = P
					if p1 == None:
						self.draw_tools.setHoverPointLabel("P1")
						self.draw_tools.setHoverPoint(P)
						self.draw_tools.setHoverBool(True)
					elif p1 != None:
						self.draw_tools.setHoverBool(False)
						self.draw_tools.setHoverPointLabel(None)
					return True

				if p3 == None:
					self.dict["P_TILT"][self.op_type][self.side]["P3P4_LINE"]["P1"] = P
					if p4 == None:
						self.draw_tools.setHoverPointLabel("P3")
						self.draw_tools.setHoverPoint(P)
						self.draw_tools.setHoverBool(True)
					elif p4 != None:
						self.draw_tools.setHoverBool(False)
						self.draw_tools.setHoverPointLabel(None)
					return True

				if p4 == None:
					self.dict["P_TILT"][self.op_type][self.side]["P3P4_LINE"]["P2"] = P
					if p3 == None:
						self.draw_tools.setHoverPointLabel("P3")
						self.draw_tools.setHoverPoint(P)
						self.draw_tools.setHoverBool(True)
					elif p3 != None:
						self.draw_tools.setHoverBool(False)
						self.draw_tools.setHoverPointLabel(None)
					return True

		return False



	def getNextLabel(self):

		if self.side != None:
			for item in self.dict["P_TILT"][self.op_type][self.side]:
				# get item type 
				item_type = self.dict["P_TILT"][self.op_type][self.side][item]["type"]

				p1 = self.dict["P_TILT"][self.op_type][self.side]["P1P2_LINE"]["P1"]
				p2 = self.dict["P_TILT"][self.op_type][self.side]["P1P2_LINE"]["P2"]
				p3 = self.dict["P_TILT"][self.op_type][self.side]["P3P4_LINE"]["P1"]
				p4 = self.dict["P_TILT"][self.op_type][self.side]["P3P4_LINE"]["P2"]

				# point only has P1
				if item_type == "line":
					# check if P1 is None				
					if p1== None:
						return (self.side + " P1")

					if p2 == None:
						return (self.side + " P2")

					if p3 == None:
						return (self.side + " P3")

					if p4 == None:
						return (self.side + " P4")

			return (self.side + " Done")

		return None		



	def hover(self, P_mouse, P_stored, hover_label):

		if hover_label == "P1":
			self.draw_tools.clear_by_tag("hover_line")
			self.draw_tools.create_myline(P_stored, P_mouse, "hover_line")


		if hover_label == "P3":
			self.draw_tools.clear_by_tag("hover_line")
			self.draw_tools.create_myline(P_stored, P_mouse, "hover_line")


	def regainHover(self, side):

		p1 = self.dict["P_TILT"][self.op_type][side]["P1P2_LINE"]["P1"]
		p2 = self.dict["P_TILT"][self.op_type][side]["P1P2_LINE"]["P2"]
		p3 = self.dict["P_TILT"][self.op_type][side]["P3P4_LINE"]["P1"]
		p4 = self.dict["P_TILT"][self.op_type][side]["P3P4_LINE"]["P2"]

		# no P1 no P2
		# P1 but no P2
		# P2 but no P1
		if p1 == None and p2 == None:
			self.draw_tools.setHoverBool(False)
			self.draw_tools.setHoverPointLabel(None)

		if p1 == None and p2 != None:
			self.draw_tools.setHoverPointLabel("P1")
			self.draw_tools.setHoverPoint(p2)
			self.draw_tools.setHoverBool(True)

		if p2 == None and p1 != None:
			self.draw_tools.setHoverPointLabel("P1")
			self.draw_tools.setHoverPoint(p1)
			self.draw_tools.setHoverBool(True)


		# no P3 no P4
		# P3 but no P4
		# P4 but no P3
		if p3 == None and p4 == None:
			self.draw_tools.setHoverBool(False)
			self.draw_tools.setHoverPointLabel(None)

		if p3 == None and p4 != None:
			self.draw_tools.setHoverPointLabel("P3")
			self.draw_tools.setHoverPoint(p4)
			self.draw_tools.setHoverBool(True)

		if p4 == None and p3 != None:
			self.draw_tools.setHoverPointLabel("P3")
			self.draw_tools.setHoverPoint(p3)
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


		p1 = self.dict["P_TILT"][self.op_type][side]["P1P2_LINE"]["P1"]
		p2 = self.dict["P_TILT"][self.op_type][side]["P1P2_LINE"]["P2"]
		p3 = self.dict["P_TILT"][self.op_type][side]["P3P4_LINE"]["P1"]
		p4 = self.dict["P_TILT"][self.op_type][side]["P3P4_LINE"]["P2"]


		if "P1P2_LINE" in tags:
			item = "P1P2_LINE"
		elif "P3P4_LINE" in tags:
			item = "P3P4_LINE"


		if "P1" in tags:

			if item == "P1P2_LINE":
				self.drag_point = p2
				self.drag_label = "P1"
				self.drag_side 	= side

			if item == "P3P4_LINE":
				self.drag_point = p4
				self.drag_label = "P3"
				self.drag_side 	= side

		elif "P2" in tags:
			
			if item == "P1P2_LINE":
				self.drag_point = p1
				self.drag_label = "P2"
				self.drag_side 	= side

			if item == "P3P4_LINE":
				self.drag_point = p3
				self.drag_label = "P4"
				self.drag_side 	= side
		

	def drag(self, P_mouse):

		if self.drag_label == "P1" or self.drag_label == "P2":
			if self.drag_point != None:

				self.draw_tools.clear_by_tag("PTILT_ANGLE")

				self.draw_tools.clear_by_tag("P1P2_LINE_LINE")
				self.draw_tools.clear_by_tag("drag_line")
				self.draw_tools.create_myline(self.drag_point, P_mouse, "drag_line")
		
		if self.drag_label == "P3" or self.drag_label == "P4":
			if self.drag_point != None:

				self.draw_tools.clear_by_tag("PTILT_ANGLE")

				self.draw_tools.clear_by_tag("P3P4_LINE_LINE")
				self.draw_tools.clear_by_tag("drag_line")
				self.draw_tools.create_myline(self.drag_point, P_mouse, "drag_line")
				

	def drag_stop(self, P_mouse):
		self.draw_tools.clear_by_tag("drag_line")

		# # FEM JOINT LINE
		if self.drag_label == "P1":
			self.dict["P_TILT"][self.op_type][self.drag_side]["P1P2_LINE"]["P1"] = P_mouse
			self.controller.save_json()
			self.draw()

		if self.drag_label == "P2":
			self.dict["P_TILT"][self.op_type][self.drag_side]["P1P2_LINE"]["P2"] = P_mouse
			self.controller.save_json()
			self.draw()


		if self.drag_label == "P3":
			self.dict["P_TILT"][self.op_type][self.drag_side]["P3P4_LINE"]["P1"] = P_mouse
			self.controller.save_json()
			self.draw()

		if self.drag_label == "P4":
			self.dict["P_TILT"][self.op_type][self.drag_side]["P3P4_LINE"]["P2"] = P_mouse
			self.controller.save_json()
			self.draw()



	def update_canvas(self, draw_tools):
		self.draw_tools = draw_tools


	def update_dict(self, master_dict):
		self.dict = master_dict


	def unset(self):
		# print("unset from "+self.name)
		self.draw_tools.clear_by_tag(self.tag)

		