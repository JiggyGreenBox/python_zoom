from copy import deepcopy

# for floor
import math

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


		self.cur_option = 1
		self.pil_options = 	{
								1: {"fontsize": 30, "padding": 20},
								2: {"fontsize": 25, "padding": 10},
								3: {"fontsize": 20, "padding": 10},
								4: {"fontsize": 10, "padding": 5},
								5: {"fontsize": 9, "padding": 1},
								6: {"fontsize": 8, "padding": 1},
								7: {"fontsize": 7, "padding": 0},
								8: {"fontsize": 6, "padding": 0},
								9: {"fontsize": 5, "padding": 0},
							}


		
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
						angle = self.draw_tools.getAnglePoints(ankle_m1, hka_point, hip)
						m_text = '{0:.1f}'.format(angle)
						# hka bugfix, impossible to recreate
						if angle < 20:
							angle = 180.0 - angle

						# angle = self.draw_tools.create_myAngle(ankle_m1, hka_point, hip, self.tag)

						elif angle > 270:
							pre_angle = self.draw_tools.getAnglePoints(hip, hka_point, ankle_m1)
							angle = 180 - pre_angle
							m_text = '180 - {0:.1f} = {1:.1f}'.format(pre_angle, angle)
						else:
							angle = self.draw_tools.create_myAngle(ankle_m1, hka_point, hip, self.tag)

					else:
						angle = self.draw_tools.getAnglePoints(hip, hka_point, ankle_m1)
						m_text = '{0:.1f}'.format(angle)
						# hka bugfix, impossible to recreate
						if angle < 20:
							angle = 180.0 - angle

						elif angle > 270:
							pre_angle = self.draw_tools.getAnglePoints(ankle_m1, hka_point, hip)
							angle = 180 - pre_angle
							m_text = '180 - {0:.1f} = {1:.1f}'.format(pre_angle, angle)
						else:
							angle = self.draw_tools.create_myAngle(hip, hka_point, ankle_m1, self.tag)
						# angle = self.draw_tools.create_myAngle(hip, hka_point, ankle_m1, self.tag)
					

					
					

					# , radius = 50, width = 3):
					# self.canvas.create_text(x-r,y+r,fill="orange", text='{0:.1f}'.format(t1), tags="tag")
					
					# self.draw_tools.create_mytext(self.dict["MAIN"][self.op_type][side]["KNEE"]["P1"], '{0:.1f}'.format(angle), self.tag, x_offset=60)
					self.draw_tools.create_mytext(hka_point, m_text, self.tag, x_offset=60, color="blue")
					


					# check if value exists
					if self.dict["EXCEL"][self.op_type][side]["HKA"] == None:

						self.dict["EXCEL"][self.op_type][side]["HASDATA"] 	= True
						self.dict["EXCEL"][self.op_type][side]["HKA"]	 	= '{0:.1f}'.format(angle)

						jda = None
						if angle > 180:
							jda = angle - 180
						else:
							jda = 180 - angle

						self.dict["EXCEL"][self.op_type][side]["JDA"] = '{0:.1f}'.format(jda)

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
				# if side == "LEFT":						
				# 	# angle = self.draw_tools.create_myAngle(ankle_m1, hka_point, hip, self.tag)
				# 	angle = self.draw_tools.getAnglePoints(ankle_m1, hka_point, hip)
				# else:
				# 	# angle = self.draw_tools.create_myAngle(hip, hka_point, ankle_m1, self.tag)
				# 	angle = self.draw_tools.getAnglePoints(hip, hka_point, ankle_m1)
				
				# # hka bugfix, impossible to recreate
				# if angle < 20:
				# 	angle = 180.0 - angle


				if side == "LEFT":						
					angle = self.draw_tools.getAnglePoints(ankle_m1, hka_point, hip)					
					# hka bugfix, impossible to recreate
					if angle < 20:
						angle = 180.0 - angle

					elif angle > 270:
						pre_angle = self.draw_tools.getAnglePoints(hip, hka_point, ankle_m1)
						angle = 180.0 - pre_angle					

				else:
					angle = self.draw_tools.getAnglePoints(hip, hka_point, ankle_m1)					
					# hka bugfix, impossible to recreate
					if angle < 20:
						angle = 180.0 - angle

					elif angle > 270:
						pre_angle = self.draw_tools.getAnglePoints(ankle_m1, hka_point, hip)
						angle = 180.0 - pre_angle		


				# check if value exists
				if self.dict["EXCEL"][self.op_type][side]["HKA"] == None:

					self.dict["EXCEL"][self.op_type][side]["HASDATA"] 	= True
					self.dict["EXCEL"][self.op_type][side]["HKA"]	 	= '{0:.1f}'.format(angle)

					jda = None
					if angle > 180:
						jda = angle - 180
					else:
						jda = 180 - angle

					self.dict["EXCEL"][self.op_type][side]["JDA"] = '{0:.1f}'.format(jda)

					# save after insert
					self.controller.save_json()

						


	def obj_draw_pil(self):

		self.obj_draw_pil2()
		return

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
						# text = "HKA: {0:.1f}".format(hka_angle)
						# offset = -1*(60 + self.draw_tools.pil_get_text_size(text))
						# print('offset: {}'.format(offset))
					else:
						# angle = self.draw_tools.create_myAngle(hip, hka_point, ankle_m1, self.tag)
						hka_angle = self.draw_tools.pil_create_myAngle(hip, hka_point, ankle_m1)
						
					

					# self.draw_tools.pil_create_mytext(hka_point, "HKA: {0:.1f}".format(hka_angle), x_offset=offset, color="blue")					


					# keep overwriting to exclude None values
					hka_text = 'HKA: {0:.1f}'.format(hka_angle)
					vca_text = ""
					mad_text = ""

					if isDist:
						vca_text = 'VCA: {0:.1f}'.format(vca_angle)
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


	def obj_draw_pil2(self):
		print('draw PIL HKA 2')

		# 1. draw points from LEFT and RIGHT
		# 2. check if LEFT RIGHT data is available
		# 3a. check if labels fit within the gap (2 legs)
		# 3b. check height and change font size accordingly (1 leg)



		# 1. draw points from LEFT and RIGHT
		# 2. check if LEFT RIGHT data is available
		isRightData = False
		isLeftData 	= False

		L_hka_angle = None
		L_vca_angle = None
		L_mad_val 	= None

		R_hka_angle = None
		R_vca_angle = None
		R_mad_val 	= None

		L_multi_text = None
		R_multi_text = None

		# borrow from draw
		self.point_size = self.controller.getViewPointSize()

		# loop left and right
		for side in ["LEFT","RIGHT"]:

			isHip 		= False
			isFemKnee 	= False
			isTibKnee 	= False
			isDist 		= False
			isAnkle		= False
			isMad 		= False

			hip 		= self.dict["MAIN"][self.op_type][side]["HIP"]["P1"]
			fem_knee 	= self.dict["MAIN"][self.op_type][side]["FEM_KNEE"]["P1"]
			tib_knee 	= self.dict["MAIN"][self.op_type][side]["TIB_KNEE"]["P1"]
			
			ankle_p1 	= self.dict["MAIN"][self.op_type][side]["ANKLE"]["P1"]
			ankle_p2 	= self.dict["MAIN"][self.op_type][side]["ANKLE"]["P2"]
			ankle_m1 	= self.dict["MAIN"][self.op_type][side]["ANKLE"]["M1"]

			# dist_fem_p1 = self.dict["MAIN"][self.op_type][side]["DIST_FEM"]["P1"]
			# dist_fem_p2 = self.dict["MAIN"][self.op_type][side]["DIST_FEM"]["P2"]
			# dist_fem_m1 = self.dict["MAIN"][self.op_type][side]["DIST_FEM"]["M1"]

			dist_fem_p1 = self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["L3"]["P1"]
			dist_fem_p2 = self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["L3"]["P2"]
			dist_fem_m1 = self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["L3"]["M1"]

			mad_val 	= self.dict["EXCEL"][self.op_type][side]["MAD"]
			
			vca_angle = None

			# keep overwriting to exclude None values
			hka_text 	= ""
			vca_text 	= ""
			mad_text 	= ""
			nl 		 	= "\n"
			multi_text 	= ""			


			# KNEE
			if fem_knee != None: isFemKnee 	= True
			if tib_knee != None: isTibKnee 	= True

			# MAD
			if mad_val 	!= None: isMad 		= True


			# HIP
			if hip != None:
				isHip = True
				self.draw_tools.pil_create_mypoint(hip, "orange", point_thickness=self.point_size)

			# DIST
			if dist_fem_p1 != None and dist_fem_p2 != None:
				try:
					vca_angle = self.draw_tools.getSmallestAngle(dist_fem_m1, fem_knee, hip)				
					isDist = True
				except Exception as e:
					print(e)
							
			# ANKLE
			if ankle_p1 != None and ankle_p2 != None:	
				self.draw_tools.pil_create_mypoint(ankle_m1, "orange", point_thickness=self.point_size)
				isAnkle = True


			# ALL data
			if isHip and isTibKnee and isFemKnee and isAnkle:

				# fem-tib-intersection
				hka_point = self.draw_tools.line_intersection((ankle_m1, tib_knee), (hip, fem_knee))

				# hip-knee line
				self.draw_tools.pil_create_myline(hip, hka_point)
				self.draw_tools.pil_create_myline(hka_point, ankle_m1)

				# consolidate all vals into multi-text
				if isDist:	vca_text = 'VCA: {0:.1f}'.format(vca_angle)
				if isMad:	mad_text = 'MAD: {}'.format(mad_val)
				
				

				if side == "LEFT":				
					isLeftData 	= True
					L_hka_angle = self.draw_tools.pil_create_myAngle(ankle_m1, hka_point, hip)

					if isDist: 	L_vca_angle = vca_angle
					if isMad: 	L_mad_val 	= mad_val

					hka_text = 'HKA: {0:.1f}'.format(L_hka_angle)
					multi_text = hka_text + nl + vca_text + nl + mad_text
					if self.op_type == "POST-OP": 
						multi_text = hka_text + nl + mad_text

					L_multi_text = multi_text
		

				else:
					isRightData = True
					R_hka_angle = self.draw_tools.pil_create_myAngle(hip, hka_point, ankle_m1)

					if isDist: 	R_vca_angle = vca_angle
					if isMad: 	R_mad_val 	= mad_val

					hka_text = 'HKA: {0:.1f}'.format(R_hka_angle)
					multi_text = hka_text + nl + vca_text + nl + mad_text
					if self.op_type == "POST-OP": 
						multi_text = hka_text + nl + mad_text

					R_multi_text = multi_text

		# debug
		print('L_hka_angle: {}'.format(L_hka_angle))
		print('L_vca_angle: {}'.format(L_vca_angle))
		print('L_mad_val: {}'.format(L_mad_val))
		print('R_hka_angle: {}'.format(R_hka_angle))
		print('R_vca_angle: {}'.format(R_vca_angle))
		print('R_mad_val: {}'.format(R_mad_val))


		
		# gap is defined by MAD line
		# for right, right MAD point
		# for left, left MAD point

		# 3a. check if labels fit within the gap
		if isRightData and isLeftData:
			pre_R_mad_p1 = self.dict["MAIN"][self.op_type]["RIGHT"]["MAD_LINE"]["P1"]
			pre_R_mad_p2 = self.dict["MAIN"][self.op_type]["RIGHT"]["MAD_LINE"]["P2"]

			pre_L_mad_p1 = self.dict["MAIN"][self.op_type]["LEFT"]["MAD_LINE"]["P1"]
			pre_L_mad_p2 = self.dict["MAIN"][self.op_type]["LEFT"]["MAD_LINE"]["P2"]

			_, R_mad =  self.draw_tools.retPointsLeftRight(pre_R_mad_p1, pre_R_mad_p2)
			L_mad, _ =  self.draw_tools.retPointsLeftRight(pre_L_mad_p1, pre_L_mad_p2)

			# L/R is geometric here, not medical, hence the flip of R/L
			# RIP 2 hours
			R_mad, L_mad = self.draw_tools.get_yaxis_adjusted_points(L_mad, R_mad)


			# debug			
			# self.draw_tools.pil_create_mypoint(R_mad, "orange", point_thickness=self.point_size)
			# self.draw_tools.pil_create_mypoint(L_mad, "orange", point_thickness=self.point_size)
			# self.draw_tools.pil_create_myline(R_mad, L_mad)
			mad_dist = self.draw_tools.getDistance(R_mad, L_mad)
			print('print dist: {}'.format(mad_dist))
			print('L text: {}'.format(self.draw_tools.pil_get_multiline_text_size(L_multi_text)))
			print('R text: {}'.format(self.draw_tools.pil_get_multiline_text_size(R_multi_text)))
			

			mad_dist = self.draw_tools.getDistance(R_mad, L_mad)
			
			gap_dist, L_text_dist, R_text_dist = self.checkFontSizePadding(mad_dist, L_multi_text, R_multi_text)
			padding = self.pil_options[self.cur_option]["padding"]


			# RIGHT
			x1,y1,x2,y2 = self.draw_tools.pil_get_text_bbox(R_mad, R_multi_text, x_offset=gap_dist, y_offset=0)
			self.draw_tools.pil_draw_rect([x1,y1,x2,y2], padding=padding)
			self.draw_tools.pil_create_multiline_text(R_mad, R_multi_text, x_offset=gap_dist, y_offset=0, color=(255,255,255,255))

			# LEFT
			L_gap = -1*(gap_dist + L_text_dist)			
			x1,y1,x2,y2 = self.draw_tools.pil_get_text_bbox(L_mad, L_multi_text, x_offset=L_gap, y_offset=0)
			self.draw_tools.pil_draw_rect([x1,y1,x2,y2], padding=padding)
			self.draw_tools.pil_create_multiline_text(L_mad, L_multi_text, x_offset=L_gap, y_offset=0, color=(255,255,255,255))


		# 3b. check height and change font size accordingly (1 leg)
		elif isRightData:

			pre_R_mad_p1 = self.dict["MAIN"][self.op_type]["RIGHT"]["MAD_LINE"]["P1"]
			pre_R_mad_p2 = self.dict["MAIN"][self.op_type]["RIGHT"]["MAD_LINE"]["P2"]

			_, R_mad =  self.draw_tools.retPointsLeftRight(pre_R_mad_p1, pre_R_mad_p2)

			padding = self.pil_options[self.cur_option]["padding"]

			# R_text_dist = self.draw_tools.pil_get_multiline_text_size(R_multi_text)
			
			# debug
			print(self.draw_tools.imheight)
			# xtop,ytop,xbot,ybot = self.draw_tools.getImageCorners()
			# print('xtop:{}, ytop:{}, xbot:{}, ybot:{}'.format(xtop,ytop,xbot,ybot))


			# default is 30
			# target smallest and increase from there
			xoffset = 30
			padding = 20

			if self.draw_tools.imheight < 2500 and self.draw_tools.imheight >= 1500:
				self.draw_tools.changePILfontsize(20)
				padding = 10
				xoffset = 20

			elif self.draw_tools.imheight < 1500:				
				self.draw_tools.changePILfontsize(10)
				padding = 5
				xoffset = 10




			# RIGHT
			x1,y1,x2,y2 = self.draw_tools.pil_get_text_bbox(R_mad, R_multi_text, x_offset=xoffset, y_offset=0)
			self.draw_tools.pil_draw_rect([x1,y1,x2,y2], padding=padding)
			self.draw_tools.pil_create_multiline_text(R_mad, R_multi_text, x_offset=xoffset, y_offset=0, color=(255,255,255,255))


		elif isLeftData:

			pre_L_mad_p1 = self.dict["MAIN"][self.op_type]["LEFT"]["MAD_LINE"]["P1"]
			pre_L_mad_p2 = self.dict["MAIN"][self.op_type]["LEFT"]["MAD_LINE"]["P2"]

			L_mad, _ =  self.draw_tools.retPointsLeftRight(pre_L_mad_p1, pre_L_mad_p2)

			padding = self.pil_options[self.cur_option]["padding"]

			L_text_dist = self.draw_tools.pil_get_multiline_text_size(L_multi_text)

			
			# debug
			print(self.draw_tools.imheight)
			# xtop,ytop,xbot,ybot = self.draw_tools.getImageCorners()
			# print('xtop:{}, ytop:{}, xbot:{}, ybot:{}'.format(xtop,ytop,xbot,ybot))


			# default is 30
			# target smallest and increase from there
			xoffset = 30
			padding = 20

			if self.draw_tools.imheight < 2500 and self.draw_tools.imheight >= 1500:
				self.draw_tools.changePILfontsize(20)
				L_text_dist = self.draw_tools.pil_get_multiline_text_size(L_multi_text)
				padding = 10
				xoffset = 20

			elif self.draw_tools.imheight < 1500:				
				self.draw_tools.changePILfontsize(10)
				L_text_dist = self.draw_tools.pil_get_multiline_text_size(L_multi_text)
				padding = 5
				xoffset = 10




			# LEFT
			L_gap = -1*(xoffset + L_text_dist)
			# L_gap = L_text_dist
			x1,y1,x2,y2 = self.draw_tools.pil_get_text_bbox(L_mad, L_multi_text, x_offset=L_gap, y_offset=0)
			self.draw_tools.pil_draw_rect([x1,y1,x2,y2], padding=padding)
			self.draw_tools.pil_create_multiline_text(L_mad, L_multi_text, x_offset=L_gap, y_offset=0, color=(255,255,255,255))





			


	# logic for resizing
	# font size, gap and padding
	# if gap distance < padding
	# try a smaller font size and padding
	def checkFontSizePadding(self, mad_dist, L_multi_text, R_multi_text):

		L_text_dist = self.draw_tools.pil_get_multiline_text_size(L_multi_text)
		R_text_dist = self.draw_tools.pil_get_multiline_text_size(R_multi_text)

		gap_dist 	= math.floor((mad_dist - (L_text_dist+R_text_dist)) / 3)
		print('gap: {}'.format(gap_dist))

		if gap_dist < self.pil_options[self.cur_option]["padding"]:
			print("change font size and recalculate")

			self.cur_option = self.cur_option+1
			if self.cur_option <= 9:
				self.draw_tools.changePILfontsize(self.pil_options[self.cur_option]["fontsize"])

				print('new font size: {}'.format(self.pil_options[self.cur_option]["fontsize"]))

				return self.checkFontSizePadding(mad_dist, L_multi_text, R_multi_text)


		return gap_dist, L_text_dist, R_text_dist
