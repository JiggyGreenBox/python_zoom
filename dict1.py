# -*- coding: utf-8 -*-
# Advanced zoom for images of various types from small to huge up to several GB
import math
import warnings
import tkinter as tk


from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk

# from gui_canvas import CanvasImage
from gui_draw_tools import DrawTools

class MainWindow(ttk.Frame):
	""" Main window class """
	def __init__(self, mainframe, path):
		""" Initialize the main Frame """
		ttk.Frame.__init__(self, master=mainframe)
		self.master.title('Advanced Zoom v3.0')
		self.master.geometry('800x600')  # size of the main window
		# self.master.rowconfigure(0, weight=1)  # make the CanvasImage widget expandable
		# self.master.columnconfigure(0, weight=1)


		navbar = Frame(self.master, width=100)
		navbar.pack(anchor=W, fill=Y, expand=False, side=LEFT)  # <----



		button = ttk.Button(navbar, text="object 1", command=self.btn1)
		button.grid(column=1, row=1)

		button = ttk.Button(navbar, text="object 2", command=self.btn2)
		button.grid(column=1, row=2)



		content_frame = Frame(self.master)
		content_frame.pack(anchor=N, fill=BOTH, expand=True, side=LEFT )
		content_frame.rowconfigure(0, weight=1)  # make the CanvasImage widget expandable
		content_frame.columnconfigure(0, weight=1)

		


		self.draw_tools = DrawTools(content_frame, path)  # create widget
		self.draw_tools.grid(row=0, column=0)  # show widget

		self.obj1 = Myobj1(self.draw_tools)
		self.obj2 = Myobj2(self.draw_tools)


	def btn1(self):
		# global cur_obj
		# cur_obj = self.obj1
		print("set obj1")
		self.draw_tools.setObject(self.obj1)

	def btn2(self):
		# global cur_obj
		# cur_obj = self.obj2
		print("set obj2")
		self.draw_tools.setObject(self.obj2)


class Myobj1:
	# instance attribute
	def __init__(self, draw_tools):
		self.name = "object1"
		self.draw_tools = draw_tools
		self.dict = {}		
		self.dict["L1"] = {"type":"midpoint","P1":None,"P2":None, "M1":None}
		self.dict["L2"] = {"type":"midpoint","P1":None,"P2":None, "M1":None}
		self.dict["R1"] = {"type":"ray","P1":None,"P2":None}
		self.dict["L3"] = {"type":"midpoint","P1":None,"P2":None, "M1":None}
		self.dict["L4"] = {"type":"point","P1":None}
		self.dict["R2"] = {"type":"ray","P1":None,"P2":None}

	def click(self, event):
		# print("click from object1")	
		ret, cur_tag = self.addDict(event)	
		if ret:
			print(cur_tag)
			self.draw_tools.create_token(event, "white", cur_tag)
			self.drawLines()
		else:
			print(self.dict)


	# return true to allow clicks
	# return current tag to draw function
	def addDict(self, event):

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


	def updateDict(self, tag, point):

		props = tag.split('_')
		
		# update point
		self.dict[props[1]][props[2]] = point

		otherPoint = "P2" if props[2] == "P1" else "P1"

		# M = ""

		# def moveMidPoint():
			
			
		# if type is midpoint update midpoint
		if self.dict[props[1]]["type"] == "midpoint":			
			# check if other point is drawn
			if self.dict[props[1]][otherPoint] != None:
				M = self.draw_tools.midpoint(self.dict[props[1]][otherPoint], point)
				self.dict[props[1]]["M1"] = M	



		# when L1 or L2
			# if exists both L1 and L2
				# if L1 update R1 P1
					# line intersection L1M1 L2M1
				# if L2 R1 P2
					# line intersection L1M1 L2M1
		if props[1] == "L1" or "L2":
			if self.dict["L1"]["P1"] != None and self.dict["L2"]["P1"] != None:
				if props[1] == "L1":
					# print(M)
					xtop, ytop, xbot, ybot = self.draw_tools.getImageCorners()
														
					# R1M1 = self.dict["L1"]["M1"]
					R1M2 = self.dict["L2"]["M1"]
					ray1P1 = self.draw_tools.line_intersection((M, R1M2), (xtop, ytop))
					self.dict["R1"]["P1"] = ray1P1
				if props[1] == "L2":
					self.dict["R1"]["P2"] = M
					
		# when L3 or L4
			# if exists both L3 and L4
				# if L3 R2 P1
					# line intersection L3M1 L4M1
				# if L4 R2 P2
					# line intersection L3M1 L4M1
		if props[1] == "L3" or "L4":
			if self.dict["L3"]["P1"] != None and self.dict["L4"]["P1"] != None:

				xtop, ytop, xbot, ybot = self.draw_tools.getImageCorners()

				if props[1] == "L3":
					self.dict["R2"]["P1"] = self.draw_tools.line_intersection((M, self.dict["L4"]["P1"]), (xtop, xbot))

				if props[1] == "L4":
					
					self.dict["R2"]["P2"] = point
					self.dict["R2"]["P1"] = self.draw_tools.line_intersection((point, self.dict["L3"]["M1"]), (xtop, xbot))


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


# box_image = self.canvas.coords(self.container)
# print(box_image)

class Myobj2:
	# instance attribute
	def __init__(self, draw_tools):
		self.name = "object2"
		self.draw_tools = draw_tools

	def click(self, event):
		print("click from object2")
		self.draw_tools.create_token(event, "black")



# filename = '500.jpg'  # place path to your image here
# filename = 'square.png'  # place path to your image here
filename = 'legit2.jpg'  # place path to your image here
# filename = '3.png'  # place path to your image here
app = MainWindow(tk.Tk(), path=filename)
app.mainloop()