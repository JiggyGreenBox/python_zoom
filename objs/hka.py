from copy import deepcopy

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


	# similiar to draw but nothing is drawn on the canvas
	def updateExcelValues(self):

		for side in ["LEFT","RIGHT"]:

			hip 		= self.dict["MAIN"][self.op_type][side]["HIP"]["P1"]
			fem_knee 	= self.dict["MAIN"][self.op_type][side]["FEM_KNEE"]["P1"]
			tib_knee 	= self.dict["MAIN"][self.op_type][side]["TIB_KNEE"]["P1"]
			
			ankle_p1 	= self.dict["MAIN"][self.op_type][side]["ANKLE"]["P1"]
			ankle_p2 	= self.dict["MAIN"][self.op_type][side]["ANKLE"]["P2"]
			ankle_m1 	= self.dict["MAIN"][self.op_type][side]["ANKLE"]["M1"]


			if( ankle_p1 != None and 
				ankle_p2 != None and
				hip != None and
				fem_knee != None and
				tib_knee != None				
				):

				# fem-tib-intersection
				hka_point = self.draw_tools.line_intersection((ankle_m1, tib_knee), (hip, fem_knee))				

				# draw angle
				angle = ""
				if side == "LEFT":						
					# angle = self.draw_tools.create_myAngle(ankle_m1, hka_point, hip, self.tag)
					angle = self.draw_tools.getAnglePoints(ankle_m1, hka_point, hip)
				else:
					# angle = self.draw_tools.create_myAngle(hip, hka_point, ankle_m1, self.tag)
					angle = self.draw_tools.getAnglePoints(hip, hka_point, ankle_m1)
				

				# check if value exists
				if self.dict["EXCEL"][self.op_type][side]["HKA"] == None:

					self.dict["EXCEL"][self.op_type][side]["HASDATA"] 	= True
					self.dict["EXCEL"][self.op_type][side]["HKA"]	 	= '{0:.2f}'.format(angle)

					# save after insert
					self.controller.save_json()

						


	def obj_draw_pil(self):
		print('draw PIL HKA')
		# create the pil image
		# self.draw_tools.createPIL()

		# borrow from draw
		self.point_size = self.controller.getViewPointSize()

		

		# local_dict = copy.deepcopy(self.dict)
		# R_draw_fem_knee 	= local_dict["MAIN"][self.op_type]["RIGHT"]["FEM_KNEE"]["P1"]
		# L_draw_fem_knee 	= local_dict["MAIN"][self.op_type]["LEFT"]["FEM_KNEE"]["P1"]

		R_draw_fem_knee 	= deepcopy(self.dict["MAIN"][self.op_type]["RIGHT"]["FEM_KNEE"]["P1"])
		L_draw_fem_knee 	= deepcopy(self.dict["MAIN"][self.op_type]["LEFT"]["FEM_KNEE"]["P1"])

		# check if both knees are availble and have adjust the knees by the Yaxis
		if R_draw_fem_knee != None and L_draw_fem_knee != None:
			L_draw_fem_knee, R_draw_fem_knee = self.draw_tools.get_yaxis_adjusted_points(L_draw_fem_knee, R_draw_fem_knee)


		# loop left and right
		for side in ["LEFT","RIGHT"]:

			isHip 		= False
			isFemKnee 	= False
			isTibKnee 	= False
			isDist 		= False
			isMad 		= False

			hip 		= self.dict["MAIN"][self.op_type][side]["HIP"]["P1"]
			fem_knee 	= self.dict["MAIN"][self.op_type][side]["FEM_KNEE"]["P1"]
			tib_knee 	= self.dict["MAIN"][self.op_type][side]["TIB_KNEE"]["P1"]
			
			ankle_p1 	= self.dict["MAIN"][self.op_type][side]["ANKLE"]["P1"]
			ankle_p2 	= self.dict["MAIN"][self.op_type][side]["ANKLE"]["P2"]
			ankle_m1 	= self.dict["MAIN"][self.op_type][side]["ANKLE"]["M1"]

			dist_fem_p1 = self.dict["MAIN"][self.op_type][side]["DIST_FEM"]["P1"]
			dist_fem_p2 = self.dict["MAIN"][self.op_type][side]["DIST_FEM"]["P2"]
			dist_fem_m1 = self.dict["MAIN"][self.op_type][side]["DIST_FEM"]["M1"]

			mad_val 	= self.dict["EXCEL"][self.op_type][side]["MAD"]


			# HIP
			if hip != None:
				isHip = True
				self.draw_tools.pil_create_mypoint(hip, "orange", point_thickness=self.point_size)

			# KNEE
			if fem_knee != None:
				isFemKnee = True
				# self.draw_tools.pil_create_mypoint(fem_knee, "orange", point_thickness=self.point_size)

			if tib_knee != None:
				isTibKnee = True
				# self.draw_tools.pil_create_mypoint(tib_knee, "orange", point_thickness=self.point_size)

			if dist_fem_p1 != None and dist_fem_p2 != None:
				try:
					vca_angle = self.draw_tools.getSmallestAngle(dist_fem_m1, fem_knee, hip)				
					isDist = True
				except Exception as e:
					print(e)
				

			if mad_val != None:
				isMad = True
				print('MAD: {}'.format(mad_val))


			# ANKLE
			if ankle_p1 != None and ankle_p2 != None:
				
				self.draw_tools.pil_create_mypoint(ankle_m1, "orange", point_thickness=self.point_size)

				if isHip and isTibKnee and isFemKnee:

					# fem-tib-intersection
					hka_point = self.draw_tools.line_intersection((ankle_m1, tib_knee), (hip, fem_knee))

					# hip-knee line
					self.draw_tools.pil_create_myline(hip, hka_point)
					self.draw_tools.pil_create_myline(hka_point, ankle_m1)

					# # draw angle
					# angle = ""

					# '''
					# if side == "LEFT":						
					# 	angle = self.draw_tools.create_myAngle(self.dict["MAIN"][self.op_type][side]["HIP"]["P1"], self.dict["MAIN"][self.op_type][side]["KNEE"]["P1"], p_top, self.tag)
					# else:
					# 	angle = self.draw_tools.create_myAngle(p_top, self.dict["MAIN"][self.op_type][side]["KNEE"]["P1"], self.dict["MAIN"][self.op_type][side]["HIP"]["P1"], self.tag)
					# '''

					hka_angle = ""
					

					if side == "LEFT":						
						# angle = self.draw_tools.create_myAngle(ankle_m1, hka_point, hip, self.tag)
						hka_angle = self.draw_tools.pil_create_myAngle(ankle_m1, hka_point, hip)
						# draw_txt.textsize(sample, font=font)
						# text = "HKA: {0:.2f}".format(hka_angle)
						# offset = -1*(60 + self.draw_tools.pil_get_text_size(text))
						# print('offset: {}'.format(offset))
					else:
						# angle = self.draw_tools.create_myAngle(hip, hka_point, ankle_m1, self.tag)
						hka_angle = self.draw_tools.pil_create_myAngle(hip, hka_point, ankle_m1)
						
					

					# self.draw_tools.pil_create_mytext(hka_point, "HKA: {0:.2f}".format(hka_angle), x_offset=offset, color="blue")					


					# keep overwriting to exclude None values
					hka_text = 'HKA: {0:.2f}'.format(hka_angle)
					vca_text = ""
					mad_text = ""

					if isDist:
						vca_text = 'VCA: {0:.2f}'.format(vca_angle)
					if isMad:
						mad_text = 'MAD: {}'.format(mad_val)

					nl = "\n"
					multi_text = hka_text + nl + vca_text + nl + mad_text
					if self.op_type == "POST-OP":
						multi_text = hka_text + nl + mad_text


					xoffset = 220
					yoffset = -120
					# draw values
					if side == "LEFT":

						# print(self.draw_tools.pil_get_multiline_text_size(multi_text))

						
						# pil_get_multiline_text_size

						# x1,y1,x2,y2 = self.draw_tools.pil_get_text_bbox(hka_point, multi_text, x_offset=xoffset)
						# self.draw_tools.pil_draw_rect([x1,y1,x2,y2], padding=20)
						# self.draw_tools.pil_create_multiline_text(hka_point, multi_text, x_offset=xoffset, color=(255,255,255,255))

						x1,y1,x2,y2 = self.draw_tools.pil_get_text_bbox(L_draw_fem_knee, multi_text, x_offset=xoffset, y_offset=yoffset)
						self.draw_tools.pil_draw_rect([x1,y1,x2,y2], padding=20)
						self.draw_tools.pil_create_multiline_text(L_draw_fem_knee, multi_text, x_offset=xoffset, y_offset=yoffset, color=(255,255,255,255))
						# L_draw_fem_knee
					elif side == "RIGHT":
						# x1,y1,x2,y2 = self.draw_tools.pil_get_text_bbox(hka_point, multi_text, x_offset=xoffset)
						# self.draw_tools.pil_draw_rect([x1,y1,x2,y2], padding=20)
						# self.draw_tools.pil_create_multiline_text(hka_point, multi_text, x_offset=xoffset, color=(255,255,255,255))

						xoffset = -1*(xoffset + self.draw_tools.pil_get_multiline_text_size(multi_text))

						x1,y1,x2,y2 = self.draw_tools.pil_get_text_bbox(R_draw_fem_knee, multi_text, x_offset=xoffset, y_offset=yoffset)
						self.draw_tools.pil_draw_rect([x1,y1,x2,y2], padding=20)
						self.draw_tools.pil_create_multiline_text(R_draw_fem_knee, multi_text, x_offset=xoffset, y_offset=yoffset, color=(255,255,255,255))
						# R_draw_fem_knee



				


		# save the image