

class MPTA():
	"""docstring for ClassName"""
	def __init__(self, draw_tools, master_dict, controller, op_type):
		self.name = "MPTA"
		self.tag = "mpta"
		self.menu_label = "MPTA_Menu"
		self.draw_tools = draw_tools
		self.dict = master_dict
		self.controller = controller
		self.side = None
		self.op_type = op_type

		# check if master dictionary has values
		# if not populate the dictionary
		self.checkMasterDict()


	def checkMasterDict(self):
		if "MPTA" not in self.dict.keys():
			self.dict["MPTA"] = 	{
									"PRE-OP":{
											"LEFT":	{
														"TIB_JOINT_LINE":	{"type":"line","P1":None,"P2":None}
													},
											"RIGHT":{
														"TIB_JOINT_LINE":	{"type":"line","P1":None,"P2":None}
													}
											},

									"POST-OP":{
											"LEFT":	{
														"TIB_JOINT_LINE":	{"type":"line","P1":None,"P2":None}
													},
											"RIGHT":{
														"TIB_JOINT_LINE":	{"type":"line","P1":None,"P2":None}
													}
											}
									}


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


		self.controller.updateMenuLabel(self.getNextLabel(), self.menu_label)		
		self.draw()

	def draw(self):

		self.draw_tools.clear_by_tag(self.tag)

		# loop left and right
		for side in ["LEFT","RIGHT"]:

			isKnee = False			
			isTamd = False

			tib_joint_p1 = self.dict["MPTA"][self.op_type][side]["TIB_JOINT_LINE"]["P1"]
			tib_joint_p2 = self.dict["MPTA"][self.op_type][side]["TIB_JOINT_LINE"]["P2"]

			knee = self.dict["MAIN"][self.op_type][side]["TIB_KNEE"]["P1"]

			ankle_p1 = self.dict["MAIN"][self.op_type][side]["ANKLE"]["P1"]
			ankle_p2 = self.dict["MAIN"][self.op_type][side]["ANKLE"]["P2"]
			ankle_m1 = self.dict["MAIN"][self.op_type][side]["ANKLE"]["M1"]


			# ------------------------
			# FROM TAMD
			# ------------------------
			if tib_joint_p1 != None:
				self.draw_tools.create_mypoint(tib_joint_p1, "orange", [self.tag, side, "P1_TIB_JOINT_LINE"])

			if tib_joint_p2 != None:
				self.draw_tools.create_mypoint(tib_joint_p2, "orange", [self.tag, side, "P2_TIB_JOINT_LINE"])

			if tib_joint_p1 != None and tib_joint_p2 != None:
				self.draw_tools.create_myline(tib_joint_p1, tib_joint_p2, [self.tag,side,"TIB_JOINT_LINE"])
				isTamd = True


			# ------------------------
			# FROM MAIN
			# ------------------------
			# KNEE
			if knee != None:
				isKnee = True
				self.draw_tools.create_mypoint(knee, "orange", [self.tag, side, "NO-DRAG"])


			# ANKLE
			if ankle_p1 != None and ankle_p2 != None:
				
				self.draw_tools.create_mypoint(ankle_p1, "orange", [self.tag, side, "NO-DRAG"])
				self.draw_tools.create_mypoint(ankle_p2, "orange", [self.tag, side, "NO-DRAG"])
				self.draw_tools.create_midpoint_line(ankle_p1, ankle_p2, ankle_m1, self.tag)

				if isTamd and isKnee:

					# ankle-knee ray
					xtop, ytop, xbot, ybot = self.draw_tools.getImageCorners()
					p_top = self.draw_tools.line_intersection((ankle_m1, knee), (xtop, ytop))
					self.draw_tools.create_myline(ankle_m1, p_top, self.tag)

						# find angle ray intersection point
					p_int = self.draw_tools.line_intersection(
							(p_top, ankle_m1),
							(tib_joint_p1, tib_joint_p2))


					L_tib, R_tib = self.draw_tools.retPointsLeftRight(tib_joint_p1, tib_joint_p2)

					if side == "RIGHT":
						angle = self.draw_tools.create_myAngle(R_tib, p_int, ankle_m1, [self.tag,side,"MPTA_ANGLE"])
						self.draw_tools.create_mytext(p_int, '{0:.2f}'.format(angle), [self.tag,side,"MPTA_ANGLE"], x_offset=60, y_offset=60, color="blue")

					if side == "LEFT":
						angle = self.draw_tools.create_myAngle(ankle_m1, p_int, L_tib, [self.tag,side,"MPTA_ANGLE"])
						self.draw_tools.create_mytext(p_int, '{0:.2f}'.format(angle), [self.tag,side,"MPTA_ANGLE"], x_offset=-60, y_offset=60, color="blue")


					# check if value exists
					if self.dict["EXCEL"][self.op_type][side]["MPTA"] == None:

						self.dict["EXCEL"][self.op_type][side]["HASDATA"] 	= True
						self.dict["EXCEL"][self.op_type][side]["MPTA"]	 	= '{0:.2f}'.format(angle)

						# save after insert
						self.controller.save_json()


	def addDict(self, event):
		for item in self.dict["MPTA"][self.op_type][self.side]:

			# get real coords
			P = self.draw_tools.getRealCoords(event)
			
			# get item type 
			item_type = self.dict["MPTA"][self.op_type][self.side][item]["type"]

			# line has P1 and P2
			if item_type == "line":

				# check if P1 is None				
				if self.dict["MPTA"][self.op_type][self.side][item]["P1"] == None:
					
					self.dict["MPTA"][self.op_type][self.side][item]["P1"] = P
					self.draw_tools.setHoverPointLabel("P1_MPTA")
					self.draw_tools.setHoverPoint(P)
					self.draw_tools.setHoverBool(True)
					return True


				# check if P2 is None				
				if self.dict["MPTA"][self.op_type][self.side][item]["P2"] == None:					
					self.dict["MPTA"][self.op_type][self.side][item]["P2"] = P
					self.draw_tools.setHoverBool(False)
					self.draw_tools.setHoverPointLabel(None)
					return True

		return False


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

		if "P1_TIB_JOINT_LINE" in tags:
			self.drag_point = self.dict["MPTA"][self.op_type][side]["TIB_JOINT_LINE"]["P2"]
			self.drag_label = "P1_TIB_JOINT_LINE"
			self.drag_side 	= side
		elif "P2_TIB_JOINT_LINE" in tags:
			self.drag_point = self.dict["MPTA"][self.op_type][side]["TIB_JOINT_LINE"]["P1"]
			self.drag_label = "P2_TIB_JOINT_LINE"
			self.drag_side 	= side

		else:
			self.drag_point = None
			self.drag_label = None
			self.drag_side 	= None

	def drag(self, P_mouse):
		if self.drag_label == "P1_TIB_JOINT_LINE" and self.drag_point != None or self.drag_label == "P2_TIB_JOINT_LINE" and self.drag_point != None:
			self.draw_tools.clear_by_tag("TIB_JOINT_LINE")
			self.draw_tools.clear_by_tag("MPTA_ANGLE")
			self.draw_tools.clear_by_tag("drag_line")		
			self.draw_tools.create_myline(P_mouse, self.drag_point, "drag_line")

	def drag_stop(self, P_mouse):
		self.draw_tools.clear_by_tag("drag_line")

		if self.drag_label == "P1_TIB_JOINT_LINE":
			self.dict["MPTA"][self.op_type][self.drag_side]["TIB_JOINT_LINE"]["P1"] = P_mouse
			self.dict["EXCEL"][self.op_type][self.drag_side]["MPTA"] = None 	# delete excel data from pat.json

		elif self.drag_label == "P2_TIB_JOINT_LINE":
			self.dict["MPTA"][self.op_type][self.drag_side]["TIB_JOINT_LINE"]["P2"] = P_mouse
			self.dict["EXCEL"][self.op_type][self.drag_side]["MPTA"] = None 	# delete excel data from pat.json

		self.controller.save_json()
		self.draw()		

	def hover(self, P_mouse, P_stored, hover_label):
		if hover_label == "P1_MPTA":
			self.draw_tools.clear_by_tag("hover_line")
			self.draw_tools.create_myline(P_mouse, P_stored, "hover_line")
	def regainHover(self, side):
		pass
	def escapeObjFunc(self):
		self.side = None
		self.draw_tools.setHoverPointLabel(None)
		self.draw_tools.setHoverBool(False)


	def getNextLabel(self):
		if self.side != None:
			for item in self.dict["MPTA"][self.op_type][self.side]:
				
				# get item type 
				item_type = self.dict["MPTA"][self.op_type][self.side][item]["type"]

				# line has P1 and P2
				if item_type == "line":

					# check if P1 is None				
					if self.dict["MPTA"][self.op_type][self.side][item]["P1"] == None:					
						return (self.side + " " + item + " P1")


					# check if P2 is None				
					if self.dict["MPTA"][self.op_type][self.side][item]["P2"] == None:				
						return (self.side + " " + item + " P2")

				return (self.side + " Done")
		return None


	# menu button clicks are routed here
	def menu_btn_click(self, action):
		print(action)
		if action == "SET-LEFT":
			self.side = "LEFT"

		if action == "SET-RIGHT":
			self.side = "RIGHT"

		if action == "DEL-LEFT-TIB-LINE":
			self.dict["MPTA"][self.op_type]["LEFT"]["TIB_JOINT_LINE"]["P1"] = None
			self.dict["MPTA"][self.op_type]["LEFT"]["TIB_JOINT_LINE"]["P2"] = None
			self.dict["EXCEL"][self.op_type]["LEFT"]["MPTA"] = None 	# delete excel data from pat.json
			self.draw()
			self.controller.save_json()

		if action == "DEL-RIGHT-TIB-LINE":
			self.dict["MPTA"][self.op_type]["RIGHT"]["TIB_JOINT_LINE"]["P1"] = None
			self.dict["MPTA"][self.op_type]["RIGHT"]["TIB_JOINT_LINE"]["P2"] = None
			self.dict["EXCEL"][self.op_type]["RIGHT"]["MPTA"] = None 	# delete excel data from pat.json
			self.draw()
			self.controller.save_json()

		self.controller.updateMenuLabel(self.getNextLabel(), self.menu_label)


	def update_canvas(self, draw_tools):
		self.draw_tools = draw_tools


	def update_dict(self, master_dict):
		self.dict = master_dict


	def unset(self):
		# print("unset from "+self.name)
		self.draw_tools.clear_by_tag(self.tag)	

		