

class VCA():
	"""docstring for ClassName"""
	def __init__(self, draw_tools, master_dict, controller, op_type):
		self.name = "VCA"
		self.tag = "vca"
		self.menu_label = "VCA_Menu"
		self.draw_tools = draw_tools
		self.dict = master_dict
		self.controller = controller
		self.side = None
		self.op_type = op_type

		# check if master dictionary has values
		# if not populate the dictionary
		self.checkMasterDict()

		# DEL-LEFT-DIST-FEM

	def checkMasterDict(self):
		if "VCA" not in self.dict.keys():
			self.dict["VCA"] = 	{
									"PRE-OP":{
												"LEFT":	{
															"DIST_FEM":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
														},
												"RIGHT":	{
															"DIST_FEM":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
														}

											},
									"POST-OP":{
												"LEFT":	{
															"DIST_FEM":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
														},
												"RIGHT":	{
															"DIST_FEM":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
														}

											}
								}		

	def click(self, event):
		print("click from " + self.name)

		if self.side == None:
			print("please choose side")
			self.controller.warningBox("Please select a Side")
		else:
			# print(self.dict)
			ret =  self.addDict(event)
			if ret:										
				self.controller.save_json()
				# pass

		self.controller.updateMenuLabel(self.getNextLabel(), self.menu_label)
		self.draw_tools.clear_by_tag(self.tag)
		self.draw()


	def addDict(self, event):
		for item in self.dict["VCA"][self.op_type][self.side]:
			
			# get real coords
			P = self.draw_tools.getRealCoords(event)

			# get item type 
			item_type = self.dict["VCA"][self.op_type][self.side][item]["type"]
			print(item)

			# point has P1 and P2, M1 is calculated
			if item_type == "midpoint":

				# check if P1 is None				
				if self.dict["VCA"][self.op_type][self.side][item]["P1"] == None:
					
					self.dict["VCA"][self.op_type][self.side][item]["P1"] = P
					self.draw_tools.setHoverPointLabel("P1_VCA")
					self.draw_tools.setHoverPoint(P)
					self.draw_tools.setHoverBool(True)
					return True


				# check if P2 is None				
				if self.dict["VCA"][self.op_type][self.side][item]["P2"] == None:					
					self.dict["VCA"][self.op_type][self.side][item]["P2"] = P
					M = self.draw_tools.midpoint(self.dict["VCA"][self.op_type][self.side][item]["P1"], P)
					self.dict["VCA"][self.op_type][self.side][item]["M1"] = M
					self.draw_tools.setHoverBool(False)
					self.draw_tools.setHoverPointLabel(None)
					return True
		return False



	# menu button clicks are routed here
	def menu_btn_click(self, action):
		print(action)
		if action == "SET-LEFT":
			self.side = "LEFT"

		if action == "SET-RIGHT":
			self.side = "RIGHT"

		if action == "DEL-LEFT-DIST-FEM":
			self.dict["VCA"][self.op_type]["LEFT"]["DIST_FEM"]["P1"] = None
			self.dict["VCA"][self.op_type]["LEFT"]["DIST_FEM"]["P2"] = None
			self.dict["VCA"][self.op_type]["LEFT"]["DIST_FEM"]["M1"] = None

			self.dict["EXCEL"][self.op_type]["LEFT"]["VCA"] = None

			self.draw_tools.clear_by_tag(self.tag)
			self.draw()
			self.controller.save_json()

		if action == "DEL-RIGHT-DIST-FEM":
			self.dict["VCA"][self.op_type]["RIGHT"]["DIST_FEM"]["P1"] = None
			self.dict["VCA"][self.op_type]["RIGHT"]["DIST_FEM"]["P2"] = None
			self.dict["VCA"][self.op_type]["RIGHT"]["DIST_FEM"]["M1"] = None

			self.dict["EXCEL"][self.op_type]["RIGHT"]["VCA"] = None



			self.draw_tools.clear_by_tag(self.tag)
			self.draw()
			self.controller.save_json()

		self.controller.updateMenuLabel(self.getNextLabel(), self.menu_label)



	def draw(self):

		self.draw_tools.clear_by_tag(self.tag)
		
		# loop left and right
		for side in ["LEFT","RIGHT"]:


			# ------------------------
			# FROM VCA
			# ------------------------

			dist_fem_p1 = self.dict["VCA"][self.op_type][side]["DIST_FEM"]["P1"]
			dist_fem_p2 = self.dict["VCA"][self.op_type][side]["DIST_FEM"]["P2"]
			dist_fem_m1 = self.dict["VCA"][self.op_type][side]["DIST_FEM"]["M1"]

			isDist = False

			if dist_fem_p1 != None:
				self.draw_tools.create_mypoint(dist_fem_p1, "orange", [self.tag, side, "P1_DIST_FEM"])

			if dist_fem_p2 != None:
				self.draw_tools.create_mypoint(dist_fem_p2, "orange", [self.tag, side, "P2_DIST_FEM"])

			if dist_fem_p1 != None and dist_fem_p2 != None:				
				self.draw_tools.create_midpoint_line(dist_fem_p1, dist_fem_p2, dist_fem_m1, [self.tag,side,"DIST_FEM_LINE"])
				isDist = True


			# ------------------------
			# FROM MAIN
			# ------------------------
			isHip = False
			isKnee = False

			hip = self.dict["MAIN"][self.op_type][side]["HIP"]["P1"]
			knee = self.dict["MAIN"][self.op_type][side]["FEM_KNEE"]["P1"]


			# HIP
			if hip != None:
				isHip = True
				self.draw_tools.create_mypoint(hip, "orange", [self.tag, side, "NO-DRAG"])

			# KNEE
			if knee != None:
				isKnee = True
				self.draw_tools.create_mypoint(knee, "orange", [self.tag, side, "NO-DRAG"])

			# HIP-KNEE-LINE
			if hip != None and knee != None:
				self.draw_tools.create_myline(hip, knee, self.tag)


			if isHip and isKnee and isDist:
				self.draw_tools.create_myline(dist_fem_m1, knee, [self.tag,side,"VCA_ANGLE"])


				a1 = self.draw_tools.getAnglePoints(hip, knee, dist_fem_m1)
				a2 = self.draw_tools.getAnglePoints(dist_fem_m1, knee, hip)
				print('{0:.2f} a1 RIGHT'.format(a1))
				print('{0:.2f} a2 RIGHT'.format(a2))

				if a1 > a2:					
					angle = self.draw_tools.create_myAngle(dist_fem_m1, knee, hip, self.tag)
				else:					
					angle = self.draw_tools.create_myAngle(hip, knee, dist_fem_m1, self.tag)

				self.draw_tools.create_mytext(dist_fem_m1, '{0:.2f}'.format(angle), [self.tag,side,"VCA_ANGLE"], x_offset=0, y_offset=-60, color="blue")


				# check if value exists
				if self.dict["EXCEL"][self.op_type][side]["VCA"] == None:

					self.dict["EXCEL"][self.op_type][side]["HASDATA"] 	= True
					# self.dict["EXCEL"][self.op_type][side]["VCA"]	 	= '{0:.2f}'.format(angle)
					self.dict["EXCEL"][self.op_type][side]["VCA"]	 	= '{0:.2f}'.format(angle)

					# save after insert
					self.controller.save_json()


	def hover(self, P_mouse, P_stored, hover_label):
		if hover_label == "P1_VCA":
			self.draw_tools.clear_by_tag("hover_line")
			m = self.draw_tools.midpoint(P_stored, P_mouse)
			self.draw_tools.create_midpoint_line(P_stored, P_mouse, m, "hover_line")
	def regainHover(self, side):
		pass

	def escapeObjFunc(self):
		self.side = None
		self.draw_tools.setHoverPointLabel(None)
		self.draw_tools.setHoverBool(False)



	def drag_start(self, tags):
		tags.remove('token')
		tags.remove('current')
		tags.remove(self.tag)
		print(tags)
		

		side = ""

		# find side
		if "LEFT" in tags:
			side = "LEFT"
		elif "RIGHT" in tags:
			side = "RIGHT"


		if "P1_DIST_FEM" in tags:
			self.drag_point = self.dict["VCA"][self.op_type][side]["DIST_FEM"]["P2"]
			self.drag_label = "P1_DIST_FEM"
			self.drag_side 	= side
		elif "P2_DIST_FEM" in tags:
			self.drag_point = self.dict["VCA"][self.op_type][side]["DIST_FEM"]["P1"]
			self.drag_label = "P2_DIST_FEM"
			self.drag_side 	= side
		else:
			self.drag_point = None
			self.drag_label = None
			self.drag_side 	= None
		


			
	def drag(self, P_mouse):
		
		if self.drag_label == "P1_DIST_FEM" and self.drag_point != None or self.drag_label == "P2_DIST_FEM" and self.drag_point != None:
			self.draw_tools.clear_by_tag("DIST_FEM_LINE")
			self.draw_tools.clear_by_tag("VCA_ANGLE")
			
			self.draw_tools.clear_by_tag("drag_line")
			m = self.draw_tools.midpoint(self.drag_point, P_mouse)
			self.draw_tools.create_midpoint_line(self.drag_point, P_mouse, m, "drag_line")

	def drag_stop(self, P_mouse):
		self.draw_tools.clear_by_tag("drag_line")

		if self.drag_label == "P1_DIST_FEM":
			self.dict["VCA"][self.op_type][self.drag_side]["DIST_FEM"]["P1"] = P_mouse
			self.dict["VCA"][self.op_type][self.drag_side]["DIST_FEM"]["M1"] = self.draw_tools.midpoint(self.drag_point, P_mouse)
		elif self.drag_label == "P2_DIST_FEM":
			self.dict["VCA"][self.op_type][self.drag_side]["DIST_FEM"]["P2"] = P_mouse
			self.dict["VCA"][self.op_type][self.drag_side]["DIST_FEM"]["M1"] = self.draw_tools.midpoint(self.drag_point, P_mouse)

		self.controller.save_json()
		self.draw()

	def update_canvas(self, draw_tools):
		self.draw_tools = draw_tools


	def update_dict(self, master_dict):
		self.dict = master_dict		


	def getNextLabel(self):

		if self.side != None:
			
			for item in self.dict["VCA"][self.op_type][self.side]:

				# get item type 
				item_type = self.dict["VCA"][self.op_type][self.side][item]["type"]


				# point has P1 and P2, M1 is calculated
				if item_type == "midpoint":

					# check if P1 is None				
					if self.dict["VCA"][self.op_type][self.side][item]["P1"] == None:
						return (self.side + " " + item + " P1")


					# check if P2 is None				
					if self.dict["VCA"][self.op_type][self.side][item]["P2"] == None:
						return (self.side + " " + item + " P2")

			return (self.side + " Done")

		return None


	def unset(self):
		# print("unset from "+self.name)
		self.draw_tools.clear_by_tag(self.tag)