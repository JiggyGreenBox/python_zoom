

class MAD():
	"""docstring for ClassName"""
	def __init__(self, draw_tools, master_dict, controller, op_type):
		self.name = "MAD"
		self.tag = "mad"
		self.menu_label = "MAD_Menu"
		self.draw_tools = draw_tools
		self.dict = master_dict		
		self.controller = controller
		self.side = None
		self.op_type = op_type

		# check if master dictionary has values
		# if not populate the dictionary
		# self.checkMasterDict()		

		self.point_size = None

		
	def checkMasterDict(self):
		if "MAD" not in self.dict.keys():
			self.dict["MAD"] = 	{
									"PRE-OP":{
											"LEFT":	{
														"MAD_LINE":	{"type":"line","P1":None,"P2":None}
													},
											"RIGHT":{
														"MAD_LINE":	{"type":"line","P1":None,"P2":None}
													}
											},

									"POST-OP":{
											"LEFT":	{
														"MAD_LINE":	{"type":"line","P1":None,"P2":None}
													},
											"RIGHT":{
														"MAD_LINE":	{"type":"line","P1":None,"P2":None}
													}
											}
									}

	def click(self, event):
		print("click from "+self.name)

		# if self.side == None:
		# 	print("please choose side")
		# 	self.controller.warningBox("Please select a Side")
		# else:
		# 	# print(self.dict)			
		# 	ret =  self.addDict(event)
		# 	if ret:
		# 		self.controller.save_json()
		# 		# pass


		# self.controller.updateMenuLabel(self.getNextLabel(), self.menu_label)		
		self.draw()



	# def getNextLabel(self):
	# 	if self.side != None:
	# 		for item in self.dict["MAD"][self.op_type][self.side]:
				
	# 			# get item type 
	# 			item_type = self.dict["MAD"][self.op_type][self.side][item]["type"]

	# 			# line has P1 and P2
	# 			if item_type == "line":

	# 				# check if P1 is None				
	# 				if self.dict["MAD"][self.op_type][self.side][item]["P1"] == None:
	# 					return (self.side + " " + item + " P1")


	# 				# check if P2 is None				
	# 				if self.dict["MAD"][self.op_type][self.side][item]["P2"] == None:
	# 					return (self.side + " " + item + " P2")

	# 			return (self.side + " Done")
	# 	return None

	def draw(self):

		self.draw_tools.clear_by_tag(self.tag)

		self.point_size = self.controller.getViewPointSize()

		# loop left and right
		for side in ["LEFT","RIGHT"]:

			hip 		= self.dict["MAIN"][self.op_type][side]["HIP"]["P1"]
			
			ankle_p1 	= self.dict["MAIN"][self.op_type][side]["ANKLE"]["P1"]
			ankle_p2 	= self.dict["MAIN"][self.op_type][side]["ANKLE"]["P2"]
			ankle_m1 	= self.dict["MAIN"][self.op_type][side]["ANKLE"]["M1"]

			mad_p1 = self.dict["MAIN"][self.op_type][side]["MAD_LINE"]["P1"]
			mad_p2 = self.dict["MAIN"][self.op_type][side]["MAD_LINE"]["P2"]

			if hip != None:
				isHip = True
				self.draw_tools.create_mypoint(hip, "orange", [self.tag, side, "NO-DRAG"], point_thickness=self.point_size)

			# ANKLE
			if ankle_p1 != None and ankle_p2 != None:
				self.draw_tools.create_mypoint(ankle_p1, "orange", [self.tag, side, "NO-DRAG"], point_thickness=self.point_size)
				self.draw_tools.create_mypoint(ankle_p2, "orange", [self.tag, side, "NO-DRAG"], point_thickness=self.point_size)
				self.draw_tools.create_midpoint_line(ankle_p1, ankle_p2, ankle_m1, self.tag, point_thickness=self.point_size)



			if hip != None and ankle_p1 != None and ankle_p2 != None:
				self.draw_tools.create_myline(ankle_m1, hip, self.tag)

			# ------------------------
			# FROM MAD
			# ------------------------
			if mad_p1 != None:
				self.draw_tools.create_mypoint(mad_p1, "orange", [self.tag, side, "P1_MAD_LINE"], point_thickness=self.point_size)

			if mad_p2 != None:
				self.draw_tools.create_mypoint(mad_p2, "orange", [self.tag, side, "P2_MAD_LINE"], point_thickness=self.point_size)

			if mad_p1 != None and mad_p2 != None:
				self.draw_tools.create_myline(mad_p1, mad_p2, [self.tag,side,"MAD_LINE"])
				# isTamd = True

				# draw the points for division
				self.draw_tools.create_mypoint(self.draw_tools.getLineSegmentByPercentage(0.2, mad_p1, mad_p2), "orange", [self.tag, side, "MAD_LINE"], point_thickness=self.point_size)
				self.draw_tools.create_mypoint(self.draw_tools.getLineSegmentByPercentage(0.4, mad_p1, mad_p2), "orange", [self.tag, side, "MAD_LINE"], point_thickness=self.point_size)
				self.draw_tools.create_mypoint(self.draw_tools.getLineSegmentByPercentage(0.6, mad_p1, mad_p2), "orange", [self.tag, side, "MAD_LINE"], point_thickness=self.point_size)
				self.draw_tools.create_mypoint(self.draw_tools.getLineSegmentByPercentage(0.8, mad_p1, mad_p2), "orange", [self.tag, side, "MAD_LINE"], point_thickness=self.point_size)


				if side == "RIGHT":
					L_mad, R_mad = self.draw_tools.retPointsLeftRight(mad_p1,mad_p2)
				else:
					# invert the direction for the LEFT case
					R_mad, L_mad = self.draw_tools.retPointsLeftRight(mad_p1,mad_p2)


				self.draw_tools.create_mytext(self.draw_tools.getLineSegmentByPercentage(0.1, L_mad, R_mad), y_offset=-10, mytext="4", mytag=[self.tag, side, "MAD_LINE"], color="blue")
				self.draw_tools.create_mytext(self.draw_tools.getLineSegmentByPercentage(0.3, L_mad, R_mad), y_offset=-10, mytext="3", mytag=[self.tag, side, "MAD_LINE"], color="blue")
				self.draw_tools.create_mytext(self.draw_tools.getLineSegmentByPercentage(0.5, L_mad, R_mad), y_offset=-10, mytext="C", mytag=[self.tag, side, "MAD_LINE"], color="blue")
				self.draw_tools.create_mytext(self.draw_tools.getLineSegmentByPercentage(0.7, L_mad, R_mad), y_offset=-10, mytext="2", mytag=[self.tag, side, "MAD_LINE"], color="blue")
				self.draw_tools.create_mytext(self.draw_tools.getLineSegmentByPercentage(0.9, L_mad, R_mad), y_offset=-10, mytext="1", mytag=[self.tag, side, "MAD_LINE"], color="blue")



	def addDict(self, event):
		for item in self.dict["MAD"][self.op_type][self.side]:

			# get real coords
			P = self.draw_tools.getRealCoords(event)
			
			# get item type 
			item_type = self.dict["MAD"][self.op_type][self.side][item]["type"]

			# line has P1 and P2
			if item_type == "line":

				# check if P1 is None				
				if self.dict["MAD"][self.op_type][self.side][item]["P1"] == None:
					
					self.dict["MAD"][self.op_type][self.side][item]["P1"] = P
					self.draw_tools.setHoverPointLabel("P1_MAD")
					self.draw_tools.setHoverPoint(P)
					self.draw_tools.setHoverBool(True)
					return True


				# check if P2 is None				
				if self.dict["MAD"][self.op_type][self.side][item]["P2"] == None:					
					self.dict["MAD"][self.op_type][self.side][item]["P2"] = P
					self.draw_tools.setHoverBool(False)
					self.draw_tools.setHoverPointLabel(None)
					return True

		return False


	# menu button clicks are routed here
	# def menu_btn_click(self, action):
	# 	print(action)
	# 	if action == "SET-LEFT":
	# 		self.side = "LEFT"
	# 		self.controller.updateMenuLabel(self.getNextLabel(), self.menu_label)
	# 		self.draw()
	# 		self.regainHover(self.side)
	# 		return

	# 	if action == "SET-RIGHT":
	# 		self.side = "RIGHT"
	# 		self.controller.updateMenuLabel(self.getNextLabel(), self.menu_label)
	# 		self.draw()
	# 		self.regainHover(self.side)
	# 		return

	# 	if action == "DEL-LEFT-MAD-LINE":
	# 		self.dict["MAD"][self.op_type]["LEFT"]["MAD_LINE"]["P1"] = None
	# 		self.dict["MAD"][self.op_type]["LEFT"]["MAD_LINE"]["P2"] = None
	# 		self.dict["EXCEL"][self.op_type]["LEFT"]["MAD"] = None 	# delete excel data from pat.json
	# 		self.draw()
	# 		self.controller.save_json()

	# 	if action == "DEL-RIGHT-MAD-LINE":
	# 		self.dict["MAD"][self.op_type]["RIGHT"]["MAD_LINE"]["P1"] = None
	# 		self.dict["MAD"][self.op_type]["RIGHT"]["MAD_LINE"]["P2"] = None
	# 		self.dict["EXCEL"][self.op_type]["RIGHT"]["MAD"] = None 	# delete excel data from pat.json
	# 		self.draw()
	# 		self.controller.save_json()

	# 	self.controller.updateMenuLabel(self.getNextLabel(), self.menu_label)


	# def drag_start(self, tags):
	# 	tags.remove('token')
	# 	tags.remove('current')
	# 	tags.remove(self.tag)
	# 	print(tags)
		

	# 	side = ""

	# 	# find side
	# 	if "LEFT" in tags:
	# 		side = "LEFT"
	# 	elif "RIGHT" in tags:
	# 		side = "RIGHT"

	# 	if "P1_MAD_LINE" in tags:
	# 		self.drag_point = self.dict["MAD"][self.op_type][side]["MAD_LINE"]["P2"]
	# 		self.drag_label = "P1_MAD_LINE"
	# 		self.drag_side 	= side
	# 	elif "P2_MAD_LINE" in tags:
	# 		self.drag_point = self.dict["MAD"][self.op_type][side]["MAD_LINE"]["P1"]
	# 		self.drag_label = "P2_MAD_LINE"
	# 		self.drag_side 	= side

	# 	else:
	# 		self.drag_point = None
	# 		self.drag_label = None
	# 		self.drag_side 	= None

	# def drag(self, P_mouse):
	# 	if self.drag_label == "P1_MAD_LINE" and self.drag_point != None or self.drag_label == "P2_MAD_LINE" and self.drag_point != None:
	# 		self.draw_tools.clear_by_tag("MAD_LINE")			
	# 		self.draw_tools.clear_by_tag("drag_line")
	# 		self.draw_tools.create_myline(P_mouse, self.drag_point, "drag_line")

	# def drag_stop(self, P_mouse):
	# 	self.draw_tools.clear_by_tag("drag_line")

	# 	if self.drag_label == "P1_MAD_LINE":
	# 		self.dict["MAD"][self.op_type][self.drag_side]["MAD_LINE"]["P1"] = P_mouse
	# 		self.dict["EXCEL"][self.op_type][self.drag_side]["MAD"] = None 	# delete excel data from pat.json

	# 	elif self.drag_label == "P2_MAD_LINE":
	# 		self.dict["MAD"][self.op_type][self.drag_side]["MAD_LINE"]["P2"] = P_mouse
	# 		self.dict["EXCEL"][self.op_type][self.drag_side]["MAD"] = None 	# delete excel data from pat.json

	# 	self.controller.save_json()
	# 	self.draw()	

	# def hover(self, P_mouse, P_stored, hover_label):
	# 	if hover_label == "P1_MAD":
	# 		self.draw_tools.clear_by_tag("hover_line")
	# 		self.draw_tools.create_myline(P_mouse, P_stored, "hover_line")

	# def regainHover(self, side):
	# 	pass

	def escapeObjFunc(self):
		self.side = None
		self.draw_tools.setHoverPointLabel(None)
		self.draw_tools.setHoverBool(False)


	def update_canvas(self, draw_tools):
		self.draw_tools = draw_tools

	def update_dict(self, master_dict):
		self.dict = master_dict

	def unset(self):
		# print("unset from "+self.name)
		self.draw_tools.clear_by_tag(self.tag)
		self.side = None


	# def getLineSegmentByPercentage(self, percent, p1, p2):
	# 	# Cx = Ax * (1-t) + Bx * t
	# 	# Cy = Ay * (1-t) + By * t

		
	# 	# Cx = Ax * (1-t) + Bx * t
	# 	# X = (x1*(1-percent)) + (x2*percent)
	# 	# X = p1[0]*(1-percent) + p2[0] * percent

	# 	# Cy = Ay * (1-t) + By * t  
	# 	# Y = (y1*(1-percent)) + (y2*percent)
	# 	# Y = p1[1]*(1-percent) + p2[1]*percent
		
	# 	return (p1[0]*(1-percent) + p2[0]*percent, p1[1]*(1-percent) + p2[1]*percent)


	def drag_start(self, P_mouse):
		pass
	def drag(self, P_mouse):
		pass
	def drag_stop(self, P_mouse):
		pass
	def menu_btn_click(self, action):
		pass
	def getNextLabel(self):
		pass
	def hover(self, P_mouse, P_stored, hover_label):
		pass
	def regainHover(self, side):
		pass

	# similiar to draw but nothing is drawn on the canvas
	def updateExcelValues(self):
		pass						