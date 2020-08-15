

class HKA():
	"""docstring for ClassName"""
	def __init__(self, draw_tools, master_dict, controller, op_type):
		self.name = "HKA"
		self.tag = "hka"
		self.draw_tools = draw_tools
		self.dict = master_dict
		self.op_type = op_type
		self.controller = controller

		
	def click(self, event):
		print("click from "+self.name)
		self.draw_tools.clear_by_tag(self.tag)
		self.draw() 


	def draw(self):

		# loop left and right
		for side in ["LEFT","RIGHT"]:

			isHip = False
			isKnee = False

			hip 		= self.dict["MAIN"][self.op_type][side]["HIP"]["P1"]
			knee 		= self.dict["MAIN"][self.op_type][side]["KNEE"]["P1"]			
			
			ankle_p1 	= self.dict["MAIN"][self.op_type][side]["ANKLE"]["P1"]
			ankle_p2 	= self.dict["MAIN"][self.op_type][side]["ANKLE"]["P2"]
			ankle_m1 	= self.dict["MAIN"][self.op_type][side]["ANKLE"]["M1"]


			# HIP
			if hip != None:
				isHip = True
				self.draw_tools.create_mypoint(hip, "white", self.tag)

			# KNEE
			if knee != None:
				isKnee = True
				self.draw_tools.create_mypoint(knee, "white", self.tag)


			# ANKLE
			if ankle_p1 != None and ankle_p2 != None:
				
				self.draw_tools.create_mypoint(ankle_p1, "white", self.tag)
				self.draw_tools.create_mypoint(ankle_p2, "white", self.tag)
				self.draw_tools.create_midpoint_line(ankle_p1, ankle_p2, ankle_m1, self.tag)

				if isHip and isKnee:

					# ankle-knee ray
					xtop, ytop, xbot, ybot = self.draw_tools.getImageCorners()
					p_top = self.draw_tools.line_intersection((ankle_m1, knee), (xtop, ytop))
					self.draw_tools.create_myline(ankle_m1, p_top, self.tag)

					# hip-knee line
					self.draw_tools.create_myline(hip, knee, self.tag)

					# draw angle
					angle = ""

					'''
					if side == "LEFT":						
						angle = self.draw_tools.create_myAngle(self.dict["MAIN"][self.op_type][side]["HIP"]["P1"], self.dict["MAIN"][self.op_type][side]["KNEE"]["P1"], p_top, self.tag)
					else:
						angle = self.draw_tools.create_myAngle(p_top, self.dict["MAIN"][self.op_type][side]["KNEE"]["P1"], self.dict["MAIN"][self.op_type][side]["HIP"]["P1"], self.tag)
					'''

					if side == "LEFT":						
						angle = self.draw_tools.create_myAngle(ankle_m1, knee, hip, self.tag)
					else:
						angle = self.draw_tools.create_myAngle(hip, knee, ankle_m1, self.tag)
						
					# , radius = 50, width = 3):
					# self.canvas.create_text(x-r,y+r,fill="white", text='{0:.2f}'.format(t1), tags="tag")
					
					self.draw_tools.create_mytext(self.dict["MAIN"][self.op_type][side]["KNEE"]["P1"], '{0:.2f}'.format(angle), self.tag, x_offset=60)


					# check if value exists
					if self.dict["EXCEL"][self.op_type][side]["HKA"] == None:

						self.dict["EXCEL"][self.op_type][side]["HASDATA"] 	= True
						self.dict["EXCEL"][self.op_type][side]["HKA"]	 	= '{0:.2f}'.format(angle)

						# save after insert
						self.controller.save_json()



	def update_canvas(self, draw_tools):
		self.draw_tools = draw_tools

	def update_dict(self, master_dict):
		self.dict = master_dict

	def unset(self):
		# print("unset from "+self.name)
		self.draw_tools.clear_by_tag(self.tag)
		self.side = None

						