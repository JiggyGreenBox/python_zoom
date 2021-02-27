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
		self.draw_dissapear_mode = True
		self.draw_fem_j_var = True
		self.draw_tib_j_var = True
		self.draw_kjlo_line = True
		self.draw_mad_line = True
		self.draw_tib_knee = True
		self.draw_fem_knee = True
		self.draw_mech_axis = False
		self.draw_anat_axis = False

		self.drag_label = None
		self.point_size = None

		self.hover_text = None			

		self.curr_display_item = None


	def checkMasterDict(self):
		if "MAIN" not in self.dict.keys():
				self.dict["MAIN"] = 	{
										"PRE-OP": 	{
													"LEFT":	{
															"HIP":				{"type":"point", "P1":None},
															"NECK_AXIS":		{"type":"midpoint","P1":None, "P2":None, "M1":None},
															"AXIS_FEM":			{
																					"type":	"axis",
																					"TOP":	{"type":"midpoint", "P1":None, "P2":None, "M1":None},
																					"BOT":	{"type":"midpoint", "P1":None, "P2":None, "M1":None}
																				},
															"FEM_KNEE":			{"type":"point", "P1":None},
															"TIB_KNEE":			{"type":"point", "P1":None},
															"FEM_JOINT_LINE":	{"type":"line", "P1":None, "P2":None},
															"TIB_JOINT_LINE":	{"type":"line", "P1":None, "P2":None},
															"AXIS_TIB":			{
																					"type":	"axis",
																					"TOP":	{"type":"midpoint", "P1":None, "P2":None, "M1":None},
																					"BOT":	{"type":"midpoint", "P1":None, "P2":None, "M1":None}
																				},
															"ANKLE":			{"type":"midpoint","P1":None,"P2":None, "M1":None},
															"DIST_FEM":			{"type":"midpoint","P1":None,"P2":None, "M1":None},
															"KJLO_LINE":		{"type":"line","P1":None,"P2":None},
															"MAD_LINE":			{"type":"line","P1":None,"P2":None}
															},
													"RIGHT":{
															"HIP":				{"type":"point","P1":None},
															"NECK_AXIS":		{"type":"midpoint","P1":None,"P2":None, "M1":None},
															"AXIS_FEM":			{
																					"type":	"axis",		
																					"TOP":	{"type":"midpoint","P1":None,"P2":None, "M1":None},
																					"BOT":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
																				},
															"FEM_KNEE":			{"type":"point","P1":None},
															"TIB_KNEE":			{"type":"point","P1":None},
															"FEM_JOINT_LINE":			{"type":"line","P1":None,"P2":None},
															"TIB_JOINT_LINE":			{"type":"line","P1":None,"P2":None},
															"AXIS_TIB":			{
																					"type":	"axis",
																					"TOP":	{"type":"midpoint","P1":None,"P2":None, "M1":None},
																					"BOT":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
																				},
															"ANKLE":			{"type":"midpoint","P1":None,"P2":None, "M1":None},
															"DIST_FEM":			{"type":"midpoint","P1":None,"P2":None, "M1":None},
															"KJLO_LINE":		{"type":"line","P1":None,"P2":None},
															"MAD_LINE":			{"type":"line","P1":None,"P2":None}
															}
												},
										"POST-OP": 	{
													"LEFT":	{
															"HIP":				{"type":"point","P1":None},
															"NECK_AXIS":		{"type":"midpoint","P1":None,"P2":None, "M1":None},
															"AXIS_FEM":			{
																					"type":	"axis",
																					"TOP":	{"type":"midpoint","P1":None,"P2":None, "M1":None},
																					"BOT":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
																				},
															"FEM_KNEE":			{"type":"point","P1":None},
															"TIB_KNEE":			{"type":"point","P1":None},
															"FEM_JOINT_LINE":	{"type":"line","P1":None,"P2":None},
															"TIB_JOINT_LINE":	{"type":"line","P1":None,"P2":None},		
															"AXIS_TIB":			{
																					"type":	"axis",
																					"TOP":	{"type":"midpoint","P1":None,"P2":None, "M1":None},
																					"BOT":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
																				},
															"ANKLE":			{"type":"midpoint","P1":None,"P2":None, "M1":None},
															"DIST_FEM":			{"type":"midpoint","P1":None,"P2":None, "M1":None},
															"KJLO_LINE":		{"type":"line","P1":None,"P2":None},
															"MAD_LINE":			{"type":"line","P1":None,"P2":None}
															},
													"RIGHT":{
															"HIP":				{"type":"point","P1":None},
															"NECK_AXIS":		{"type":"midpoint","P1":None,"P2":None, "M1":None},
															"AXIS_FEM":			{
																					"type":	"axis",
																					"TOP":	{"type":"midpoint","P1":None,"P2":None, "M1":None},
																					"BOT":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
																				},
															"FEM_KNEE":			{"type":"point","P1":None},
															"TIB_KNEE":			{"type":"point","P1":None},
															"FEM_JOINT_LINE":	{"type":"line","P1":None,"P2":None},
															"TIB_JOINT_LINE":	{"type":"line","P1":None,"P2":None},
															"AXIS_TIB":			{
																					"type":	"axis",
																					"TOP":	{"type":"midpoint","P1":None,"P2":None, "M1":None},
																					"BOT":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
																				},
															"ANKLE":			{"type":"midpoint","P1":None,"P2":None, "M1":None},
															"DIST_FEM":			{"type":"midpoint","P1":None,"P2":None, "M1":None},
															"KJLO_LINE":		{"type":"line","P1":None,"P2":None},
															"MAD_LINE":			{"type":"line","P1":None,"P2":None}
															}
													}
												
										}


	def click(self, event):
		print("click from "+self.name)

		# self.controller.calculateExcel()

		if self.side == None:
			print("please choose side")
			self.controller.warningBox("Please select a Side")			
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
			self.deleteExcelValues(["HKA", "MNSA", "VCA", "mLDFA"], self.side)

		if action == "DEL-RIGHT-HIP":
			self.dict["MAIN"][self.op_type]["RIGHT"]["HIP"]["P1"] = None
			self.side = "RIGHT"
			self.deleteExcelValues(["HKA", "MNSA", "VCA", "mLDFA"], self.side)


		if action == "DEL-LEFT-NECK-AXIS":			
			self.dict["MAIN"][self.op_type]["LEFT"]["NECK_AXIS"]["P1"] = None
			self.dict["MAIN"][self.op_type]["LEFT"]["NECK_AXIS"]["P2"] = None
			self.dict["MAIN"][self.op_type]["LEFT"]["NECK_AXIS"]["M1"] = None
			self.side = "LEFT"
			# self.deleteExcelValues(["HKA", "MNSA", "VCA", "mLDFA"], self.side)

		if action == "DEL-RIGHT-NECK-AXIS":			
			self.dict["MAIN"][self.op_type]["RIGHT"]["NECK_AXIS"]["P1"] = None
			self.dict["MAIN"][self.op_type]["RIGHT"]["NECK_AXIS"]["P2"] = None
			self.dict["MAIN"][self.op_type]["RIGHT"]["NECK_AXIS"]["M1"] = None
			self.side = "RIGHT"
			# self.deleteExcelValues(["HKA", "MNSA", "VCA", "mLDFA"], self.side)


		if action == "DEL-LEFT-DIST-FEM":			
			self.dict["MAIN"][self.op_type]["LEFT"]["DIST_FEM"]["P1"] = None
			self.dict["MAIN"][self.op_type]["LEFT"]["DIST_FEM"]["P2"] = None
			self.dict["MAIN"][self.op_type]["LEFT"]["DIST_FEM"]["M1"] = None
			self.side = "LEFT"
			# self.deleteExcelValues(["HKA", "MNSA", "VCA", "mLDFA"], self.side)

		if action == "DEL-RIGHT-DIST-FEM":			
			self.dict["MAIN"][self.op_type]["RIGHT"]["DIST_FEM"]["P1"] = None
			self.dict["MAIN"][self.op_type]["RIGHT"]["DIST_FEM"]["P2"] = None
			self.dict["MAIN"][self.op_type]["RIGHT"]["DIST_FEM"]["M1"] = None
			self.side = "RIGHT"
			# self.deleteExcelValues(["HKA", "MNSA", "VCA", "mLDFA"], self.side)

			

		if action == "DEL-LEFT-FEM-KNEE":
			self.dict["MAIN"][self.op_type]["LEFT"]["FEM_KNEE"]["P1"] = None
			self.side = "LEFT"
			self.deleteExcelValues(["HKA", "VCA", "mLDFA"], self.side)

		if action == "DEL-RIGHT-FEM-KNEE":
			self.dict["MAIN"][self.op_type]["RIGHT"]["FEM_KNEE"]["P1"] = None
			self.side = "RIGHT"
			self.deleteExcelValues(["HKA", "VCA", "mLDFA"], self.side)


		if action == "DEL-LEFT-TIB-KNEE":
			self.dict["MAIN"][self.op_type]["LEFT"]["TIB_KNEE"]["P1"] = None
			self.side = "LEFT"
			self.deleteExcelValues(["HKA", "TAMD", "MPTA"], self.side)

		if action == "DEL-RIGHT-TIB-KNEE":
			self.dict["MAIN"][self.op_type]["RIGHT"]["TIB_KNEE"]["P1"] = None
			self.side = "RIGHT"
			self.deleteExcelValues(["HKA", "TAMD", "MPTA"], self.side)

		if action == "DEL-LEFT-ANKLE":
			self.dict["MAIN"][self.op_type]["LEFT"]["ANKLE"]["P1"] = None
			self.dict["MAIN"][self.op_type]["LEFT"]["ANKLE"]["P2"] = None
			self.dict["MAIN"][self.op_type]["LEFT"]["ANKLE"]["M1"] = None
			self.side = "LEFT"
			self.deleteExcelValues(["HKA", "TAMD", "MPTA", "KJLO", "KAOL"], self.side)

		if action == "DEL-RIGHT-ANKLE":
			self.dict["MAIN"][self.op_type]["RIGHT"]["ANKLE"]["P1"] = None
			self.dict["MAIN"][self.op_type]["RIGHT"]["ANKLE"]["P2"] = None
			self.dict["MAIN"][self.op_type]["RIGHT"]["ANKLE"]["M1"] = None
			self.side = "RIGHT"
			self.deleteExcelValues(["HKA", "TAMD", "MPTA", "KJLO", "KAOL"], self.side)

		if action == "DEL-LEFT-FEM-TOP":
			self.dict["MAIN"][self.op_type]["LEFT"]["AXIS_FEM"]["TOP"]["P1"] = None
			self.dict["MAIN"][self.op_type]["LEFT"]["AXIS_FEM"]["TOP"]["P2"] = None
			self.dict["MAIN"][self.op_type]["LEFT"]["AXIS_FEM"]["TOP"]["M1"] = None
			self.side = "LEFT"
			self.deleteExcelValues(["MNSA", "aFTA", "aLDFA"], self.side)

		if action == "DEL-RIGHT-FEM-TOP":
			self.dict["MAIN"][self.op_type]["RIGHT"]["AXIS_FEM"]["TOP"]["P1"] = None
			self.dict["MAIN"][self.op_type]["RIGHT"]["AXIS_FEM"]["TOP"]["P2"] = None
			self.dict["MAIN"][self.op_type]["RIGHT"]["AXIS_FEM"]["TOP"]["M1"] = None
			self.side = "RIGHT"
			self.deleteExcelValues(["MNSA", "aFTA", "aLDFA"], self.side)


		if action == "DEL-LEFT-FEM-BOT":
			self.dict["MAIN"][self.op_type]["LEFT"]["AXIS_FEM"]["BOT"]["P1"] = None
			self.dict["MAIN"][self.op_type]["LEFT"]["AXIS_FEM"]["BOT"]["P2"] = None
			self.dict["MAIN"][self.op_type]["LEFT"]["AXIS_FEM"]["BOT"]["M1"] = None
			self.side = "LEFT"
			self.deleteExcelValues(["MNSA", "aFTA", "aLDFA"], self.side)

		if action == "DEL-RIGHT-FEM-BOT":
			self.dict["MAIN"][self.op_type]["RIGHT"]["AXIS_FEM"]["BOT"]["P1"] = None
			self.dict["MAIN"][self.op_type]["RIGHT"]["AXIS_FEM"]["BOT"]["P2"] = None
			self.dict["MAIN"][self.op_type]["RIGHT"]["AXIS_FEM"]["BOT"]["M1"] = None
			self.side = "RIGHT"
			self.deleteExcelValues(["MNSA", "aFTA", "aLDFA"], self.side)


		if action == "DEL-LEFT-TIB-TOP":
			self.dict["MAIN"][self.op_type]["LEFT"]["AXIS_TIB"]["TOP"]["P1"] = None
			self.dict["MAIN"][self.op_type]["LEFT"]["AXIS_TIB"]["TOP"]["P2"] = None
			self.dict["MAIN"][self.op_type]["LEFT"]["AXIS_TIB"]["TOP"]["M1"] = None
			self.side = "LEFT"
			self.deleteExcelValues(["aFTA", "TAMD"], self.side)

		if action == "DEL-RIGHT-TIB-TOP":
			self.dict["MAIN"][self.op_type]["RIGHT"]["AXIS_TIB"]["TOP"]["P1"] = None
			self.dict["MAIN"][self.op_type]["RIGHT"]["AXIS_TIB"]["TOP"]["P2"] = None
			self.dict["MAIN"][self.op_type]["RIGHT"]["AXIS_TIB"]["TOP"]["M1"] = None
			self.side = "RIGHT"
			self.deleteExcelValues(["aFTA", "TAMD"], self.side)

		if action == "DEL-LEFT-TIB-BOT":
			self.dict["MAIN"][self.op_type]["LEFT"]["AXIS_TIB"]["BOT"]["P1"] = None
			self.dict["MAIN"][self.op_type]["LEFT"]["AXIS_TIB"]["BOT"]["P2"] = None
			self.dict["MAIN"][self.op_type]["LEFT"]["AXIS_TIB"]["BOT"]["M1"] = None
			self.side = "LEFT"
			self.deleteExcelValues(["aFTA", "TAMD"], self.side)

		if action == "DEL-RIGHT-TIB-BOT":
			self.dict["MAIN"][self.op_type]["RIGHT"]["AXIS_TIB"]["BOT"]["P1"] = None
			self.dict["MAIN"][self.op_type]["RIGHT"]["AXIS_TIB"]["BOT"]["P2"] = None
			self.dict["MAIN"][self.op_type]["RIGHT"]["AXIS_TIB"]["BOT"]["M1"] = None
			self.side = "RIGHT"
			self.deleteExcelValues(["aFTA", "TAMD"], self.side)



		if action == "DEL-RIGHT-FEM-JOINT-LINE":
			self.dict["MAIN"][self.op_type]["RIGHT"]["FEM_JOINT_LINE"]["P1"] = None
			self.dict["MAIN"][self.op_type]["RIGHT"]["FEM_JOINT_LINE"]["P2"] = None
			self.side = "RIGHT"
		if action == "DEL-LEFT-FEM-JOINT-LINE":
			self.dict["MAIN"][self.op_type]["LEFT"]["FEM_JOINT_LINE"]["P1"] = None
			self.dict["MAIN"][self.op_type]["LEFT"]["FEM_JOINT_LINE"]["P2"] = None
			self.side = "LEFT"


		if action == "DEL-RIGHT-TIB-JOINT-LINE":
			self.dict["MAIN"][self.op_type]["RIGHT"]["TIB_JOINT_LINE"]["P1"] = None
			self.dict["MAIN"][self.op_type]["RIGHT"]["TIB_JOINT_LINE"]["P2"] = None
			self.side = "RIGHT"
		if action == "DEL-LEFT-TIB-JOINT-LINE":
			self.dict["MAIN"][self.op_type]["LEFT"]["TIB_JOINT_LINE"]["P1"] = None
			self.dict["MAIN"][self.op_type]["LEFT"]["TIB_JOINT_LINE"]["P2"] = None
			self.side = "LEFT"




		if action == "DEL-RIGHT-KJLO-LINE":
			self.dict["MAIN"][self.op_type]["RIGHT"]["KJLO_LINE"]["P1"] = None
			self.dict["MAIN"][self.op_type]["RIGHT"]["KJLO_LINE"]["P2"] = None
			self.side = "RIGHT"
		if action == "DEL-LEFT-KJLO-LINE":
			self.dict["MAIN"][self.op_type]["LEFT"]["KJLO_LINE"]["P1"] = None
			self.dict["MAIN"][self.op_type]["LEFT"]["KJLO_LINE"]["P2"] = None
			self.side = "LEFT"


		if action == "DEL-RIGHT-MAD-LINE":
			self.dict["MAIN"][self.op_type]["RIGHT"]["MAD_LINE"]["P1"] = None
			self.dict["MAIN"][self.op_type]["RIGHT"]["MAD_LINE"]["P2"] = None
			self.side = "RIGHT"
		if action == "DEL-LEFT-MAD-LINE":
			self.dict["MAIN"][self.op_type]["LEFT"]["MAD_LINE"]["P1"] = None
			self.dict["MAIN"][self.op_type]["LEFT"]["MAD_LINE"]["P2"] = None
			self.side = "LEFT"



		
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

				# fem/tib joint line
				if item_type == "line":
					# check if P1 is None
					if self.dict["MAIN"][self.op_type][self.side][item]["P1"] == None:
						return (self.side + " " + item + " P1")
					# check if P2 is None
					if self.dict["MAIN"][self.op_type][self.side][item]["P2"] == None:
						return (self.side + " " + item + " P2")

			return (self.side + " Done")

		return None


 
	def addDict(self, event):

		for item in self.dict["MAIN"][self.op_type][self.side]:
			# get item type 
			item_type = self.dict["MAIN"][self.op_type][self.side][item]["type"]
			# get real point
			P = self.draw_tools.getRealCoords(event)

			# store ref for dissapearing items
			self.curr_display_item = item


			# point only has P1
			if item_type == "point":
				# check if P1 is None				
				if self.dict["MAIN"][self.op_type][self.side][item]["P1"] == None:
					self.dict["MAIN"][self.op_type][self.side][item]["P1"] = P
					return True

			# point has P1 and P2, M1 is calculated
			# ANKLE / NECK-AXIS
			if item_type == "midpoint":

				# check if P1 is None				
				if self.dict["MAIN"][self.op_type][self.side][item]["P1"] == None:
					self.dict["MAIN"][self.op_type][self.side][item]["P1"] = P
					if item == "ANKLE":
						self.draw_tools.setHoverPointLabel("P1_ANKLE")
					elif item == "NECK_AXIS":
						self.draw_tools.setHoverPointLabel("P1_MNSA")
					elif item == "DIST_FEM":
						self.draw_tools.setHoverPointLabel("P1_VCA")					
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


			# line has P1 and P2
			if item_type == "line":

				# check if P1 is None
				if self.dict["MAIN"][self.op_type][self.side][item]["P1"] == None:
					self.dict["MAIN"][self.op_type][self.side][item]["P1"] = P
					if item == "FEM_JOINT_LINE":
						self.draw_tools.setHoverPointLabel("P1_FEM_J_LINE")
					elif item == "TIB_JOINT_LINE":
						self.draw_tools.setHoverPointLabel("P1_TIB_J_LINE")
					elif item == "KJLO_LINE":
						self.draw_tools.setHoverPointLabel("P1_KJLO_LINE")
					elif item == "MAD_LINE":
						self.draw_tools.setHoverPointLabel("P1_MAD_LINE")
					self.draw_tools.setHoverPoint(P)
					self.draw_tools.setHoverBool(True)
					return True


				# check if P2 is None
				if self.dict["MAIN"][self.op_type][self.side][item]["P2"] == None:
					self.dict["MAIN"][self.op_type][self.side][item]["P2"] = P
					self.draw_tools.setHoverBool(False)
					self.draw_tools.setHoverPointLabel(None)
					return True

		return False				

	


	def draw(self):
		# for items in self.dict["MAIN"]:
		self.draw_tools.clear_by_tag(self.tag)

		self.point_size = self.controller.getViewPointSize()

		if self.draw_anat_axis:
			print("draw draw_anat_axis")

		if self.draw_mech_axis:
			print("draw draw_mech_axis")

		# loop left and right
		for side in ["LEFT","RIGHT"]:
			for item in self.dict["MAIN"][self.op_type][side]:

				# if dissapearing is checked
				# only draw curr item
				# else see list of checked items

				if self.draw_dissapear_mode:
					if item == self.curr_display_item:
						self.common_draw_func(item,side)
				else:
					self.common_draw_func(item,side)


				# item_type = self.dict["MAIN"][self.op_type][side][item]["type"]
				# side_pre = side[0]+"_" # R/L

				# # HIP & KNEE
				# if item_type == "point":
				# 	if self.dict["MAIN"][self.op_type][side][item]["P1"] != None:

				# 		self.draw_tools.create_mypoint(self.dict["MAIN"][self.op_type][side][item]["P1"], "orange", [self.tag, side, item,"P1"], point_thickness=self.point_size)
				# 		# self.draw_tools.create_mytext(self.dict["MAIN"][self.op_type][side][item]["P1"], x_offset=80, mytext=(side_pre+item), mytag=self.tag)

				# 		if self.draw_labels:
				# 			if item == "TIB_KNEE" and side == "RIGHT":
				# 				self.draw_tools.create_mytext(self.dict["MAIN"][self.op_type][side][item]["P1"],x_offset=-80, mytext=(side_pre+item), mytag=self.tag, color="blue")
				# 			elif item == "FEM_KNEE" and side == "LEFT":
				# 				self.draw_tools.create_mytext(self.dict["MAIN"][self.op_type][side][item]["P1"],x_offset=-80, mytext=(side_pre+item), mytag=self.tag, color="blue")
				# 			else:
				# 				self.draw_tools.create_mytext(self.dict["MAIN"][self.op_type][side][item]["P1"],x_offset=80, mytext=(side_pre+item), mytag=self.tag, color="blue")
				# 		# self, point, color="white", font_size=8, mytext, mytag):

				# # ANKLE
				# if item_type == "midpoint":
				# 	if self.dict["MAIN"][self.op_type][side][item]["P1"] != None:
				# 		self.draw_tools.create_mypoint(self.dict["MAIN"][self.op_type][side][item]["P1"], "orange", [self.tag, side, "ANKLE", "P1"], point_thickness=self.point_size)

				# 	if self.dict["MAIN"][self.op_type][side][item]["P2"] != None:
				# 		self.draw_tools.create_mypoint(self.dict["MAIN"][self.op_type][side][item]["P2"], "orange", [self.tag, side, "ANKLE", "P2"], point_thickness=self.point_size)


				# 	if self.dict["MAIN"][self.op_type][side][item]["P1"] != None and self.dict["MAIN"][self.op_type][side][item]["P2"] != None:
				# 		p1 = self.dict["MAIN"][self.op_type][side][item]["P1"]
				# 		p2 = self.dict["MAIN"][self.op_type][side][item]["P2"]
				# 		m1 = self.dict["MAIN"][self.op_type][side][item]["M1"]
				# 		self.draw_tools.create_midpoint_line(p1, p2, m1, [self.tag, side, "ANKLE_LINE"], point_thickness=self.point_size)
				# 		if self.draw_labels:
				# 			self.draw_tools.create_mytext(self.dict["MAIN"][self.op_type][side][item]["P2"], x_offset=80, mytext=(side_pre+item), mytag=[self.tag, side, "ANKLE_LINE"], color="blue")


				# # AXIS_TIB & AXIS_FEM
				# if item_type == "axis":
					
				# 	if self.dict["MAIN"][self.op_type][side][item]["TOP"]["P1"] != None:						
				# 		self.draw_tools.create_mypoint(self.dict["MAIN"][self.op_type][side][item]["TOP"]["P1"], "orange", [self.tag, side, item, "TOP", "P1"], point_thickness=self.point_size)

				# 	if self.dict["MAIN"][self.op_type][side][item]["TOP"]["P2"] != None:
				# 		self.draw_tools.create_mypoint(self.dict["MAIN"][self.op_type][side][item]["TOP"]["P2"], "orange", [self.tag, side, item, "TOP", "P2"], point_thickness=self.point_size)

				# 	if self.dict["MAIN"][self.op_type][side][item]["TOP"]["P1"] != None and self.dict["MAIN"][self.op_type][side][item]["TOP"]["P2"] != None:
				# 		p1 = self.dict["MAIN"][self.op_type][side][item]["TOP"]["P1"]
				# 		p2 = self.dict["MAIN"][self.op_type][side][item]["TOP"]["P2"]
				# 		m1 = self.dict["MAIN"][self.op_type][side][item]["TOP"]["M1"]
				# 		self.draw_tools.create_midpoint_line(p1, p2, m1, [self.tag,side,"AXIS_LINE"], point_thickness=self.point_size)

				# 		axis_text = side_pre + item.replace("AXIS_", "") + "_TOP"
				# 		if self.draw_labels:
				# 			self.draw_tools.create_mytext(p2, x_offset=80, mytext=axis_text, mytag=self.tag, color="blue")


				# 	if self.dict["MAIN"][self.op_type][side][item]["BOT"]["P1"] != None:						
				# 		self.draw_tools.create_mypoint(self.dict["MAIN"][self.op_type][side][item]["BOT"]["P1"], "orange", [self.tag, side, item, "BOT", "P1"], point_thickness=self.point_size)

				# 	if self.dict["MAIN"][self.op_type][side][item]["BOT"]["P2"] != None:						
				# 		self.draw_tools.create_mypoint(self.dict["MAIN"][self.op_type][side][item]["BOT"]["P2"], "orange", [self.tag, side, item, "BOT", "P2"], point_thickness=self.point_size)

				# 	if self.dict["MAIN"][self.op_type][side][item]["BOT"]["P1"] != None and self.dict["MAIN"][self.op_type][side][item]["BOT"]["P2"] != None:
				# 		p1 = self.dict["MAIN"][self.op_type][side][item]["BOT"]["P1"]
				# 		p2 = self.dict["MAIN"][self.op_type][side][item]["BOT"]["P2"]
				# 		m1 = self.dict["MAIN"][self.op_type][side][item]["BOT"]["M1"]
				# 		self.draw_tools.create_midpoint_line(p1, p2, m1, [self.tag,side,"AXIS_LINE"], point_thickness=self.point_size)

				# 		axis_text = side_pre + item.replace("AXIS_", "") + "_BOT"
				# 		if self.draw_labels:
				# 			self.draw_tools.create_mytext(p2, x_offset=80, mytext=axis_text, mytag=self.tag, color="blue")


				# # NOT ANLE
				# if item_type == "line":
				# 	if self.dict["MAIN"][self.op_type][side][item]["P1"] != None:
				# 		self.draw_tools.create_mypoint(self.dict["MAIN"][self.op_type][side][item]["P1"], "orange", [self.tag, side, "ANKLE", "P1"], point_thickness=self.point_size)

				# 	if self.dict["MAIN"][self.op_type][side][item]["P2"] != None:
				# 		self.draw_tools.create_mypoint(self.dict["MAIN"][self.op_type][side][item]["P2"], "orange", [self.tag, side, "ANKLE", "P2"], point_thickness=self.point_size)


				# 	if self.dict["MAIN"][self.op_type][side][item]["P1"] != None and self.dict["MAIN"][self.op_type][side][item]["P2"] != None:
				# 		p1 = self.dict["MAIN"][self.op_type][side][item]["P1"]
				# 		p2 = self.dict["MAIN"][self.op_type][side][item]["P2"]						
				# 		self.draw_tools.create_myline(self.dict["MAIN"][self.op_type][side][item]["P1"], self.dict["MAIN"][self.op_type][side][item]["P2"], [self.tag,side,"LINE_MLDFA"])
				# 		# self.draw_tools.create_midpoint_line(p1, p2, m1, [self.tag, side, "ANKLE_LINE"], point_thickness=self.point_size)
				# 		# if self.draw_labels:
				# 			# self.draw_tools.create_mytext(self.dict["MAIN"][self.op_type][side][item]["P2"], x_offset=80, mytext=(side_pre+item), mytag=[self.tag, side, "ANKLE_LINE"], color="blue")
				


	def update_canvas(self, draw_tools):
		self.draw_tools = draw_tools


	def hover(self, P_mouse, P_stored, hover_label):


		if self.draw_hover:

			side_pre = self.side[0]+"_"


			if(	hover_label == "P0_HIP" or
				hover_label == "P0_NECK_AXIS" or
				hover_label == "P0_FEM_KNEE" or
				hover_label == "P0_TIB_KNEE" or
				hover_label == "P0_ANKLE" or
				hover_label == "P0_DIST_FEM" or
				hover_label == "P0_AXIS_FEM_TOP" or
				hover_label == "P0_AXIS_FEM_BOT" or
				hover_label == "P0_AXIS_TIB_TOP" or
				hover_label == "P0_FEM_J_LINE" or
				hover_label == "P0_TIB_J_LINE" or
				hover_label == "P0_AXIS_TIB_BOT" or
				hover_label == "P0_KJLO_LINE" or
				hover_label == "P0_MAD_LINE"
				):
				self.draw_tools.clear_by_tag("hover_line")
				self.draw_tools.create_mypoint(P_mouse, "red", [self.tag, "hover_line"], hover_point=True, point_thickness=self.point_size)
				if self.draw_labels:
					self.draw_tools.create_mytext(P_mouse,x_offset=80, mytext=(side_pre+self.hover_text), mytag=[self.tag, "hover_line"])


		
		if(	hover_label == "P1_ANKLE" or
			hover_label == "P1_MNSA" or
			hover_label == "P1_VCA" or
			hover_label == "P1_TOP_AXIS_FEM" or
			hover_label == "P1_TOP_AXIS_TIB" or
			hover_label == "P1_BOT_AXIS_FEM" or
			hover_label == "P1_BOT_AXIS_TIB" 
			):
			self.draw_tools.clear_by_tag("hover_line")
			m = self.draw_tools.midpoint(P_stored, P_mouse)
			self.draw_tools.create_midpoint_line(P_stored, P_mouse, m, "hover_line", point_thickness=self.point_size)


		if( hover_label == "P1_FEM_J_LINE" or
			hover_label == "P1_TIB_J_LINE" or 
			hover_label == "P1_KJLO_LINE" or
			hover_label == "P1_MAD_LINE"
			):
			self.draw_tools.clear_by_tag("hover_line")			
			self.draw_tools.create_myline(P_mouse, P_stored, "hover_line")
			


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


		elif label == "RIGHT NECK_AXIS P1":
			self.side = "RIGHT"
			self.hover_text = "NECK_AXIS"
			self.draw_tools.setHoverPointLabel("P0_NECK_AXIS")
			self.draw_tools.setHoverPoint(None)
			self.draw_tools.setHoverBool(True)
		elif label == "LEFT NECK_AXIS P1":
			self.side = "LEFT"
			self.hover_text = "NECK_AXIS"
			self.draw_tools.setHoverPointLabel("P0_NECK_AXIS")
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


		elif label == "RIGHT DIST_FEM P1":
			self.side = "RIGHT"
			self.hover_text = "DIST_FEM_P1"
			self.draw_tools.setHoverPointLabel("P0_DIST_FEM")
			self.draw_tools.setHoverPoint(None)
			self.draw_tools.setHoverBool(True)
		elif label == "LEFT DIST_FEM P1":
			self.side = "LEFT"
			self.hover_text = "DIST_FEM_P1"
			self.draw_tools.setHoverPointLabel("P0_DIST_FEM")
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


		# FEM and TIB joint lines
		elif label == "LEFT FEM_JOINT_LINE P1":
			self.side = "LEFT"
			self.hover_text = "FEM_J_LINE_P1"
			self.draw_tools.setHoverPointLabel("P0_FEM_J_LINE")
			self.draw_tools.setHoverPoint(None)
			self.draw_tools.setHoverBool(True)
		elif label == "RIGHT FEM_JOINT_LINE P1":
			self.side = "RIGHT"
			self.hover_text = "FEM_J_LINE_P1"
			self.draw_tools.setHoverPointLabel("P0_FEM_J_LINE")
			self.draw_tools.setHoverPoint(None)
			self.draw_tools.setHoverBool(True)
		elif label == "LEFT TIB_JOINT_LINE P1":
			self.side = "LEFT"
			self.hover_text = "TIB_J_LINE_P1"
			self.draw_tools.setHoverPointLabel("P0_TIB_J_LINE")
			self.draw_tools.setHoverPoint(None)
			self.draw_tools.setHoverBool(True)
		elif label == "RIGHT TIB_JOINT_LINE P1":
			self.side = "RIGHT"
			self.hover_text = "TIB_J_LINE_P1"
			self.draw_tools.setHoverPointLabel("P0_TIB_J_LINE")
			self.draw_tools.setHoverPoint(None)
			self.draw_tools.setHoverBool(True)

		elif label == "LEFT KJLO_LINE P1":
			self.side = "LEFT"
			self.hover_text = "KJLO_LINE_P1"
			self.draw_tools.setHoverPointLabel("P0_KJLO_LINE")
			self.draw_tools.setHoverPoint(None)
			self.draw_tools.setHoverBool(True)
		elif label == "RIGHT KJLO_LINE P1":
			self.side = "RIGHT"
			self.hover_text = "KJLO_LINE_P1"
			self.draw_tools.setHoverPointLabel("P0_KJLO_LINE")
			self.draw_tools.setHoverPoint(None)
			self.draw_tools.setHoverBool(True)

		elif label == "LEFT MAD_LINE P1":
			self.side = "LEFT"
			self.hover_text = "MAD_LINE_P1"
			self.draw_tools.setHoverPointLabel("P0_MAD_LINE")
			self.draw_tools.setHoverPoint(None)
			self.draw_tools.setHoverBool(True)
		elif label == "RIGHT MAD_LINE P1":
			self.side = "RIGHT"
			self.hover_text = "MAD_LINE_P1"
			self.draw_tools.setHoverPointLabel("P0_MAD_LINE")
			self.draw_tools.setHoverPoint(None)
			self.draw_tools.setHoverBool(True)


		elif label == "LEFT Done" or label == "RIGHT Done":
			self.draw_tools.setHoverPointLabel("")
			self.draw_tools.setHoverPoint(None)
			self.draw_tools.setHoverBool(False)
			self.drawFromMain()

		# else:
		# 	self.draw_tools.setHoverPointLabel(None)
		# 	self.draw_tools.setHoverPoint(None)
		# 	self.draw_tools.setHoverBool(False)





	def regainHover(self, side):
		p1_ankle = self.dict["MAIN"][self.op_type][side]["ANKLE"]["P1"]
		p2_ankle = self.dict["MAIN"][self.op_type][side]["ANKLE"]["P2"]

		p1_neck_axis = self.dict["MAIN"][self.op_type][side]["NECK_AXIS"]["P1"]
		p2_neck_axis = self.dict["MAIN"][self.op_type][side]["NECK_AXIS"]["P2"]

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

		if p1_ankle != None and p2_ankle == None:
			self.draw_tools.setHoverPointLabel("P1_ANKLE")
			self.draw_tools.setHoverPoint(p1_ankle)
			self.draw_tools.setHoverBool(True)

		elif p1_neck_axis != None and p2_neck_axis == None:
			self.draw_tools.setHoverPointLabel("P1_MNSA")
			self.draw_tools.setHoverPoint(p1_neck_axis)
			self.draw_tools.setHoverBool(True)

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

		elif "NECK_AXIS" in tags:
			if "P1" in tags:
				self.drag_point = self.dict["MAIN"][self.op_type][side]["NECK_AXIS"]["P2"]
				self.drag_label = "P1_NECK_AXIS"
				self.drag_side 	= side
			elif "P2" in tags:
				self.drag_point = self.dict["MAIN"][self.op_type][side]["NECK_AXIS"]["P1"]
				self.drag_label = "P2_NECK_AXIS"
				self.drag_side 	= side

		elif "DIST_FEM" in tags:
			if "P1" in tags:
				self.drag_point = self.dict["MAIN"][self.op_type][side]["DIST_FEM"]["P2"]
				self.drag_label = "P1_DIST_FEM"
				self.drag_side 	= side
			elif "P2" in tags:
				self.drag_point = self.dict["MAIN"][self.op_type][side]["DIST_FEM"]["P1"]
				self.drag_label = "P2_DIST_FEM"
				self.drag_side 	= side

		elif "FEM_JOINT_LINE" in tags:
			if "P1" in tags:
				self.drag_point = self.dict["MAIN"][self.op_type][side]["FEM_JOINT_LINE"]["P2"]
				self.drag_label = "P1_FEM_JOINT_LINE"
				self.drag_side 	= side
			elif "P2" in tags:
				self.drag_point = self.dict["MAIN"][self.op_type][side]["FEM_JOINT_LINE"]["P1"]
				self.drag_label = "P2_FEM_JOINT_LINE"
				self.drag_side 	= side

		elif "TIB_JOINT_LINE" in tags:
			if "P1" in tags:
				self.drag_point = self.dict["MAIN"][self.op_type][side]["TIB_JOINT_LINE"]["P2"]
				self.drag_label = "P1_TIB_JOINT_LINE"
				self.drag_side 	= side
			elif "P2" in tags:
				self.drag_point = self.dict["MAIN"][self.op_type][side]["TIB_JOINT_LINE"]["P1"]
				self.drag_label = "P2_TIB_JOINT_LINE"
				self.drag_side 	= side


		elif "KJLO_LINE" in tags:
			if "P1" in tags:
				self.drag_point = self.dict["MAIN"][self.op_type][side]["KJLO_LINE"]["P2"]
				self.drag_label = "P1_KJLO_LINE"
				self.drag_side 	= side
			elif "P2" in tags:
				self.drag_point = self.dict["MAIN"][self.op_type][side]["KJLO_LINE"]["P1"]
				self.drag_label = "P2_KJLO_LINE"
				self.drag_side 	= side

		elif "MAD_LINE" in tags:
			if "P1" in tags:
				self.drag_point = self.dict["MAIN"][self.op_type][side]["MAD_LINE"]["P2"]
				self.drag_label = "P1_MAD_LINE"
				self.drag_side 	= side
			elif "P2" in tags:
				self.drag_point = self.dict["MAIN"][self.op_type][side]["MAD_LINE"]["P1"]
				self.drag_label = "P2_MAD_LINE"
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
		if (self.drag_label == "P1_ANKLE" and self.drag_point != None or 
			self.drag_label == "P2_ANKLE" and self.drag_point != None or
			self.drag_label == "P1_NECK_AXIS" and self.drag_point != None or 
			self.drag_label == "P2_NECK_AXIS" and self.drag_point != None or
			self.drag_label == "P1_DIST_FEM" and self.drag_point != None or
			self.drag_label == "P2_DIST_FEM" and self.drag_point != None
			):
			self.draw_tools.clear_by_tag("ANKLE_LINE")
			self.draw_tools.clear_by_tag("drag_line")
			m = self.draw_tools.midpoint(self.drag_point, P_mouse)
			self.draw_tools.create_midpoint_line(self.drag_point, P_mouse, m, "drag_line", point_thickness=self.point_size)


		if (self.drag_label == "P1_AXIS_FEM_TOP" or self.drag_label == "P2_AXIS_FEM_TOP" or self.drag_label == "P1_AXIS_FEM_BOT" or self.drag_label == "P2_AXIS_FEM_BOT" or
			self.drag_label == "P1_AXIS_TIB_TOP" or self.drag_label == "P2_AXIS_TIB_TOP" or self.drag_label == "P1_AXIS_TIB_BOT" or self.drag_label == "P2_AXIS_TIB_BOT"):
			self.draw_tools.clear_by_tag("AXIS_LINE")
			self.draw_tools.clear_by_tag("drag_line")
			m = self.draw_tools.midpoint(self.drag_point, P_mouse)
			self.draw_tools.create_midpoint_line(self.drag_point, P_mouse, m, "drag_line", point_thickness=self.point_size)


		if (self.drag_label == "P1_FEM_JOINT_LINE" and self.drag_point != None or 
			self.drag_label == "P2_FEM_JOINT_LINE" and self.drag_point != None or
			self.drag_label == "P1_TIB_JOINT_LINE" and self.drag_point != None or 
			self.drag_label == "P2_TIB_JOINT_LINE" and self.drag_point != None or
			self.drag_label == "P1_KJLO_LINE" and self.drag_point != None or
			self.drag_label == "P2_KJLO_LINE" and self.drag_point != None			
			):
			self.draw_tools.clear_by_tag("JOINT_LINE")
			self.draw_tools.clear_by_tag("drag_line")
			self.draw_tools.create_myline(P_mouse, self.drag_point, "drag_line")


		if (self.drag_label == "P1_MAD_LINE" and self.drag_point != None or
			self.drag_label == "P2_MAD_LINE" and self.drag_point != None
			):
			self.draw_tools.clear_by_tag("MAD_DIV_PTS")
			self.draw_tools.clear_by_tag("drag_line")
			self.draw_tools.create_myline(P_mouse, self.drag_point, "drag_line")

		
		# self.drag_label = "P2_AXIS_FEM_"+topbot
		# self.drag_label = "P1_AXIS_TIB_"+topbot
		# self.drag_label = "P2_AXIS_TIB_"+topbot
		# pass

	def drag_stop(self, P_mouse):

		self.draw_tools.clear_by_tag("drag_line")

		if self.drag_label == "HIP":
			self.dict["MAIN"][self.op_type][self.drag_side]["HIP"]["P1"] = P_mouse
			self.deleteExcelValues(["HKA", "MNSA", "VCA", "mLDFA"], self.drag_side)		# clear excel values
			
		elif self.drag_label == "FEM_KNEE":
			self.dict["MAIN"][self.op_type][self.drag_side]["FEM_KNEE"]["P1"] = P_mouse
			self.deleteExcelValues(["HKA", "VCA", "mLDFA"], self.drag_side)		# clear excel values

		elif self.drag_label == "TIB_KNEE":
			self.dict["MAIN"][self.op_type][self.drag_side]["TIB_KNEE"]["P1"] = P_mouse
			self.deleteExcelValues(["HKA", "TAMD", "MPTA"], self.drag_side)		# clear excel values


		elif self.drag_label == "P1_ANKLE":
			self.dict["MAIN"][self.op_type][self.drag_side]["ANKLE"]["P1"] = P_mouse
			self.dict["MAIN"][self.op_type][self.drag_side]["ANKLE"]["M1"] = self.draw_tools.midpoint(self.drag_point, P_mouse)
			self.deleteExcelValues(["HKA", "TAMD", "MPTA", "KJLO", "KAOL"], self.drag_side)		# clear excel values
		elif self.drag_label == "P2_ANKLE":
			self.dict["MAIN"][self.op_type][self.drag_side]["ANKLE"]["P2"] = P_mouse
			self.dict["MAIN"][self.op_type][self.drag_side]["ANKLE"]["M1"] = self.draw_tools.midpoint(self.drag_point, P_mouse)
			self.deleteExcelValues(["HKA", "TAMD", "MPTA", "KJLO", "KAOL"], self.drag_side)		# clear excel values


		elif self.drag_label == "P1_AXIS_FEM_TOP":
			self.dict["MAIN"][self.op_type][self.drag_side]["AXIS_FEM"]["TOP"]["P1"] = P_mouse
			self.dict["MAIN"][self.op_type][self.drag_side]["AXIS_FEM"]["TOP"]["M1"] = self.draw_tools.midpoint(self.drag_point, P_mouse)
			self.deleteExcelValues(["MNSA", "aFTA", "aLDFA"], self.drag_side)		# clear excel values
		elif self.drag_label == "P2_AXIS_FEM_TOP":
			self.dict["MAIN"][self.op_type][self.drag_side]["AXIS_FEM"]["TOP"]["P2"] = P_mouse
			self.dict["MAIN"][self.op_type][self.drag_side]["AXIS_FEM"]["TOP"]["M1"] = self.draw_tools.midpoint(self.drag_point, P_mouse)
			self.deleteExcelValues(["MNSA", "aFTA", "aLDFA"], self.drag_side)		# clear excel values


		elif self.drag_label == "P1_AXIS_FEM_BOT":
			self.dict["MAIN"][self.op_type][self.drag_side]["AXIS_FEM"]["BOT"]["P1"] = P_mouse
			self.dict["MAIN"][self.op_type][self.drag_side]["AXIS_FEM"]["BOT"]["M1"] = self.draw_tools.midpoint(self.drag_point, P_mouse)
			self.deleteExcelValues(["MNSA", "aFTA", "aLDFA"], self.drag_side)		# clear excel values
		elif self.drag_label == "P2_AXIS_FEM_BOT":
			self.dict["MAIN"][self.op_type][self.drag_side]["AXIS_FEM"]["BOT"]["P2"] = P_mouse
			self.dict["MAIN"][self.op_type][self.drag_side]["AXIS_FEM"]["BOT"]["M1"] = self.draw_tools.midpoint(self.drag_point, P_mouse)
			self.deleteExcelValues(["MNSA", "aFTA", "aLDFA"], self.drag_side)		# clear excel values


		elif self.drag_label == "P1_AXIS_TIB_TOP":
			self.dict["MAIN"][self.op_type][self.drag_side]["AXIS_TIB"]["TOP"]["P1"] = P_mouse
			self.dict["MAIN"][self.op_type][self.drag_side]["AXIS_TIB"]["TOP"]["M1"] = self.draw_tools.midpoint(self.drag_point, P_mouse)
			self.deleteExcelValues(["aFTA", "TAMD"], self.drag_side)		# clear excel values
		elif self.drag_label == "P2_AXIS_TIB_TOP":
			self.dict["MAIN"][self.op_type][self.drag_side]["AXIS_TIB"]["TOP"]["P2"] = P_mouse
			self.dict["MAIN"][self.op_type][self.drag_side]["AXIS_TIB"]["TOP"]["M1"] = self.draw_tools.midpoint(self.drag_point, P_mouse)
			self.deleteExcelValues(["aFTA", "TAMD"], self.drag_side)		# clear excel values


		elif self.drag_label == "P1_AXIS_TIB_BOT":
			self.dict["MAIN"][self.op_type][self.drag_side]["AXIS_TIB"]["BOT"]["P1"] = P_mouse
			self.dict["MAIN"][self.op_type][self.drag_side]["AXIS_TIB"]["BOT"]["M1"] = self.draw_tools.midpoint(self.drag_point, P_mouse)
			self.deleteExcelValues(["aFTA", "TAMD"], self.drag_side)		# clear excel values
		elif self.drag_label == "P2_AXIS_TIB_BOT":
			self.dict["MAIN"][self.op_type][self.drag_side]["AXIS_TIB"]["BOT"]["P2"] = P_mouse
			self.dict["MAIN"][self.op_type][self.drag_side]["AXIS_TIB"]["BOT"]["M1"] = self.draw_tools.midpoint(self.drag_point, P_mouse)
			self.deleteExcelValues(["aFTA", "TAMD"], self.drag_side)		# clear excel values


		elif self.drag_label == "P1_NECK_AXIS":
			self.dict["MAIN"][self.op_type][self.drag_side]["NECK_AXIS"]["P1"] = P_mouse
			self.dict["MAIN"][self.op_type][self.drag_side]["NECK_AXIS"]["M1"] = self.draw_tools.midpoint(self.drag_point, P_mouse)
			# self.deleteExcelValues(["HKA", "TAMD", "MPTA", "KJLO", "KAOL"], self.drag_side)		# clear excel values
		elif self.drag_label == "P2_NECK_AXIS":
			self.dict["MAIN"][self.op_type][self.drag_side]["NECK_AXIS"]["P2"] = P_mouse
			self.dict["MAIN"][self.op_type][self.drag_side]["NECK_AXIS"]["M1"] = self.draw_tools.midpoint(self.drag_point, P_mouse)
			# self.deleteExcelValues(["HKA", "TAMD", "MPTA", "KJLO", "KAOL"], self.drag_side)		# clear excel values

		elif self.drag_label == "P1_FEM_JOINT_LINE":
			self.dict["MAIN"][self.op_type][self.drag_side]["FEM_JOINT_LINE"]["P1"] = P_mouse
			# self.deleteExcelValues(["HKA", "MNSA", "VCA", "mLDFA"], self.drag_side)		# clear excel values
		elif self.drag_label == "P2_FEM_JOINT_LINE":
			self.dict["MAIN"][self.op_type][self.drag_side]["FEM_JOINT_LINE"]["P2"] = P_mouse
			# self.deleteExcelValues(["HKA", "MNSA", "VCA", "mLDFA"], self.drag_side)		# clear excel values

		elif self.drag_label == "P1_TIB_JOINT_LINE":
			self.dict["MAIN"][self.op_type][self.drag_side]["TIB_JOINT_LINE"]["P1"] = P_mouse
			# self.deleteExcelValues(["HKA", "MNSA", "VCA", "mLDFA"], self.drag_side)		# clear excel values
		elif self.drag_label == "P2_TIB_JOINT_LINE":
			self.dict["MAIN"][self.op_type][self.drag_side]["TIB_JOINT_LINE"]["P2"] = P_mouse
			# self.deleteExcelValues(["HKA", "MNSA", "VCA", "mLDFA"], self.drag_side)		# clear excel values


		elif self.drag_label == "P1_DIST_FEM":
			self.dict["MAIN"][self.op_type][self.drag_side]["DIST_FEM"]["P1"] = P_mouse
			self.dict["MAIN"][self.op_type][self.drag_side]["DIST_FEM"]["M1"] = self.draw_tools.midpoint(self.drag_point, P_mouse)
			# self.deleteExcelValues(["HKA", "TAMD", "MPTA", "KJLO", "KAOL"], self.drag_side)		# clear excel values
		elif self.drag_label == "P2_DIST_FEM":
			self.dict["MAIN"][self.op_type][self.drag_side]["DIST_FEM"]["P2"] = P_mouse
			self.dict["MAIN"][self.op_type][self.drag_side]["DIST_FEM"]["M1"] = self.draw_tools.midpoint(self.drag_point, P_mouse)
			# self.deleteExcelValues(["HKA", "TAMD", "MPTA", "KJLO", "KAOL"], self.drag_side)		# clear excel values

		elif self.drag_label == "P1_KJLO_LINE":
			self.dict["MAIN"][self.op_type][self.drag_side]["KJLO_LINE"]["P1"] = P_mouse
			# self.deleteExcelValues(["HKA", "MNSA", "VCA", "mLDFA"], self.drag_side)		# clear excel values
		elif self.drag_label == "P2_KJLO_LINE":
			self.dict["MAIN"][self.op_type][self.drag_side]["KJLO_LINE"]["P2"] = P_mouse
			# self.deleteExcelValues(["HKA", "MNSA", "VCA", "mLDFA"], self.drag_side)		# clear excel values

		elif self.drag_label == "P1_MAD_LINE":
			self.dict["MAIN"][self.op_type][self.drag_side]["MAD_LINE"]["P1"] = P_mouse
			# self.deleteExcelValues(["HKA", "MNSA", "VCA", "mLDFA"], self.drag_side)		# clear excel values
		elif self.drag_label == "P2_MAD_LINE":
			self.dict["MAIN"][self.op_type][self.drag_side]["MAD_LINE"]["P2"] = P_mouse
			# self.deleteExcelValues(["HKA", "MNSA", "VCA", "mLDFA"], self.drag_side)		# clear excel values

		self.controller.save_json()
		self.draw()


	def unset(self):
		# print("unset from "+self.name)
		self.draw_tools.clear_by_tag(self.tag)
		self.side = None


	def checkbox_click(self,action, val):

		print('checkbox {} val{}'.format(action,val.get()))

		if action == "TOGGLE_DISSAPEAR_MODE":
			if val.get() == 0:
				self.draw_dissapear_mode = False
			elif val.get() == 1:
				self.draw_dissapear_mode = True
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


		if action == "TOGGLE_FEM_J":
			if val.get() == 0:
				self.draw_fem_j_var = False
			elif val.get() == 1:
				self.draw_fem_j_var = True
			self.draw()

		if action == "TOGGLE_TIB_J":
			if val.get() == 0:
				self.draw_tib_j_var = False
			elif val.get() == 1:
				self.draw_tib_j_var = True
			self.draw()

		if action == "TOGGLE_KJLO_LINE":
			if val.get() == 0:
				self.draw_kjlo_line = False
			elif val.get() == 1:
				self.draw_kjlo_line = True
			self.draw()

		if action == "TOGGLE_MAD_LINE":
			if val.get() == 0:
				self.draw_mad_line = False
			elif val.get() == 1:
				self.draw_mad_line = True
			self.draw()


		if action == "TOGGLE_FEM_KNEE":
			if val.get() == 0:
				self.draw_fem_knee = False
			elif val.get() == 1:
				self.draw_fem_knee = True
			self.draw()

		if action == "TOGGLE_TIB_KNEE":
			if val.get() == 0:
				self.draw_tib_knee = False
			elif val.get() == 1:
				self.draw_tib_knee = True
			self.draw()


	def deleteExcelValues(self, del_list, side=None):

		# HKA 		hip, tib-knee, fem-knee, ankle
		# MNSA 		fem-top-bot, hip
		# VCA 		hip, fem-knee
		# AFTA 		fem-top-bot, tib-top-bot
		# MLDFA 	hip, fem-knee
		# ALDFA 	fem-top-bot
		# TAMD 		tib-top-bot, tib-knee, ankle
		# MPTA 		tib-knee, ankle
		# KJLO 		ankle
		# KAOL 		ankle


		# hip 			HKA, MNSA, VCA, MLDFA
		# fem-top-bot	MNSA, AFTA, ALDFA
		# fem-knee 		HKA, VCA, MLDFA
		# tib-knee 		HKA, TAMD, MPTA
		# tib-top-bot 	AFTA, TAMD
		# ankle 		HKA, TAMD, MPTA, KJLO, KAOL

		for key in del_list:
			print(key)

			if side != None:
				print(side)
				self.dict["EXCEL"][self.op_type][side][key] = None
			else:
				print("left and right")
				self.dict["EXCEL"][self.op_type]["LEFT"][key] = None
				self.dict["EXCEL"][self.op_type]["RIGHT"][key] = None



	def common_draw_func(self, item, side):
		item_type = self.dict["MAIN"][self.op_type][side][item]["type"]
		side_pre = side[0]+"_" # R/L

		# HIP & KNEE
		if item_type == "point":
			if self.dict["MAIN"][self.op_type][side][item]["P1"] != None:

				if( item == "TIB_KNEE" and self.draw_tib_knee or
					item == "FEM_KNEE" and self.draw_fem_knee or
					item == "HIP"
					):

					self.draw_tools.create_mypoint(self.dict["MAIN"][self.op_type][side][item]["P1"], "orange", [self.tag, side, item,"P1"], point_thickness=self.point_size)
					# self.draw_tools.create_mytext(self.dict["MAIN"][self.op_type][side][item]["P1"], x_offset=80, mytext=(side_pre+item), mytag=self.tag)

					if self.draw_labels:
						if item == "TIB_KNEE":
							self.draw_tools.create_mytext(self.dict["MAIN"][self.op_type][side][item]["P1"],y_offset=20, mytext=(side_pre+item), mytag=self.tag, color="blue")
						elif item == "FEM_KNEE":
							self.draw_tools.create_mytext(self.dict["MAIN"][self.op_type][side][item]["P1"],y_offset=-20, mytext=(side_pre+item), mytag=self.tag, color="blue")
						else:
							self.draw_tools.create_mytext(self.dict["MAIN"][self.op_type][side][item]["P1"],y_offset=-30, mytext=(side_pre+item), mytag=self.tag, color="blue")
					# self, point, color="white", font_size=8, mytext, mytag):

		# ANKLE / NECK_AXIS
		if item_type == "midpoint":			
			if self.dict["MAIN"][self.op_type][side][item]["P1"] != None:
				self.draw_tools.create_mypoint(self.dict["MAIN"][self.op_type][side][item]["P1"], "orange", [self.tag, side, item, "P1"], point_thickness=self.point_size)

			if self.dict["MAIN"][self.op_type][side][item]["P2"] != None:
				self.draw_tools.create_mypoint(self.dict["MAIN"][self.op_type][side][item]["P2"], "orange", [self.tag, side, item, "P2"], point_thickness=self.point_size)


			if self.dict["MAIN"][self.op_type][side][item]["P1"] != None and self.dict["MAIN"][self.op_type][side][item]["P2"] != None:
				p1 = self.dict["MAIN"][self.op_type][side][item]["P1"]
				p2 = self.dict["MAIN"][self.op_type][side][item]["P2"]
				m1 = self.dict["MAIN"][self.op_type][side][item]["M1"]
				self.draw_tools.create_midpoint_line(p1, p2, m1, [self.tag, side, "ANKLE_LINE"], point_thickness=self.point_size)
				if self.draw_labels:
					self.draw_tools.create_mytext(self.dict["MAIN"][self.op_type][side][item]["P2"], x_offset=80, mytext=(side_pre+item), mytag=[self.tag, side, "ANKLE_LINE"], color="blue")


		# AXIS_TIB & AXIS_FEM
		if item_type == "axis":
			
			if self.dict["MAIN"][self.op_type][side][item]["TOP"]["P1"] != None:						
				self.draw_tools.create_mypoint(self.dict["MAIN"][self.op_type][side][item]["TOP"]["P1"], "orange", [self.tag, side, item, "TOP", "P1"], point_thickness=self.point_size)

			if self.dict["MAIN"][self.op_type][side][item]["TOP"]["P2"] != None:
				self.draw_tools.create_mypoint(self.dict["MAIN"][self.op_type][side][item]["TOP"]["P2"], "orange", [self.tag, side, item, "TOP", "P2"], point_thickness=self.point_size)

			if self.dict["MAIN"][self.op_type][side][item]["TOP"]["P1"] != None and self.dict["MAIN"][self.op_type][side][item]["TOP"]["P2"] != None:
				p1 = self.dict["MAIN"][self.op_type][side][item]["TOP"]["P1"]
				p2 = self.dict["MAIN"][self.op_type][side][item]["TOP"]["P2"]
				m1 = self.dict["MAIN"][self.op_type][side][item]["TOP"]["M1"]
				self.draw_tools.create_midpoint_line(p1, p2, m1, [self.tag,side,"AXIS_LINE"], point_thickness=self.point_size)

				axis_text = side_pre + item.replace("AXIS_", "") + "_TOP"
				if self.draw_labels:
					self.draw_tools.create_mytext(p2, x_offset=80, mytext=axis_text, mytag=self.tag, color="blue")


			if self.dict["MAIN"][self.op_type][side][item]["BOT"]["P1"] != None:						
				self.draw_tools.create_mypoint(self.dict["MAIN"][self.op_type][side][item]["BOT"]["P1"], "orange", [self.tag, side, item, "BOT", "P1"], point_thickness=self.point_size)

			if self.dict["MAIN"][self.op_type][side][item]["BOT"]["P2"] != None:						
				self.draw_tools.create_mypoint(self.dict["MAIN"][self.op_type][side][item]["BOT"]["P2"], "orange", [self.tag, side, item, "BOT", "P2"], point_thickness=self.point_size)

			if self.dict["MAIN"][self.op_type][side][item]["BOT"]["P1"] != None and self.dict["MAIN"][self.op_type][side][item]["BOT"]["P2"] != None:
				p1 = self.dict["MAIN"][self.op_type][side][item]["BOT"]["P1"]
				p2 = self.dict["MAIN"][self.op_type][side][item]["BOT"]["P2"]
				m1 = self.dict["MAIN"][self.op_type][side][item]["BOT"]["M1"]
				self.draw_tools.create_midpoint_line(p1, p2, m1, [self.tag,side,"AXIS_LINE"], point_thickness=self.point_size)

				axis_text = side_pre + item.replace("AXIS_", "") + "_BOT"
				if self.draw_labels:
					self.draw_tools.create_mytext(p2, x_offset=80, mytext=axis_text, mytag=self.tag, color="blue")


		# FEM and TIB JOINT LINES
		if item_type == "line":

			if( item == "FEM_JOINT_LINE" and self.draw_fem_j_var or
				item == "TIB_JOINT_LINE" and self.draw_tib_j_var or
				item == "KJLO_LINE" and self.draw_kjlo_line			
				):

				if self.dict["MAIN"][self.op_type][side][item]["P1"] != None:
					self.draw_tools.create_mypoint(self.dict["MAIN"][self.op_type][side][item]["P1"], "orange", [self.tag, side, item, "P1"], point_thickness=self.point_size)

				if self.dict["MAIN"][self.op_type][side][item]["P2"] != None:
					self.draw_tools.create_mypoint(self.dict["MAIN"][self.op_type][side][item]["P2"], "orange", [self.tag, side, item, "P2"], point_thickness=self.point_size)


				if self.dict["MAIN"][self.op_type][side][item]["P1"] != None and self.dict["MAIN"][self.op_type][side][item]["P2"] != None:
					p1 = self.dict["MAIN"][self.op_type][side][item]["P1"]
					p2 = self.dict["MAIN"][self.op_type][side][item]["P2"]						
					self.draw_tools.create_myline(self.dict["MAIN"][self.op_type][side][item]["P1"], self.dict["MAIN"][self.op_type][side][item]["P2"], [self.tag,side,"JOINT_LINE"])
					# self.draw_tools.create_midpoint_line(p1, p2, m1, [self.tag, side, "ANKLE_LINE"], point_thickness=self.point_size)
					if self.draw_labels:
						if item == "FEM_JOINT_LINE" or item == "KJLO_LINE":
							self.draw_tools.create_mytext(self.dict["MAIN"][self.op_type][side][item]["P1"], y_offset=-20, mytext=(side_pre+item), mytag=[self.tag,side,"JOINT_LINE"], color="blue")
						if item == "TIB_JOINT_LINE":
							self.draw_tools.create_mytext(self.dict["MAIN"][self.op_type][side][item]["P1"], y_offset=20, mytext=(side_pre+item), mytag=[self.tag,side,"JOINT_LINE"], color="blue")


			# MAD differences
			if item == "MAD_LINE" and self.draw_mad_line:
				mad_p1 = self.dict["MAIN"][self.op_type][side][item]["P1"]
				mad_p2 = self.dict["MAIN"][self.op_type][side][item]["P2"]
				if mad_p1 != None:
					self.draw_tools.create_mypoint(mad_p1, "orange", [self.tag, side, item, "P1"], point_thickness=self.point_size)

				if mad_p2 != None:
					self.draw_tools.create_mypoint(mad_p2, "orange", [self.tag, side, item, "P2"], point_thickness=self.point_size)

				if mad_p1 != None and mad_p2 != None:
					self.draw_tools.create_myline(mad_p1, mad_p2, [self.tag,side,"MAD_DIV_PTS"])

					# draw the points for division
					self.draw_tools.create_mypoint(self.draw_tools.getLineSegmentByPercentage(0.2, mad_p1, mad_p2), "orange", [self.tag, side, "MAD_DIV_PTS"], point_thickness=self.point_size)
					self.draw_tools.create_mypoint(self.draw_tools.getLineSegmentByPercentage(0.4, mad_p1, mad_p2), "orange", [self.tag, side, "MAD_DIV_PTS"], point_thickness=self.point_size)
					self.draw_tools.create_mypoint(self.draw_tools.getLineSegmentByPercentage(0.6, mad_p1, mad_p2), "orange", [self.tag, side, "MAD_DIV_PTS"], point_thickness=self.point_size)
					self.draw_tools.create_mypoint(self.draw_tools.getLineSegmentByPercentage(0.8, mad_p1, mad_p2), "orange", [self.tag, side, "MAD_DIV_PTS"], point_thickness=self.point_size)

					if self.draw_labels:
						if side == "RIGHT":
							L_mad, R_mad = self.draw_tools.retPointsLeftRight(mad_p1,mad_p2)
						else:
							# invert the direction for the LEFT case
							R_mad, L_mad = self.draw_tools.retPointsLeftRight(mad_p1,mad_p2)

						self.draw_tools.create_mytext(self.draw_tools.getLineSegmentByPercentage(0.1, L_mad, R_mad), y_offset=10, mytext="4", mytag=[self.tag, side, "MAD_DIV_PTS"], color="blue")
						self.draw_tools.create_mytext(self.draw_tools.getLineSegmentByPercentage(0.3, L_mad, R_mad), y_offset=10, mytext="3", mytag=[self.tag, side, "MAD_DIV_PTS"], color="blue")
						self.draw_tools.create_mytext(self.draw_tools.getLineSegmentByPercentage(0.5, L_mad, R_mad), y_offset=10, mytext="C", mytag=[self.tag, side, "MAD_DIV_PTS"], color="blue")
						self.draw_tools.create_mytext(self.draw_tools.getLineSegmentByPercentage(0.7, L_mad, R_mad), y_offset=10, mytext="2", mytag=[self.tag, side, "MAD_DIV_PTS"], color="blue")
						self.draw_tools.create_mytext(self.draw_tools.getLineSegmentByPercentage(0.9, L_mad, R_mad), y_offset=10, mytext="1", mytag=[self.tag, side, "MAD_DIV_PTS"], color="blue")

	def drawFromMain(self):
		self.controller.calculateExcel()








