

class TSLOPE():
	"""docstring for ClassName"""
	def __init__(self, draw_tools, master_dict, controller):
		self.name = "TSLOPE"
		self.tag = "tslope"
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

		self.controller.updateMenuLabel(self.getNextLabel(), "TSLOPE_Menu")
		self.draw_tools.clear_by_tag(self.tag)
		self.draw()		
		# print(self.dict)


	# menu button clicks are routed here
	def menu_btn_click(self, action):
		print(action)
		if action == "SET-LEFT":
			self.side = "LEFT"
			self.controller.updateMenuLabel(self.getNextLabel(), "TSLOPE_Menu")
			return # avoid clear,draw,json_save

		if action == "SET-RIGHT":
			self.side = "RIGHT"
			self.controller.updateMenuLabel(self.getNextLabel(), "TSLOPE_Menu")
			return # avoid clear,draw,json_save


		if action == "DEL-LEFT-TIB-LINE":
			self.dict["TSLOPE"]["LEFT"]["TIB_JOINT_LINE"]["P1"] = None
			self.dict["TSLOPE"]["LEFT"]["TIB_JOINT_LINE"]["P2"] = None

		if action == "DEL-RIGHT-TIB-LINE":
			self.dict["TSLOPE"]["RIGHT"]["TIB_JOINT_LINE"]["P1"] = None
			self.dict["TSLOPE"]["RIGHT"]["TIB_JOINT_LINE"]["P2"] = None



		if action == "DEL-LEFT-TIB-TOP":			
			self.dict["TSLOPE"]["LEFT"]["AXIS_TIB"]["TOP"]["P1"] = None
			self.dict["TSLOPE"]["LEFT"]["AXIS_TIB"]["TOP"]["P2"] = None
			self.dict["TSLOPE"]["LEFT"]["AXIS_TIB"]["TOP"]["M1"] = None

		if action == "DEL-RIGHT-TIB-TOP":
			self.dict["TSLOPE"]["RIGHT"]["AXIS_TIB"]["TOP"]["P1"] = None
			self.dict["TSLOPE"]["RIGHT"]["AXIS_TIB"]["TOP"]["P2"] = None
			self.dict["TSLOPE"]["RIGHT"]["AXIS_TIB"]["TOP"]["M1"] = None

		if action == "DEL-LEFT-TIB-BOT":
			self.dict["TSLOPE"]["LEFT"]["AXIS_TIB"]["BOT"]["P1"] = None
			self.dict["TSLOPE"]["LEFT"]["AXIS_TIB"]["BOT"]["P2"] = None
			self.dict["TSLOPE"]["LEFT"]["AXIS_TIB"]["BOT"]["M1"] = None

		if action == "DEL-RIGHT-TIB-BOT":
			self.dict["TSLOPE"]["RIGHT"]["AXIS_TIB"]["BOT"]["P1"] = None
			self.dict["TSLOPE"]["RIGHT"]["AXIS_TIB"]["BOT"]["P2"] = None
			self.dict["TSLOPE"]["RIGHT"]["AXIS_TIB"]["BOT"]["M1"] = None

		self.controller.updateMenuLabel(self.getNextLabel(), "TSLOPE_Menu")
		self.draw_tools.clear_by_tag(self.tag)
		self.controller.save_json()
		self.draw()

	
	def draw(self):

		# loop left and right
		for side in ["LEFT","RIGHT"]:

			isTibTop 	= False
			isTibBot 	= False		
			isTibP1P2 	= False

			joint_line_p1 = self.dict["TSLOPE"][side]["TIB_JOINT_LINE"]["P1"]
			joint_line_p2 = self.dict["TSLOPE"][side]["TIB_JOINT_LINE"]["P2"]

			top_axis_tib_p1 = self.dict[self.name][side]["AXIS_TIB"]["TOP"]["P1"]
			top_axis_tib_p2 = self.dict[self.name][side]["AXIS_TIB"]["TOP"]["P2"]
			top_axis_tib_m1 = self.dict[self.name][side]["AXIS_TIB"]["TOP"]["M1"]

			bot_axis_tib_p1 = self.dict[self.name][side]["AXIS_TIB"]["BOT"]["P1"]
			bot_axis_tib_p2 = self.dict[self.name][side]["AXIS_TIB"]["BOT"]["P2"]			
			bot_axis_tib_m1 = self.dict[self.name][side]["AXIS_TIB"]["BOT"]["M1"]


			if joint_line_p1 != None:
				self.draw_tools.create_mypoint(joint_line_p1, "white", self.tag)

			if joint_line_p2 != None:
				self.draw_tools.create_mypoint(joint_line_p2, "white", self.tag)

			if joint_line_p1 != None and joint_line_p2 != None:
				self.draw_tools.create_myline(joint_line_p1, joint_line_p2, self.tag)
				isTibP1P2 = True


			# TIB AXIS
			# TOP
			if top_axis_tib_p1 != None:
				self.draw_tools.create_mypoint(top_axis_tib_p1, "white", self.tag)

			if top_axis_tib_p2 != None:
				self.draw_tools.create_mypoint(top_axis_tib_p2, "white", self.tag)

			if top_axis_tib_p1 != None and top_axis_tib_p2 != None:				
				self.draw_tools.create_midpoint_line(top_axis_tib_p1, top_axis_tib_p2, top_axis_tib_m1, self.tag)
				isTibTop = True


			# BOT
			if bot_axis_tib_p1 != None:
				self.draw_tools.create_mypoint(bot_axis_tib_p1, "white", self.tag)

			if bot_axis_tib_p2 != None:
				self.draw_tools.create_mypoint(bot_axis_tib_p2, "white", self.tag)

			if bot_axis_tib_p1 != None and bot_axis_tib_p2 != None:				
				self.draw_tools.create_midpoint_line(bot_axis_tib_p1, bot_axis_tib_p2, bot_axis_tib_m1, self.tag)
				isTibBot = True

			xtop, ytop, xbot, ybot = self.draw_tools.getImageCorners()

			if isTibTop and isTibBot and isTibP1P2:

				L_p1, R_p1 = self.draw_tools.retPointsLeftRight(joint_line_p1, joint_line_p2)
				U_m1, D_m1 = self.draw_tools.retPointsUpDown(top_axis_tib_m1, bot_axis_tib_m1)

				# TIB-AXIS ray
				p_top = self.draw_tools.line_intersection(
					(U_m1, D_m1),
					(xtop, ytop))
				self.draw_tools.create_myline(D_m1, p_top, self.tag)


				# intersection point
				p_int = self.draw_tools.line_intersection(
					(U_m1, D_m1),
					(joint_line_p1, joint_line_p2))				

				# find and draw angles
				if side == "LEFT":
					angle = self.draw_tools.create_myAngle(D_m1, p_int, L_p1, self.tag,radius=30)
					self.draw_tools.create_mytext(p_int, '{0:.2f}'.format(angle), self.tag, x_offset=-60, y_offset=60)

				if side == "RIGHT":
					angle = self.draw_tools.create_myAngle(R_p1, p_int, D_m1, self.tag,radius=30)
					self.draw_tools.create_mytext(p_int, '{0:.2f}'.format(angle), self.tag, x_offset=60, y_offset=60)





	def checkMasterDict(self):
		if "TSLOPE" not in self.dict.keys():
			self.dict["TSLOPE"] = 	{
									"LEFT":	{
												"TIB_JOINT_LINE":	{"type":"line","P1":None,"P2":None},
												"AXIS_TIB":	{
																"type":	"axis",
																"TOP":	{"type":"midpoint","P1":None,"P2":None, "M1":None},
																"BOT":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
															}
											},
									"RIGHT":	{
												"TIB_JOINT_LINE":	{"type":"line","P1":None,"P2":None},
												"AXIS_TIB":	{
																"type":	"axis",
																"TOP":	{"type":"midpoint","P1":None,"P2":None, "M1":None},
																"BOT":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
															}
											}
									}



	def addDict(self, event):

		for item in self.dict["TSLOPE"][self.side]:
			# get item type 
			item_type = self.dict["TSLOPE"][self.side][item]["type"]

			
			# line has P1 and P2
			if item_type == "line":

				# check if P1 is None				
				if self.dict["TSLOPE"][self.side][item]["P1"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["TSLOPE"][self.side][item]["P1"] = P
					return True


				# check if P2 is None				
				if self.dict["TSLOPE"][self.side][item]["P2"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["TSLOPE"][self.side][item]["P2"] = P
					return True


			# axis has two midpoints
			if item_type == "axis":				
				# axis has a top and a bottom
				# TOP

				# check if P1 is None
				if self.dict["TSLOPE"][self.side][item]["TOP"]["P1"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["TSLOPE"][self.side][item]["TOP"]["P1"] = P
					return True

				# check if P2 is None				
				if self.dict["TSLOPE"][self.side][item]["TOP"]["P2"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["TSLOPE"][self.side][item]["TOP"]["P2"] = P

					M = self.draw_tools.midpoint(self.dict["TSLOPE"][self.side][item]["TOP"]["P1"], P)
					self.dict["TSLOPE"][self.side][item]["TOP"]["M1"] = M
					return True

				# BOT
				# check if P1 is None
				if self.dict["TSLOPE"][self.side][item]["BOT"]["P1"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["TSLOPE"][self.side][item]["BOT"]["P1"] = P
					return True

				# check if P2 is None				
				if self.dict["TSLOPE"][self.side][item]["BOT"]["P2"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["TSLOPE"][self.side][item]["BOT"]["P2"] = P

					M = self.draw_tools.midpoint(self.dict["TSLOPE"][self.side][item]["BOT"]["P1"], P)
					self.dict["TSLOPE"][self.side][item]["BOT"]["M1"] = M
					return True					

		return False	


	def getNextLabel(self):

		if self.side != None:
			for item in self.dict["TSLOPE"][self.side]:
				# get item type 
				item_type = self.dict["TSLOPE"][self.side][item]["type"]

				
				# line has P1 and P2
				if item_type == "line":

					# check if P1 is None				
					if self.dict["TSLOPE"][self.side][item]["P1"] == None:						
						return (self.side + " " + item + " P1")


					# check if P2 is None				
					if self.dict["TSLOPE"][self.side][item]["P2"] == None:						
						return (self.side + " " + item + " P1")


				# axis has two midpoints
				if item_type == "axis":				
					# axis has a top and a bottom
					# TOP

					# check if P1 is None
					if self.dict["TSLOPE"][self.side][item]["TOP"]["P1"] == None:						
						return (self.side + " " + item + " P1")

					# check if P2 is None				
					if self.dict["TSLOPE"][self.side][item]["TOP"]["P2"] == None:						
						return (self.side + " " + item + " P2")

					# BOT
					# check if P1 is None
					if self.dict["TSLOPE"][self.side][item]["BOT"]["P1"] == None:						
						return (self.side + " " + item + " P1")

					# check if P2 is None				
					if self.dict["TSLOPE"][self.side][item]["BOT"]["P2"] == None:
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