

class P_TILT():
	"""docstring for ClassName"""
	def __init__(self, draw_tools, master_dict, controller):
		self.name = "P_TILT"
		self.tag = "p_tilt"
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
		else:
			ret =  self.addDict(event)
			if not ret:
				# print("dict full")
				print(self.dict)
			# print(self.side)

		self.draw()
		# print(self.dict)


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

			p1 = self.dict["P_TILT"][side]["P1"]["P1"]
			p2 = self.dict["P_TILT"][side]["P2"]["P1"]			

			if p1 != None:
				self.draw_tools.create_mypoint(p1, "white", self.tag)

			if p2 != None:
				self.draw_tools.create_mypoint(p2, "white", self.tag)
			

			if p1!=None and p2!=None:
				self.draw_tools.create_myline(p1, p2, self.tag)

				try:
					sa_p1 = self.dict["SA"][side]["P1"]["P1"]				
					sa_p3 = self.dict["SA"][side]["P3"]["P1"]

					self.draw_tools.create_myline(sa_p1, sa_p3, self.tag)

				except Exception as e:
					print(e)
				
				
	def checkMasterDict(self):
		if "P_TILT" not in self.dict.keys():
			self.dict["P_TILT"] = 	{
									"LEFT":	{
												"P1":		{"type":"point","P1":None},
												"P2":		{"type":"point","P1":None}																
											},
									"RIGHT":	{
												"P1":		{"type":"point","P1":None},
												"P2":		{"type":"point","P1":None}
											}
									}



	def addDict(self, event):

		for item in self.dict["P_TILT"][self.side]:
			# get item type 
			item_type = self.dict["P_TILT"][self.side][item]["type"]

			# point only has P1
			if item_type == "point":
				# check if P1 is None				
				if self.dict["P_TILT"][self.side]["P1"]["P1"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["P_TILT"][self.side]["P1"]["P1"] = P
					return True

				if self.dict["P_TILT"][self.side]["P2"]["P1"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["P_TILT"][self.side]["P2"]["P1"] = P
					return True

		return False


	def update_canvas(self, draw_tools):
		self.draw_tools = draw_tools

	def unset(self):
		print("unset from "+self.name)
		self.draw_tools.clear_by_tag(self.tag)