

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
			return

		if action == "SET-RIGHT":
			self.side = "RIGHT"	
			self.controller.updateMenuLabel(self.getNextLabel(), "P_TILT_Menu")
			return


		if action == "DEL-LEFT-P1":
			self.dict["P_TILT"]["LEFT"]["P1"]["P1"] = None

		if action == "DEL-RIGHT-P1":
			self.dict["P_TILT"]["RIGHT"]["P1"]["P1"] = None

		if action == "DEL-LEFT-P2":
			self.dict["P_TILT"]["LEFT"]["P2"]["P1"] = None

		if action == "DEL-RIGHT-P2":
			self.dict["P_TILT"]["RIGHT"]["P2"]["P1"] = None


		self.draw_tools.clear_by_tag(self.tag)
		self.draw()
		self.controller.save_json()
		self.controller.updateMenuLabel(self.getNextLabel(), "P_TILT_Menu")

	
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

					self.draw_tools.create_mypoint(sa_p1, "white", self.tag)
					self.draw_tools.create_mypoint(sa_p3, "white", self.tag)
					self.draw_tools.create_myline(sa_p1, sa_p3, self.tag)
					

					# get left and right points
					L_sa, R_sa = self.draw_tools.retPointsLeftRight(sa_p1, sa_p3)
					L_p, R_p = self.draw_tools.retPointsLeftRight(p1, p2)
					p_int = self.draw_tools.line_intersection((sa_p1, sa_p3), (p1, p2))

					# self.draw_tools.create_mypoint(p_int, "white", self.tag)

					if side == "LEFT":
						angle = self.draw_tools.create_myAngle(L_sa, p_int, L_p, self.tag)
					else:
						angle = self.draw_tools.create_myAngle(R_p, p_int, R_sa, self.tag)

					self.draw_tools.create_mytext(p_int, '{0:.2f}'.format(angle), self.tag, y_offset=60)




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



	def getNextLabel(self):

		if self.side != None:
			for item in self.dict["P_TILT"][self.side]:
				# get item type 
				item_type = self.dict["P_TILT"][self.side][item]["type"]

				# point only has P1
				if item_type == "point":
					# check if P1 is None				
					if self.dict["P_TILT"][self.side]["P1"]["P1"] == None:						
						return (self.side + " " + "P1")

					if self.dict["P_TILT"][self.side]["P2"]["P1"] == None:						
						return (self.side + " " + "P2")

			return (self.side + " Done")

		return None		


	def update_canvas(self, draw_tools):
		self.draw_tools = draw_tools


	def update_dict(self, master_dict):
		self.dict = master_dict


	def unset(self):
		# print("unset from "+self.name)
		self.draw_tools.clear_by_tag(self.tag)