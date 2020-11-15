import json

class MAIN:
	# instance attribute
	def __init__(self, draw_tools, master_dict, controller, op_type):
		self.name = "MAIN"
		self.tag = "main"
		self.menu_label = "MAIN_Menu"
		self.draw_tools = draw_tools
		self.dict = master_dict
		self.controller = controller
		self.side = None
		self.op_type = op_type

		# check if master dictionary has values
		# if not populate the dictionary
		self.checkMasterDict()

		# unique to main
		self.draw_labels = True
		self.draw_hover = True
		self.draw_mech_axis = False
		self.draw_anat_axis = False

		self.drag_label = None

		self.hover_text = None



	def checkMasterDict(self):
		if "MAIN" not in self.dict.keys():
				self.dict["MAIN"] = 	{
										"PRE-OP": 	{
													"LEFT":	{
															"HIP":		{"type":"point","P1":None},
															"FEM_KNEE":	{"type":"point","P1":None},
															"TIB_KNEE":	{"type":"point","P1":None},
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
															"FEM_KNEE":	{"type":"point","P1":None},
															"TIB_KNEE":	{"type":"point","P1":None},
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
															"FEM_KNEE":	{"type":"point","P1":None},
															"TIB_KNEE":	{"type":"point","P1":None},
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
															"FEM_KNEE":	{"type":"point","P1":None},
															"TIB_KNEE":	{"type":"point","P1":None},
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
		# print(self.dict)

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
			# find if P0 hovers are required
			self.mainHoverUsingNextLabel()
			if ret:				
				self.controller.save_json()
				# pass

		self.controller.updateMenuLabel(self.getNextLabel(), self.menu_label)		
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
			self.controller.updateMenuLabel(self.getNextLabel(), self.menu_label)
			self.draw()
			self.regainHover(self.side)
			return # avoid clear,draw,json_save

		if action == "SET-RIGHT":
			self.side = "RIGHT"
			self.controller.updateMenuLabel(self.getNextLabel(), self.menu_label)
			self.draw()
			self.regainHover(self.side)
			return # avoid clear,draw,json_save



		if action == "DEL-LEFT-HIP":
			self.dict["MAIN"][self.op_type]["LEFT"]["HIP"]["P1"] = None
			self.side = "LEFT"

		if action == "DEL-RIGHT-HIP":
			self.dict["MAIN"][self.op_type]["RIGHT"]["HIP"]["P1"] = None
			self.side = "RIGHT"

		if action == "DEL-LEFT-FEM-KNEE":
			self.dict["MAIN"][self.op_type]["LEFT"]["FEM_KNEE"]["P1"] = None
			self.side = "LEFT"

		if action == "DEL-RIGHT-FEM-KNEE":
			self.dict["MAIN"][self.op_type]["RIGHT"]["FEM_KNEE"]["P1"] = None
			self.side = "RIGHT"


		if action == "DEL-LEFT-TIB-KNEE":
			self.dict["MAIN"][self.op_type]["LEFT"]["TIB_KNEE"]["P1"] = None
			self.side = "LEFT"

		if action == "DEL-RIGHT-TIB-KNEE":
			self.dict["MAIN"][self.op_type]["RIGHT"]["TIB_KNEE"]["P1"] = None
			self.side = "RIGHT"

		if action == "DEL-LEFT-ANKLE":
			self.dict["MAIN"][self.op_type]["LEFT"]["ANKLE"]["P1"] = None
			self.dict["MAIN"][self.op_type]["LEFT"]["ANKLE"]["P2"] = None
			self.dict["MAIN"][self.op_type]["LEFT"]["ANKLE"]["M1"] = None
			self.side = "LEFT"

		if action == "DEL-RIGHT-ANKLE":
			self.dict["MAIN"][self.op_type]["RIGHT"]["ANKLE"]["P1"] = None
			self.dict["MAIN"][self.op_type]["RIGHT"]["ANKLE"]["P2"] = None
			self.dict["MAIN"][self.op_type]["RIGHT"]["ANKLE"]["M1"] = None
			self.side = "RIGHT"

		if action == "DEL-LEFT-FEM-TOP":
			self.dict["MAIN"][self.op_type]["LEFT"]["AXIS_FEM"]["TOP"]["P1"] = None
			self.dict["MAIN"][self.op_type]["LEFT"]["AXIS_FEM"]["TOP"]["P2"] = None
			self.dict["MAIN"][self.op_type]["LEFT"]["AXIS_FEM"]["TOP"]["M1"] = None
			self.side = "LEFT"

		if action == "DEL-RIGHT-FEM-TOP":
			self.dict["MAIN"][self.op_type]["RIGHT"]["AXIS_FEM"]["TOP"]["P1"] = None
			self.dict["MAIN"][self.op_type]["RIGHT"]["AXIS_FEM"]["TOP"]["P2"] = None
			self.dict["MAIN"][self.op_type]["RIGHT"]["AXIS_FEM"]["TOP"]["M1"] = None
			self.side = "RIGHT"


		if action == "DEL-LEFT-FEM-BOT":
			self.dict["MAIN"][self.op_type]["LEFT"]["AXIS_FEM"]["BOT"]["P1"] = None
			self.dict["MAIN"][self.op_type]["LEFT"]["AXIS_FEM"]["BOT"]["P2"] = None
			self.dict["MAIN"][self.op_type]["LEFT"]["AXIS_FEM"]["BOT"]["M1"] = None
			self.side = "LEFT"

		if action == "DEL-RIGHT-FEM-BOT":
			self.dict["MAIN"][self.op_type]["RIGHT"]["AXIS_FEM"]["BOT"]["P1"] = None
			self.dict["MAIN"][self.op_type]["RIGHT"]["AXIS_FEM"]["BOT"]["P2"] = None
			self.dict["MAIN"][self.op_type]["RIGHT"]["AXIS_FEM"]["BOT"]["M1"] = None
			self.side = "RIGHT"


		if action == "DEL-LEFT-TIB-TOP":
			self.dict["MAIN"][self.op_type]["LEFT"]["AXIS_TIB"]["TOP"]["P1"] = None
			self.dict["MAIN"][self.op_type]["LEFT"]["AXIS_TIB"]["TOP"]["P2"] = None
			self.dict["MAIN"][self.op_type]["LEFT"]["AXIS_TIB"]["TOP"]["M1"] = None
			self.side = "LEFT"

		if action == "DEL-RIGHT-TIB-TOP":
			self.dict["MAIN"][self.op_type]["RIGHT"]["AXIS_TIB"]["TOP"]["P1"] = None
			self.dict["MAIN"][self.op_type]["RIGHT"]["AXIS_TIB"]["TOP"]["P2"] = None
			self.dict["MAIN"][self.op_type]["RIGHT"]["AXIS_TIB"]["TOP"]["M1"] = None
			self.side = "RIGHT"

		if action == "DEL-LEFT-TIB-BOT":
			self.dict["MAIN"][self.op_type]["LEFT"]["AXIS_TIB"]["BOT"]["P1"] = None
			self.dict["MAIN"][self.op_type]["LEFT"]["AXIS_TIB"]["BOT"]["P2"] = None
			self.dict["MAIN"][self.op_type]["LEFT"]["AXIS_TIB"]["BOT"]["M1"] = None
			self.side = "LEFT"

		if action == "DEL-RIGHT-TIB-BOT":
			self.dict["MAIN"][self.op_type]["RIGHT"]["AXIS_TIB"]["BOT"]["P1"] = None
			self.dict["MAIN"][self.op_type]["RIGHT"]["AXIS_TIB"]["BOT"]["P2"] = None
			self.dict["MAIN"][self.op_type]["RIGHT"]["AXIS_TIB"]["BOT"]["M1"] = None
			self.side = "RIGHT"


		
		self.draw()
		self.regainHover(self.side)
		self.controller.save_json()
		self.controller.updateMenuLabel(self.getNextLabel(), self.menu_label)



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
						return (self.side + " " + item + " TOP P1")

					# check if P2 is None				
					if self.dict["MAIN"][self.op_type][self.side][item]["TOP"]["P2"] == None:
						return (self.side + " " + item + " TOP P2")


					# check if P1 is None
					if self.dict["MAIN"][self.op_type][self.side][item]["BOT"]["P1"] == None:
						return (self.side + " " + item + " BOT P1")

					# check if P2 is None				
					if self.dict["MAIN"][self.op_type][self.side][item]["BOT"]["P2"] == None:
						return (self.side + " " + item + " BOT P2")

			return (self.side + " Done")

		return None


 
	def addDict(self, event):

		for item in self.dict["MAIN"][self.op_type][self.side]:
			# get item type 
			item_type = self.dict["MAIN"][self.op_type][self.side][item]["type"]
			# get real point
			P = self.draw_tools.getRealCoords(event)


			# point only has P1
			if item_type == "point":
				# check if P1 is None				
				if self.dict["MAIN"][self.op_type][self.side][item]["P1"] == None:
					self.dict["MAIN"][self.op_type][self.side][item]["P1"] = P
					return True

			# point has P1 and P2, M1 is calculated
			# ANKLE
			if item_type == "midpoint":

				# check if P1 is None				
				if self.dict["MAIN"][self.op_type][self.side][item]["P1"] == None:					
					self.dict["MAIN"][self.op_type][self.side][item]["P1"] = P
					self.draw_tools.setHoverPointLabel("P1_ANKLE")
					self.draw_tools.setHoverPoint(P)
					self.draw_tools.setHoverBool(True)
					return True


				# check if P2 is None				
				if self.dict["MAIN"][self.op_type][self.side][item]["P2"] == None:					
					self.dict["MAIN"][self.op_type][self.side][item]["P2"] = P
					self.dict["MAIN"][self.op_type][self.side][item]["M1"] = self.draw_tools.midpoint(self.dict["MAIN"][self.op_type][self.side][item]["P1"], P)
					self.draw_tools.setHoverBool(False)
					self.draw_tools.setHoverPointLabel(None)
					return True

			# axis has two midpoints
			if item_type == "axis":
				print("axis" + item)
				# axis has a top and a bottom

				# check if P1 is None
				if self.dict["MAIN"][self.op_type][self.side][item]["TOP"]["P1"] == None:					
					self.dict["MAIN"][self.op_type][self.side][item]["TOP"]["P1"] = P
					self.draw_tools.setHoverPointLabel("P1_TOP_"+item)
					self.draw_tools.setHoverPoint(P)
					self.draw_tools.setHoverBool(True)
					return True

				# check if P2 is None				
				if self.dict["MAIN"][self.op_type][self.side][item]["TOP"]["P2"] == None:					
					self.dict["MAIN"][self.op_type][self.side][item]["TOP"]["P2"] = P
					self.dict["MAIN"][self.op_type][self.side][item]["TOP"]["M1"] = self.draw_tools.midpoint(self.dict["MAIN"][self.op_type][self.side][item]["TOP"]["P1"], P)					 
					self.draw_tools.setHoverBool(False)
					self.draw_tools.setHoverPointLabel(None)
					return True


				# check if P1 is None
				if self.dict["MAIN"][self.op_type][self.side][item]["BOT"]["P1"] == None:					
					self.dict["MAIN"][self.op_type][self.side][item]["BOT"]["P1"] = P
					self.draw_tools.setHoverPointLabel("P1_BOT_"+item)
					self.draw_tools.setHoverPoint(P)
					self.draw_tools.setHoverBool(True)
					return True

				# check if P2 is None				
				if self.dict["MAIN"][self.op_type][self.side][item]["BOT"]["P2"] == None:					
					self.dict["MAIN"][self.op_type][self.side][item]["BOT"]["P2"] = P					
					self.dict["MAIN"][self.op_type][self.side][item]["BOT"]["M1"] = self.draw_tools.midpoint(self.dict["MAIN"][self.op_type][self.side][item]["BOT"]["P1"], P)
					self.draw_tools.setHoverBool(False)
					self.draw_tools.setHoverPointLabel(None)
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
		self.draw_tools.clear_by_tag(self.tag)

		if self.draw_anat_axis:
			print("draw draw_anat_axis")

		if self.draw_mech_axis:
			print("draw draw_mech_axis")

		# loop left and right
		for side in ["LEFT","RIGHT"]:
			for item in self.dict["MAIN"][self.op_type][side]:



				item_type = self.dict["MAIN"][self.op_type][side][item]["type"]
				side_pre = side[0]+"_" # R/L

				# HIP & KNEE
				if item_type == "point":
					if self.dict["MAIN"][self.op_type][side][item]["P1"] != None:

						self.draw_tools.create_mypoint(self.dict["MAIN"][self.op_type][side][item]["P1"], "orange", [self.tag, side, item,"P1"])
						# self.draw_tools.create_mytext(self.dict["MAIN"][self.op_type][side][item]["P1"], x_offset=80, mytext=(side_pre+item), mytag=self.tag)

						if self.draw_labels:
							if item == "TIB_KNEE" and side == "RIGHT":
								self.draw_tools.create_mytext(self.dict["MAIN"][self.op_type][side][item]["P1"],x_offset=-80, mytext=(side_pre+item), mytag=self.tag, color="blue")
							elif item == "FEM_KNEE" and side == "LEFT":
								self.draw_tools.create_mytext(self.dict["MAIN"][self.op_type][side][item]["P1"],x_offset=-80, mytext=(side_pre+item), mytag=self.tag, color="blue")
							else:
								self.draw_tools.create_mytext(self.dict["MAIN"][self.op_type][side][item]["P1"],x_offset=80, mytext=(side_pre+item), mytag=self.tag, color="blue")
						# self, point, color="white", font_size=8, mytext, mytag):

				# ANKLE
				if item_type == "midpoint":
					if self.dict["MAIN"][self.op_type][side][item]["P1"] != None:
						self.draw_tools.create_mypoint(self.dict["MAIN"][self.op_type][side][item]["P1"], "orange", [self.tag, side, "ANKLE", "P1"])

					if self.dict["MAIN"][self.op_type][side][item]["P2"] != None:
						self.draw_tools.create_mypoint(self.dict["MAIN"][self.op_type][side][item]["P2"], "orange", [self.tag, side, "ANKLE", "P2"])


					if self.dict["MAIN"][self.op_type][side][item]["P1"] != None and self.dict["MAIN"][self.op_type][side][item]["P2"] != None:
						p1 = self.dict["MAIN"][self.op_type][side][item]["P1"]
						p2 = self.dict["MAIN"][self.op_type][side][item]["P2"]
						m1 = self.dict["MAIN"][self.op_type][side][item]["M1"]
						self.draw_tools.create_midpoint_line(p1, p2, m1, [self.tag, side, "ANKLE_LINE"])
						if self.draw_labels:
							self.draw_tools.create_mytext(self.dict["MAIN"][self.op_type][side][item]["P2"], x_offset=80, mytext=(side_pre+item), mytag=[self.tag, side, "ANKLE_LINE"], color="blue")


				# AXIS_TIB & AXIS_FEM
				if item_type == "axis":
					
					if self.dict["MAIN"][self.op_type][side][item]["TOP"]["P1"] != None:						
						self.draw_tools.create_mypoint(self.dict["MAIN"][self.op_type][side][item]["TOP"]["P1"], "orange", [self.tag, side, item, "TOP", "P1"])

					if self.dict["MAIN"][self.op_type][side][item]["TOP"]["P2"] != None:
						self.draw_tools.create_mypoint(self.dict["MAIN"][self.op_type][side][item]["TOP"]["P2"], "orange", [self.tag, side, item, "TOP", "P2"])

					if self.dict["MAIN"][self.op_type][side][item]["TOP"]["P1"] != None and self.dict["MAIN"][self.op_type][side][item]["TOP"]["P2"] != None:
						p1 = self.dict["MAIN"][self.op_type][side][item]["TOP"]["P1"]
						p2 = self.dict["MAIN"][self.op_type][side][item]["TOP"]["P2"]
						m1 = self.dict["MAIN"][self.op_type][side][item]["TOP"]["M1"]
						self.draw_tools.create_midpoint_line(p1, p2, m1, [self.tag,side,"AXIS_LINE"])

						axis_text = side_pre + item.replace("AXIS_", "") + "_TOP"
						if self.draw_labels:
							self.draw_tools.create_mytext(p2, x_offset=80, mytext=axis_text, mytag=self.tag, color="blue")


					if self.dict["MAIN"][self.op_type][side][item]["BOT"]["P1"] != None:						
						self.draw_tools.create_mypoint(self.dict["MAIN"][self.op_type][side][item]["BOT"]["P1"], "orange", [self.tag, side, item, "BOT", "P1"])

					if self.dict["MAIN"][self.op_type][side][item]["BOT"]["P2"] != None:						
						self.draw_tools.create_mypoint(self.dict["MAIN"][self.op_type][side][item]["BOT"]["P2"], "orange", [self.tag, side, item, "BOT", "P2"])

					if self.dict["MAIN"][self.op_type][side][item]["BOT"]["P1"] != None and self.dict["MAIN"][self.op_type][side][item]["BOT"]["P2"] != None:
						p1 = self.dict["MAIN"][self.op_type][side][item]["BOT"]["P1"]
						p2 = self.dict["MAIN"][self.op_type][side][item]["BOT"]["P2"]
						m1 = self.dict["MAIN"][self.op_type][side][item]["BOT"]["M1"]
						self.draw_tools.create_midpoint_line(p1, p2, m1, [self.tag,side,"AXIS_LINE"])

						axis_text = side_pre + item.replace("AXIS_", "") + "_BOT"
						if self.draw_labels:
							self.draw_tools.create_mytext(p2, x_offset=80, mytext=axis_text, mytag=self.tag, color="blue")
					


	def update_canvas(self, draw_tools):
		self.draw_tools = draw_tools


	def hover(self, P_mouse, P_stored, hover_label):


		if self.draw_hover:

			side_pre = self.side[0]+"_"

			if(	hover_label == "P0_HIP" or
				hover_label == "P0_FEM_KNEE" or
				hover_label == "P0_TIB_KNEE" or
				hover_label == "P0_ANKLE" or
				hover_label == "P0_AXIS_FEM_TOP" or
				hover_label == "P0_AXIS_FEM_BOT" or
				hover_label == "P0_AXIS_TIB_TOP" or
				hover_label == "P0_AXIS_TIB_BOT"
				):
				self.draw_tools.clear_by_tag("hover_line")
				self.draw_tools.create_mypoint(P_mouse, "red", [self.tag, "hover_line"], hover_point=True)
				if self.draw_labels:
					self.draw_tools.create_mytext(P_mouse,x_offset=80, mytext=(side_pre+self.hover_text), mytag=[self.tag, "hover_line"])



		if(	hover_label == "P1_ANKLE" or
			hover_label == "P1_TOP_AXIS_FEM" or
			hover_label == "P1_TOP_AXIS_TIB" or
			hover_label == "P1_BOT_AXIS_FEM" or
			hover_label == "P1_BOT_AXIS_TIB" 
			):
			self.draw_tools.clear_by_tag("hover_line")
			m = self.draw_tools.midpoint(P_stored, P_mouse)
			self.draw_tools.create_midpoint_line(P_stored, P_mouse, m, "hover_line")


	def mainHoverUsingNextLabel(self):
		label = self.getNextLabel()

		if label == "RIGHT HIP":
			self.side = "RIGHT"
			self.hover_text = "HIP"
			self.draw_tools.setHoverPointLabel("P0_HIP")
			self.draw_tools.setHoverPoint(None)
			self.draw_tools.setHoverBool(True)
		elif label == "LEFT HIP":
			self.side = "LEFT"
			self.hover_text = "HIP"
			self.draw_tools.setHoverPointLabel("P0_HIP")
			self.draw_tools.setHoverPoint(None)
			self.draw_tools.setHoverBool(True)

		elif label == "RIGHT FEM_KNEE":			
			self.side = "RIGHT"
			self.hover_text = "FEM_KNEE"
			self.draw_tools.setHoverPointLabel("P0_FEM_KNEE")
			self.draw_tools.setHoverPoint(None)
			self.draw_tools.setHoverBool(True)
		elif label == "LEFT FEM_KNEE":
			self.side = "LEFT"
			self.hover_text = "FEM_KNEE"
			self.draw_tools.setHoverPointLabel("P0_FEM_KNEE")
			self.draw_tools.setHoverPoint(None)
			self.draw_tools.setHoverBool(True)

		elif label == "RIGHT TIB_KNEE":			
			self.side = "RIGHT"
			self.hover_text = "TIB_KNEE"
			self.draw_tools.setHoverPointLabel("P0_TIB_KNEE")
			self.draw_tools.setHoverPoint(None)
			self.draw_tools.setHoverBool(True)
		elif label == "LEFT TIB_KNEE":
			self.side = "LEFT"
			self.hover_text = "TIB_KNEE"
			self.draw_tools.setHoverPointLabel("P0_TIB_KNEE")
			self.draw_tools.setHoverPoint(None)
			self.draw_tools.setHoverBool(True)

		elif label == "RIGHT ANKLE P1":
			self.side = "RIGHT"
			self.hover_text = "ANKLE_P1"
			self.draw_tools.setHoverPointLabel("P0_ANKLE")
			self.draw_tools.setHoverPoint(None)
			self.draw_tools.setHoverBool(True)
		elif label == "LEFT ANKLE P1":
			self.side = "LEFT"
			self.hover_text = "ANKLE_P1"
			self.draw_tools.setHoverPointLabel("P0_ANKLE")
			self.draw_tools.setHoverPoint(None)
			self.draw_tools.setHoverBool(True)

		
		elif label == "RIGHT AXIS_FEM TOP P1":
			self.side = "RIGHT"
			self.hover_text = "AXIS_FEM_TOP_P1"
			self.draw_tools.setHoverPointLabel("P0_AXIS_FEM_TOP")
			self.draw_tools.setHoverPoint(None)
			self.draw_tools.setHoverBool(True)
		elif label == "LEFT AXIS_FEM TOP P1":
			self.side = "LEFT"
			self.hover_text = "AXIS_FEM_TOP_P1"
			self.draw_tools.setHoverPointLabel("P0_AXIS_FEM_TOP")
			self.draw_tools.setHoverPoint(None)
			self.draw_tools.setHoverBool(True)

		elif label == "RIGHT AXIS_FEM BOT P1":
			self.side = "RIGHT"
			self.hover_text = "AXIS_FEM_BOT_P1"
			self.draw_tools.setHoverPointLabel("P0_AXIS_FEM_BOT")
			self.draw_tools.setHoverPoint(None)
			self.draw_tools.setHoverBool(True)
		elif label == "LEFT AXIS_FEM BOT P1":
			self.side = "LEFT"
			self.hover_text = "AXIS_FEM_BOT_P1"
			self.draw_tools.setHoverPointLabel("P0_AXIS_FEM_BOT")
			self.draw_tools.setHoverPoint(None)
			self.draw_tools.setHoverBool(True)

		
		elif label == "RIGHT AXIS_TIB TOP P1":
			self.side = "RIGHT"
			self.hover_text = "AXIS_TIB_TOP_P1"
			self.draw_tools.setHoverPointLabel("P0_AXIS_TIB_TOP")
			self.draw_tools.setHoverPoint(None)
			self.draw_tools.setHoverBool(True)
		elif label == "LEFT AXIS_TIB TOP P1":
			self.side = "LEFT"
			self.hover_text = "AXIS_TIB_TOP_P1"
			self.draw_tools.setHoverPointLabel("P0_AXIS_TIB_TOP")
			self.draw_tools.setHoverPoint(None)
			self.draw_tools.setHoverBool(True)
		
		elif label == "RIGHT AXIS_TIB BOT P1":
			self.side = "RIGHT"
			self.hover_text = "AXIS_TIB_BOT_P1"
			self.draw_tools.setHoverPointLabel("P0_AXIS_TIB_BOT")
			self.draw_tools.setHoverPoint(None)
			self.draw_tools.setHoverBool(True)
		elif label == "LEFT AXIS_TIB BOT P1":
			self.side = "LEFT"
			self.hover_text = "AXIS_TIB_BOT_P1"
			self.draw_tools.setHoverPointLabel("P0_AXIS_TIB_BOT")
			self.draw_tools.setHoverPoint(None)
			self.draw_tools.setHoverBool(True)

		elif label == "LEFT Done" or label == "RIGHT Done":
			self.draw_tools.setHoverPointLabel("")
			self.draw_tools.setHoverPoint(None)
			self.draw_tools.setHoverBool(False)

		# else:
		# 	self.draw_tools.setHoverPointLabel(None)
		# 	self.draw_tools.setHoverPoint(None)
		# 	self.draw_tools.setHoverBool(False)





	def regainHover(self, side):
		p1_ankle = self.dict["MAIN"][self.op_type][side]["ANKLE"]["P1"]
		p2_ankle = self.dict["MAIN"][self.op_type][side]["ANKLE"]["P2"]

		p1_axis_fem_top = self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["TOP"]["P1"]
		p2_axis_fem_top = self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["TOP"]["P2"]
		p1_axis_fem_bot = self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["BOT"]["P1"]
		p2_axis_fem_bot = self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["BOT"]["P2"]

		p1_axis_tib_top = self.dict["MAIN"][self.op_type][side]["AXIS_TIB"]["TOP"]["P1"]
		p2_axis_tib_top = self.dict["MAIN"][self.op_type][side]["AXIS_TIB"]["TOP"]["P2"]
		p1_axis_tib_bot = self.dict["MAIN"][self.op_type][side]["AXIS_TIB"]["BOT"]["P1"]
		p2_axis_tib_bot = self.dict["MAIN"][self.op_type][side]["AXIS_TIB"]["BOT"]["P2"]

		# find if P0 hovers are required
		self.mainHoverUsingNextLabel()

		if p1_ankle == None and p2_ankle != None:
			self.draw_tools.setHoverPointLabel("P1_ANKLE")
			self.draw_tools.setHoverPoint(p2_ankle)
			self.draw_tools.setHoverBool(True)

		# elif p1_ankle != None and p2_ankle == None:
		# 	self.draw_tools.setHoverPointLabel("P1_ANKLE")
		# 	self.draw_tools.setHoverPoint(P)
		# 	self.draw_tools.setHoverBool(True)

		elif p1_axis_fem_top != None and p2_axis_fem_top == None:						
			self.draw_tools.setHoverPointLabel("P1_TOP_AXIS_FEM")
			self.draw_tools.setHoverPoint(p1_axis_fem_top)
			self.draw_tools.setHoverBool(True)
		# elif p1_axis_fem_top != None and p2_axis_fem_top == None:

		elif p1_axis_fem_bot != None and p2_axis_fem_bot == None:
			self.draw_tools.setHoverPointLabel("P1_BOT_AXIS_FEM")
			self.draw_tools.setHoverPoint(p1_axis_fem_bot)
			self.draw_tools.setHoverBool(True)
		# elif p1_axis_fem_bot != None and p2_axis_fem_bot == None:

		elif p1_axis_tib_top != None and p2_axis_tib_top == None:
			self.draw_tools.setHoverPointLabel("P1_TOP_AXIS_TIB")
			self.draw_tools.setHoverPoint(p1_axis_tib_top)
			self.draw_tools.setHoverBool(True)
		# elif p1_axis_tib_top != None and p2_axis_tib_top == None:

		elif p1_axis_tib_bot != None and p2_axis_tib_bot == None:
			self.draw_tools.setHoverPointLabel("P1_BOT_AXIS_TIB")
			self.draw_tools.setHoverPoint(p1_axis_tib_bot)
			self.draw_tools.setHoverBool(True)
		# elif p1_axis_tib_bot != None and p2_axis_tib_bot == None:

	def escapeObjFunc(self):
		self.side = None
		self.draw_tools.setHoverPointLabel(None)
		self.draw_tools.setHoverBool(False)	

	def update_dict(self, master_dict):
		self.dict = master_dict


	def updatePosition(self, tag_list, point):

		'''
		# find side
		# find P1 P2
		["HIP"]["P1"]
		["KNEE"]["P1"]

		# new M1
			["ANKLE"]["P1"]
			# find TOP / BOT
			["AXIS_FEM"]["TOP"]["P1"]
			["AXIS_FEM"]["BOT"]["P1"]			
			["AXIS_TIB"]["TOP"]["P1"]
			["AXIS_TIB"]["BOT"]["P1"]
		'''
		# find side
		if "LEFT" in tag_list:
			side = "LEFT"
		elif "RIGHT" in tag_list:
			side = "RIGHT"

		# find P1 P2
		if "P1" in tag_list:
			P = "P1"
			other_P = "P2"
		elif "P2" in tag_list:
			P = "P2"
			other_P = "P1"

		if "HIP" in tag_list:
			self.dict["MAIN"][self.op_type][side]["HIP"]["P1"] = point
			return

		if "KNEE" in tag_list:
			self.dict["MAIN"][self.op_type][side]["KNEE"]["P1"] = point
			return

		if "ANKLE" in tag_list:
			pre = self.dict["MAIN"][self.op_type][side]["ANKLE"]

			pre[P] = point
			M = self.draw_tools.midpoint(pre[other_P], point)
			pre["M1"] = M
			return


		# find TOP BOT
		if "TOP" in tag_list:
			topbot = "TOP"
		elif "BOT" in tag_list:
			topbot = "BOT"


		if "AXIS_FEM" in tag_list:

			pre = self.dict["MAIN"][self.op_type][side]["AXIS_FEM"][topbot]

			pre[P] = point
			M = self.draw_tools.midpoint(pre[other_P], point)
			pre["M1"] = M
			return

		if "AXIS_TIB" in tag_list:

			pre = self.dict["MAIN"][self.op_type][side]["AXIS_TIB"][topbot]

			pre[P] = point
			M = self.draw_tools.midpoint(pre[other_P], point)
			pre["M1"] = M
			return



	def drag_start(self, tags):
		tags.remove('token')
		tags.remove('current')
		tags.remove(self.tag)
		print(tags)
		

		side = ""
		item = ""
		topbot = ""

		# find side
		if "LEFT" in tags:
			side = "LEFT"
		elif "RIGHT" in tags:
			side = "RIGHT"


		# find side
		if "TOP" in tags:
			topbot = "TOP"
		elif "BOT" in tags:
			topbot = "BOT"


		if "HIP" in tags:
			self.drag_point = None
			self.drag_label = "HIP"
			self.drag_side 	= side

		elif "FEM_KNEE" in tags:
			self.drag_point = None
			self.drag_label = "FEM_KNEE"
			self.drag_side 	= side

		elif "TIB_KNEE" in tags:
			self.drag_point = None
			self.drag_label = "TIB_KNEE"
			self.drag_side 	= side


		elif "ANKLE" in tags:
			if "P1" in tags:
				self.drag_point = self.dict["MAIN"][self.op_type][side]["ANKLE"]["P2"]
				self.drag_label = "P1_ANKLE"
				self.drag_side 	= side
			elif "P2" in tags:
				self.drag_point = self.dict["MAIN"][self.op_type][side]["ANKLE"]["P1"]
				self.drag_label = "P2_ANKLE"
				self.drag_side 	= side


		elif "AXIS_FEM" in tags:
			if "P1" in tags:
				self.drag_point = self.dict["MAIN"][self.op_type][side]["AXIS_FEM"][topbot]["P2"]
				self.drag_label = "P1_AXIS_FEM_"+topbot
				self.drag_side 	= side
			elif "P2" in tags:
				self.drag_point = self.dict["MAIN"][self.op_type][side]["AXIS_FEM"][topbot]["P1"]
				self.drag_label = "P2_AXIS_FEM_"+topbot
				self.drag_side 	= side

		elif "AXIS_TIB" in tags:
			if "P1" in tags:
				self.drag_point = self.dict["MAIN"][self.op_type][side]["AXIS_TIB"][topbot]["P2"]
				self.drag_label = "P1_AXIS_TIB_"+topbot
				self.drag_side 	= side
			elif "P2" in tags:
				self.drag_point = self.dict["MAIN"][self.op_type][side]["AXIS_TIB"][topbot]["P1"]
				self.drag_label = "P2_AXIS_TIB_"+topbot
				self.drag_side 	= side

	def drag(self, P_mouse):


		# self.drag_label = "HIP"
		# self.drag_label = "KNEE"
		if self.drag_label == "P1_ANKLE" and self.drag_point != None or self.drag_label == "P2_ANKLE" and self.drag_point != None:
			self.draw_tools.clear_by_tag("ANKLE_LINE")
			self.draw_tools.clear_by_tag("drag_line")
			m = self.draw_tools.midpoint(self.drag_point, P_mouse)
			self.draw_tools.create_midpoint_line(self.drag_point, P_mouse, m, "drag_line")


		if (self.drag_label == "P1_AXIS_FEM_TOP" or self.drag_label == "P2_AXIS_FEM_TOP" or self.drag_label == "P1_AXIS_FEM_BOT" or self.drag_label == "P2_AXIS_FEM_BOT" or
			self.drag_label == "P1_AXIS_TIB_TOP" or self.drag_label == "P2_AXIS_TIB_TOP" or self.drag_label == "P1_AXIS_TIB_BOT" or self.drag_label == "P2_AXIS_TIB_BOT"):
			self.draw_tools.clear_by_tag("AXIS_LINE")
			self.draw_tools.clear_by_tag("drag_line")
			m = self.draw_tools.midpoint(self.drag_point, P_mouse)
			self.draw_tools.create_midpoint_line(self.drag_point, P_mouse, m, "drag_line")


		# self.drag_label = "P2_AXIS_FEM_"+topbot
		# self.drag_label = "P1_AXIS_TIB_"+topbot
		# self.drag_label = "P2_AXIS_TIB_"+topbot
		# pass

	def drag_stop(self, P_mouse):

		self.draw_tools.clear_by_tag("drag_line")

		if self.drag_label == "HIP":
			self.dict["MAIN"][self.op_type][self.drag_side]["HIP"]["P1"] = P_mouse
			
		elif self.drag_label == "FEM_KNEE":
			self.dict["MAIN"][self.op_type][self.drag_side]["FEM_KNEE"]["P1"] = P_mouse

		elif self.drag_label == "TIB_KNEE":
			self.dict["MAIN"][self.op_type][self.drag_side]["TIB_KNEE"]["P1"] = P_mouse


		elif self.drag_label == "P1_ANKLE":
			self.dict["MAIN"][self.op_type][self.drag_side]["ANKLE"]["P1"] = P_mouse
			self.dict["MAIN"][self.op_type][self.drag_side]["ANKLE"]["M1"] = self.draw_tools.midpoint(self.drag_point, P_mouse)
		elif self.drag_label == "P2_ANKLE":
			self.dict["MAIN"][self.op_type][self.drag_side]["ANKLE"]["P2"] = P_mouse
			self.dict["MAIN"][self.op_type][self.drag_side]["ANKLE"]["M1"] = self.draw_tools.midpoint(self.drag_point, P_mouse)


		elif self.drag_label == "P1_AXIS_FEM_TOP":
			self.dict["MAIN"][self.op_type][self.drag_side]["AXIS_FEM"]["TOP"]["P1"] = P_mouse
			self.dict["MAIN"][self.op_type][self.drag_side]["AXIS_FEM"]["TOP"]["M1"] = self.draw_tools.midpoint(self.drag_point, P_mouse)
		elif self.drag_label == "P2_AXIS_FEM_TOP":
			self.dict["MAIN"][self.op_type][self.drag_side]["AXIS_FEM"]["TOP"]["P2"] = P_mouse
			self.dict["MAIN"][self.op_type][self.drag_side]["AXIS_FEM"]["TOP"]["M1"] = self.draw_tools.midpoint(self.drag_point, P_mouse)


		elif self.drag_label == "P1_AXIS_FEM_BOT":
			self.dict["MAIN"][self.op_type][self.drag_side]["AXIS_FEM"]["BOT"]["P1"] = P_mouse
			self.dict["MAIN"][self.op_type][self.drag_side]["AXIS_FEM"]["BOT"]["M1"] = self.draw_tools.midpoint(self.drag_point, P_mouse)
		elif self.drag_label == "P2_AXIS_FEM_BOT":
			self.dict["MAIN"][self.op_type][self.drag_side]["AXIS_FEM"]["BOT"]["P2"] = P_mouse
			self.dict["MAIN"][self.op_type][self.drag_side]["AXIS_FEM"]["BOT"]["M1"] = self.draw_tools.midpoint(self.drag_point, P_mouse)


		elif self.drag_label == "P1_AXIS_TIB_TOP":
			self.dict["MAIN"][self.op_type][self.drag_side]["AXIS_TIB"]["TOP"]["P1"] = P_mouse
			self.dict["MAIN"][self.op_type][self.drag_side]["AXIS_TIB"]["TOP"]["M1"] = self.draw_tools.midpoint(self.drag_point, P_mouse)
		elif self.drag_label == "P2_AXIS_TIB_TOP":
			self.dict["MAIN"][self.op_type][self.drag_side]["AXIS_TIB"]["TOP"]["P2"] = P_mouse
			self.dict["MAIN"][self.op_type][self.drag_side]["AXIS_TIB"]["TOP"]["M1"] = self.draw_tools.midpoint(self.drag_point, P_mouse)


		elif self.drag_label == "P1_AXIS_TIB_BOT":
			self.dict["MAIN"][self.op_type][self.drag_side]["AXIS_TIB"]["BOT"]["P1"] = P_mouse
			self.dict["MAIN"][self.op_type][self.drag_side]["AXIS_TIB"]["BOT"]["M1"] = self.draw_tools.midpoint(self.drag_point, P_mouse)
		elif self.drag_label == "P2_AXIS_TIB_BOT":
			self.dict["MAIN"][self.op_type][self.drag_side]["AXIS_TIB"]["BOT"]["P2"] = P_mouse
			self.dict["MAIN"][self.op_type][self.drag_side]["AXIS_TIB"]["BOT"]["M1"] = self.draw_tools.midpoint(self.drag_point, P_mouse)

		self.controller.save_json()
		self.draw()


	def unset(self):
		# print("unset from "+self.name)
		self.draw_tools.clear_by_tag(self.tag)
		self.side = None


	def checkbox_click(self,action, val):

		print('checkbox {} val{}'.format(action,val.get()))

		if action == "TOGGLE_MECH_AXIS":
			if val.get() == 0:
				self.draw_mech_axis = False
			elif val.get() == 1:
				self.draw_mech_axis = True
			self.draw()

		if action == "TOGGLE_ANAT_AXIS":
			if val.get() == 0:
				self.draw_anat_axis = False
			elif val.get() == 1:
				self.draw_anat_axis = True
			self.draw()

		if action == "TOGGLE_LABEL":
			if val.get() == 0:
				self.draw_labels = False
			elif val.get() == 1:
				self.draw_labels = True
			self.draw()

		if action == "TOGGLE_HOVER":
			if val.get() == 0:
				self.draw_hover = False
			elif val.get() == 1:
				self.draw_hover = True
			self.draw()

