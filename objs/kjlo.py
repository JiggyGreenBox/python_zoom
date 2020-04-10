import math

class KJLO():
	"""docstring for ClassName"""
	def __init__(self, draw_tools, master_dict, controller):
		self.name = "KJLO"
		self.tag = "kjlo"
		self.draw_tools = draw_tools
		self.dict = master_dict		

		
	def click(self, event):
		print("click from "+self.name)
		# self.draw() 

		print(self.slope((0,0),(10,10)))



	def slope(self, point1, point2):
		x1 = point1[0]
		y1 = point1[1]
		x2 = point2[0]
		y2 = point2[1]
		return (y2-y1)/(x2-x1)


	def draw(self):

		# loop left and right
		for side in ["LEFT","RIGHT"]:

			isTamd = False


			# ------------------------
			# FROM TAMD
			# ------------------------
			if self.dict["TAMD"][side]["TIB_JOINT_LINE"]["P1"] != None:
				self.draw_tools.create_mypoint(self.dict["TAMD"][side]["TIB_JOINT_LINE"]["P1"], "white", self.tag)

			if self.dict["TAMD"][side]["TIB_JOINT_LINE"]["P2"] != None:
				self.draw_tools.create_mypoint(self.dict["TAMD"][side]["TIB_JOINT_LINE"]["P2"], "white", self.tag)

			if self.dict["TAMD"][side]["TIB_JOINT_LINE"]["P1"] != None and self.dict["TAMD"][side]["TIB_JOINT_LINE"]["P2"] != None:
				self.draw_tools.create_myline(self.dict["TAMD"][side]["TIB_JOINT_LINE"]["P1"], self.dict["TAMD"][side]["TIB_JOINT_LINE"]["P2"], self.tag)
				isTamd = True


			# ------------------------
			# FROM MAIN
			# ------------------------			
			# ANKLE
			if self.dict["MAIN"][side]["ANKLE"]["P1"] != None and self.dict["MAIN"][side]["ANKLE"]["P2"] != None:


				p1 = self.dict["MAIN"][side]["ANKLE"]["P1"]
				p2 = self.dict["MAIN"][side]["ANKLE"]["P2"]
				m1 = self.dict["MAIN"][side]["ANKLE"]["M1"]
				self.draw_tools.create_mypoint(p1, "white", self.tag)
				self.draw_tools.create_mypoint(p2, "white", self.tag)
				self.draw_tools.create_midpoint_line(p1, p2, m1, self.tag)



				# =============CLEAN UP==================================
				slope = self.slope(p1,p2)

				C = [0,0]
				# D = p1

				dy = math.sqrt(100**2/(slope**2+1))
				dx = -slope*dy
				# print("DX"+str(dx))
				# print("DY"+str(dy))
				C[0] = m1[0] + dx
				C[1] = m1[1] + dy
				# D[0] = m1[0] - dx
				# D[1] = m1[1] - dy

				print(C)
				# print(D)

				self.draw_tools.create_mypoint(C, "white", self.tag)
				# self.draw_tools.create_mypoint(D, "white", self.tag)

				# self.draw_tools.create_myline(C, D, self.tag)

				if isTamd:

					xtop, ytop, xbot, ybot = self.draw_tools.getImageCorners()

					# hip-knee ray
					p_top = self.draw_tools.line_intersection(
						(m1, C),
						(xtop, ytop))

					self.draw_tools.create_myline(m1, p_top, self.tag)


	def update_canvas(self, draw_tools):
		self.draw_tools = draw_tools


	def unset(self):
		print("unset from "+self.name)
		self.draw_tools.clear_by_tag(self.tag)		

						