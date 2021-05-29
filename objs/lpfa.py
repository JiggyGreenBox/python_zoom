

class LPFA():
	"""docstring for ClassName"""
	def __init__(self, draw_tools, master_dict, controller, op_type):
		self.name = "LPFA"
		self.tag = "lpfa"
		self.menu_label = "LPFA_Menu"
		self.draw_tools = draw_tools
		self.dict = master_dict
		self.controller = controller
		self.side = None
		self.op_type = op_type

		# check if master dictionary has values
		# if not populate the dictionary
		self.checkMasterDict()

		self.point_size = None

		self.draw_labels = True
		self.draw_hover = True

		self.hover_text = None


		self.mpfa_var = False


	def checkMasterDict(self):
		if "LPFA" not in self.dict.keys():
			self.dict["LPFA"] = 	{
									"PRE-OP":{
												"LEFT":	{
															"TRO_HIP_LINE":	{"type":"point","P1":None}
														},
												"RIGHT":	{
															"TRO_HIP_LINE":	{"type":"point","P1":None}
														}
											},
									"POST-OP":{
												"LEFT":	{
															"TRO_HIP_LINE":	{"type":"point","P1":None}
														},
												"RIGHT":	{
															"TRO_HIP_LINE":	{"type":"point","P1":None}
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
			# find if P0 hovers are required
			self.mainHoverUsingNextLabel()
			if ret:										
				self.controller.save_json()
				# pass

		# self.controller.updateMenuLabel(self.getNextLabel(), self.menu_label)
		# self.draw_tools.clear_by_tag(self.tag)
		self.draw()


	def right_click(self, event):
		pass


	def keyRightObjFunc(self):
		print('set right')
		self.side = "RIGHT"
		self.controller.updateMenuLabel(self.getNextLabel(), self.menu_label)
		self.draw()
		self.regainHover(self.side)

	def keyLeftObjFunc(self):
		print('set left')
		self.side = "LEFT"
		self.controller.updateMenuLabel(self.getNextLabel(), self.menu_label)
		self.draw()
		self.regainHover(self.side)



	def addDict(self, event):
		for item in self.dict["LPFA"][self.op_type][self.side]:
			
			# get real coords
			P = self.draw_tools.getRealCoords(event)

			# get item type 
			item_type = self.dict["LPFA"][self.op_type][self.side][item]["type"]
			# print(item)

			# point only has P1
			if item_type == "point":
				# check if P1 is None				
				if self.dict["LPFA"][self.op_type][self.side][item]["P1"] == None:
					self.dict["LPFA"][self.op_type][self.side][item]["P1"] = P
					self.draw_tools.setHoverBool(False)
					self.draw_tools.setHoverPointLabel(None)
					return True
		return False



	# menu button clicks are routed here
	def menu_btn_click(self, action):
		print(action)
		if action == "SET-LEFT":
			self.side = "LEFT"
			self.controller.updateMenuLabel(self.getNextLabel(), self.menu_label)
			self.draw()
			self.regainHover(self.side)
			return 

		if action == "SET-RIGHT":
			self.side = "RIGHT"
			self.controller.updateMenuLabel(self.getNextLabel(), self.menu_label)
			self.draw()
			self.regainHover(self.side)
			return 

		if action == "DEL-LEFT-TRO-HIP-LINE":
			self.dict["LPFA"][self.op_type]["LEFT"]["TRO_HIP_LINE"]["P1"] = None						
			self.dict["EXCEL"][self.op_type]["LEFT"]["LPFA"] = None	# delete excel data from pat.json
			self.dict["EXCEL"][self.op_type]["LEFT"]["MPFA"] = None	# delete excel data from pat.json
			
		if action == "DEL-RIGHT-TRO-HIP-LINE":
			self.dict["LPFA"][self.op_type]["RIGHT"]["TRO_HIP_LINE"]["P1"] = None						
			self.dict["EXCEL"][self.op_type]["RIGHT"]["VCA"] = None	# delete excel data from pat.json
			self.dict["EXCEL"][self.op_type]["RIGHT"]["LPFA"] = None	# delete excel data from pat.json
			self.dict["EXCEL"][self.op_type]["RIGHT"]["MPFA"] = None	# delete excel data from pat.json


		self.draw()
		self.regainHover(self.side)
		self.controller.save_json()
		self.controller.updateMenuLabel(self.getNextLabel(), self.menu_label)



	def draw(self):

		self.draw_tools.clear_by_tag(self.tag)

		self.point_size = self.controller.getViewPointSize()
		
		# loop left and right
		for side in ["LEFT","RIGHT"]:

			# ------------------------
			# FROM MAIN
			# ------------------------
			isHip 	 = False
			isKnee 	 = False
			isTroHip = False
			isFem3   = False

			hip 	= self.dict["MAIN"][self.op_type][side]["HIP"]["P1"]
			knee 	= self.dict["MAIN"][self.op_type][side]["FEM_KNEE"]["P1"]
			tro_hip = self.dict["LPFA"][self.op_type][side]["TRO_HIP_LINE"]["P1"]


			fem_U3_m1 	= self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["U3"]["M1"]
			fem_L3_m1 	= self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["L3"]["M1"]

			lpfa_angle = None
			mpfa_angle = None


			if tro_hip != None:
				isTroHip = True
				self.draw_tools.create_mypoint(tro_hip, "orange", [self.tag, side, "NO-DRAG"], point_thickness=self.point_size)			
			if hip != None:
				isHip = True
				self.draw_tools.create_mypoint(hip, "orange", [self.tag, side, "NO-DRAG"], point_thickness=self.point_size)
			if isHip and isTroHip:
				self.draw_tools.create_myline(hip, tro_hip, self.tag)

			if fem_L3_m1 != None and fem_U3_m1 != None:				
				isFem3 = True

			if knee != None:
				isKnee = True


			if self.mpfa_var:
				if isFem3:
					self.draw_tools.create_mypoint(fem_L3_m1, "orange", [self.tag, side, "NO-DRAG"], point_thickness=self.point_size)
					self.draw_tools.create_mypoint(fem_U3_m1, "orange", [self.tag, side, "NO-DRAG"], point_thickness=self.point_size)
					self.draw_tools.create_myline(fem_L3_m1, fem_U3_m1, self.tag)	


				if isHip and isTroHip and isFem3:

					p_int = self.draw_tools.line_intersection((fem_L3_m1, fem_U3_m1),(hip, tro_hip))
					self.draw_tools.create_myline(fem_U3_m1, p_int, self.tag)


					if side == "RIGHT":
						mpfa_angle = self.draw_tools.create_myAngle(hip, p_int, fem_U3_m1, self.tag)
					else:
						mpfa_angle = self.draw_tools.create_myAngle(fem_U3_m1, p_int, hip, self.tag)

					self.draw_tools.create_mytext(hip, '{0:.1f}'.format(mpfa_angle), [self.tag,side, "NO-DRAG"], x_offset=0, y_offset=-60, color="blue")			

			else:				
				if isKnee:					
					self.draw_tools.create_mypoint(knee, "orange", [self.tag, side, "NO-DRAG"], point_thickness=self.point_size)

				# HIP-KNEE-LINE
				if isHip and isKnee:
					self.draw_tools.create_myline(hip, knee, self.tag)

				if isHip and isKnee and isTroHip:

					if side == "RIGHT":
						lpfa_angle = self.draw_tools.create_myAngle(knee, hip, tro_hip, self.tag)
					else:
						lpfa_angle = self.draw_tools.create_myAngle(tro_hip, hip, knee, self.tag)
					self.draw_tools.create_mytext(hip, '{0:.1f}'.format(lpfa_angle), [self.tag,side, "NO-DRAG"], x_offset=0, y_offset=-60, color="blue")


				




			# save to excel should happen for both values
			# user might not toggle
			# if none recalculate for checkbox toggle error
			if lpfa_angle != None:
				print('not null write')
				# check if value exists
				if self.dict["EXCEL"][self.op_type][side]["LPFA"] == None:
					self.dict["EXCEL"][self.op_type][side]["HASDATA"] 	= True					
					self.dict["EXCEL"][self.op_type][side]["LPFA"]	 	= '{0:.1f}'.format(lpfa_angle)
					self.controller.save_json()
			else:
				print('null calculate')
				if isHip and isKnee and isTroHip:
					print('points exist')
					if side == "RIGHT":
						lpfa_angle = self.draw_tools.getAnglePoints(knee, hip, tro_hip)
					else:
						lpfa_angle = self.draw_tools.getAnglePoints(tro_hip, hip, knee)

					# check if value exists
					if self.dict["EXCEL"][self.op_type][side]["LPFA"] == None:
						self.dict["EXCEL"][self.op_type][side]["HASDATA"] 	= True					
						self.dict["EXCEL"][self.op_type][side]["LPFA"]	 	= '{0:.1f}'.format(lpfa_angle)
						self.controller.save_json()


			if mpfa_angle != None:
				# check if value exists
				if self.dict["EXCEL"][self.op_type][side]["MPFA"] == None:
					self.dict["EXCEL"][self.op_type][side]["HASDATA"] 	= True					
					self.dict["EXCEL"][self.op_type][side]["MPFA"]	 	= '{0:.1f}'.format(mpfa_angle)
					self.controller.save_json()
			else:
				if isHip and isTroHip and isFem3:

					p_int = self.draw_tools.line_intersection((fem_L3_m1, fem_U3_m1),(hip, tro_hip))
					if side == "RIGHT":
						mpfa_angle = self.draw_tools.getAnglePoints(hip, p_int, fem_U3_m1)
					else:
						mpfa_angle = self.draw_tools.getAnglePoints(fem_U3_m1, p_int, hip)

					# check if value exists
					if self.dict["EXCEL"][self.op_type][side]["MPFA"] == None:
						self.dict["EXCEL"][self.op_type][side]["HASDATA"] 	= True					
						self.dict["EXCEL"][self.op_type][side]["MPFA"]	 	= '{0:.1f}'.format(mpfa_angle)
						self.controller.save_json()






	def hover(self, P_mouse, P_stored, hover_label):

		# prevent auto curObject set bug
		if self.side == None:
			return

		if self.draw_hover:
			side_pre = self.side[0]+"_"
			if	hover_label == "P0_TRO_HIP_LINE":
				self.draw_tools.clear_by_tag("hover_line")
				self.draw_tools.create_mypoint(P_mouse, "red", [self.tag, "hover_line"], hover_point=True, point_thickness=self.point_size)

				# joing P_mouse to fem_knee
				hip = self.dict["MAIN"][self.op_type][self.side]["HIP"]["P1"]
				if hip != None:
					self.draw_tools.create_myline(P_mouse, hip, "hover_line")
				else:
					print('none')

				if self.draw_labels:
					self.draw_tools.create_mytext(P_mouse,x_offset=80, mytext=(side_pre+self.hover_text), mytag=[self.tag, "hover_line"])

	def regainHover(self, side):
		# find if P0 hovers are required
		self.mainHoverUsingNextLabel()

	def escapeObjFunc(self):
		self.side = None
		self.draw_tools.setHoverPointLabel(None)
		self.draw_tools.setHoverBool(False)
		self.controller.updateMenuLabel("CHOOSE SIDE", self.menu_label)


	def mainHoverUsingNextLabel(self):
		label = self.getNextLabel()

		if label == "RIGHT TRO_HIP_LINE":
			self.side = "RIGHT"
			self.hover_text = "TRO_HIP_LINE"
			self.draw_tools.setHoverPointLabel("P0_TRO_HIP_LINE")
			self.draw_tools.setHoverPoint(None)
			self.draw_tools.setHoverBool(True)
		elif label == "LEFT TRO_HIP_LINE":
			self.side = "LEFT"
			self.hover_text = "TRO_HIP_LINE"
			self.draw_tools.setHoverPointLabel("P0_TRO_HIP_LINE")
			self.draw_tools.setHoverPoint(None)
			self.draw_tools.setHoverBool(True)




	def checkbox_click(self,action, val):
		print('checkbox {} val{}'.format(action,val.get()))

		if action == "TOGGLE_MPFA":
			if val.get() == 0:
				self.mpfa_var = False
			elif val.get() == 1:
				self.mpfa_var = True
			self.draw()

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


	# 	if "P1_DIST_FEM" in tags:
	# 		self.drag_point = self.dict["VCA"][self.op_type][side]["DIST_FEM"]["P2"]
	# 		self.drag_label = "P1_DIST_FEM"
	# 		self.drag_side 	= side
	# 	elif "P2_DIST_FEM" in tags:
	# 		self.drag_point = self.dict["VCA"][self.op_type][side]["DIST_FEM"]["P1"]
	# 		self.drag_label = "P2_DIST_FEM"
	# 		self.drag_side 	= side
	# 	else:
	# 		self.drag_point = None
	# 		self.drag_label = None
	# 		self.drag_side 	= None
		


			
	# def drag(self, P_mouse):
		
	# 	if self.drag_label == "P1_DIST_FEM" and self.drag_point != None or self.drag_label == "P2_DIST_FEM" and self.drag_point != None:
	# 		self.draw_tools.clear_by_tag("DIST_FEM_LINE")
	# 		self.draw_tools.clear_by_tag("VCA_ANGLE")
			
	# 		self.draw_tools.clear_by_tag("drag_line")
	# 		m = self.draw_tools.midpoint(self.drag_point, P_mouse)
	# 		self.draw_tools.create_midpoint_line(self.drag_point, P_mouse, m, "drag_line", point_thickness=self.point_size)

	# def drag_stop(self, P_mouse):
	# 	self.draw_tools.clear_by_tag("drag_line")

	# 	if self.drag_label == "P1_DIST_FEM":
	# 		self.dict["VCA"][self.op_type][self.drag_side]["DIST_FEM"]["P1"] = P_mouse
	# 		self.dict["VCA"][self.op_type][self.drag_side]["DIST_FEM"]["M1"] = self.draw_tools.midpoint(self.drag_point, P_mouse)
	# 		self.dict["EXCEL"][self.op_type][self.drag_side]["VCA"] = None	# delete excel data from pat.json
	# 	elif self.drag_label == "P2_DIST_FEM":
	# 		self.dict["VCA"][self.op_type][self.drag_side]["DIST_FEM"]["P2"] = P_mouse
	# 		self.dict["VCA"][self.op_type][self.drag_side]["DIST_FEM"]["M1"] = self.draw_tools.midpoint(self.drag_point, P_mouse)
	# 		self.dict["EXCEL"][self.op_type][self.drag_side]["VCA"] = None	# delete excel data from pat.json

	# 	self.controller.save_json()
	# 	self.draw()

	def update_canvas(self, draw_tools):
		self.draw_tools = draw_tools


	def update_dict(self, master_dict):
		self.dict = master_dict		


	def getNextLabel(self):

		if self.side != None:
			
			for item in self.dict["LPFA"][self.op_type][self.side]:

				# get item type 
				item_type = self.dict["LPFA"][self.op_type][self.side][item]["type"]


				# point only has P1
				if item_type == "point":
					# check if P1 is None				
					if self.dict["LPFA"][self.op_type][self.side][item]["P1"] == None:
						return (self.side + " " + item)

			return (self.side + " Done")
		return None


	def unset(self):
		# print("unset from "+self.name)
		self.draw_tools.clear_by_tag(self.tag)


	def drag_start(self, P_mouse):
		pass
	def drag(self, P_mouse):
		pass
	def drag_stop(self, P_mouse):
		pass	
	
	
		
	# similiar to draw but nothing is drawn on the canvas
	def updateExcelValues(self):
		return 
		# loop left and right
		for side in ["LEFT","RIGHT"]:


			# ------------------------
			# FROM MAIN
			# ------------------------
			isHip 	 = False
			isKnee 	 = False
			isTroHip = False
			isFem3   = False

			hip 	= self.dict["MAIN"][self.op_type][side]["HIP"]["P1"]
			knee 	= self.dict["MAIN"][self.op_type][side]["FEM_KNEE"]["P1"]
			tro_hip = self.dict["LPFA"][self.op_type][side]["TRO_HIP_LINE"]["P1"]


			fem_U3_m1 	= self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["U3"]["M1"]
			fem_L3_m1 	= self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["L3"]["M1"]

			lpfa_angle = None
			mpfa_angle = None


			if tro_hip != None:
				isTroHip = True
			if hip != None:
				isHip = True

			if fem_L3_m1 != None and fem_U3_m1 != None:				
				isFem3 = True

			if knee != None:
				isKnee = True


			if isHip and isTroHip and isFem3:

				p_int = self.draw_tools.line_intersection((fem_L3_m1, fem_U3_m1),(hip, tro_hip))
				self.draw_tools.create_myline(fem_U3_m1, p_int, self.tag)
				if side == "RIGHT":
					mpfa_angle = self.draw_tools.getAnglePoints(hip, p_int, fem_U3_m1)
				else:
					mpfa_angle = self.draw_tools.getAnglePoints(fem_U3_m1, p_int, hip)

				# check if value exists
				if self.dict["EXCEL"][self.op_type][side]["MPFA"] == None:
					self.dict["EXCEL"][self.op_type][side]["HASDATA"] 	= True					
					self.dict["EXCEL"][self.op_type][side]["MPFA"]	 	= '{0:.1f}'.format(lpfa_angle)
					self.controller.save_json()



			if isHip and isKnee and isTroHip:
				if side == "RIGHT":
					lpfa_angle = self.draw_tools.getAnglePoints(knee, hip, tro_hip)
				else:
					lpfa_angle = self.draw_tools.getAnglePoints(tro_hip, hip, knee)

				# check if value exists
				if self.dict["EXCEL"][self.op_type][side]["LPFA"] == None:
					self.dict["EXCEL"][self.op_type][side]["HASDATA"] 	= True					
					self.dict["EXCEL"][self.op_type][side]["LPFA"]	 	= '{0:.1f}'.format(lpfa_angle)
					self.controller.save_json()