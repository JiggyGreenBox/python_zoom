import json

class MAIN:
	# instance attribute
	def __init__(self, draw_tools, master_dict, controller, op_type):
		self.name = "MAIN"
		self.tag = "main"
		self.draw_tools = draw_tools
		self.dict = master_dict
		self.controller = controller
		self.side = None
		self.op_type = op_type

		# check if master dictionary has values
		# if not populate the dictionary
		self.checkMasterDict()


	def checkMasterDict(self):
		if "MAIN" not in self.dict.keys():
				self.dict["MAIN"] = 	{
										"PRE-OP": 	{
													"LEFT":	{
															"HIP":		{"type":"point","P1":None},
															"KNEE":		{"type":"point","P1":None},
															"ANKLE":	{"type":"midpoint","P1":None,"P2":None, "M1":None},
															"AXIS_FEM":	{
																			"type":	"axis",
																			"TOP":	{"type":"midpoint","P1":None,"P2":None, "M1":None},
																			"BOT":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
																		},
															"AXIS_TIB":	{
																			"type":	"axis",
																			"TOP":	{"type":"midpoint","P1":None,"P2":None, "M1":None},
																			"BOT":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
																		}
															},
													"RIGHT":{
															"HIP":		{"type":"point","P1":None},
															"KNEE":		{"type":"point","P1":None},
															"ANKLE":	{"type":"midpoint","P1":None,"P2":None, "M1":None},
															"AXIS_FEM":	{
																			"type":	"axis",
																			"TOP":	{"type":"midpoint","P1":None,"P2":None, "M1":None},
																			"BOT":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
																		},
															"AXIS_TIB":	{
																			"type":	"axis",
																			"TOP":	{"type":"midpoint","P1":None,"P2":None, "M1":None},
																			"BOT":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
																		}
															}
												},
										"POST-OP": 	{
													"LEFT":	{
															"HIP":		{"type":"point","P1":None},
															"KNEE":		{"type":"point","P1":None},
															"ANKLE":	{"type":"midpoint","P1":None,"P2":None, "M1":None},
															"AXIS_FEM":	{
																			"type":	"axis",
																			"TOP":	{"type":"midpoint","P1":None,"P2":None, "M1":None},
																			"BOT":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
																		},
															"AXIS_TIB":	{
																			"type":	"axis",
																			"TOP":	{"type":"midpoint","P1":None,"P2":None, "M1":None},
																			"BOT":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
																		}
															},
													"RIGHT":{
															"HIP":		{"type":"point","P1":None},
															"KNEE":		{"type":"point","P1":None},
															"ANKLE":	{"type":"midpoint","P1":None,"P2":None, "M1":None},
															"AXIS_FEM":	{
																			"type":	"axis",
																			"TOP":	{"type":"midpoint","P1":None,"P2":None, "M1":None},
																			"BOT":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
																		},
															"AXIS_TIB":	{
																			"type":	"axis",
																			"TOP":	{"type":"midpoint","P1":None,"P2":None, "M1":None},
																			"BOT":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
																		}
															}
													}
												
										}


	def click(self, event):
		print("click from "+self.name)
		print(self.dict)

		# self.controller.updateMenuLabel("jiggy", "MAIN_Menu")
		# self.updateLabel(self.getNextLabel())
		# self.controller.updateMenuLabel(self.getNextLabel(), "MAIN_Menu")


		# self.draw()

		if self.side == None:
			print("please choose side")
			self.controller.warningBox("Please select a Side")
			# self.controller.testbubble()
		else:
			# print("proceed")
			ret =  self.addDict(event)
			if ret:				
				self.controller.save_json()
				# pass

		self.controller.updateMenuLabel(self.getNextLabel(), "MAIN_Menu")
		self.draw_tools.clear_by_tag(self.tag)
		self.draw()

			# self.controller.updateMenuLabel("jiggy", "MAIN_Menu")

		# ret, cur_tag = self.addDict(event), cur_tag = self.addDict(event)	
		# if ret:
		# 	print(cur_tag)
		# 	self.draw_tools.create_token(event, "white", cur_tag)
		# 	self.drawLines()
		# else:
		# 	print(self.dict)




	# save dictionary to file
	def saveDict(self):
		pass
		# with open('patient.json', 'w') as fp:
		# 	json.dump(self.dict, fp, indent=4)		

	# menu button clicks are routed here
	def menu_btn_click(self, action):
		print(action)
		if action == "SET-LEFT":
			self.side = "LEFT"
			self.controller.updateMenuLabel(self.getNextLabel(), "MAIN_Menu")
			return # avoid clear,draw,json_save

		if action == "SET-RIGHT":
			self.side = "RIGHT"
			self.controller.updateMenuLabel(self.getNextLabel(), "MAIN_Menu")
			return # avoid clear,draw,json_save



		if action == "DEL-LEFT-HIP":
			self.dict["MAIN"][self.op_type]["LEFT"]["HIP"]["P1"] = None

		if action == "DEL-RIGHT-HIP":
			self.dict["MAIN"][self.op_type]["RIGHT"]["HIP"]["P1"] = None

		if action == "DEL-LEFT-KNEE":
			self.dict["MAIN"][self.op_type]["LEFT"]["KNEE"]["P1"] = None

		if action == "DEL-RIGHT-KNEE":
			self.dict["MAIN"][self.op_type]["RIGHT"]["KNEE"]["P1"] = None

		if action == "DEL-LEFT-ANKLE":
			self.dict["MAIN"][self.op_type]["LEFT"]["ANKLE"]["P1"] = None
			self.dict["MAIN"][self.op_type]["LEFT"]["ANKLE"]["P2"] = None
			self.dict["MAIN"][self.op_type]["LEFT"]["ANKLE"]["M1"] = None

		if action == "DEL-RIGHT-ANKLE":
			self.dict["MAIN"][self.op_type]["RIGHT"]["ANKLE"]["P1"] = None
			self.dict["MAIN"][self.op_type]["RIGHT"]["ANKLE"]["P2"] = None
			self.dict["MAIN"][self.op_type]["RIGHT"]["ANKLE"]["M1"] = None

		if action == "DEL-LEFT-FEM-TOP":
			self.dict["MAIN"][self.op_type]["LEFT"]["AXIS_FEM"]["TOP"]["P1"] = None
			self.dict["MAIN"][self.op_type]["LEFT"]["AXIS_FEM"]["TOP"]["P2"] = None
			self.dict["MAIN"][self.op_type]["LEFT"]["AXIS_FEM"]["TOP"]["M1"] = None

		if action == "DEL-RIGHT-FEM-TOP":
			self.dict["MAIN"][self.op_type]["RIGHT"]["AXIS_FEM"]["TOP"]["P1"] = None
			self.dict["MAIN"][self.op_type]["RIGHT"]["AXIS_FEM"]["TOP"]["P2"] = None
			self.dict["MAIN"][self.op_type]["RIGHT"]["AXIS_FEM"]["TOP"]["M1"] = None


		if action == "DEL-LEFT-FEM-BOT":
			self.dict["MAIN"][self.op_type]["LEFT"]["AXIS_FEM"]["BOT"]["P1"] = None
			self.dict["MAIN"][self.op_type]["LEFT"]["AXIS_FEM"]["BOT"]["P2"] = None
			self.dict["MAIN"][self.op_type]["LEFT"]["AXIS_FEM"]["BOT"]["M1"] = None

		if action == "DEL-RIGHT-FEM-BOT":
			self.dict["MAIN"][self.op_type]["RIGHT"]["AXIS_FEM"]["BOT"]["P1"] = None
			self.dict["MAIN"][self.op_type]["RIGHT"]["AXIS_FEM"]["BOT"]["P2"] = None
			self.dict["MAIN"][self.op_type]["RIGHT"]["AXIS_FEM"]["BOT"]["M1"] = None


		if action == "DEL-LEFT-TIB-TOP":
			self.dict["MAIN"][self.op_type]["LEFT"]["AXIS_TIB"]["TOP"]["P1"] = None
			self.dict["MAIN"][self.op_type]["LEFT"]["AXIS_TIB"]["TOP"]["P2"] = None
			self.dict["MAIN"][self.op_type]["LEFT"]["AXIS_TIB"]["TOP"]["M1"] = None

		if action == "DEL-RIGHT-TIB-TOP":
			self.dict["MAIN"][self.op_type]["RIGHT"]["AXIS_TIB"]["TOP"]["P1"] = None
			self.dict["MAIN"][self.op_type]["RIGHT"]["AXIS_TIB"]["TOP"]["P2"] = None
			self.dict["MAIN"][self.op_type]["RIGHT"]["AXIS_TIB"]["TOP"]["M1"] = None

		if action == "DEL-LEFT-TIB-BOT":
			self.dict["MAIN"][self.op_type]["LEFT"]["AXIS_TIB"]["BOT"]["P1"] = None
			self.dict["MAIN"][self.op_type]["LEFT"]["AXIS_TIB"]["BOT"]["P2"] = None
			self.dict["MAIN"][self.op_type]["LEFT"]["AXIS_TIB"]["BOT"]["M1"] = None

		if action == "DEL-RIGHT-TIB-BOT":
			self.dict["MAIN"][self.op_type]["RIGHT"]["AXIS_TIB"]["BOT"]["P1"] = None
			self.dict["MAIN"][self.op_type]["RIGHT"]["AXIS_TIB"]["BOT"]["P2"] = None
			self.dict["MAIN"][self.op_type]["RIGHT"]["AXIS_TIB"]["BOT"]["M1"] = None


		self.draw_tools.clear_by_tag("main")
		self.draw()
		self.controller.save_json()

		self.controller.updateMenuLabel(self.getNextLabel(), "MAIN_Menu")



	def getNextLabel(self):

		if self.side != None:
			
			for item in self.dict["MAIN"][self.op_type][self.side]:
				# get item type 
				item_type = self.dict["MAIN"][self.op_type][self.side][item]["type"]

				# point only has P1
				if item_type == "point":
					# check if P1 is None				
					if self.dict["MAIN"][self.op_type][self.side][item]["P1"] == None:						
						return (self.side + " " + item)

				# point has P1 and P2, M1 is calculated
				if item_type == "midpoint":

					# check if P1 is None				
					if self.dict["MAIN"][self.op_type][self.side][item]["P1"] == None:
						return (self.side + " " + item + " P1")


					# check if P2 is None				
					if self.dict["MAIN"][self.op_type][self.side][item]["P2"] == None:
						return (self.side + " " + item + " P2")

				# axis has two midpoints
				if item_type == "axis":
					print("axis" + item)
					# axis has a top and a bottom

					# check if P1 is None
					if self.dict["MAIN"][self.op_type][self.side][item]["TOP"]["P1"] == None:
						return (self.side + " " + item + " P1")

					# check if P2 is None				
					if self.dict["MAIN"][self.op_type][self.side][item]["TOP"]["P2"] == None:
						return (self.side + " " + item + " P2")


					# check if P1 is None
					if self.dict["MAIN"][self.op_type][self.side][item]["BOT"]["P1"] == None:
						return (self.side + " " + item + " P1")

					# check if P2 is None				
					if self.dict["MAIN"][self.op_type][self.side][item]["BOT"]["P2"] == None:
						return (self.side + " " + item + " P2")

			return (self.side + " Done")

		return None


 
	def addDict(self, event):

		for item in self.dict["MAIN"][self.op_type][self.side]:
			# get item type 
			item_type = self.dict["MAIN"][self.op_type][self.side][item]["type"]

			# point only has P1
			if item_type == "point":
				# check if P1 is None				
				if self.dict["MAIN"][self.op_type][self.side][item]["P1"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["MAIN"][self.op_type][self.side][item]["P1"] = P
					return True

			# point has P1 and P2, M1 is calculated
			if item_type == "midpoint":

				# check if P1 is None				
				if self.dict["MAIN"][self.op_type][self.side][item]["P1"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["MAIN"][self.op_type][self.side][item]["P1"] = P
					return True


				# check if P2 is None				
				if self.dict["MAIN"][self.op_type][self.side][item]["P2"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["MAIN"][self.op_type][self.side][item]["P2"] = P

					M = self.draw_tools.midpoint(self.dict["MAIN"][self.op_type][self.side][item]["P1"], P)
					self.dict["MAIN"][self.op_type][self.side][item]["M1"] = M
					return True

			# axis has two midpoints
			if item_type == "axis":
				print("axis" + item)
				# axis has a top and a bottom

				# check if P1 is None
				if self.dict["MAIN"][self.op_type][self.side][item]["TOP"]["P1"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["MAIN"][self.op_type][self.side][item]["TOP"]["P1"] = P
					return True

				# check if P2 is None				
				if self.dict["MAIN"][self.op_type][self.side][item]["TOP"]["P2"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["MAIN"][self.op_type][self.side][item]["TOP"]["P2"] = P

					M = self.draw_tools.midpoint(self.dict["MAIN"][self.op_type][self.side][item]["TOP"]["P1"], P)
					self.dict["MAIN"][self.op_type][self.side][item]["TOP"]["M1"] = M
					return True


				# check if P1 is None
				if self.dict["MAIN"][self.op_type][self.side][item]["BOT"]["P1"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["MAIN"][self.op_type][self.side][item]["BOT"]["P1"] = P
					return True

				# check if P2 is None				
				if self.dict["MAIN"][self.op_type][self.side][item]["BOT"]["P2"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["MAIN"][self.op_type][self.side][item]["BOT"]["P2"] = P

					M = self.draw_tools.midpoint(self.dict["MAIN"][self.op_type][self.side][item]["BOT"]["P1"], P)
					self.dict["MAIN"][self.op_type][self.side][item]["BOT"]["M1"] = M
					return True					

		return False				

	




	def drawLines(self):
		for lines in self.dict:
			for points in self.dict[lines]:

				# if type is point cannot draw line
				if self.dict[lines]["type"] != "point":
					# draw line if P1 and P2 have values
					if self.dict[lines]["P1"] != None and self.dict[lines]["P2"] != None:

						p1 = self.dict[lines]["P1"]
						p2 = self.dict[lines]["P2"]

						# if it has a midpoint draw it
						if self.dict[lines]["type"] == "midpoint":
							m1 = self.dict[lines]["M1"]
							tag = "MNSA_"+str(lines)+"_"+str()
							self.draw_tools.create_midpoint_line(p1, p2, m1)
						else:
							self.draw_tools.create_myline(p1, p2)



	def draw(self):
		# for items in self.dict["MAIN"]:

		# loop left and right
		for side in ["LEFT","RIGHT"]:
			for item in self.dict["MAIN"][self.op_type][side]:

				item_type = self.dict["MAIN"][self.op_type][side][item]["type"]
				side_pre = side[0]+"_"

				if item_type == "point":
					if self.dict["MAIN"][self.op_type][side][item]["P1"] != None:
						self.draw_tools.create_mypoint(self.dict["MAIN"][self.op_type][side][item]["P1"], "white", "main")
						self.draw_tools.create_mytext(self.dict["MAIN"][self.op_type][side][item]["P1"], x_offset=80, mytext=(side_pre+item), mytag=self.tag)
						# self, point, color="white", font_size=8, mytext, mytag):


				if item_type == "midpoint":
					if self.dict["MAIN"][self.op_type][side][item]["P1"] != None:
						self.draw_tools.create_mypoint(self.dict["MAIN"][self.op_type][side][item]["P1"], "white", "main")

					if self.dict["MAIN"][self.op_type][side][item]["P2"] != None:
						self.draw_tools.create_mypoint(self.dict["MAIN"][self.op_type][side][item]["P2"], "white", "main")						


					if self.dict["MAIN"][self.op_type][side][item]["P1"] != None and self.dict["MAIN"][self.op_type][side][item]["P2"] != None:
						p1 = self.dict["MAIN"][self.op_type][side][item]["P1"]
						p2 = self.dict["MAIN"][self.op_type][side][item]["P2"]
						m1 = self.dict["MAIN"][self.op_type][side][item]["M1"]
						self.draw_tools.create_midpoint_line(p1, p2, m1, "main")
						self.draw_tools.create_mytext(self.dict["MAIN"][self.op_type][side][item]["P2"], x_offset=80, mytext=(side_pre+item), mytag=self.tag)



				if item_type == "axis":
					if self.dict["MAIN"][self.op_type][side][item]["TOP"]["P1"] != None:
						self.draw_tools.create_mypoint(self.dict["MAIN"][self.op_type][side][item]["TOP"]["P1"], "white", "main")

					if self.dict["MAIN"][self.op_type][side][item]["TOP"]["P2"] != None:
						self.draw_tools.create_mypoint(self.dict["MAIN"][self.op_type][side][item]["TOP"]["P2"], "white", "main")

					if self.dict["MAIN"][self.op_type][side][item]["TOP"]["P1"] != None and self.dict["MAIN"][self.op_type][side][item]["TOP"]["P2"] != None:
						p1 = self.dict["MAIN"][self.op_type][side][item]["TOP"]["P1"]
						p2 = self.dict["MAIN"][self.op_type][side][item]["TOP"]["P2"]
						m1 = self.dict["MAIN"][self.op_type][side][item]["TOP"]["M1"]
						self.draw_tools.create_midpoint_line(p1, p2, m1, "main")

						axis_text = side_pre + item.replace("AXIS_", "") + "_TOP"						
						self.draw_tools.create_mytext(p2, x_offset=80, mytext=axis_text, mytag=self.tag)


					if self.dict["MAIN"][self.op_type][side][item]["BOT"]["P1"] != None:
						self.draw_tools.create_mypoint(self.dict["MAIN"][self.op_type][side][item]["BOT"]["P1"], "white", "main")

					if self.dict["MAIN"][self.op_type][side][item]["BOT"]["P2"] != None:
						self.draw_tools.create_mypoint(self.dict["MAIN"][self.op_type][side][item]["BOT"]["P2"], "white", "main")

					if self.dict["MAIN"][self.op_type][side][item]["BOT"]["P1"] != None and self.dict["MAIN"][self.op_type][side][item]["BOT"]["P2"] != None:
						p1 = self.dict["MAIN"][self.op_type][side][item]["BOT"]["P1"]
						p2 = self.dict["MAIN"][self.op_type][side][item]["BOT"]["P2"]
						m1 = self.dict["MAIN"][self.op_type][side][item]["BOT"]["M1"]
						self.draw_tools.create_midpoint_line(p1, p2, m1, "main")

						axis_text = side_pre + item.replace("AXIS_", "") + "_BOT"
						self.draw_tools.create_mytext(p2, x_offset=80, mytext=axis_text, mytag=self.tag)
					


	def update_canvas(self, draw_tools):
		self.draw_tools = draw_tools


	def update_dict(self, master_dict):
		self.dict = master_dict


	def unset(self):
		# print("unset from "+self.name)
		self.draw_tools.clear_by_tag(self.tag)
		self.side = None