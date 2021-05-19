

class JCA():
	"""docstring for ClassName"""
	def __init__(self, draw_tools, master_dict, controller, op_type):
		self.name = "JCA"
		self.tag = "jca"
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

			isFemTop 	= False
			isFemBot 	= False

			isTib 	= False
			isFem 	= False

			tib_joint_p1 = self.dict["MAIN"][self.op_type][side]["TIB_JOINT_LINE"]["P1"]
			tib_joint_p2 = self.dict["MAIN"][self.op_type][side]["TIB_JOINT_LINE"]["P2"]

			fem_joint_p1 = self.dict["MAIN"][self.op_type][side]["FEM_JOINT_LINE"]["P1"]
			fem_joint_p2 = self.dict["MAIN"][self.op_type][side]["FEM_JOINT_LINE"]["P2"]


			if fem_joint_p1 != None:
				self.draw_tools.create_mypoint(fem_joint_p1, "orange", [self.tag, side, "NO-DRAG"], point_thickness=self.point_size)
			if fem_joint_p2 != None:
				self.draw_tools.create_mypoint(fem_joint_p2, "orange", [self.tag, side, "NO-DRAG"], point_thickness=self.point_size)
			if fem_joint_p1 != None and fem_joint_p2 != None:
				self.draw_tools.create_myline(fem_joint_p1, fem_joint_p2, [self.tag, side, "NO-DRAG"])
				isFem = True


			if tib_joint_p1 != None:
				self.draw_tools.create_mypoint(tib_joint_p1, "orange", [self.tag, side, "NO-DRAG"], point_thickness=self.point_size)
			if tib_joint_p2 != None:
				self.draw_tools.create_mypoint(tib_joint_p2, "orange", [self.tag, side, "NO-DRAG"], point_thickness=self.point_size)
			if tib_joint_p1 != None and tib_joint_p2 != None:
				self.draw_tools.create_myline(tib_joint_p1, tib_joint_p2, [self.tag, side, "NO-DRAG"])
				isTib = True




			xtop, ytop, xbot, ybot = self.draw_tools.getImageCorners()

			if isTib and isFem:

				p_int = self.draw_tools.line_intersection(
					(tib_joint_p1, tib_joint_p2),
					(fem_joint_p1, fem_joint_p2))

				# angle = self.draw_tools.getSmallestAngle(tib_joint_p1, p_int, fem_joint_p1)

				

				L_fem, R_fem = self.draw_tools.retPointsLeftRight(fem_joint_p1, fem_joint_p2)
				L_tib, R_tib = self.draw_tools.retPointsLeftRight(tib_joint_p1, tib_joint_p2)

				if side == "RIGHT":
					# angle2 = self.draw_tools.create_myAngle(L_tib, p_int, L_fem, self.tag)
					angle = self.draw_tools.getSmallestAngle(L_tib, p_int, L_fem)
					self.draw_tools.create_mytext(R_fem, y_offset=-20, mytext='{0:.1f}'.format(angle), mytag=[self.tag], color="blue")
				elif side == "LEFT":
					# angle2 = self.draw_tools.create_myAngle(R_fem, p_int, R_tib, self.tag)
					angle = self.draw_tools.getSmallestAngle(R_fem, p_int, R_tib)
					self.draw_tools.create_mytext(L_fem, y_offset=-20, mytext='{0:.1f}'.format(angle), mytag=[self.tag], color="blue")


				# check if value exists
				if self.dict["EXCEL"][self.op_type][side]["JCA"] == None:

					self.dict["EXCEL"][self.op_type][side]["HASDATA"] 	= True
					self.dict["EXCEL"][self.op_type][side]["JCA"]	 	= '{0:.1f}'.format(angle)

					# save after insert
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
		
		self.draw_tools.clear_by_tag(self.tag)

		self.point_size = self.controller.getViewPointSize()
		
		# loop left and right
		for side in ["LEFT","RIGHT"]:

			isTib 	= False
			isFem 	= False

			tib_joint_p1 = self.dict["MAIN"][self.op_type][side]["TIB_JOINT_LINE"]["P1"]
			tib_joint_p2 = self.dict["MAIN"][self.op_type][side]["TIB_JOINT_LINE"]["P2"]

			fem_joint_p1 = self.dict["MAIN"][self.op_type][side]["FEM_JOINT_LINE"]["P1"]
			fem_joint_p2 = self.dict["MAIN"][self.op_type][side]["FEM_JOINT_LINE"]["P2"]


			if fem_joint_p1 != None and fem_joint_p2 != None:				
				isFem = True
			
			if tib_joint_p1 != None and tib_joint_p2 != None:
				isTib = True




			xtop, ytop, xbot, ybot = self.draw_tools.getImageCorners()

			if isTib and isFem:

				p_int = self.draw_tools.line_intersection(
					(tib_joint_p1, tib_joint_p2),
					(fem_joint_p1, fem_joint_p2))

				angle = self.draw_tools.getSmallestAngle(tib_joint_p1, p_int, fem_joint_p1)

				
				# check if value exists
				if self.dict["EXCEL"][self.op_type][side]["JCA"] == None:

					self.dict["EXCEL"][self.op_type][side]["HASDATA"] 	= True
					self.dict["EXCEL"][self.op_type][side]["JCA"]	 	= '{0:.1f}'.format(angle)

					# save after insert
					self.controller.save_json()