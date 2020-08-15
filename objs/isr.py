

class ISR():
	"""docstring for ClassName"""
	def __init__(self, draw_tools, master_dict, controller, op_type):
		self.name = "ISR"
		self.tag = "isr"
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
			self.controller.testbubble()
			print(self.dict)
		else:
			ret =  self.addDict(event)
			if ret:
				self.controller.save_json()
				# pass

		self.controller.updateMenuLabel(self.getNextLabel(), "ISR_Menu")
		self.draw_tools.clear_by_tag(self.tag)
		self.draw()


	# menu button clicks are routed here
	def menu_btn_click(self, action):
		print(action)
		if action == "SET-LEFT":
			self.side = "LEFT"
			self.controller.updateMenuLabel(self.getNextLabel(), "ISR_Menu")
			return # avoid clear,draw,json_save

		if action == "SET-RIGHT":
			self.side = "RIGHT"			
			self.controller.updateMenuLabel(self.getNextLabel(), "ISR_Menu")
			return # avoid clear,draw,json_save


		if action == "DEL-LEFT-P1":
			self.dict[self.name][self.op_type]["LEFT"]["P1"]["P1"] = None

		if action == "DEL-RIGHT-P1":
			self.dict[self.name][self.op_type]["RIGHT"]["P1"]["P1"] = None

		if action == "DEL-LEFT-P2":
			self.dict[self.name][self.op_type]["LEFT"]["P2"]["P1"] = None

		if action == "DEL-RIGHT-P2":
			self.dict[self.name][self.op_type]["RIGHT"]["P2"]["P1"] = None


		if action == "DEL-LEFT-P3":
			self.dict[self.name][self.op_type]["LEFT"]["P3"]["P1"] = None

		if action == "DEL-RIGHT-P3":
			self.dict[self.name][self.op_type]["RIGHT"]["P3"]["P1"] = None

		self.draw_tools.clear_by_tag(self.tag)
		self.draw()
		self.controller.save_json()

		self.controller.updateMenuLabel(self.getNextLabel(), "ISR_Menu")			



	def draw(self):
		# loop left and right				
		for side in ["LEFT","RIGHT"]:
			
			isP1 	= False
			isP2 	= False
			isP3 	= False

			p1 = self.dict["ISR"][self.op_type][side]["P1"]["P1"]
			p2 = self.dict["ISR"][self.op_type][side]["P2"]["P1"]
			p3 = self.dict["ISR"][self.op_type][side]["P3"]["P1"]

			
			if p1 != None:
				self.draw_tools.create_mypoint(p1, "white", self.tag)
				isP1 = True

			if p2 != None:
				self.draw_tools.create_mypoint(p2, "white", self.tag)
				isP2 = True

			if p3 != None:
				self.draw_tools.create_mypoint(p3, "white", self.tag)
				isP3 = True


			if isP1 and isP2 and isP3:
				self.draw_tools.create_myline(p1, p2, self.tag)
				self.draw_tools.create_myline(p2, p3, self.tag)



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
				P = self.draw_tools.getRealCoords(event)
				self.dict["ISR"][self.op_type][self.side][item]["P1"] = P
				return True
		return False


	def getNextLabel(self):

		if self.side != None:
			for item in self.dict["ISR"][self.op_type][self.side]:

				if self.dict["ISR"][self.op_type][self.side][item]["P1"] == None:					
					return (self.side + " " + item)

			return (self.side + " Done")

		return None							


	def update_canvas(self, draw_tools):
		self.draw_tools = draw_tools

	def update_dict(self, master_dict):
		self.dict = master_dict

	def unset(self):
		# print("unset from "+self.name)
		self.draw_tools.clear_by_tag(self.tag)