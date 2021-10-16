

class VANG():
	"""docstring for ClassName"""
	def __init__(self, draw_tools, master_dict, controller, op_type):
		self.name = "VANG"
		self.tag = "vang"
		self.draw_tools = draw_tools
		self.dict = master_dict
		self.op_type = op_type
		self.controller = controller

		self.point_size = None

	def click(self, event):
		print("click from "+self.name)
		self.draw()


	def right_click(self, event):
		pass

	def keyRightObjFunc(self):
		pass

	def keyLeftObjFunc(self):
		pass


	def draw(self):

		self.draw_tools.clear_by_tag(self.tag)

		self.point_size = self.controller.getViewPointSize()
		
		# loop left and right
		for side in ["LEFT","RIGHT"]:

			isTibKnee 	= False
			isAnkle 	= False

			isTibTop 	= False
			isTibBot 	= False

			# AXIS_TIB
			tib_U3_p1 = self.dict["MAIN"][self.op_type][side]["AXIS_TIB"]["U3"]["P1"]
			tib_U3_p2 = self.dict["MAIN"][self.op_type][side]["AXIS_TIB"]["U3"]["P2"]
			tib_U3_m1 = self.dict["MAIN"][self.op_type][side]["AXIS_TIB"]["U3"]["M1"]

			tib_L3_p1 = self.dict["MAIN"][self.op_type][side]["AXIS_TIB"]["L3"]["P1"]
			tib_L3_p2 = self.dict["MAIN"][self.op_type][side]["AXIS_TIB"]["L3"]["P2"]
			tib_L3_m1 = self.dict["MAIN"][self.op_type][side]["AXIS_TIB"]["L3"]["M1"]

			tib_knee 	= self.dict["MAIN"][self.op_type][side]["TIB_KNEE"]["P1"]

			ankle_m1 	= self.dict["MAIN"][self.op_type][side]["ANKLE"]["M1"]

			if tib_U3_m1 != None and tib_L3_m1 != None:
				tib_U3_m1, tib_L3_m1 = self.draw_tools.retPointsUpDown(tib_U3_m1, tib_L3_m1)

			# TIB AXIS
			# U3
			if tib_U3_p1 != None:
				self.draw_tools.create_mypoint(tib_U3_p1, "orange", [self.tag, side, "NO-DRAG"], point_thickness=self.point_size)

			if tib_U3_p2 != None:
				self.draw_tools.create_mypoint(tib_U3_p2, "orange", [self.tag, side, "NO-DRAG"], point_thickness=self.point_size)

			if tib_U3_p1 != None and tib_U3_p2 != None:				
				self.draw_tools.create_midpoint_line(tib_U3_p1, tib_U3_p2, tib_U3_m1, self.tag, point_thickness=self.point_size)
				isTibTop = True


			# L3
			if tib_L3_p1 != None:
				self.draw_tools.create_mypoint(tib_L3_p1, "orange", [self.tag, side, "NO-DRAG"], point_thickness=self.point_size)

			if tib_L3_p2 != None:
				self.draw_tools.create_mypoint(tib_L3_p2, "orange", [self.tag, side, "NO-DRAG"], point_thickness=self.point_size)

			if tib_L3_p1 != None and tib_L3_p2 != None:				
				self.draw_tools.create_midpoint_line(tib_L3_p1, tib_L3_p2, tib_L3_m1, self.tag, point_thickness=self.point_size)
				isTibBot = True


			if tib_knee != None:
				self.draw_tools.create_mypoint(tib_knee, "orange", [self.tag, side, "NO-DRAG"], point_thickness=self.point_size)
				isTibKnee = True

			if ankle_m1 != None:
				self.draw_tools.create_mypoint(ankle_m1, "orange", [self.tag, side, "NO-DRAG"], point_thickness=self.point_size)
				isAnkle = True




			if isTibTop and isTibBot and isTibKnee and isAnkle:
				# knee U3 and ankle L3 intersection point
				p_int = self.draw_tools.line_intersection((tib_knee, tib_U3_m1),(ankle_m1, tib_L3_m1))

				self.draw_tools.create_mypoint(p_int, "orange", [self.tag, side, "NO-DRAG"], point_thickness=self.point_size)

				self.draw_tools.create_myline(tib_knee, p_int, self.tag)
				self.draw_tools.create_myline(ankle_m1, p_int, self.tag)


				# get the smaller angle
				# a1 = self.draw_tools.getAnglePoints(tib_knee, p_int, ankle_m1)
				# a2 = self.draw_tools.getAnglePoints(ankle_m1, p_int, tib_knee)
				# if a1 < a2:
				# 	angle = self.draw_tools.create_myAngle(tib_knee, p_int, ankle_m1, self.tag)
				# else:
				# 	angle = self.draw_tools.create_myAngle(ankle_m1, p_int, tib_knee, self.tag)

				# self.draw_tools.create_mytext(p_int, '{0:.1f}'.format(angle), self.tag, x_offset=60, color="blue")

				a1 = self.draw_tools.getAnglePoints(tib_knee, p_int, ankle_m1)
				a2 = self.draw_tools.getAnglePoints(ankle_m1, p_int, tib_knee)

				if side == "RIGHT":
					if a1 < a2:
						angle = self.draw_tools.create_myAngle(tib_knee, p_int, ankle_m1, self.tag)
					else:
						angle = self.draw_tools.create_myAngle(ankle_m1, p_int, tib_knee, self.tag)
						angle = angle * -1

				else:
					if a1 < a2:
						angle = self.draw_tools.create_myAngle(tib_knee, p_int, ankle_m1, self.tag)
						angle = angle * -1
					else:
						angle = self.draw_tools.create_myAngle(ankle_m1, p_int, tib_knee, self.tag)
				

				self.draw_tools.create_mytext(p_int, '{0:.1f}'.format(angle), self.tag, x_offset=60, color="blue")



				# # side based angle orientation
				# if side == "RIGHT":
				# 	angle = self.draw_tools.create_myAngle(tib_knee, p_int, ankle_m1, self.tag)
				# else:
				# 	angle = self.draw_tools.create_myAngle(ankle_m1, p_int, tib_knee, self.tag)
				# self.draw_tools.create_mytext(p_int, '{0:.1f}'.format(angle), self.tag, x_offset=60, color="blue")


				# check if value exists
				if self.dict["EXCEL"][self.op_type][side]["VANG"] == None:
					self.dict["EXCEL"][self.op_type][side]["HASDATA"] 	= True
					self.dict["EXCEL"][self.op_type][side]["VANG"]	 	= '{0:.1f}'.format(angle)
					self.controller.save_json()



	def update_canvas(self, draw_tools):
		self.draw_tools = draw_tools
		print("updated canvas from" + self.tag)

	def update_dict(self, master_dict):
		self.dict = master_dict

	def unset(self):
		# print("unset from "+self.name)
		self.draw_tools.clear_by_tag(self.tag)



	def drag_start(self, tags):
		pass		
	def drag(self, P_mouse):
		pass
	def drag_stop(self, P_mouse):
		self.draw()
	def hover(self, P_mouse, P_stored, hover_label):
		pass
	def regainHover(self, side):
		pass
	def escapeObjFunc(self):
		pass

		
	# similiar to draw but nothing is drawn on the canvas
	def updateExcelValues(self):

		# loop left and right
		for side in ["LEFT","RIGHT"]:

			isTibKnee 	= False
			isAnkle 	= False

			isTibTop 	= False
			isTibBot 	= False

			# AXIS_TIB
			tib_U3_p1 = self.dict["MAIN"][self.op_type][side]["AXIS_TIB"]["U3"]["P1"]
			tib_U3_p2 = self.dict["MAIN"][self.op_type][side]["AXIS_TIB"]["U3"]["P2"]
			tib_U3_m1 = self.dict["MAIN"][self.op_type][side]["AXIS_TIB"]["U3"]["M1"]

			tib_L3_p1 = self.dict["MAIN"][self.op_type][side]["AXIS_TIB"]["L3"]["P1"]
			tib_L3_p2 = self.dict["MAIN"][self.op_type][side]["AXIS_TIB"]["L3"]["P2"]
			tib_L3_m1 = self.dict["MAIN"][self.op_type][side]["AXIS_TIB"]["L3"]["M1"]

			if tib_U3_m1 != None and tib_L3_m1 != None:
				tib_U3_m1, tib_L3_m1 = self.draw_tools.retPointsUpDown(tib_U3_m1, tib_L3_m1)

			tib_knee 	= self.dict["MAIN"][self.op_type][side]["TIB_KNEE"]["P1"]

			ankle_m1 	= self.dict["MAIN"][self.op_type][side]["ANKLE"]["M1"]

			# TIB AXIS
			if tib_U3_p1 != None and tib_U3_p2 != None:				
				isTibTop = True

			if tib_L3_p1 != None and tib_L3_p2 != None:				
				isTibBot = True

			if tib_knee != None:
				isTibKnee = True

			if ankle_m1 != None:
				isAnkle = True

			if isTibTop and isTibBot and isTibKnee and isAnkle:
				# knee U3 and ankle L3 intersection point
				p_int = self.draw_tools.line_intersection((tib_knee, tib_U3_m1),(ankle_m1, tib_L3_m1))

				# get the smaller angle
				# a1 = self.draw_tools.getAnglePoints(tib_knee, p_int, ankle_m1)
				# a2 = self.draw_tools.getAnglePoints(ankle_m1, p_int, tib_knee)
				# if a1 < a2:
				# 	angle = self.draw_tools.getAnglePoints(tib_knee, p_int, ankle_m1)
				# else:
				# 	angle = self.draw_tools.getAnglePoints(ankle_m1, p_int, tib_knee)

				# self.draw_tools.create_mytext(p_int, '{0:.1f}'.format(angle), self.tag, x_offset=60, color="blue")


				# # side based angle orientation
				# if side == "RIGHT":
				# 	angle = self.draw_tools.getAnglePoints(tib_knee, p_int, ankle_m1)
				# else:
				# 	angle = self.draw_tools.getAnglePoints(ankle_m1, p_int, tib_knee)



				a1 = self.draw_tools.getAnglePoints(tib_knee, p_int, ankle_m1)
				a2 = self.draw_tools.getAnglePoints(ankle_m1, p_int, tib_knee)

				if side == "RIGHT":
					if a1 < a2:
						angle = a1
					else:
						angle = a2
						angle = angle * -1

				else:
					if a1 < a2:
						angle = a1
						angle = angle * -1
					else:
						angle = a2				


				# check if value exists
				if self.dict["EXCEL"][self.op_type][side]["VANG"] == None:
					self.dict["EXCEL"][self.op_type][side]["HASDATA"] 	= True
					self.dict["EXCEL"][self.op_type][side]["VANG"]	 	= '{0:.1f}'.format(angle)
					self.controller.save_json()