import math

class UNI_TIB_VAL():
	"""docstring for ClassName"""
	def __init__(self, draw_tools, master_dict, controller):
		self.name = "UNI_TIB_VAL"
		self.tag = "uni_tib_val"
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

		self.controller.updateMenuLabel(self.getNextLabel(), "UNI_TIB_VAL_Menu")
		self.draw_tools.clear_by_tag(self.tag)
		self.draw()


	# menu button clicks are routed here
	def menu_btn_click(self, action):
		print(action)
		if action == "SET-LEFT":
			self.side = "LEFT"
			self.controller.updateMenuLabel(self.getNextLabel(), "UNI_TIB_VAL_Menu")
			return # avoid clear,draw,json_save

		if action == "SET-RIGHT":
			self.side = "RIGHT"
			self.controller.updateMenuLabel(self.getNextLabel(), "UNI_TIB_VAL_Menu")
			return # avoid clear,draw,json_save

		if action == "DEL-LEFT-FEM-LINE":
			self.dict["UNI_TIB_VAL"]["LEFT"]["FEM_JOINT_LINE"]["P1"] = None
			self.dict["UNI_TIB_VAL"]["LEFT"]["FEM_JOINT_LINE"]["P2"] = None

		if action == "DEL-RIGHT-FEM-LINE":
			self.dict["UNI_TIB_VAL"]["RIGHT"]["FEM_JOINT_LINE"]["P1"] = None
			self.dict["UNI_TIB_VAL"]["RIGHT"]["FEM_JOINT_LINE"]["P2"] = None

		if action == "DEL-LEFT-TIB-TOP":			
			self.dict["UNI_TIB_VAL"]["LEFT"]["AXIS_TIB"]["TOP"]["P1"] = None
			self.dict["UNI_TIB_VAL"]["LEFT"]["AXIS_TIB"]["TOP"]["P2"] = None
			self.dict["UNI_TIB_VAL"]["LEFT"]["AXIS_TIB"]["TOP"]["M1"] = None

		if action == "DEL-RIGHT-TIB-TOP":
			self.dict["UNI_TIB_VAL"]["RIGHT"]["AXIS_TIB"]["TOP"]["P1"] = None
			self.dict["UNI_TIB_VAL"]["RIGHT"]["AXIS_TIB"]["TOP"]["P2"] = None
			self.dict["UNI_TIB_VAL"]["RIGHT"]["AXIS_TIB"]["TOP"]["M1"] = None

		if action == "DEL-LEFT-TIB-BOT":
			self.dict["UNI_TIB_VAL"]["LEFT"]["AXIS_TIB"]["BOT"]["P1"] = None
			self.dict["UNI_TIB_VAL"]["LEFT"]["AXIS_TIB"]["BOT"]["P2"] = None
			self.dict["UNI_TIB_VAL"]["LEFT"]["AXIS_TIB"]["BOT"]["M1"] = None

		if action == "DEL-RIGHT-TIB-BOT":
			self.dict["UNI_TIB_VAL"]["RIGHT"]["AXIS_TIB"]["BOT"]["P1"] = None
			self.dict["UNI_TIB_VAL"]["RIGHT"]["AXIS_TIB"]["BOT"]["P2"] = None
			self.dict["UNI_TIB_VAL"]["RIGHT"]["AXIS_TIB"]["BOT"]["M1"] = None

		self.controller.updateMenuLabel(self.getNextLabel(), "UNI_TIB_VAL_Menu")
		self.draw_tools.clear_by_tag(self.tag)
		self.controller.save_json()
		self.draw()




	def draw(self):
		# loop left and right				
		for side in ["LEFT","RIGHT"]:

			isFemJointLine = False
			isFemTop 	= False
			isFemBot 	= False


			fem_joint_p1 = self.dict[self.name][side]["FEM_JOINT_LINE"]["P1"]
			fem_joint_p2 = self.dict[self.name][side]["FEM_JOINT_LINE"]["P2"]


			# FEM JOINT LINE
			if fem_joint_p1 != None:
				self.draw_tools.create_mypoint(fem_joint_p1, "white", self.tag)

			if fem_joint_p2 != None:
				self.draw_tools.create_mypoint(fem_joint_p2, "white", self.tag)

			if fem_joint_p1 != None and fem_joint_p2 != None:
				self.draw_tools.create_myline(fem_joint_p1, fem_joint_p2, self.tag)
				isFemJointLine = True


			# FEM AXIS
			# TOP
			top_axis_tib_p1 = self.dict[self.name][side]["AXIS_TIB"]["TOP"]["P1"]
			top_axis_tib_p2 = self.dict[self.name][side]["AXIS_TIB"]["TOP"]["P2"]
			bot_axis_tib_p1 = self.dict[self.name][side]["AXIS_TIB"]["BOT"]["P1"]
			bot_axis_tib_p2 = self.dict[self.name][side]["AXIS_TIB"]["BOT"]["P2"]

			top_axis_tib_m1 = self.dict["UNI_TIB_VAL"][side]["AXIS_TIB"]["TOP"]["M1"]
			bot_axis_tib_m1 = self.dict["UNI_TIB_VAL"][side]["AXIS_TIB"]["BOT"]["M1"]

			if top_axis_tib_p1 != None:
				self.draw_tools.create_mypoint(top_axis_tib_p1, "white", self.tag)

			if top_axis_tib_p2 != None:
				self.draw_tools.create_mypoint(top_axis_tib_p2, "white", self.tag)

			if top_axis_tib_p1 != None and top_axis_tib_p2 != None:				
				
				self.draw_tools.create_midpoint_line(top_axis_tib_p1, top_axis_tib_p2, top_axis_tib_m1, self.tag)
				isFemTop = True


			# BOT
			if bot_axis_tib_p1 != None:
				self.draw_tools.create_mypoint(bot_axis_tib_p1, "white", self.tag)

			if bot_axis_tib_p2 != None:
				self.draw_tools.create_mypoint(bot_axis_tib_p2, "white", self.tag)

			if bot_axis_tib_p1 != None and bot_axis_tib_p2 != None:				
				m1 = self.dict["UNI_TIB_VAL"][side]["AXIS_TIB"]["TOP"]["M1"]
				self.draw_tools.create_midpoint_line(bot_axis_tib_p1, bot_axis_tib_p2, bot_axis_tib_m1, self.tag)
				isFemBot = True


			if isFemJointLine and isFemTop and isFemBot:
				U_m1, D_m1 = self.draw_tools.retPointsUpDown(top_axis_tib_m1, bot_axis_tib_m1)

				xtop, ytop, xbot, ybot = self.draw_tools.getImageCorners()

				p_top = self.draw_tools.line_intersection((D_m1, U_m1), (xtop, ytop))
				self.draw_tools.create_myline(D_m1, p_top, self.tag)


				# fem to axis intersection
				p_int = self.draw_tools.line_intersection((fem_joint_p1, fem_joint_p2), (p_top, D_m1))
				self.draw_tools.create_mypoint(p_int, "white", self.tag)

				# find parallel point
				slope = self.slope(U_m1, D_m1)				
				dy = math.sqrt(100**2/(slope**2+1))
				dx = -slope*dy

				C = [0,0]
				C[0] = p_int[0] + dx
				C[1] = p_int[1] + dy

				self.draw_tools.create_mypoint(C, "white", self.tag)

				# find L R point
				L_fem, R_fem = self.draw_tools.retPointsLeftRight(fem_joint_p1, fem_joint_p2)

				if side == "LEFT":
					L_p_border = self.draw_tools.line_intersection((C, p_int), (ytop, ybot))
					self.draw_tools.create_myline(L_p_border, p_int, self.tag)

					a1 = self.draw_tools.getAnglePoints(L_p_border, p_int, R_fem)
					a2 = self.draw_tools.getAnglePoints(R_fem, p_int, L_p_border)
					print('{0:.2f} a1 left'.format(a1))
					print('{0:.2f} a2 left'.format(a2))

					if a1 > a2:						
						angle = self.draw_tools.create_myAngle(R_fem, p_int, L_p_border, self.tag)
					else:
						angle = self.draw_tools.create_myAngle(L_p_border, p_int, R_fem, self.tag)
					self.draw_tools.create_mytext(R_fem, '{0:.2f}'.format(angle), self.tag, x_offset=60)



				if side == "RIGHT":
					R_p_border = self.draw_tools.line_intersection((C, p_int), (xtop, xbot))
					self.draw_tools.create_myline(R_p_border, p_int, self.tag)


					a1 = self.draw_tools.getAnglePoints(R_p_border, p_int, L_fem)
					a2 = self.draw_tools.getAnglePoints(L_fem, p_int, R_p_border)
					print('{0:.2f} a1 RIGHT'.format(a1))
					print('{0:.2f} a2 RIGHT'.format(a2))

					if a1 > a2:						
						angle = self.draw_tools.create_myAngle(L_fem, p_int, R_p_border, self.tag)
					else:
						angle = self.draw_tools.create_myAngle(R_p_border, p_int, L_fem, self.tag)
						
					self.draw_tools.create_mytext(L_fem, '{0:.2f}'.format(angle), self.tag, x_offset=-60)

			

	def slope(self, point1, point2):
		x1 = point1[0]
		y1 = point1[1]
		x2 = point2[0]
		y2 = point2[1]
		return (y2-y1)/(x2-x1)




	def checkMasterDict(self):
		if "UNI_TIB_VAL" not in self.dict.keys():
			self.dict["UNI_TIB_VAL"] = 	{
									"LEFT":	{
												"AXIS_TIB":	{
																"type":	"axis",
																"TOP":	{"type":"midpoint","P1":None,"P2":None, "M1":None},
																"BOT":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
															},
												"FEM_JOINT_LINE":	{"type":"line","P1":None,"P2":None}
											},
									"RIGHT":	{
												"AXIS_TIB":	{
																"type":	"axis",
																"TOP":	{"type":"midpoint","P1":None,"P2":None, "M1":None},
																"BOT":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
															},
												"FEM_JOINT_LINE":	{"type":"line","P1":None,"P2":None}
											}
									}


	def addDict(self, event):
		for item in self.dict["UNI_TIB_VAL"][self.side]:
			# get item type 
			item_type = self.dict["UNI_TIB_VAL"][self.side][item]["type"]
			
			
			# axis has two midpoints
			if item_type == "axis":
				print("axis" + item)
				# axis has a top and a bottom

				# check if P1 is None
				if self.dict["UNI_TIB_VAL"][self.side][item]["TOP"]["P1"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["UNI_TIB_VAL"][self.side][item]["TOP"]["P1"] = P
					return True

				# check if P2 is None				
				if self.dict["UNI_TIB_VAL"][self.side][item]["TOP"]["P2"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["UNI_TIB_VAL"][self.side][item]["TOP"]["P2"] = P

					M = self.draw_tools.midpoint(self.dict["UNI_TIB_VAL"][self.side][item]["TOP"]["P1"], P)
					self.dict["UNI_TIB_VAL"][self.side][item]["TOP"]["M1"] = M
					return True


				# check if P1 is None
				if self.dict["UNI_TIB_VAL"][self.side][item]["BOT"]["P1"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["UNI_TIB_VAL"][self.side][item]["BOT"]["P1"] = P
					return True

				# check if P2 is None				
				if self.dict["UNI_TIB_VAL"][self.side][item]["BOT"]["P2"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["UNI_TIB_VAL"][self.side][item]["BOT"]["P2"] = P

					M = self.draw_tools.midpoint(self.dict["UNI_TIB_VAL"][self.side][item]["BOT"]["P1"], P)
					self.dict["UNI_TIB_VAL"][self.side][item]["BOT"]["M1"] = M
					return True	


			# line has P1 and P2
			if item_type == "line":

				# check if P1 is None				
				if self.dict["UNI_TIB_VAL"][self.side][item]["P1"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["UNI_TIB_VAL"][self.side][item]["P1"] = P
					return True


				# check if P2 is None				
				if self.dict["UNI_TIB_VAL"][self.side][item]["P2"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["UNI_TIB_VAL"][self.side][item]["P2"] = P
					return True

		return False									
 

	def getNextLabel(self):
		if self.side != None:
			for item in self.dict["UNI_TIB_VAL"][self.side]:
				# get item type 
				item_type = self.dict["UNI_TIB_VAL"][self.side][item]["type"]
				
				
				# axis has two midpoints
				if item_type == "axis":
					print("axis" + item)
					# axis has a top and a bottom

					# check if P1 is None
					if self.dict["UNI_TIB_VAL"][self.side][item]["TOP"]["P1"] == None:						
						return (self.side + " " + item + " P1")

					# check if P2 is None				
					if self.dict["UNI_TIB_VAL"][self.side][item]["TOP"]["P2"] == None:						
						return (self.side + " " + item + " P2")


					# check if P1 is None
					if self.dict["UNI_TIB_VAL"][self.side][item]["BOT"]["P1"] == None:						
						return (self.side + " " + item + " P1")

					# check if P2 is None				
					if self.dict["UNI_TIB_VAL"][self.side][item]["BOT"]["P2"] == None:						
						return (self.side + " " + item + " P2")


				# line has P1 and P2
				if item_type == "line":

					# check if P1 is None				
					if self.dict["UNI_TIB_VAL"][self.side][item]["P1"] == None:						
						return (self.side + " " + item + " P1")


					# check if P2 is None				
					if self.dict["UNI_TIB_VAL"][self.side][item]["P2"] == None:
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