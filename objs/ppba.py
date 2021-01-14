

class PPBA():
	"""docstring for ClassName"""
	def __init__(self, draw_tools, master_dict, controller, op_type):
		self.name = "PPBA"
		self.tag = "ppba"
		self.menu_label = "PPBA_Menu"
		self.draw_tools = draw_tools
		self.dict = master_dict
		self.controller = controller
		self.side = None
		self.op_type = op_type

		# check if master dictionary has values
		# if not populate the dictionary
		self.checkMasterDict()


	def click(self, event):
		# print("click from "+self.name)
		# self.draw()
		if self.side == None:
			print("please choose side")
			self.controller.warningBox("Please select a Side")
			self.controller.testbubble()
			print(self.dict)
		else:
			ret =  self.addDict(event)
			if ret:
				self.controller.save_json()
				# pass

		self.controller.updateMenuLabel(self.getNextLabel(), self.menu_label)		
		self.draw()


	# menu button clicks are routed here
	def menu_btn_click(self, action):
		print(action)
		if action == "SET-LEFT":
			self.side = "LEFT"
			self.controller.updateMenuLabel(self.getNextLabel(), self.menu_label)
			self.regainHover(self.side)
			return # avoid clear,draw,json_save

		if action == "SET-RIGHT":
			self.side = "RIGHT"			
			self.controller.updateMenuLabel(self.getNextLabel(), self.menu_label)
			self.regainHover(self.side)
			return # avoid clear,draw,json_save


		if action == "DEL-LEFT-P1":
			self.dict[self.name][self.op_type]["LEFT"]["KNEE_CAP_LINE"]["P1"] = None
			self.side = "LEFT"

		if action == "DEL-RIGHT-P1":
			self.dict[self.name][self.op_type]["RIGHT"]["KNEE_CAP_LINE"]["P1"] = None
			self.side = "RIGHT"

		if action == "DEL-LEFT-P2":
			self.dict[self.name][self.op_type]["LEFT"]["KNEE_CAP_LINE"]["P2"] = None
			self.side = "LEFT"

		if action == "DEL-RIGHT-P2":
			self.dict[self.name][self.op_type]["RIGHT"]["KNEE_CAP_LINE"]["P2"] = None
			self.side = "RIGHT"


		# delete excel data from pat.json
		self.dict["EXCEL"][self.op_type][self.side]["PPBA"] = None

		self.draw()
		self.regainHover(self.side)

		self.controller.save_json()
		self.controller.updateMenuLabel(self.getNextLabel(), self.menu_label)			



	def draw(self):
		# self.draw_tools.clear_by_tag("hover_line")
		self.draw_tools.clear_by_tag(self.tag)
		# loop left and right				
		for side in ["LEFT","RIGHT"]:
			
				
			line1 = False
			line2 = False

			# from P-TILT
			# p1 = self.dict["P_TILT"][self.op_type][side]["P1P2_LINE"]["P1"]
			# p2 = self.dict["P_TILT"][self.op_type][side]["P1P2_LINE"]["P2"]

			p1 = self.dict["P_TILT"][self.op_type][side]["PAT_CROSS_SECTION"]["P1"]
			p2 = self.dict["P_TILT"][self.op_type][side]["PAT_CROSS_SECTION"]["P2"]

			
			knee_cap_line_p1 = self.dict["PPBA"][self.op_type][side]["KNEE_CAP_LINE"]["P1"]
			knee_cap_line_p2 = self.dict["PPBA"][self.op_type][side]["KNEE_CAP_LINE"]["P2"]

			
			if p1 != None:
				self.draw_tools.create_mypoint(p1, "orange", [self.tag, side, "NO-DRAG"])
			if p2 != None:
				self.draw_tools.create_mypoint(p2, "orange", [self.tag, side, "NO-DRAG"])
			if p1 != None and p2 != None:
				self.draw_tools.create_myline(p1, p2, [self.tag, side, "NO-DRAG"])
				line1 = True


			if knee_cap_line_p1 != None:
				self.draw_tools.create_mypoint(knee_cap_line_p1, "orange", [self.tag, side, "KNEE_P1"])
				self.draw_tools.create_mytext(knee_cap_line_p1, "P1", [self.tag,"P_LABEL"], y_offset=30)
			if knee_cap_line_p2 != None:
				self.draw_tools.create_mypoint(knee_cap_line_p2, "orange", [self.tag, side, "KNEE_P2"])
				self.draw_tools.create_mytext(knee_cap_line_p2, "P2", [self.tag,"P_LABEL"], y_offset=30)
			if knee_cap_line_p1 != None and knee_cap_line_p2 != None:
				self.draw_tools.create_myline(knee_cap_line_p1, knee_cap_line_p2, [self.tag, side, "KNEE_LINE"])
				line2 = True

			if line1 and line2:
				p_int = self.draw_tools.line_intersection((knee_cap_line_p1, knee_cap_line_p2),(p1, p2))

				angle = self.draw_tools.getSmallestAngle(p1, p_int, knee_cap_line_p1)
				self.draw_tools.create_mytext(p2, '{0:.2f}'.format(angle), [self.tag,"PPBA_ANGLE"], y_offset=-40, color="blue")

				# check if value exists
				if self.dict["EXCEL"][self.op_type][side]["PPBA"] == None:
				# if self.dict["EXCEL"][self.op_type][side]["TSLOPE"] == None:
					self.dict["EXCEL"][self.op_type][side]["HASDATA"] 	= True
					self.dict["EXCEL"][self.op_type][side]["PPBA"]	= '{0:.2f}'.format(angle)
					# save after insert
					self.controller.save_json()
			

			# if isP2 and isP3:							
			# 	self.draw_tools.create_myline(p2, p3, [self.tag, side, "P2P3_line"])

			# if isP1 and isP2 and isP3:
			# 	p2p3_dist = self.draw_tools.getDistance(p2, p3)
			# 	p1p2_dist = self.draw_tools.getDistance(p1, p2)
			# 	isr_val = p2p3_dist / p1p2_dist
			# 	print('isr_val: {}'.format(isr_val))
			# 	print('isr_val: {:.2f}'.format(isr_val))

			# 	if side == "RIGHT":
			# 		self.draw_tools.create_mytext(p2, x_offset=60, color="blue", mytext='{:.2f}'.format(isr_val), mytag=[self.tag, side, "ISR_LABEL"])
			# 	elif side == "LEFT":
			# 		self.draw_tools.create_mytext(p2, x_offset=-60, color="blue", mytext='{:.2f}'.format(isr_val), mytag=[self.tag, side, "ISR_LABEL"])



	def checkMasterDict(self):
		if "PPBA" not in self.dict.keys():
			self.dict["PPBA"] = 	{
									"PRE-OP":{
										"LEFT":	{
											"KNEE_CAP_LINE":	{"type":"line","P1":None,"P2":None}
										},
										"RIGHT":{
											"KNEE_CAP_LINE":	{"type":"line","P1":None,"P2":None}
										}
									},
									"POST-OP":{
										"LEFT":	{
											"KNEE_CAP_LINE":	{"type":"line","P1":None,"P2":None}
										},
										"RIGHT":{
											"KNEE_CAP_LINE":	{"type":"line","P1":None,"P2":None}
										}
									}
								}


	def addDict(self, event):
		for item in self.dict["PPBA"][self.op_type][self.side]:
			
			P = self.draw_tools.getRealCoords(event)
			
			if self.dict["PPBA"][self.op_type][self.side]["KNEE_CAP_LINE"]["P1"] == None:
				self.dict["PPBA"][self.op_type][self.side]["KNEE_CAP_LINE"]["P1"] = P

				if self.dict["PPBA"][self.op_type][self.side]["KNEE_CAP_LINE"]["P2"] == None:
					self.draw_tools.setHoverPoint(P)
					self.draw_tools.setHoverPointLabel("P1")
					self.draw_tools.setHoverBool(True)
				else:
					self.draw_tools.setHoverBool(False)
					self.draw_tools.setHoverPointLabel(None)
				return True

			if self.dict["PPBA"][self.op_type][self.side]["KNEE_CAP_LINE"]["P2"] == None:
				self.dict["PPBA"][self.op_type][self.side]["KNEE_CAP_LINE"]["P2"] = P

				if self.dict["PPBA"][self.op_type][self.side]["KNEE_CAP_LINE"]["P1"] == None:
					self.draw_tools.setHoverPoint(P)
					self.draw_tools.setHoverPointLabel("P1")
					self.draw_tools.setHoverBool(True)
				else:
					self.draw_tools.setHoverBool(False)
					self.draw_tools.setHoverPointLabel(None)
				return True
		return False


	def getNextLabel(self):

		if self.side != None:
			for item in self.dict["ISR"][self.op_type][self.side]:

				if self.dict["ISR"][self.op_type][self.side][item]["P1"] == None:					
					return (self.side + " " + item)

			return (self.side + " Done")

		return None							

	def hover(self, P_mouse, P_stored, hover_label):

		if hover_label == "P1":
			if P_stored != None:
				self.draw_tools.clear_by_tag("hover_line")
				self.draw_tools.create_myline(P_stored, P_mouse, "hover_line")


	def regainHover(self, side):
		
		knee_p1 = self.dict["PPBA"][self.op_type][side]["KNEE_CAP_LINE"]["P1"]
		knee_p2 = self.dict["PPBA"][self.op_type][side]["KNEE_CAP_LINE"]["P2"]		

		if knee_p1 == None and knee_p2 == None:
			self.draw_tools.setHoverBool(False)
			self.draw_tools.setHoverPointLabel(None)

		if knee_p1 == None and knee_p2 != None:
			self.draw_tools.setHoverPoint(knee_p2)
			self.draw_tools.setHoverPointLabel("P1")
			self.draw_tools.setHoverBool(True)

		if knee_p1 != None and knee_p2 == None:
			self.draw_tools.setHoverPoint(knee_p1)
			self.draw_tools.setHoverPointLabel("P1")
			self.draw_tools.setHoverBool(True)


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


		# dissallow drag from other objects
		if "NO-DRAG" in tags:
			self.drag_point = None
			self.drag_label = "NO-DRAG"
			self.drag_side 	= None



		# vars for code readability
		knee_cap_line_p1 = self.dict["PPBA"][self.op_type][side]["KNEE_CAP_LINE"]["P1"]
		knee_cap_line_p2 = self.dict["PPBA"][self.op_type][side]["KNEE_CAP_LINE"]["P2"]

		


		if "KNEE_P1" in tags:
			
			self.draw_tools.clear_by_tag("KNEE_LINE")
			self.draw_tools.clear_by_tag("PPBA_ANGLE")
			self.drag_point = knee_cap_line_p2
			self.drag_label = "KNEE_P1"
			self.drag_side 	= side


		if "KNEE_P2" in tags:
			
			self.draw_tools.clear_by_tag("KNEE_LINE")
			self.draw_tools.clear_by_tag("PPBA_ANGLE")
			self.drag_point = knee_cap_line_p1
			self.drag_label = "KNEE_P2"
			self.drag_side 	= side


	def drag(self, P_mouse):
		if self.drag_label == "DRAG":
			pass




		if self.drag_label == "KNEE_P1" or self.drag_label == "KNEE_P2":
			self.draw_tools.clear_by_tag("P_LABEL")
			self.draw_tools.clear_by_tag("drag_line")
			if self.drag_point != None:
				self.draw_tools.create_myline(self.drag_point, P_mouse, "drag_line")




	def drag_stop(self, P_mouse):
		self.draw_tools.clear_by_tag("drag_line")

		# # FEM JOINT LINE
		if self.drag_label == "KNEE_P1":
			self.dict["PPBA"][self.op_type][self.drag_side]["KNEE_CAP_LINE"]["P1"] = P_mouse		
			self.dict["EXCEL"][self.op_type][self.drag_side]["PPBA"] = None	# delete excel data from pat.json
			self.controller.save_json()
			self.draw()

		if self.drag_label == "KNEE_P2":
			self.dict["PPBA"][self.op_type][self.drag_side]["KNEE_CAP_LINE"]["P2"] = P_mouse
			self.dict["EXCEL"][self.op_type][self.drag_side]["PPBA"] = None	# delete excel data from pat.json
			self.controller.save_json()
			self.draw()
			


	def getPointCount(self, side):
		p1 = self.dict["ISR"][self.op_type][side]["P1"]["P1"]
		p2 = self.dict["ISR"][self.op_type][side]["P2"]["P1"]
		p3 = self.dict["ISR"][self.op_type][side]["P3"]["P1"]

		count = 0
		p_hover = None
		for p in [p1,p2,p3]:
			# print('p {}'.format(p))
			if p != None:
				count = count+1
				p_hover = p			

		return count, p_hover

	def update_canvas(self, draw_tools):
		self.draw_tools = draw_tools

	def update_dict(self, master_dict):
		self.dict = master_dict

	def unset(self):
		# print("unset from "+self.name)
		self.draw_tools.setHoverPointLabel(None)
		self.draw_tools.setHoverBool(False)
		self.draw_tools.clear_by_tag(self.tag)