

class VCA():
	"""docstring for ClassName"""
	def __init__(self, draw_tools, master_dict, controller):
		self.name = "VCA"
		self.tag = "vca"
		self.draw_tools = draw_tools
		self.dict = master_dict
		self.controller = controller
		self.side = None

	def click(self, event):
		print("click from "+self.name)

	def draw(self):

		# loop left and right
		for side in ["LEFT","RIGHT"]:


			# ------------------------
			# FROM MAIN
			# ------------------------

			isHip = False
			isKnee = False
			isFemBot = False


			# HIP
			if self.dict["MAIN"][side]["HIP"]["P1"] != None:
				isHip = True
				self.draw_tools.create_mypoint(self.dict["MAIN"][side]["HIP"]["P1"], "white", self.tag)

			# KNEE
			if self.dict["MAIN"][side]["KNEE"]["P1"] != None:
				isKnee = True
				self.draw_tools.create_mypoint(self.dict["MAIN"][side]["KNEE"]["P1"], "white", self.tag)

			# HIP-KNEE-LINE
			if self.dict["MAIN"][side]["HIP"]["P1"] != None and self.dict["MAIN"][side]["KNEE"]["P1"] != None:
				self.draw_tools.create_myline(self.dict["MAIN"][side]["HIP"]["P1"], self.dict["MAIN"][side]["KNEE"]["P1"], self.tag)
				isAldfa = True



			# FEM AXIS			
			# BOT
			if self.dict["MAIN"][side]["AXIS_FEM"]["BOT"]["P1"] != None:
				self.draw_tools.create_mypoint(self.dict["MAIN"][side]["AXIS_FEM"]["BOT"]["P1"], "white", self.tag)

			if self.dict["MAIN"][side]["AXIS_FEM"]["BOT"]["P2"] != None:
				self.draw_tools.create_mypoint(self.dict["MAIN"][side]["AXIS_FEM"]["BOT"]["P2"], "white", self.tag)

			if self.dict["MAIN"][side]["AXIS_FEM"]["BOT"]["P1"] != None and self.dict["MAIN"][side]["AXIS_FEM"]["BOT"]["P2"] != None:
				p1 = self.dict["MAIN"][side]["AXIS_FEM"]["BOT"]["P1"]
				p2 = self.dict["MAIN"][side]["AXIS_FEM"]["BOT"]["P2"]
				m1 = self.dict["MAIN"][side]["AXIS_FEM"]["BOT"]["M1"]
				self.draw_tools.create_midpoint_line(p1, p2, m1, self.tag)
				isFemBot = True

			if isHip and isKnee and isFemBot:

				# knee fem-bot ray
				xtop, ytop, xbot, ybot = self.draw_tools.getImageCorners()
				p_top = self.draw_tools.line_intersection((self.dict["MAIN"][side]["KNEE"]["P1"], self.dict["MAIN"][side]["AXIS_FEM"]["BOT"]["M1"]), (xtop, ytop))
				self.draw_tools.create_myline(self.dict["MAIN"][side]["KNEE"]["P1"], p_top, self.tag)




	def unset(self):
		print("unset from "+self.name)
		self.draw_tools.clear_by_tag(self.tag)