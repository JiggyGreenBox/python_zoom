import json

class MNSA():
	"""docstring for ClassName"""
	def __init__(self, draw_tools, master_dict, controller):
		self.name = "MNSA"
		self.tag = "mnsa"
		self.draw_tools = draw_tools
		self.dict = master_dict
		self.controller = controller
		self.side = None

		# check if master dictionary has values
		# if not populate the dictionary
		self.checkMasterDict()



	def checkMasterDict(self):
		if "MNSA" not in self.dict.keys():
			self.dict["MNSA"] = 	{
									"LEFT":	{
												"NECK_AXIS":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
											},
									"RIGHT":	{
												"NECK_AXIS":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
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
				pass
			else:
				print(self.dict)
				self.saveDict()

		self.draw()





	def addDict(self, event):
		for item in self.dict["MNSA"][self.side]:
			
			# get item type 
			item_type = self.dict["MNSA"][self.side][item]["type"]

			# point has P1 and P2, M1 is calculated
			if item_type == "midpoint":

				# check if P1 is None				
				if self.dict["MNSA"][self.side][item]["P1"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["MNSA"][self.side][item]["P1"] = P
					return True


				# check if P2 is None				
				if self.dict["MNSA"][self.side][item]["P2"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["MNSA"][self.side][item]["P2"] = P

					M = self.draw_tools.midpoint(self.dict["MNSA"][self.side][item]["P1"], P)
					self.dict["MNSA"][self.side][item]["M1"] = M
					return True
		return False



	def draw(self):

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
			if self.dict["MNSA"][side]["NECK_AXIS"]["P1"] != None:
				self.draw_tools.create_mypoint(self.dict["MNSA"][side]["NECK_AXIS"]["P1"], "white", self.tag)

			if self.dict["MNSA"][side]["NECK_AXIS"]["P2"] != None:
				self.draw_tools.create_mypoint(self.dict["MNSA"][side]["NECK_AXIS"]["P2"], "white", self.tag)

			if self.dict["MNSA"][side]["NECK_AXIS"]["P1"] != None and self.dict["MNSA"][side]["NECK_AXIS"]["P2"] != None:
				p1 = self.dict["MNSA"][side]["NECK_AXIS"]["P1"]
				p2 = self.dict["MNSA"][side]["NECK_AXIS"]["P2"]
				m1 = self.dict["MNSA"][side]["NECK_AXIS"]["M1"]
				self.draw_tools.create_midpoint_line(p1, p2, m1, self.tag)
				isNeck = True



			# ------------------------
			# FROM MAIN
			# ------------------------
			# HIP
			if self.dict["MAIN"][side]["HIP"]["P1"] != None:				
				self.draw_tools.create_mypoint(self.dict["MAIN"][side]["HIP"]["P1"], "white", self.tag)


			# FEM AXIS
			# TOP
			if self.dict["MAIN"][side]["AXIS_FEM"]["TOP"]["P1"] != None:
				self.draw_tools.create_mypoint(self.dict["MAIN"][side]["AXIS_FEM"]["TOP"]["P1"], "white", self.tag)

			if self.dict["MAIN"][side]["AXIS_FEM"]["TOP"]["P2"] != None:
				self.draw_tools.create_mypoint(self.dict["MAIN"][side]["AXIS_FEM"]["TOP"]["P2"], "white", self.tag)

			if self.dict["MAIN"][side]["AXIS_FEM"]["TOP"]["P1"] != None and self.dict["MAIN"][side]["AXIS_FEM"]["TOP"]["P2"] != None:
				p1 = self.dict["MAIN"][side]["AXIS_FEM"]["TOP"]["P1"]
				p2 = self.dict["MAIN"][side]["AXIS_FEM"]["TOP"]["P2"]
				m1 = self.dict["MAIN"][side]["AXIS_FEM"]["TOP"]["M1"]
				self.draw_tools.create_midpoint_line(p1, p2, m1, self.tag)
				isFemTop = True


			# BOT
			if self.dict["MAIN"][side]["AXIS_FEM"]["BOT"]["P1"] != None:
				self.draw_tools.create_mypoint(self.dict["MAIN"][side]["AXIS_FEM"]["BOT"]["P1"], "white", self.tag)

			if self.dict["MAIN"][side]["AXIS_FEM"]["BOT"]["P2"] != None:
				self.draw_tools.create_mypoint(self.dict["MAIN"][side]["AXIS_FEM"]["BOT"]["P2"], "white", self.tag)

			if self.dict["MAIN"][side]["AXIS_FEM"]["BOT"]["P1"] != None and self.dict["MAIN"][side]["AXIS_FEM"]["BOT"]["P2"] != None:
				p1 = self.dict["MAIN"][side]["AXIS_FEM"]["BOT"]["P1"]
				p2 = self.dict["MAIN"][side]["AXIS_FEM"]["BOT"]["P2"]
				m1 = self.dict["MAIN"][side]["AXIS_FEM"]["BOT"]["M1"]
				self.draw_tools.create_midpoint_line(p1, p2, m1, self.tag)
				isFemBot = True

			if isNeck and isFemBot and isFemTop:
				
				xtop, ytop, xbot, ybot = self.draw_tools.getImageCorners()

				# FEM-AXIS ray
				p_top = self.draw_tools.line_intersection(
					(self.dict["MAIN"][side]["AXIS_FEM"]["BOT"]["M1"], self.dict["MAIN"][side]["AXIS_FEM"]["TOP"]["M1"]),
					(xtop, ytop))

				self.draw_tools.create_myline(self.dict["MAIN"][side]["AXIS_FEM"]["BOT"]["M1"], p_top, self.tag)

				# NECK-SHAFT ray
				if side == "LEFT":
					p_left = self.draw_tools.line_intersection(
						(self.dict["MNSA"][side]["NECK_AXIS"]["M1"], self.dict["MAIN"][side]["HIP"]["P1"]),
						(xtop, xbot))
					self.draw_tools.create_myline(self.dict["MAIN"][side]["HIP"]["P1"], p_left, self.tag)

				if side == "RIGHT":
					p_right = self.draw_tools.line_intersection(
						(self.dict["MNSA"][side]["NECK_AXIS"]["M1"], self.dict["MAIN"][side]["HIP"]["P1"]),
						(ytop, ybot))
					self.draw_tools.create_myline(self.dict["MAIN"][side]["HIP"]["P1"], p_right, self.tag)



	# save dictionary to file
	def saveDict(self):
		with open('patient.json', 'w') as fp:
			json.dump(self.dict, fp, indent=4)	

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
		self.draw_tools.clear_by_tag("mnsa")
		self.side = None
