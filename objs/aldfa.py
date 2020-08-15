

class ALDFA():
	"""docstring for ClassName"""
	def __init__(self, draw_tools, master_dict, controller, op_type):
		self.name = "ALDFA"
		self.tag = "aldfa"
		self.draw_tools = draw_tools
		self.dict = master_dict
		self.controller = controller
		self.side = None
		self.op_type = op_type

		# check if master dictionary has values
		# if not populate the dictionary
		self.checkMasterDict()

	def click(self, event):
		print("click from "+self.name)

		if self.side == None:
			print("please choose side")
			self.controller.warningBox("Please select a Side")
		else:
			# print(self.dict)
			ret =  self.addDict(event)
			if ret:
				self.controller.save_json()
				# pass

		self.controller.updateMenuLabel(self.getNextLabel(), "ALDFA_Menu")
		self.draw_tools.clear_by_tag(self.tag)
		self.draw()



	def checkMasterDict(self):
		if "ALDFA" not in self.dict.keys():
			self.dict["ALDFA"] = 	{
									"PRE-OP": 	{
												"LEFT":	{
															"FEM_JOINT_LINE":	{"type":"line","P1":None,"P2":None}
														},
												"RIGHT":	{
															"FEM_JOINT_LINE":	{"type":"line","P1":None,"P2":None}
														}
												},
									"POST-OP": 	{
												"LEFT":	{
															"FEM_JOINT_LINE":	{"type":"line","P1":None,"P2":None}
														},
												"RIGHT":	{
															"FEM_JOINT_LINE":	{"type":"line","P1":None,"P2":None}
														}
												}
									}


	def addDict(self, event):
		for item in self.dict["ALDFA"][self.op_type][self.side]:
			
			# get item type 
			item_type = self.dict["ALDFA"][self.op_type][self.side][item]["type"]

			# line has P1 and P2
			if item_type == "line":

				# check if P1 is None				
				if self.dict["ALDFA"][self.op_type][self.side][item]["P1"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["ALDFA"][self.op_type][self.side][item]["P1"] = P
					return True


				# check if P2 is None				
				if self.dict["ALDFA"][self.op_type][self.side][item]["P2"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["ALDFA"][self.op_type][self.side][item]["P2"] = P
					return True

		return False



	def draw(self):

		# loop left and right
		for side in ["LEFT","RIGHT"]:

			isHip = False
			isKnee = False
			isAldfa = False

			hip = self.dict["MAIN"][self.op_type][side]["HIP"]["P1"]
			knee = self.dict["MAIN"][self.op_type][side]["KNEE"]["P1"]

			fem_p1 = self.dict["ALDFA"][self.op_type][side]["FEM_JOINT_LINE"]["P1"]
			fem_p2 = self.dict["ALDFA"][self.op_type][side]["FEM_JOINT_LINE"]["P2"]

			# ------------------------
			# FROM ALDFA
			# ------------------------
			if fem_p1 != None:
				self.draw_tools.create_mypoint(fem_p1, "white", self.tag)

			if fem_p2 != None:
				self.draw_tools.create_mypoint(fem_p2, "white", self.tag)

			if fem_p1 != None and fem_p2 != None:
				self.draw_tools.create_myline(fem_p1, fem_p2, self.tag)
				isAldfa = True


			# ------------------------
			# FROM MAIN
			# ------------------------
			# HIP
			if hip != None:
				isHip = True
				self.draw_tools.create_mypoint(hip, "white", self.tag)

			# KNEE
			if knee != None:
				isKnee = True
				self.draw_tools.create_mypoint(knee, "white", self.tag)


			if not isAldfa:
				if isHip and isKnee:
					# hip-knee line
					self.draw_tools.create_myline(hip, knee, self.tag)
			else:
				if isHip and isKnee:
					
					xtop, ytop, xbot, ybot = self.draw_tools.getImageCorners()

					# hip-knee ray
					p_bot = self.draw_tools.line_intersection(
						(hip, knee),
						(xbot, ybot))

					self.draw_tools.create_myline(hip, p_bot, self.tag)

					# find angle ray intersection point
					p_int = self.draw_tools.line_intersection(
							(hip, p_bot),
							(fem_p1, fem_p2))


						
					L_fem, R_fem = self.draw_tools.retPointsLeftRight(fem_p1, fem_p2)
						


					if side == "LEFT":
						angle = self.draw_tools.create_myAngle(hip, p_int, R_fem, self.tag)
						self.draw_tools.create_mytext(p_int, '{0:.2f}'.format(angle), self.tag, x_offset=60, y_offset=-60)

					if side == "RIGHT":
						angle = self.draw_tools.create_myAngle(L_fem, p_int, hip, self.tag)
						self.draw_tools.create_mytext(p_int, '{0:.2f}'.format(angle), self.tag, x_offset=-60, y_offset=-60)


					# check if value exists
					if self.dict["EXCEL"][self.op_type][side]["aLDFA"] == None:

						self.dict["EXCEL"][self.op_type][side]["HASDATA"] 	= True
						self.dict["EXCEL"][self.op_type][side]["aLDFA"]	 	= '{0:.2f}'.format(angle)

						# save after insert
						self.controller.save_json()

			


	# menu button clicks are routed here
	def menu_btn_click(self, action):
		print(action)
		if action == "SET-LEFT":
			self.side = "LEFT"

		if action == "SET-RIGHT":
			self.side = "RIGHT"



		if action == "DEL-LEFT-FEM-LINE":
			self.dict["ALDFA"][self.op_type]["LEFT"]["FEM_JOINT_LINE"]["P1"] = None
			self.dict["ALDFA"][self.op_type]["LEFT"]["FEM_JOINT_LINE"]["P2"] = None
			self.draw_tools.clear_by_tag(self.tag)
			self.draw()
			self.controller.save_json()

		if action == "DEL-RIGHT-FEM-LINE":
			self.dict["ALDFA"][self.op_type]["RIGHT"]["FEM_JOINT_LINE"]["P1"] = None
			self.dict["ALDFA"][self.op_type]["RIGHT"]["FEM_JOINT_LINE"]["P2"] = None
			self.draw_tools.clear_by_tag(self.tag)
			self.draw()
			self.controller.save_json()

		self.controller.updateMenuLabel(self.getNextLabel(), "ALDFA_Menu")



	def getNextLabel(self):

		if self.side != None:

			for item in self.dict["ALDFA"][self.op_type][self.side]:
				
				# get item type 
				item_type = self.dict["ALDFA"][self.op_type][self.side][item]["type"]

				# line has P1 and P2
				if item_type == "line":

					# check if P1 is None				
					if self.dict["ALDFA"][self.op_type][self.side][item]["P1"] == None:						
						return (self.side + " " + item + " P1")


					# check if P2 is None				
					if self.dict["ALDFA"][self.op_type][self.side][item]["P2"] == None:						
						return (self.side + " " + item + " P2")

				return (self.side + " Done")

		return None


	def update_canvas(self, draw_tools):
		self.draw_tools = draw_tools

	def update_dict(self, master_dict):
		self.dict = master_dict
		
	def unset(self):
		# print("unset from "+self.name)
		self.draw_tools.clear_by_tag(self.tag)