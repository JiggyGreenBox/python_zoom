

class AFTA():
	"""docstring for ClassName"""
	def __init__(self, draw_tools, master_dict, controller, op_type):
		self.name = "AFTA"
		self.tag = "afta"
		self.draw_tools = draw_tools
		self.dict = master_dict
		self.op_type = op_type
		self.controller = controller

	def click(self, event):
		print("click from "+self.name)

	def draw(self):

		self.draw_tools.clear_by_tag(self.tag)
		
		# loop left and right
		for side in ["LEFT","RIGHT"]:

			isFemTop 	= False
			isFemBot 	= False

			isTibTop 	= False
			isTibBot 	= False

			# AXIS_FEM
			fem_top_p1 = self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["TOP"]["P1"]
			fem_top_p2 = self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["TOP"]["P2"]
			fem_top_m1 = self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["TOP"]["M1"]

			fem_bot_p1 = self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["BOT"]["P1"]
			fem_bot_p2 = self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["BOT"]["P2"]
			fem_bot_m1 = self.dict["MAIN"][self.op_type][side]["AXIS_FEM"]["BOT"]["M1"]

			# AXIS_TIB
			tib_top_p1 = self.dict["MAIN"][self.op_type][side]["AXIS_TIB"]["TOP"]["P1"]
			tib_top_p2 = self.dict["MAIN"][self.op_type][side]["AXIS_TIB"]["TOP"]["P2"]
			tib_top_m1 = self.dict["MAIN"][self.op_type][side]["AXIS_TIB"]["TOP"]["M1"]

			tib_bot_p1 = self.dict["MAIN"][self.op_type][side]["AXIS_TIB"]["BOT"]["P1"]
			tib_bot_p2 = self.dict["MAIN"][self.op_type][side]["AXIS_TIB"]["BOT"]["P2"]
			tib_bot_m1 = self.dict["MAIN"][self.op_type][side]["AXIS_TIB"]["BOT"]["M1"]

			# FEM AXIS
			# TOP
			if fem_top_p1 != None:
				self.draw_tools.create_mypoint(fem_top_p1, "white", [self.tag, side, "NO-DRAG"])

			if fem_top_p2 != None:
				self.draw_tools.create_mypoint(fem_top_p2, "white", [self.tag, side, "NO-DRAG"])

			if fem_top_p1 != None and fem_top_p2 != None:
				self.draw_tools.create_midpoint_line(fem_top_p1, fem_top_p2, fem_top_m1, self.tag)
				isFemTop = True


			# BOT
			if fem_bot_p1 != None:
				self.draw_tools.create_mypoint(fem_bot_p1, "white", [self.tag, side, "NO-DRAG"])

			if fem_bot_p2 != None:
				self.draw_tools.create_mypoint(fem_bot_p2, "white", [self.tag, side, "NO-DRAG"])

			if fem_bot_p1 != None and fem_bot_p2 != None:				
				self.draw_tools.create_midpoint_line(fem_bot_p1, fem_bot_p2, fem_bot_m1, self.tag)
				isFemBot = True


			# TIB AXIS
			# TOP
			if tib_top_p1 != None:
				self.draw_tools.create_mypoint(tib_top_p1, "white", [self.tag, side, "NO-DRAG"])

			if tib_top_p2 != None:
				self.draw_tools.create_mypoint(tib_top_p2, "white", [self.tag, side, "NO-DRAG"])

			if tib_top_p1 != None and tib_top_p2 != None:				
				self.draw_tools.create_midpoint_line(tib_top_p1, tib_top_p2, tib_top_m1, self.tag)
				isTibTop = True


			# BOT
			if tib_bot_p1 != None:
				self.draw_tools.create_mypoint(tib_bot_p1, "white", [self.tag, side, "NO-DRAG"])

			if tib_bot_p2 != None:
				self.draw_tools.create_mypoint(tib_bot_p2, "white", [self.tag, side, "NO-DRAG"])

			if tib_bot_p1 != None and tib_bot_p2 != None:				
				self.draw_tools.create_midpoint_line(tib_bot_p1, tib_bot_p1, tib_bot_m1, self.tag)
				isTibBot = True




			xtop, ytop, xbot, ybot = self.draw_tools.getImageCorners()

			if isFemBot and isFemTop:
				
				# FEM-AXIS ray
				p_fem = self.draw_tools.line_intersection(
					(fem_bot_m1, fem_top_m1),
					(xbot, ybot))

				# self.draw_tools.create_myline(fem_top_m1, p_fem, self.tag)

			if isTibTop and isTibBot:

				# TIB-AXIS ray
				p_tib = self.draw_tools.line_intersection(
					(tib_bot_m1, tib_top_m1),
					(xtop, ytop))

				self.draw_tools.create_myline(tib_bot_m1, p_tib, self.tag)


			if isFemBot and isFemTop and isTibTop and isTibBot:

				p_int = self.draw_tools.line_intersection((tib_bot_m1, tib_top_m1),
					(fem_bot_m1, fem_top_m1))

				# int debug
				self.draw_tools.create_mypoint(p_int, "white", [self.tag, side, "NO-DRAG"])
				self.draw_tools.create_myline(fem_top_m1, p_int, self.tag)

				a1 = self.draw_tools.getAnglePoints(p_tib, p_int, fem_top_m1)
				a2 = self.draw_tools.getAnglePoints(fem_top_m1, p_int, p_tib)
				print('{0:.2f} a1 RIGHT'.format(a1))
				print('{0:.2f} a2 RIGHT'.format(a2))

				if a1 < a2:					
					angle = self.draw_tools.create_myAngle(p_tib, p_int, fem_top_m1, self.tag)
				else:
					angle = self.draw_tools.create_myAngle(fem_top_m1, p_int, p_tib, self.tag)

				self.draw_tools.create_mytext(p_int, '{0:.2f}'.format(angle), self.tag, x_offset=-60)

				# p_int = self.draw_tools.line_intersection((tib_bot_m1, tib_top_m1),
				# 	(fem_bot_m1, fem_top_m1))

				# # int debug
				# self.draw_tools.create_mypoint(p_int, "white", self.tag)

				# a1 = self.draw_tools.getAnglePoints(tib_top_m1, p_int, fem_bot_m1)
				# a2 = self.draw_tools.getAnglePoints(fem_bot_m1, p_int, tib_top_m1)
				# print('{0:.2f} a1 RIGHT'.format(a1))
				# print('{0:.2f} a2 RIGHT'.format(a2))

				# if a1 < a2:					
				# 	angle = self.draw_tools.create_myAngle(tib_top_m1, p_int, fem_bot_m1, self.tag)
				# else:
				# 	angle = self.draw_tools.create_myAngle(fem_bot_m1, p_int, tib_top_m1, self.tag)

				# self.draw_tools.create_mytext(p_int, '{0:.2f}'.format(angle), self.tag, x_offset=-60)


				# check if value exists
				if self.dict["EXCEL"][self.op_type][side]["aFTA"] == None:

					self.dict["EXCEL"][self.op_type][side]["HASDATA"] 	= True
					self.dict["EXCEL"][self.op_type][side]["aFTA"]	 	= '{0:.2f}'.format(angle)

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
