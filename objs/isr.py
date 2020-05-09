

class ISR():
	"""docstring for ClassName"""
	def __init__(self, draw_tools, master_dict, controller):
		self.name = "ISR"
		self.tag = "isr"
		self.draw_tools = draw_tools
		self.dict = master_dict
		self.controller = controller
		self.side = None

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
			if not ret:
				print("dict full")
			# print(self.side)

		self.draw()
		print(self.dict)


	# menu button clicks are routed here
	def menu_btn_click(self, action):
		print(action)
		if action == "SET-LEFT":
			self.side = "LEFT"

		if action == "SET-RIGHT":
			self.side = "RIGHT"			



	def draw(self):
		# loop left and right				
		for side in ["LEFT","RIGHT"]:
			
			isP1 	= False
			isP2 	= False
			isP3 	= False

			
			if self.dict["ISR"][side]["P1"]["P1"] != None:
				self.draw_tools.create_mypoint(self.dict["ISR"][side]["P1"]["P1"], "white", self.tag)
				isP1 = True

			if self.dict["ISR"][side]["P2"]["P1"] != None:
				self.draw_tools.create_mypoint(self.dict["ISR"][side]["P2"]["P1"], "white", self.tag)
				isP2 = True

			if self.dict["ISR"][side]["P3"]["P1"] != None:
				self.draw_tools.create_mypoint(self.dict["ISR"][side]["P3"]["P1"], "white", self.tag)
				isP3 = True


			if isP1 and isP2 and isP3:
				self.draw_tools.create_myline(self.dict["ISR"][side]["P1"]["P1"], self.dict["ISR"][side]["P2"]["P1"], self.tag)
				self.draw_tools.create_myline(self.dict["ISR"][side]["P2"]["P1"], self.dict["ISR"][side]["P3"]["P1"], self.tag)



	def checkMasterDict(self):
		if "ISR" not in self.dict.keys():
			self.dict["ISR"] = 	{
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


	def addDict(self, event):
		for item in self.dict["ISR"][self.side]:
			
			
			if self.dict["ISR"][self.side][item]["P1"] == None:
				P = self.draw_tools.getRealCoords(event)
				self.dict["ISR"][self.side][item]["P1"] = P
				return True
		return False									


	def update_canvas(self, draw_tools):
		self.draw_tools = draw_tools


	def unset(self):
		print("unset from "+self.name)
		self.draw_tools.clear_by_tag(self.tag)