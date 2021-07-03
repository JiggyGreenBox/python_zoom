

class DRAW():
	"""docstring for ClassName"""
	def __init__(self, draw_tools, master_dict, controller, op_type):
		self.name = "DRAW"
		self.tag = "draw"
		self.menu_label = "DRAW_Menu"
		self.draw_tools = draw_tools
		self.dict = master_dict
		self.controller = controller
		self.side = None
		self.op_type = op_type

		self.point_size = None

		self.draw_line 	= False
		self.draw_angle = False
		self.draw_map 	= False

		self.line_list = []
		self.angle_list = []
		self.map_list = []

		self.line_dict = {}
		self.angle_dict = {}
		self.map_dict = {}

		self.map_val_cm = 0
		self.map_val_px = 0

		self.px_to_cm = 0


	def click(self, event):
		# print("click from "+self.name)		
		ret =  self.addDict(event)
		# print(self.map_list)
		self.draw()

	def right_click(self, event):
		pass

	def keyRightObjFunc(self):
		pass

	def keyLeftObjFunc(self):
		pass

	def hover(self, P_mouse, P_stored, hover_label):

		if hover_label == "h_line":			
			self.draw_tools.clear_by_tag("hover_line")
			self.draw_tools.create_myline(P_stored, P_mouse, "hover_line")

	def regainHover(self, side):
		pass
	def escapeObjFunc(self):
		pass


	def addDict(self, event):
		if self.draw_line:

			# get the point from mouse click
			P = self.draw_tools.getRealCoords(event)

			# at least one pair exits
			if (bool(self.line_dict)):
				# get the last element
				last_key = list(self.line_dict.keys())[-1]
				last = self.line_dict[last_key]['points']
				

				# check if pair is incomplete
				if( len(last) == 1 ):
					# add to pair
					last.append(P)
					self.controller.obj_to_menu(self.menu_label, "line_dict", self.line_dict)

					self.draw_tools.setHoverPointLabel(None)
					self.draw_tools.setHoverPoint(None)
					self.draw_tools.setHoverBool(False)
					

				elif( len(last) == 2 ):
					# add to next pair
					temp=[]					
					temp.append(P)
					next_val = int(''.join(filter(str.isdigit, last_key))) + 1
					next_key = 'L'+str(next_val)
					
					self.line_dict[next_key] = {}				
					self.line_dict[next_key]['points'] = temp
					self.line_dict[next_key]['px'] = None
					self.line_dict[next_key]['cm'] = None
					self.controller.obj_to_menu(self.menu_label, "line_dict", self.line_dict)

					self.draw_tools.setHoverPointLabel("h_line")
					self.draw_tools.setHoverPoint(P)
					self.draw_tools.setHoverBool(True)

			# first click
			else:
				# add to list
				temp=[]
				temp.append(P)
				self.line_dict['L1'] = {}		
				self.line_dict['L1']['points'] = temp
				self.line_dict['L1']['px'] = None
				self.line_dict['L1']['cm'] = None
				self.controller.obj_to_menu(self.menu_label, "line_dict", self.line_dict)

				self.draw_tools.setHoverPointLabel("h_line")
				self.draw_tools.setHoverPoint(P)
				self.draw_tools.setHoverBool(True)

			print(self.line_dict)
			
		elif self.draw_angle:

			# get the point from mouse click
			P = self.draw_tools.getRealCoords(event)

			# at least one pair exits
			if (bool(self.angle_dict)):
				# get the last element
				last_key = list(self.angle_dict.keys())[-1]
				last = self.angle_dict[last_key]['points']

				# check if pair is incomplete				
				if( len(last) == 1 ):
					# add to pair
					last.append(P)
					self.controller.obj_to_menu(self.menu_label, "angle_dict", self.angle_dict)

					self.draw_tools.setHoverPointLabel("h_line")
					self.draw_tools.setHoverPoint(P)
					self.draw_tools.setHoverBool(True)

				elif( len(last) == 2 ):
					# add to pair
					last.append(P)
					# self.controller.obj_to_menu(self.menu_label, "angle_dict", self.angle_dict)

					self.draw_tools.setHoverPointLabel(None)
					self.draw_tools.setHoverPoint(None)
					self.draw_tools.setHoverBool(False)

				elif( len(last) == 3 ):
					# add to next pair					
					temp=[]					
					temp.append(P)
					next_val = int(''.join(filter(str.isdigit, last_key))) + 1
					next_key = 'A'+str(next_val)

					self.angle_dict[next_key] = {}
					self.angle_dict[next_key]['points'] = temp
					self.angle_dict[next_key]['angle'] = None
					self.angle_dict[next_key]['flip'] = False
					# self.controller.obj_to_menu(self.menu_label, "angle_dict", self.angle_dict)

					self.draw_tools.setHoverPointLabel("h_line")
					self.draw_tools.setHoverPoint(P)
					self.draw_tools.setHoverBool(True)

			# first click
			else:
				# add to list
				temp=[]
				temp.append(P)
				self.angle_dict['A1'] = {}
				self.angle_dict['A1']['points'] = temp
				self.angle_dict['A1']['angle'] = None
				self.angle_dict['A1']['flip'] = False
				self.controller.obj_to_menu(self.menu_label, "angle_dict", self.angle_dict)

				self.draw_tools.setHoverPointLabel("h_line")
				self.draw_tools.setHoverPoint(P)
				self.draw_tools.setHoverBool(True)

		elif self.draw_map:

			# get the point from mouse click
			P = self.draw_tools.getRealCoords(event)

			# at least one pair exits
			if (bool(self.map_dict)):
				# get the last element
				last_key = list(self.map_dict.keys())[-1]
				last = self.map_dict[last_key]

				# check if pair is incomplete
				# print('last size:{}'.format(len(last)))
				if( len(last) == 1 ):
					# add to pair
					last.append(P)
					self.controller.obj_to_menu(self.menu_label, "map_dict", self.map_dict)

					self.draw_tools.setHoverPointLabel(None)
					self.draw_tools.setHoverPoint(None)
					self.draw_tools.setHoverBool(False)
					
			# first click
			else:
				# add to list
				temp=[]
				temp.append(P)
				self.map_dict['M1'] = temp
				self.controller.obj_to_menu(self.menu_label, "map_dict", self.map_dict)

				self.draw_tools.setHoverPointLabel("h_line")
				self.draw_tools.setHoverPoint(P)
				self.draw_tools.setHoverBool(True)






	def draw(self):
		
		self.draw_tools.clear_by_tag(self.tag)

		self.point_size = self.controller.getViewPointSize()

		# lines
		if bool(self.line_dict) > 0:
			for k in self.line_dict.keys():
				
				pair = self.line_dict[k]['points']
				
				if len(pair) == 2:
					self.draw_tools.create_mypoint(pair[0], "orange", [self.tag], point_thickness=self.point_size)
					self.draw_tools.create_mypoint(pair[1], "orange", [self.tag], point_thickness=self.point_size)
					self.draw_tools.create_myline(pair[0], pair[1], [self.tag])
					m = self.draw_tools.midpoint(pair[0], pair[1])
					self.draw_tools.create_mytext(m, k, [self.tag], color="blue")

					# update the length in px
					if self.line_dict[k]['px'] == None:						
						self.line_dict[k]['px']	= self.draw_tools.getDistance(pair[0],pair[1])

					# update the length in cm
					if self.line_dict[k]['cm'] == None and self.line_dict[k]['px'] != None:
						if self.px_to_cm != 0:							
							self.line_dict[k]['cm'] = self.px_to_cm * self.line_dict[k]['px']

							# update the dict in menu list
							self.controller.obj_to_menu(self.menu_label, "line_dict", self.line_dict)

				else:
					self.draw_tools.create_mypoint(pair[0], "orange", [self.tag], point_thickness=self.point_size)



		# angles
		if bool(self.angle_dict) > 0:
			for k in self.angle_dict.keys():

				triplet = self.angle_dict[k]['points']

				if len(triplet) == 3:
					self.draw_tools.create_mypoint(triplet[0], "orange", [self.tag], point_thickness=self.point_size)
					self.draw_tools.create_mypoint(triplet[1], "orange", [self.tag], point_thickness=self.point_size)
					self.draw_tools.create_mypoint(triplet[2], "orange", [self.tag], point_thickness=self.point_size)

					angle = None
					if self.angle_dict[k]['flip'] == True:
						angle = self.draw_tools.create_myAngle(triplet[0],triplet[1],triplet[2], [self.tag])
					else:
						angle = self.draw_tools.create_myAngle(triplet[2],triplet[1],triplet[0], [self.tag])

					if angle != None:
						self.angle_dict[k]['angle'] = angle

					# update the menu obj
					self.controller.obj_to_menu(self.menu_label, "angle_dict", self.angle_dict)

					self.draw_tools.create_myline(triplet[0], triplet[1], [self.tag])
					self.draw_tools.create_myline(triplet[1], triplet[2], [self.tag])
					self.draw_tools.create_mytext(triplet[1], k, [self.tag], color="blue")
					self.draw_tools.create_mytext(triplet[1], '{0:.1f}'.format(angle), [self.tag], y_offset=30, color="blue")
				elif len(triplet) == 2:
					self.draw_tools.create_mypoint(triplet[0], "orange", [self.tag], point_thickness=self.point_size)
					self.draw_tools.create_mypoint(triplet[1], "orange", [self.tag], point_thickness=self.point_size)
					self.draw_tools.create_myline(triplet[0], triplet[1], [self.tag])				
				elif len(triplet) == 1:
					self.draw_tools.create_mypoint(triplet[0], "orange", [self.tag], point_thickness=self.point_size)


		# map
		if bool(self.map_dict) > 0:
			for k in self.map_dict.keys():
				
				# print(self.map_dict)
				pair = self.map_dict[k]

				if len(pair) == 2:
					self.draw_tools.create_mypoint(pair[0], "orange", [self.tag], point_thickness=self.point_size)
					self.draw_tools.create_mypoint(pair[1], "orange", [self.tag], point_thickness=self.point_size)
					self.draw_tools.create_myline(pair[0], pair[1], [self.tag])

					self.map_val_px = self.draw_tools.getDistance(pair[0], pair[1])
					self.map_px_to_cm()
				else:
					self.draw_tools.create_mypoint(pair[0], "orange", [self.tag], point_thickness=self.point_size)
		# if len(self.map_list) > 0:
		# 	for pair in self.map_list:
		# 		if len(pair) == 2:
		# 			self.draw_tools.create_mypoint(pair[0], "orange", [self.tag], point_thickness=self.point_size)
		# 			self.draw_tools.create_mypoint(pair[1], "orange", [self.tag], point_thickness=self.point_size)
		# 			self.draw_tools.create_myline(pair[0], pair[1], [self.tag])
		# 		else:
		# 			self.draw_tools.create_mypoint(pair[0], "orange", [self.tag], point_thickness=self.point_size)





	def drag_start(self, tags):
		pass

	def drag(self, P_mouse):
		pass

	def drag_stop(self, P_mouse):
		pass
		

	# menu button clicks are routed here
	def menu_btn_click(self, action):
		print(action)

		if action == "SET-LINE":
			self.draw_line 	= True
			self.draw_angle = False
			self.draw_map 	= False

		elif action == "SET-ANGLE":
			self.draw_angle = True
			self.draw_line 	= False
			self.draw_map 	= False

		elif action == "SET-MAP":
			self.draw_map 	= True
			self.draw_line 	= False
			self.draw_angle = False
			


	def update_canvas(self, draw_tools):
		self.draw_tools = draw_tools


	def update_dict(self, master_dict):
		self.dict = master_dict


	def unset(self):
		print("unset from "+self.name)
		self.draw_tools.clear_by_tag(self.tag)


	def menu_to_obj(self, key, val):
		print('key: {} : val:{}'.format(key,val))

		if key == "UPDATE_ANGLE":
			self.angle_dict = val

		if key == "UPDATE_LINE":
			self.line_dict = val

		if key == "UPDATE_MAP":
			self.map_dict = val

		if key == "MAP_VAL":
			self.map_val_cm = int(val)
			self.map_px_to_cm()

		self.draw()


	def map_px_to_cm(self):
		print('map')
		if self.map_val_px != 0 and self.map_val_cm != 0:
			self.px_to_cm = self.map_val_cm / self.map_val_px
			print('map_px: {} map_cm:{} cm_to_px:{}'.format(self.map_val_px,self.map_val_cm,self.px_to_cm))