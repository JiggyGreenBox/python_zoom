

class ISR():
	"""docstring for ClassName"""
	def __init__(self, draw_tools, master_dict, controller, op_type):
		self.name = "ISR"
		self.tag = "isr"
		self.menu_label = "ISR_Menu"
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
			self.controller.testbubble()
			print(self.dict)
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
			self.regainHover(self.side)
			return # avoid clear,draw,json_save

		if action == "SET-RIGHT":
			self.side = "RIGHT"			
			self.controller.updateMenuLabel(self.getNextLabel(), self.menu_label)
			self.regainHover(self.side)
			return # avoid clear,draw,json_save


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


		# delete excel data from pat.json	
		self.dict["EXCEL"][self.op_type][self.side]["ISR"] = None


		self.draw()
		self.regainHover(self.side)

		self.controller.save_json()
		self.controller.updateMenuLabel(self.getNextLabel(), self.menu_label)			



	def draw(self):
		
		self.draw_tools.clear_by_tag(self.tag)

		self.point_size = self.controller.getViewPointSize()

		# loop left and right				
		for side in ["LEFT","RIGHT"]:
			
			isP1 	= False
			isP2 	= False
			isP3 	= False

			p1 = self.dict["ISR"][self.op_type][side]["P1"]["P1"]
			p2 = self.dict["ISR"][self.op_type][side]["P2"]["P1"]
			p3 = self.dict["ISR"][self.op_type][side]["P3"]["P1"]

			
			if p1 != None:
				self.draw_tools.create_mypoint(p1, "orange", [self.tag, side, "P1"], point_thickness=self.point_size)
				isP1 = True

			if p2 != None:
				self.draw_tools.create_mypoint(p2, "orange", [self.tag, side, "P2"], point_thickness=self.point_size)
				isP2 = True

			if p3 != None:
				self.draw_tools.create_mypoint(p3, "orange", [self.tag, side, "P3"], point_thickness=self.point_size)
				isP3 = True


			if isP1 and isP2:
				self.draw_tools.create_myline(p1, p2, [self.tag, side, "P1P2_line"])

			if isP2 and isP3:							
				self.draw_tools.create_myline(p2, p3, [self.tag, side, "P2P3_line"])

			if isP1 and isP2 and isP3:
				p2p3_dist = self.draw_tools.getDistance(p2, p3)
				p1p2_dist = self.draw_tools.getDistance(p1, p2)
				isr_val = p2p3_dist / p1p2_dist
				print('isr_val: {}'.format(isr_val))
				print('isr_val: {:.2f}'.format(isr_val))

				if side == "RIGHT":
					self.draw_tools.create_mytext(p2, x_offset=60, color="blue", mytext='{:.2f}'.format(isr_val), mytag=[self.tag, side, "ISR_LABEL"])
				elif side == "LEFT":
					self.draw_tools.create_mytext(p2, x_offset=-60, color="blue", mytext='{:.2f}'.format(isr_val), mytag=[self.tag, side, "ISR_LABEL"])

				if self.dict["EXCEL"][self.op_type][side]["ISR"] == None:
					self.dict["EXCEL"][self.op_type][side]["HASDATA"] 	= True
					self.dict["EXCEL"][self.op_type][side]["ISR"]	= '{0:.2f}'.format(isr_val)
					# save after insert
					self.controller.save_json()



	def checkMasterDict(self):
		if "ISR" not in self.dict.keys():
			self.dict["ISR"] = 	{
									"PRE-OP":{
												"LEFT":	{
														"P1":	{"type":"point","P1":None},
														"P2":	{"type":"point","P1":None},
														"P3":	{"type":"point","P1":None},
														},
												"RIGHT":	{
														"P1":	{"type":"point","P1":None},
														"P2":	{"type":"point","P1":None},
														"P3":	{"type":"point","P1":None},
														}
									},
									"POST-OP":{
												"LEFT":	{
														"P1":	{"type":"point","P1":None},
														"P2":	{"type":"point","P1":None},
														"P3":	{"type":"point","P1":None},
														},
												"RIGHT":	{
														"P1":	{"type":"point","P1":None},
														"P2":	{"type":"point","P1":None},
														"P3":	{"type":"point","P1":None},
														}
									}
								}


	def addDict(self, event):
		for item in self.dict["ISR"][self.op_type][self.side]:
			
			
			if self.dict["ISR"][self.op_type][self.side][item]["P1"] == None:

				p1 = self.dict["ISR"][self.op_type][self.side]["P1"]["P1"]
				p2 = self.dict["ISR"][self.op_type][self.side]["P2"]["P1"]
				p3 = self.dict["ISR"][self.op_type][self.side]["P3"]["P1"]

				P = self.draw_tools.getRealCoords(event)
				self.dict["ISR"][self.op_type][self.side][item]["P1"] = P

				count, p_hover = self.getPointCount(self.side)

				if count == 3 or count == 0:
					self.draw_tools.setHoverBool(False)
					self.draw_tools.setHoverPointLabel(None)


				if count == 1:
					self.draw_tools.setHoverPoint(p_hover)
					self.draw_tools.setHoverPointLabel("P1")
					self.draw_tools.setHoverBool(True)
					
				# one point is None, 
				if count == 2:
					if p1 == None:				
						self.draw_tools.setHoverPoint(p_hover)
					if p2 == None:				
						self.draw_tools.setHoverPoint(p_hover)
					if p3 == None:				
						self.draw_tools.setHoverPoint(p_hover)
					self.draw_tools.setHoverBool(True)
					self.draw_tools.setHoverPointLabel("P2")



				# if item == "P1":
				# 	self.draw_tools.setHoverPoint(P)
				# 	self.draw_tools.setHoverBool(True)
				# 	self.draw_tools.setHoverPointLabel("P1")

				# if item == "P2":
				# 	self.draw_tools.setHoverPoint(P)
				# 	self.draw_tools.setHoverBool(True)
				# 	self.draw_tools.setHoverPointLabel("P2")

				# if item == "P3":
				# 	self.draw_tools.setHoverBool(False)
				# 	self.draw_tools.setHoverPointLabel(None)

				
				return True
		return False


	def getNextLabel(self):

		if self.side != None:
			for item in self.dict["ISR"][self.op_type][self.side]:

				if self.dict["ISR"][self.op_type][self.side][item]["P1"] == None:					
					return (self.side + " " + item)

			return (self.side + " Done")

		return None							

	def hover(self, P_mouse, P_stored, hover_label):

		if hover_label == "P1":
			self.draw_tools.clear_by_tag("hover_line")
			self.draw_tools.create_myline(P_stored, P_mouse, "hover_line")

		if hover_label == "P2":
			self.draw_tools.clear_by_tag("hover_line")
			self.draw_tools.create_myline(P_stored, P_mouse, "hover_line")



	def regainHover(self, side):
		
		p1 = self.dict["ISR"][self.op_type][side]["P1"]["P1"]
		p2 = self.dict["ISR"][self.op_type][side]["P2"]["P1"]
		p3 = self.dict["ISR"][self.op_type][side]["P3"]["P1"]

		count, p_hover = self.getPointCount(side)
		# print(count)

		if count == 1:
			self.draw_tools.setHoverPoint(p_hover)
			self.draw_tools.setHoverPointLabel("P1")
			self.draw_tools.setHoverBool(True)
			
		# one point is None, 
		if count == 2:
			if p1 == None:				
				self.draw_tools.setHoverPoint(p2)
			if p2 == None:				
				self.draw_tools.setHoverPoint(p1)
			if p3 == None:				
				self.draw_tools.setHoverPoint(p2)
			self.draw_tools.setHoverBool(True)
			self.draw_tools.setHoverPointLabel("P2")


		if count == 3 or count == 0:
			self.draw_tools.setHoverBool(False)
			self.draw_tools.setHoverPointLabel(None)

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
		p1 = self.dict["ISR"][self.op_type][side]["P1"]["P1"]
		p2 = self.dict["ISR"][self.op_type][side]["P2"]["P1"]
		p3 = self.dict["ISR"][self.op_type][side]["P3"]["P1"]

		


		if "P1" in tags:
			
			# self.draw_tools.clear_by_tag("FFLEX_angle")
			self.drag_point = p2
			self.drag_label = "P1"
			self.drag_side 	= side


		if "P2" in tags:
			
			# self.draw_tools.clear_by_tag("FFLEX_angle")
			self.drag_point = p3
			self.drag_label = "P2"
			self.drag_side 	= side

		if "P3" in tags:
			
			# self.draw_tools.clear_by_tag("FFLEX_angle")
			self.drag_point = p2
			self.drag_label = "P3"
			self.drag_side 	= side


	def drag(self, P_mouse):
		if self.drag_label == "P1":
			if self.drag_point != None:
				self.draw_tools.clear_by_tag("ISR_LABEL")
				self.draw_tools.clear_by_tag("P1P2_line")
				self.draw_tools.clear_by_tag("drag_line")			
				self.draw_tools.create_myline(self.drag_point, P_mouse, "drag_line")


		if self.drag_label == "P2":
			self.draw_tools.clear_by_tag("ISR_LABEL")
			self.draw_tools.clear_by_tag("P1P2_line")
			self.draw_tools.clear_by_tag("P2P3_line")
			self.draw_tools.clear_by_tag("drag_line")

			if self.dict["ISR"][self.op_type][self.drag_side]["P1"]["P1"] != None:
				self.draw_tools.create_myline(self.dict["ISR"][self.op_type][self.drag_side]["P1"]["P1"], P_mouse, "drag_line")

			if self.dict["ISR"][self.op_type][self.drag_side]["P3"]["P1"] != None:
				self.draw_tools.create_myline(self.dict["ISR"][self.op_type][self.drag_side]["P3"]["P1"], P_mouse, "drag_line")

			

		if self.drag_label == "P3":
			if self.drag_point != None:
				self.draw_tools.clear_by_tag("ISR_LABEL")
				self.draw_tools.clear_by_tag("P2P3_line")
				self.draw_tools.clear_by_tag("drag_line")				
				self.draw_tools.create_myline(self.drag_point, P_mouse, "drag_line")
			
			




	def drag_stop(self, P_mouse):
		self.draw_tools.clear_by_tag("drag_line")

		# # FEM JOINT LINE
		if self.drag_label == "P1":
			self.dict["ISR"][self.op_type][self.drag_side]["P1"]["P1"] = P_mouse
			self.dict["EXCEL"][self.op_type][self.drag_side]["ISR"] = None	# delete excel data from pat.json
			self.controller.save_json()
			self.draw()

		if self.drag_label == "P2":
			self.dict["ISR"][self.op_type][self.drag_side]["P2"]["P1"] = P_mouse
			self.dict["EXCEL"][self.op_type][self.drag_side]["ISR"] = None	# delete excel data from pat.json
			self.controller.save_json()
			self.draw()


		if self.drag_label == "P3":
			self.dict["ISR"][self.op_type][self.drag_side]["P3"]["P1"] = P_mouse
			self.dict["EXCEL"][self.op_type][self.drag_side]["ISR"] = None	# delete excel data from pat.json	
			self.controller.save_json()
			self.draw()


	def getPointCount(self, side):
		p1 = self.dict["ISR"][self.op_type][side]["P1"]["P1"]
		p2 = self.dict["ISR"][self.op_type][side]["P2"]["P1"]
		p3 = self.dict["ISR"][self.op_type][side]["P3"]["P1"]

		count = 0
		p_hover = None
		for p in [p1,p2,p3]:
			# print('p {}'.format(p))
			if p != None:
				count = count+1
				p_hover = p			

		return count, p_hover

	def update_canvas(self, draw_tools):
		self.draw_tools = draw_tools

	def update_dict(self, master_dict):
		self.dict = master_dict

	def unset(self):
		# print("unset from "+self.name)
		self.draw_tools.setHoverPointLabel(None)
		self.draw_tools.setHoverBool(False)
		self.draw_tools.clear_by_tag(self.tag)