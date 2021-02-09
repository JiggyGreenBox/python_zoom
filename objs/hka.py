

class HKA():
	"""docstring for ClassName"""
	def __init__(self, draw_tools, master_dict, controller, op_type):
		self.name = "HKA"
		self.tag = "hka"
		self.draw_tools = draw_tools
		self.dict = master_dict
		self.op_type = op_type
		self.controller = controller

		self.point_size = None

		
	def click(self, event):
		print("click from "+self.name)		
		self.draw() 


	def draw(self):

		self.draw_tools.clear_by_tag(self.tag)

		self.point_size = self.controller.getViewPointSize()

		# loop left and right
		for side in ["LEFT","RIGHT"]:

			isHip = False
			isFemKnee = False
			isTibKnee = False

			hip 		= self.dict["MAIN"][self.op_type][side]["HIP"]["P1"]
			fem_knee 	= self.dict["MAIN"][self.op_type][side]["FEM_KNEE"]["P1"]
			tib_knee 	= self.dict["MAIN"][self.op_type][side]["TIB_KNEE"]["P1"]
			
			ankle_p1 	= self.dict["MAIN"][self.op_type][side]["ANKLE"]["P1"]
			ankle_p2 	= self.dict["MAIN"][self.op_type][side]["ANKLE"]["P2"]
			ankle_m1 	= self.dict["MAIN"][self.op_type][side]["ANKLE"]["M1"]


			# HIP
			if hip != None:
				isHip = True
				self.draw_tools.create_mypoint(hip, "orange", [self.tag, side, "NO-DRAG"], point_thickness=self.point_size)

			# KNEE
			if fem_knee != None:
				isFemKnee = True
				self.draw_tools.create_mypoint(fem_knee, "orange", [self.tag, side, "NO-DRAG"], point_thickness=self.point_size)

			if tib_knee != None:
				isTibKnee = True
				self.draw_tools.create_mypoint(tib_knee, "orange", [self.tag, side, "NO-DRAG"], point_thickness=self.point_size)


			# ANKLE
			if ankle_p1 != None and ankle_p2 != None:
				
				self.draw_tools.create_mypoint(ankle_p1, "orange", [self.tag, side, "NO-DRAG"], point_thickness=self.point_size)
				self.draw_tools.create_mypoint(ankle_p2, "orange", [self.tag, side, "NO-DRAG"], point_thickness=self.point_size)
				self.draw_tools.create_midpoint_line(ankle_p1, ankle_p2, ankle_m1, self.tag, point_thickness=self.point_size)

				if isHip and isTibKnee and isFemKnee:

					# ankle-tib-knee ray
					xtop, ytop, xbot, ybot = self.draw_tools.getImageCorners()
					p_top = self.draw_tools.line_intersection((ankle_m1, tib_knee), (xtop, ytop))
					self.draw_tools.create_myline(ankle_m1, p_top, self.tag)


					# fem-tib-intersection
					hka_point = self.draw_tools.line_intersection((ankle_m1, tib_knee), (hip, fem_knee))

					# hip-knee line
					self.draw_tools.create_myline(hip, hka_point, self.tag)

					# draw angle
					angle = ""

					'''
					if side == "LEFT":						
						angle = self.draw_tools.create_myAngle(self.dict["MAIN"][self.op_type][side]["HIP"]["P1"], self.dict["MAIN"][self.op_type][side]["KNEE"]["P1"], p_top, self.tag)
					else:
						angle = self.draw_tools.create_myAngle(p_top, self.dict["MAIN"][self.op_type][side]["KNEE"]["P1"], self.dict["MAIN"][self.op_type][side]["HIP"]["P1"], self.tag)
					'''

					if side == "LEFT":						
						angle = self.draw_tools.create_myAngle(ankle_m1, hka_point, hip, self.tag)
					else:
						angle = self.draw_tools.create_myAngle(hip, hka_point, ankle_m1, self.tag)
						
					# , radius = 50, width = 3):
					# self.canvas.create_text(x-r,y+r,fill="orange", text='{0:.2f}'.format(t1), tags="tag")
					
					# self.draw_tools.create_mytext(self.dict["MAIN"][self.op_type][side]["KNEE"]["P1"], '{0:.2f}'.format(angle), self.tag, x_offset=60)
					self.draw_tools.create_mytext(hka_point, '{0:.2f}'.format(angle), self.tag, x_offset=60, color="blue")
					


					# check if value exists
					if self.dict["EXCEL"][self.op_type][side]["HKA"] == None:

						self.dict["EXCEL"][self.op_type][side]["HASDATA"] 	= True
						self.dict["EXCEL"][self.op_type][side]["HKA"]	 	= '{0:.2f}'.format(angle)

						# save after insert
						self.controller.save_json()


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


	def update_canvas(self, draw_tools):
		self.draw_tools = draw_tools

	def update_dict(self, master_dict):
		self.dict = master_dict

	def unset(self):
		# print("unset from "+self.name)
		self.draw_tools.clear_by_tag(self.tag)
		self.side = None

						