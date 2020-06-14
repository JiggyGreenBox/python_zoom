import json

class MAIN:
	# instance attribute
	def __init__(self, draw_tools, master_dict, controller):
		self.name = "MAIN"
		self.draw_tools = draw_tools
		self.dict = master_dict
		self.controller = controller
		self.side = None

		# check if master dictionary has values
		# if not populate the dictionary
		self.checkMasterDict()


	def checkMasterDict(self):
		if "MAIN" not in self.dict.keys():
				self.dict["MAIN"] = 	{
										"LEFT":	{
												"HIP":		{"type":"point","P1":None},
												"KNEE":		{"type":"point","P1":None},
												"ANKLE":	{"type":"midpoint","P1":None,"P2":None, "M1":None},
												"AXIS_FEM":	{
																"type":	"axis",
																"TOP":	{"type":"midpoint","P1":None,"P2":None, "M1":None},
																"BOT":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
															},
												"AXIS_TIB":	{
																"type":	"axis",
																"TOP":	{"type":"midpoint","P1":None,"P2":None, "M1":None},
																"BOT":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
															}
												},
										"RIGHT":{
												"HIP":		{"type":"point","P1":None},
												"KNEE":		{"type":"point","P1":None},
												"ANKLE":	{"type":"midpoint","P1":None,"P2":None, "M1":None},
												"AXIS_FEM":	{
																"type":	"axis",
																"TOP":	{"type":"midpoint","P1":None,"P2":None, "M1":None},
																"BOT":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
															},
												"AXIS_TIB":	{
																"type":	"axis",
																"TOP":	{"type":"midpoint","P1":None,"P2":None, "M1":None},
																"BOT":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
															}
												}
										}


	def click(self, event):
		print("click from "+self.name)
		print(self.dict)

		# self.controller.updateMenuLabel("jiggy", "MAIN_Menu")
		# self.updateLabel(self.getNextLabel())
		# self.controller.updateMenuLabel(self.getNextLabel(), "MAIN_Menu")


		# self.draw()

		if self.side == None:
			print("please choose side")
			self.controller.warningBox("Please select a Side")
			# self.controller.testbubble()
		else:
			# print("proceed")
			ret =  self.addDict(event)
			if ret:				
				self.controller.save_json()
				# pass

		self.controller.updateMenuLabel(self.getNextLabel(), "MAIN_Menu")
		self.draw_tools.clear_by_tag("main")
		self.draw()

			# self.controller.updateMenuLabel("jiggy", "MAIN_Menu")

		# ret, cur_tag = self.addDict(event), cur_tag = self.addDict(event)	
		# if ret:
		# 	print(cur_tag)
		# 	self.draw_tools.create_token(event, "white", cur_tag)
		# 	self.drawLines()
		# else:
		# 	print(self.dict)




	# save dictionary to file
	def saveDict(self):
		pass
		# with open('patient.json', 'w') as fp:
		# 	json.dump(self.dict, fp, indent=4)		

	# menu button clicks are routed here
	def menu_btn_click(self, action):
		print(action)
		if action == "SET-LEFT":
			self.side = "LEFT"
			self.controller.updateMenuLabel(self.getNextLabel(), "MAIN_Menu")
			return # avoid clear,draw,json_save

		if action == "SET-RIGHT":
			self.side = "RIGHT"
			self.controller.updateMenuLabel(self.getNextLabel(), "MAIN_Menu")
			return # avoid clear,draw,json_save



		if action == "DEL-LEFT-HIP":
			self.dict["MAIN"]["LEFT"]["HIP"]["P1"] = None

		if action == "DEL-RIGHT-HIP":
			self.dict["MAIN"]["RIGHT"]["HIP"]["P1"] = None

		if action == "DEL-LEFT-KNEE":
			self.dict["MAIN"]["LEFT"]["KNEE"]["P1"] = None

		if action == "DEL-RIGHT-KNEE":
			self.dict["MAIN"]["RIGHT"]["KNEE"]["P1"] = None

		if action == "DEL-LEFT-ANKLE":
			self.dict["MAIN"]["LEFT"]["ANKLE"]["P1"] = None
			self.dict["MAIN"]["LEFT"]["ANKLE"]["P2"] = None
			self.dict["MAIN"]["LEFT"]["ANKLE"]["M1"] = None

		if action == "DEL-RIGHT-ANKLE":
			self.dict["MAIN"]["RIGHT"]["ANKLE"]["P1"] = None
			self.dict["MAIN"]["RIGHT"]["ANKLE"]["P2"] = None
			self.dict["MAIN"]["RIGHT"]["ANKLE"]["M1"] = None

		if action == "DEL-LEFT-FEM-TOP":
			self.dict["MAIN"]["LEFT"]["AXIS_FEM"]["TOP"]["P1"] = None
			self.dict["MAIN"]["LEFT"]["AXIS_FEM"]["TOP"]["P2"] = None
			self.dict["MAIN"]["LEFT"]["AXIS_FEM"]["TOP"]["M1"] = None

		if action == "DEL-RIGHT-FEM-TOP":
			self.dict["MAIN"]["RIGHT"]["AXIS_FEM"]["TOP"]["P1"] = None
			self.dict["MAIN"]["RIGHT"]["AXIS_FEM"]["TOP"]["P2"] = None
			self.dict["MAIN"]["RIGHT"]["AXIS_FEM"]["TOP"]["M1"] = None


		if action == "DEL-LEFT-FEM-BOT":
			self.dict["MAIN"]["LEFT"]["AXIS_FEM"]["BOT"]["P1"] = None
			self.dict["MAIN"]["LEFT"]["AXIS_FEM"]["BOT"]["P2"] = None
			self.dict["MAIN"]["LEFT"]["AXIS_FEM"]["BOT"]["M1"] = None

		if action == "DEL-RIGHT-FEM-BOT":
			self.dict["MAIN"]["RIGHT"]["AXIS_FEM"]["BOT"]["P1"] = None
			self.dict["MAIN"]["RIGHT"]["AXIS_FEM"]["BOT"]["P2"] = None
			self.dict["MAIN"]["RIGHT"]["AXIS_FEM"]["BOT"]["M1"] = None


		if action == "DEL-LEFT-TIB-TOP":
			self.dict["MAIN"]["LEFT"]["AXIS_TIB"]["TOP"]["P1"] = None
			self.dict["MAIN"]["LEFT"]["AXIS_TIB"]["TOP"]["P2"] = None
			self.dict["MAIN"]["LEFT"]["AXIS_TIB"]["TOP"]["M1"] = None

		if action == "DEL-RIGHT-TIB-TOP":
			self.dict["MAIN"]["RIGHT"]["AXIS_TIB"]["TOP"]["P1"] = None
			self.dict["MAIN"]["RIGHT"]["AXIS_TIB"]["TOP"]["P2"] = None
			self.dict["MAIN"]["RIGHT"]["AXIS_TIB"]["TOP"]["M1"] = None

		if action == "DEL-LEFT-TIB-BOT":
			self.dict["MAIN"]["LEFT"]["AXIS_TIB"]["BOT"]["P1"] = None
			self.dict["MAIN"]["LEFT"]["AXIS_TIB"]["BOT"]["P2"] = None
			self.dict["MAIN"]["LEFT"]["AXIS_TIB"]["BOT"]["M1"] = None

		if action == "DEL-RIGHT-TIB-BOT":
			self.dict["MAIN"]["RIGHT"]["AXIS_TIB"]["BOT"]["P1"] = None
			self.dict["MAIN"]["RIGHT"]["AXIS_TIB"]["BOT"]["P2"] = None
			self.dict["MAIN"]["RIGHT"]["AXIS_TIB"]["BOT"]["M1"] = None


		self.draw_tools.clear_by_tag("main")
		self.draw()
		self.controller.save_json()

		self.controller.updateMenuLabel(self.getNextLabel(), "MAIN_Menu")


	# return true to allow clicks
	# return current tag to draw function
	def addDict2(self, event):

		cur_tag = "MNSA_"

		# L1, L2, R1, L3, L4, R2
		for lines in self.dict:

			# type, P1, P2, M1
			for points in self.dict[lines]:	

				# rays are generated automatically dont allow
				if self.dict[lines]["type"] != "ray":

					# add points P1 and P2
					if points == "P1" or points == "P2":
						# only P1 and P2
						if self.dict[lines][points] == None:
							P = self.draw_tools.getRealCoords(event)						
							self.dict[lines][points] = P

							# set tag and pass to "create_token" for drag and drop
							cur_tag += str(lines)+"_"+str(points)

							# if P2 and line type is midpoint calculate and store
							if points == "P2" and self.dict[lines]["type"] == "midpoint":
								M = self.draw_tools.midpoint(self.dict[lines]["P1"], P)
								self.dict[lines]["M1"] = M


							

							# check if R1 is not None
							if self.dict["R1"]["P1"] == None:
								# if both midpoints of lines L1 ad L2, then draw ray R1
								# edit proof incase L1 or L2 is deleted
								if (self.dict["L1"]["P1"] != None 
									and self.dict["L1"]["P2"] != None
									and self.dict["L2"]["P1"] != None
									and self.dict["L2"]["P2"] != None):

									print("draw rays1")
									xtop, ytop, xbot, ybot = self.draw_tools.getImageCorners()
									
									print(xtop, ytop, xbot, ybot)
									R1M1 = self.dict["L1"]["M1"]
									R1M2 = self.dict["L2"]["M1"]
									ray1P1 = self.draw_tools.line_intersection((R1M1, R1M2), (xtop, ytop))
									print(ray1P1)
									self.dict["R1"]["P1"] = ray1P1
									self.dict["R1"]["P2"] = R1M2


							# check if R2 is not None
							if self.dict["R2"]["P1"] == None:
								# print("ray2")
								# if both midpoints of lines L1 ad L2, then draw ray R1
								# edit proof incase L1 or L2 is deleted
								if (self.dict["L3"]["P1"] != None 
									and self.dict["L3"]["P2"] != None
									and self.dict["L4"]["P1"] != None):

									print("draw rays2")
									xtop, ytop, xbot, ybot = self.draw_tools.getImageCorners()
									
									print(xtop, ytop, xbot, ybot)
									R2M1 = self.dict["L3"]["M1"]
									R2M2 = self.dict["L4"]["P1"]
									ray2P1 = self.draw_tools.line_intersection((R2M1, R2M2), (xtop, xbot))
									print(ray2P1)
									self.dict["R2"]["P1"] = ray2P1
									self.dict["R2"]["P2"] = R2M2

							return True, cur_tag
		return False, cur_tag

	


	def getNextLabel(self):

		if self.side != None:
			
			for item in self.dict["MAIN"][self.side]:
				# get item type 
				item_type = self.dict["MAIN"][self.side][item]["type"]

				# point only has P1
				if item_type == "point":
					# check if P1 is None				
					if self.dict["MAIN"][self.side][item]["P1"] == None:						
						return (self.side + " " + item)

				# point has P1 and P2, M1 is calculated
				if item_type == "midpoint":

					# check if P1 is None				
					if self.dict["MAIN"][self.side][item]["P1"] == None:
						return (self.side + " " + item + " P1")


					# check if P2 is None				
					if self.dict["MAIN"][self.side][item]["P2"] == None:
						return (self.side + " " + item + " P2")

				# axis has two midpoints
				if item_type == "axis":
					print("axis" + item)
					# axis has a top and a bottom

					# check if P1 is None
					if self.dict["MAIN"][self.side][item]["TOP"]["P1"] == None:
						return (self.side + " " + item + " P1")

					# check if P2 is None				
					if self.dict["MAIN"][self.side][item]["TOP"]["P2"] == None:
						return (self.side + " " + item + " P2")


					# check if P1 is None
					if self.dict["MAIN"][self.side][item]["BOT"]["P1"] == None:
						return (self.side + " " + item + " P1")

					# check if P2 is None				
					if self.dict["MAIN"][self.side][item]["BOT"]["P2"] == None:
						return (self.side + " " + item + " P2")

			return (self.side + " Done")

		return None


 
	def addDict(self, event):

		for item in self.dict["MAIN"][self.side]:
			# get item type 
			item_type = self.dict["MAIN"][self.side][item]["type"]

			# point only has P1
			if item_type == "point":
				# check if P1 is None				
				if self.dict["MAIN"][self.side][item]["P1"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["MAIN"][self.side][item]["P1"] = P
					return True

			# point has P1 and P2, M1 is calculated
			if item_type == "midpoint":

				# check if P1 is None				
				if self.dict["MAIN"][self.side][item]["P1"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["MAIN"][self.side][item]["P1"] = P
					return True


				# check if P2 is None				
				if self.dict["MAIN"][self.side][item]["P2"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["MAIN"][self.side][item]["P2"] = P

					M = self.draw_tools.midpoint(self.dict["MAIN"][self.side][item]["P1"], P)
					self.dict["MAIN"][self.side][item]["M1"] = M
					return True

			# axis has two midpoints
			if item_type == "axis":
				print("axis" + item)
				# axis has a top and a bottom

				# check if P1 is None
				if self.dict["MAIN"][self.side][item]["TOP"]["P1"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["MAIN"][self.side][item]["TOP"]["P1"] = P
					return True

				# check if P2 is None				
				if self.dict["MAIN"][self.side][item]["TOP"]["P2"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["MAIN"][self.side][item]["TOP"]["P2"] = P

					M = self.draw_tools.midpoint(self.dict["MAIN"][self.side][item]["TOP"]["P1"], P)
					self.dict["MAIN"][self.side][item]["TOP"]["M1"] = M
					return True


				# check if P1 is None
				if self.dict["MAIN"][self.side][item]["BOT"]["P1"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["MAIN"][self.side][item]["BOT"]["P1"] = P
					return True

				# check if P2 is None				
				if self.dict["MAIN"][self.side][item]["BOT"]["P2"] == None:
					P = self.draw_tools.getRealCoords(event)
					self.dict["MAIN"][self.side][item]["BOT"]["P2"] = P

					M = self.draw_tools.midpoint(self.dict["MAIN"][self.side][item]["BOT"]["P1"], P)
					self.dict["MAIN"][self.side][item]["BOT"]["M1"] = M
					return True					

		return False				

	



	# def updateDict(self, tag, point):

	# 	props = tag.split('_')
		
	# 	# update point
	# 	self.dict[props[1]][props[2]] = point

	# 	otherPoint = "P2" if props[2] == "P1" else "P1"

	# 	# M = ""

	# 	# def moveMidPoint():
			
			
	# 	# if type is midpoint update midpoint
	# 	if self.dict[props[1]]["type"] == "midpoint":			
	# 		# check if other point is drawn
	# 		if self.dict[props[1]][otherPoint] != None:
	# 			M = self.draw_tools.midpoint(self.dict[props[1]][otherPoint], point)
	# 			self.dict[props[1]]["M1"] = M	



	# 	# when L1 or L2
	# 		# if exists both L1 and L2
	# 			# if L1 update R1 P1
	# 				# line intersection L1M1 L2M1
	# 			# if L2 R1 P2
	# 				# line intersection L1M1 L2M1
	# 	if props[1] == "L1" or "L2":
	# 		if self.dict["L1"]["P1"] != None and self.dict["L2"]["P1"] != None:
	# 			if props[1] == "L1":
	# 				# print(M)
	# 				xtop, ytop, xbot, ybot = self.draw_tools.getImageCorners()
														
	# 				# R1M1 = self.dict["L1"]["M1"]
	# 				R1M2 = self.dict["L2"]["M1"]
	# 				ray1P1 = self.draw_tools.line_intersection((M, R1M2), (xtop, ytop))
	# 				self.dict["R1"]["P1"] = ray1P1
	# 			if props[1] == "L2":
	# 				self.dict["R1"]["P2"] = M
					
	# 	# when L3 or L4
	# 		# if exists both L3 and L4
	# 			# if L3 R2 P1
	# 				# line intersection L3M1 L4M1
	# 			# if L4 R2 P2
	# 				# line intersection L3M1 L4M1
	# 	if props[1] == "L3" or "L4":
	# 		if self.dict["L3"]["P1"] != None and self.dict["L4"]["P1"] != None:

	# 			xtop, ytop, xbot, ybot = self.draw_tools.getImageCorners()

	# 			if props[1] == "L3":
	# 				self.dict["R2"]["P1"] = self.draw_tools.line_intersection((M, self.dict["L4"]["P1"]), (xtop, xbot))

	# 			if props[1] == "L4":
					
	# 				self.dict["R2"]["P2"] = point
	# 				self.dict["R2"]["P1"] = self.draw_tools.line_intersection((point, self.dict["L3"]["M1"]), (xtop, xbot))


	def drawLines(self):
		for lines in self.dict:
			for points in self.dict[lines]:

				# if type is point cannot draw line
				if self.dict[lines]["type"] != "point":
					# draw line if P1 and P2 have values
					if self.dict[lines]["P1"] != None and self.dict[lines]["P2"] != None:

						p1 = self.dict[lines]["P1"]
						p2 = self.dict[lines]["P2"]

						# if it has a midpoint draw it
						if self.dict[lines]["type"] == "midpoint":
							m1 = self.dict[lines]["M1"]
							tag = "MNSA_"+str(lines)+"_"+str()
							self.draw_tools.create_midpoint_line(p1, p2, m1)
						else:
							self.draw_tools.create_myline(p1, p2)



	def draw(self):
		# for items in self.dict["MAIN"]:

		# loop left and right
		for side in ["LEFT","RIGHT"]:
			for item in self.dict["MAIN"][side]:

				item_type = self.dict["MAIN"][side][item]["type"]
				side_pre = side[0]+"_"

				if item_type == "point":
					if self.dict["MAIN"][side][item]["P1"] != None:
						self.draw_tools.create_mypoint(self.dict["MAIN"][side][item]["P1"], "white", "main")
						self.draw_tools.create_mytext(self.dict["MAIN"][side][item]["P1"], x_offset=80, mytext=(side_pre+item), mytag="main")
						# self, point, color="white", font_size=8, mytext, mytag):


				if item_type == "midpoint":
					if self.dict["MAIN"][side][item]["P1"] != None:
						self.draw_tools.create_mypoint(self.dict["MAIN"][side][item]["P1"], "white", "main")

					if self.dict["MAIN"][side][item]["P2"] != None:
						self.draw_tools.create_mypoint(self.dict["MAIN"][side][item]["P2"], "white", "main")						


					if self.dict["MAIN"][side][item]["P1"] != None and self.dict["MAIN"][side][item]["P2"] != None:
						p1 = self.dict["MAIN"][side][item]["P1"]
						p2 = self.dict["MAIN"][side][item]["P2"]
						m1 = self.dict["MAIN"][side][item]["M1"]
						self.draw_tools.create_midpoint_line(p1, p2, m1, "main")
						self.draw_tools.create_mytext(self.dict["MAIN"][side][item]["P2"], x_offset=80, mytext=(side_pre+item), mytag="main")



				if item_type == "axis":
					if self.dict["MAIN"][side][item]["TOP"]["P1"] != None:
						self.draw_tools.create_mypoint(self.dict["MAIN"][side][item]["TOP"]["P1"], "white", "main")

					if self.dict["MAIN"][side][item]["TOP"]["P2"] != None:
						self.draw_tools.create_mypoint(self.dict["MAIN"][side][item]["TOP"]["P2"], "white", "main")

					if self.dict["MAIN"][side][item]["TOP"]["P1"] != None and self.dict["MAIN"][side][item]["TOP"]["P2"] != None:
						p1 = self.dict["MAIN"][side][item]["TOP"]["P1"]
						p2 = self.dict["MAIN"][side][item]["TOP"]["P2"]
						m1 = self.dict["MAIN"][side][item]["TOP"]["M1"]
						self.draw_tools.create_midpoint_line(p1, p2, m1, "main")

						axis_text = side_pre + item.replace("AXIS_", "") + "_TOP"						
						self.draw_tools.create_mytext(p2, x_offset=80, mytext=axis_text, mytag="main")


					if self.dict["MAIN"][side][item]["BOT"]["P1"] != None:
						self.draw_tools.create_mypoint(self.dict["MAIN"][side][item]["BOT"]["P1"], "white", "main")

					if self.dict["MAIN"][side][item]["BOT"]["P2"] != None:
						self.draw_tools.create_mypoint(self.dict["MAIN"][side][item]["BOT"]["P2"], "white", "main")

					if self.dict["MAIN"][side][item]["BOT"]["P1"] != None and self.dict["MAIN"][side][item]["BOT"]["P2"] != None:
						p1 = self.dict["MAIN"][side][item]["BOT"]["P1"]
						p2 = self.dict["MAIN"][side][item]["BOT"]["P2"]
						m1 = self.dict["MAIN"][side][item]["BOT"]["M1"]
						self.draw_tools.create_midpoint_line(p1, p2, m1, "main")

						axis_text = side_pre + item.replace("AXIS_", "") + "_BOT"
						self.draw_tools.create_mytext(p2, x_offset=80, mytext=axis_text, mytag="main")

			# for points in self.dict[lines]:

			# 	# if type is point cannot draw line
			# 	if self.dict[lines]["type"] != "point":
			# 		# draw line if P1 and P2 have values
			# 		if self.dict[lines]["P1"] != None and self.dict[lines]["P2"] != None:

			# 			p1 = self.dict[lines]["P1"]
			# 			p2 = self.dict[lines]["P2"]

			# 			# if it has a midpoint draw it
			# 			if self.dict[lines]["type"] == "midpoint":
			# 				m1 = self.dict[lines]["M1"]
			# 				tag = "MNSA_"+str(lines)+"_"+str()
			# 				self.draw_tools.create_midpoint_line(p1, p2, m1)
			# 			else:
			# 				self.draw_tools.create_myline(p1, p2)							


	def update_canvas(self, draw_tools):
		self.draw_tools = draw_tools


	def update_dict(self, master_dict):
		self.dict = master_dict


	def unset(self):
		# print("unset from "+self.name)
		self.draw_tools.clear_by_tag("main")
		self.side = None