

class SA():
	"""docstring for ClassName"""
	def __init__(self, draw_tools, master_dict, controller, op_type):
		self.name = "SA"
		self.tag = "sa"
		self.menu_label = "SA_Menu"
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


	# menu button clicks are routed here
	def menu_btn_click(self, action):
		print(action)
		if action == "SET-LEFT":
			self.side = "LEFT"
			self.controller.updateMenuLabel(self.getNextLabel(), self.menu_label)
			self.regainHover(self.side)
			return

		if action == "SET-RIGHT":
			self.side = "RIGHT"
			self.controller.updateMenuLabel(self.getNextLabel(), self.menu_label)
			self.regainHover(self.side)
			return


		if action == "DEL-LEFT-P1":
			self.dict["SA"][self.op_type]["LEFT"]["P1"]["P1"] = None
			self.side = "LEFT"

		if action == "DEL-RIGHT-P1":
			self.dict["SA"][self.op_type]["RIGHT"]["P1"]["P1"] = None
			self.side = "RIGHT"

		if action == "DEL-LEFT-P2":
			self.dict["SA"][self.op_type]["LEFT"]["P2"]["P1"] = None
			self.side = "LEFT"

		if action == "DEL-RIGHT-P2":
			self.dict["SA"][self.op_type]["RIGHT"]["P2"]["P1"] = None
			self.side = "RIGHT"

		if action == "DEL-LEFT-P3":
			self.dict["SA"][self.op_type]["LEFT"]["P3"]["P1"] = None
			self.side = "LEFT"

		if action == "DEL-RIGHT-P3":
			self.dict["SA"][self.op_type]["RIGHT"]["P3"]["P1"] = None
			self.side = "RIGHT"
			
		
		# delete excel data from pat.json
		self.dict["EXCEL"][self.op_type][self.side]["SA"] = None

		self.controller.save_json()
		self.draw()
		self.regainHover(self.side)
		self.controller.updateMenuLabel(self.getNextLabel(), self.menu_label)
	
	def draw(self):

		self.draw_tools.clear_by_tag(self.tag)

		# loop left and right
		for side in ["LEFT","RIGHT"]:

			p1 = self.dict["SA"][self.op_type][side]["P1"]["P1"]
			p2 = self.dict["SA"][self.op_type][side]["P2"]["P1"]
			p3 = self.dict["SA"][self.op_type][side]["P3"]["P1"]

			if p1 != None:
				self.draw_tools.create_mypoint(p1, "orange", [self.tag, side, "P1"])

			if p2 != None:
				self.draw_tools.create_mypoint(p2, "orange", [self.tag, side, "P2"])

			if p3 != None:
				self.draw_tools.create_mypoint(p3, "orange", [self.tag, side, "P3"])


			if p1 != None and p2 != None:
				self.draw_tools.create_myline(p1, p2, [self.tag, "P1P2_line"])
			if p2 != None and p3!=None:
				self.draw_tools.create_myline(p2, p3, [self.tag, "P2P3_line"])


			if p1!=None and p2!=None and p3!=None:

				angle = self.draw_tools.create_myAngle(p1, p2, p3, [self.tag, "P1P2P3_angle"])
				self.draw_tools.create_mytext(p2, '{0:.2f}'.format(angle), [self.tag, "P1P2P3_angle"], y_offset=-60, color="blue")
				
				# check if value exists
				if self.dict["EXCEL"][self.op_type][side]["SA"] == None:

					self.dict["EXCEL"][self.op_type][side]["HASDATA"] 	= True
					self.dict["EXCEL"][self.op_type][side]["SA"]	 	= '{0:.2f}'.format(angle)

					# save after insert
					self.controller.save_json()




	def checkMasterDict(self):
		if "SA" not in self.dict.keys():
			self.dict["SA"] = 	{
								"PRE-OP":	{
											"LEFT":	{
														"P1":		{"type":"point","P1":None},
														"P2":		{"type":"point","P1":None},
														"P3":		{"type":"point","P1":None}
													},
											"RIGHT":{
														"P1":		{"type":"point","P1":None},
														"P2":		{"type":"point","P1":None},
														"P3":		{"type":"point","P1":None}
													}
											},
								"POST-OP":	{
											"LEFT":	{
														"P1":		{"type":"point","P1":None},
														"P2":		{"type":"point","P1":None},
														"P3":		{"type":"point","P1":None}
													},
											"RIGHT":{
														"P1":		{"type":"point","P1":None},
														"P2":		{"type":"point","P1":None},
														"P3":		{"type":"point","P1":None}
													}
											}		
								}


	def getNextLabel(self):

		if self.side != None:
			for item in self.dict["SA"][self.op_type][self.side]:
				# get item type 
				item_type = self.dict["SA"][self.op_type][self.side][item]["type"]

				# point only has P1
				if item_type == "point":
					# check if P1 is None				
					if self.dict["SA"][self.op_type][self.side]["P1"]["P1"] == None:
						return (self.side + " " + "P1")

					if self.dict["SA"][self.op_type][self.side]["P2"]["P1"] == None:
						return (self.side + " " + "P2")

					if self.dict["SA"][self.op_type][self.side]["P3"]["P1"] == None:
						return (self.side + " " + "P3")

			return (self.side + " Done")

		return None	



	'''
	def addDict(self, event):

		for item in self.dict["SA"][self.op_type][self.side]:
			# get item type 
			item_type = self.dict["SA"][self.op_type][self.side][item]["type"]

			# point only has P1
			if item_type == "point":
				# check if P1 is None				
				if self.dict["SA"][self.op_type][self.side]["P1"]["P1"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["SA"][self.op_type][self.side]["P1"]["P1"] = P
					return True

				if self.dict["SA"][self.op_type][self.side]["P2"]["P1"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["SA"][self.op_type][self.side]["P2"]["P1"] = P
					return True

				if self.dict["SA"][self.op_type][self.side]["P3"]["P1"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["SA"][self.op_type][self.side]["P3"]["P1"] = P
					return True
		return False
	'''

	def addDict(self, event):

		for item in self.dict["SA"][self.op_type][self.side]:
			
			if self.dict["SA"][self.op_type][self.side][item]["P1"] == None:

				p1 = self.dict["SA"][self.op_type][self.side]["P1"]["P1"]
				p2 = self.dict["SA"][self.op_type][self.side]["P2"]["P1"]
				p3 = self.dict["SA"][self.op_type][self.side]["P3"]["P1"]

				P = self.draw_tools.getRealCoords(event)
				self.dict["SA"][self.op_type][self.side][item]["P1"] = P

				count, p_hover = self.getPointCount(self.side)
				print("count {}".format(count))

				if count == 1:
					self.draw_tools.setHoverPoint(p_hover)
					print("p_hover {}".format(p_hover))
					self.draw_tools.setHoverPointLabel("P1")
					self.draw_tools.setHoverBool(True)
					
				# one point is None, 
				if count == 2:

					# special case
					if p2 == None and p1 != None and p3 != None:
						self.draw_tools.setHoverPoint(p_hover)
						self.draw_tools.setHoverBool(True)
						self.draw_tools.setHoverPointLabel("P_middle")
					else:
						self.draw_tools.setHoverPoint(p_hover)
						self.draw_tools.setHoverBool(True)
						self.draw_tools.setHoverPointLabel("P2")


				if count == 3 or count == 0:
					self.draw_tools.setHoverBool(False)
					self.draw_tools.setHoverPointLabel(None)

				return True
		return False	


	def hover(self, P_mouse, P_stored, hover_label):

		if hover_label == "P1":
			self.draw_tools.clear_by_tag("hover_line")
			self.draw_tools.create_myline(P_stored, P_mouse, "hover_line")

		if hover_label == "P2":
			self.draw_tools.clear_by_tag("hover_line")
			self.draw_tools.create_myline(P_stored, P_mouse, "hover_line")

		if hover_label == "P_middle" and self.side != None:
			p1 = self.dict["SA"][self.op_type][self.side]["P1"]["P1"]			
			p3 = self.dict["SA"][self.op_type][self.side]["P3"]["P1"]
			self.draw_tools.clear_by_tag("hover_line")
			self.draw_tools.create_myline(p1, P_mouse, "hover_line")
			self.draw_tools.create_myline(p3, P_mouse, "hover_line")

	def regainHover(self, side):
		
		p1 = self.dict["SA"][self.op_type][side]["P1"]["P1"]
		p2 = self.dict["SA"][self.op_type][side]["P2"]["P1"]
		p3 = self.dict["SA"][self.op_type][side]["P3"]["P1"]

		count, p_hover = self.getPointCount(side)
		

		if count == 1:
			self.draw_tools.setHoverPoint(p_hover)
			self.draw_tools.setHoverPointLabel("P1")
			self.draw_tools.setHoverBool(True)
			
		# one point is None, 
		if count == 2:
			# special case
			print("p1 {}".format(p1))
			print("p2 {}".format(p3))
			print("p3 {}".format(p2))

			if p2 == None and p1 != None and p3 != None:
				print("P_middle case")
				self.draw_tools.setHoverPoint(p_hover)
				self.draw_tools.setHoverBool(True)
				self.draw_tools.setHoverPointLabel("P_middle")
			else:
				if p1 == None and p2 != None:
					self.draw_tools.setHoverPoint(p2)
				else:				
					self.draw_tools.setHoverPoint(p_hover)
				self.draw_tools.setHoverBool(True)
				self.draw_tools.setHoverPointLabel("P2")


		if count == 3 or count == 0:
			self.draw_tools.setHoverBool(False)
			self.draw_tools.setHoverPointLabel(None)

	def getPointCount(self, side):
		p1 = self.dict["SA"][self.op_type][side]["P1"]["P1"]
		p2 = self.dict["SA"][self.op_type][side]["P2"]["P1"]
		p3 = self.dict["SA"][self.op_type][side]["P3"]["P1"]

		count = 0
		p_hover = None
		for p in [p1,p2,p3]:
			# print('p {}'.format(p))
			if p != None:
				count = count+1
				p_hover = p			

		return count, p_hover

	def escapeObjFunc(self):
		self.side = None
		self.draw_tools.setHoverPointLabel(None)
		self.draw_tools.setHoverBool(False)




	def drag_start(self, tags):
		
		tags.remove('token')
		tags.remove('current')
		tags.remove(self.tag)
		print(tags)

		# self.draw_tools.clear_by_tag('current')

		# find side
		if "LEFT" in tags:
			side = "LEFT"
		elif "RIGHT" in tags:
			side = "RIGHT"


		# SA specific functions
		p1 = self.dict["SA"][self.op_type][side]["P1"]["P1"]
		p2 = self.dict["SA"][self.op_type][side]["P2"]["P1"]
		p3 = self.dict["SA"][self.op_type][side]["P3"]["P1"]

		self.draw_tools.clear_by_tag("P1P2P3_angle")
		if "P1" in tags:
			if p2 != None:
				self.drag_point = p2
				self.drag_label = "P1"
				self.drag_side 	= side

		if "P2" in tags:
			self.drag_label = "P2"
			self.drag_side 	= side


		if "P3" in tags:
			if p2 != None:
				self.drag_point = p2
				self.drag_label = "P3" 
				self.drag_side 	= side


	def drag(self, P_mouse):
		if self.drag_label == "P1":
			if self.drag_point != None:
				self.draw_tools.clear_by_tag("P1P2_line")
				self.draw_tools.clear_by_tag("drag_line")
				self.draw_tools.create_myline(self.drag_point, P_mouse, "drag_line")


		if self.drag_label == "P3":
			if self.drag_point != None:
				self.draw_tools.clear_by_tag("P2P3_line")
				self.draw_tools.clear_by_tag("drag_line")
				self.draw_tools.create_myline(self.drag_point, P_mouse, "drag_line")

		if self.drag_label == "P2":
			p1 = self.dict["SA"][self.op_type][self.drag_side]["P1"]["P1"]			
			p3 = self.dict["SA"][self.op_type][self.drag_side]["P3"]["P1"]

			if p1 != None and p3 != None:			
				self.draw_tools.clear_by_tag("P1P2_line")
				self.draw_tools.clear_by_tag("P2P3_line")
				self.draw_tools.clear_by_tag("drag_line")
				self.draw_tools.create_myline(p1, P_mouse, "drag_line")
				self.draw_tools.create_myline(p3, P_mouse, "drag_line")

			elif p1 != None:
				self.draw_tools.clear_by_tag("P1P2_line")
				self.draw_tools.clear_by_tag("P2P3_line")
				self.draw_tools.clear_by_tag("drag_line")
				self.draw_tools.create_myline(p1, P_mouse, "drag_line")

			elif p3 != None:
				self.draw_tools.clear_by_tag("P1P2_line")
				self.draw_tools.clear_by_tag("P2P3_line")
				self.draw_tools.clear_by_tag("drag_line")
				self.draw_tools.create_myline(p3, P_mouse, "drag_line")



	def drag_stop(self, P_mouse):
		self.draw_tools.clear_by_tag("drag_line")
		if self.drag_label == "P1":
			self.dict["SA"][self.op_type][self.drag_side]["P1"]["P1"] = P_mouse			
			self.dict["EXCEL"][self.op_type][self.drag_side]["SA"] = None	# delete excel data from pat.json
			self.controller.save_json()
			self.draw()

		if self.drag_label == "P2":
			self.dict["SA"][self.op_type][self.drag_side]["P2"]["P1"] = P_mouse
			self.dict["EXCEL"][self.op_type][self.drag_side]["SA"] = None	# delete excel data from pat.json
			self.controller.save_json()
			self.draw()

		if self.drag_label == "P3":
			self.dict["SA"][self.op_type][self.drag_side]["P3"]["P1"] = P_mouse
			self.dict["EXCEL"][self.op_type][self.drag_side]["SA"] = None	# delete excel data from pat.json
			self.controller.save_json()
			self.draw()



	def update_canvas(self, draw_tools):
		self.draw_tools = draw_tools


	def update_dict(self, master_dict):
		self.dict = master_dict


	def unset(self):
		# print("unset from "+self.name)
		self.draw_tools.clear_by_tag(self.tag)