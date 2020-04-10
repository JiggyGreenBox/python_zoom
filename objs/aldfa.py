

class ALDFA():
	"""docstring for ClassName"""
	def __init__(self, draw_tools, master_dict, controller):
		self.name = "ALDFA"
		self.tag = "aldfa"
		self.draw_tools = draw_tools
		self.dict = master_dict
		self.controller = controller
		self.side = None

		# check if master dictionary has values
		# if not populate the dictionary
		self.checkMasterDict()

	def click(self, event):
		print("click from "+self.name)

		if self.side == None:
			print("please choose side")
			self.controller.warningBox("Please select a Side")
		else:
			print(self.dict)
			ret =  self.addDict(event)
			if ret:
				pass
			else:
				print(self.dict)			
		self.draw()



	def checkMasterDict(self):
		if "ALDFA" not in self.dict.keys():
			self.dict["ALDFA"] = 	{
									"LEFT":	{
												"FEM_JOINT_LINE":	{"type":"line","P1":None,"P2":None}
											},
									"RIGHT":	{
												"FEM_JOINT_LINE":	{"type":"line","P1":None,"P2":None}
											}
									}


	def addDict(self, event):
		for item in self.dict["ALDFA"][self.side]:
			
			# get item type 
			item_type = self.dict["ALDFA"][self.side][item]["type"]

			# line has P1 and P2
			if item_type == "line":

				# check if P1 is None				
				if self.dict["ALDFA"][self.side][item]["P1"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["ALDFA"][self.side][item]["P1"] = P
					return True


				# check if P2 is None				
				if self.dict["ALDFA"][self.side][item]["P2"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["ALDFA"][self.side][item]["P2"] = P
					return True

		return False



	def draw(self):

		# loop left and right
		for side in ["LEFT","RIGHT"]:

			isHip = False
			isKnee = False
			isAldfa = False

			# ------------------------
			# FROM ALDFA
			# ------------------------
			if self.dict["ALDFA"][side]["FEM_JOINT_LINE"]["P1"] != None:
				self.draw_tools.create_mypoint(self.dict["ALDFA"][side]["FEM_JOINT_LINE"]["P1"], "white", self.tag)

			if self.dict["ALDFA"][side]["FEM_JOINT_LINE"]["P2"] != None:
				self.draw_tools.create_mypoint(self.dict["ALDFA"][side]["FEM_JOINT_LINE"]["P2"], "white", self.tag)

			if self.dict["ALDFA"][side]["FEM_JOINT_LINE"]["P1"] != None and self.dict["ALDFA"][side]["FEM_JOINT_LINE"]["P2"] != None:
				self.draw_tools.create_myline(self.dict["ALDFA"][side]["FEM_JOINT_LINE"]["P1"], self.dict["ALDFA"][side]["FEM_JOINT_LINE"]["P2"], self.tag)
				isAldfa = True


			# ------------------------
			# FROM MAIN
			# ------------------------
			# HIP
			if self.dict["MAIN"][side]["HIP"]["P1"] != None:
				isHip = True
				self.draw_tools.create_mypoint(self.dict["MAIN"][side]["HIP"]["P1"], "white", self.tag)

			# KNEE
			if self.dict["MAIN"][side]["KNEE"]["P1"] != None:
				isKnee = True
				self.draw_tools.create_mypoint(self.dict["MAIN"][side]["KNEE"]["P1"], "white", self.tag)


			if not isAldfa:
				if isHip and isKnee:
					# hip-knee line
					self.draw_tools.create_myline(self.dict["MAIN"][side]["HIP"]["P1"], self.dict["MAIN"][side]["KNEE"]["P1"], self.tag)
			else:
				if isHip and isKnee:
					
					xtop, ytop, xbot, ybot = self.draw_tools.getImageCorners()

					# hip-knee ray
					p_bot = self.draw_tools.line_intersection(
						(self.dict["MAIN"][side]["HIP"]["P1"], self.dict["MAIN"][side]["KNEE"]["P1"]),
						(xbot, ybot))

					self.draw_tools.create_myline(self.dict["MAIN"][side]["HIP"]["P1"], p_bot, self.tag)



	# menu button clicks are routed here
	def menu_btn_click(self, action):
		print(action)
		if action == "SET-LEFT":
			self.side = "LEFT"

		if action == "SET-RIGHT":
			self.side = "RIGHT"


	def update_canvas(self, draw_tools):
		self.draw_tools = draw_tools
		
	def unset(self):
		print("unset from "+self.name)
		self.draw_tools.clear_by_tag(self.tag)