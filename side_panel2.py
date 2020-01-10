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


		# navbar
		navbar = Frame(self.master, width=100)
		navbar.pack(anchor=W, fill=Y, expand=False, side=LEFT)  # <----

		# btn 1
		button = ttk.Button(navbar, text="object 1", command=self.btn1)
		button.grid(column=1, row=1)
		# btn 2
		button = ttk.Button(navbar, text="object 2", command=self.btn2)
		button.grid(column=1, row=2)


		# add menu bar
		menubar = Menu(self.master)
		filemenu = Menu(menubar, tearoff=0)
		filemenu.add_command(label="New", command=self.donothing)
		filemenu.add_command(label="Open", command=self.donothing)
		filemenu.add_command(label="Save", command=self.donothing)
		filemenu.add_separator()
		filemenu.add_command(label="Exit", command=self.master.quit)
		menubar.add_cascade(label="File", menu=filemenu)
		helpmenu = Menu(menubar, tearoff=0)
		helpmenu.add_command(label="Help Index", command=self.donothing)
		helpmenu.add_command(label="About...", command=self.donothing)
		menubar.add_cascade(label="Help", menu=helpmenu)
		self.master.config(menu=menubar)


		# canvas frame
		content_frame = Frame(self.master)
		content_frame.pack(anchor=N, fill=BOTH, expand=True, side=LEFT )
		content_frame.rowconfigure(0, weight=1)  # make the CanvasImage widget expandable
		content_frame.columnconfigure(0, weight=1)

		# gui for draw tools
		self.canvas = DrawTools(content_frame, path)  # create widget
		self.canvas.grid(row=0, column=0)  # show widget

		# create objects
		self.obj1 = Myobj1(self.canvas)
		self.obj2 = Myobj2(self.canvas)


	def donothing(self):
		x = 0


	def btn1(self):
		# global cur_obj
		# cur_obj = self.obj1
		print("set obj1")
		self.canvas.setObject(self.obj1)

	def btn2(self):
		# global cur_obj
		# cur_obj = self.obj2
		print("set obj2")
		self.canvas.setObject(self.obj2)


class Myobj1:
	# instance attribute
	def __init__(self, canvas):
		self.name = "object1"
		self.canvas = canvas

	def click(self, event):
		print("click from object1")
		self.canvas.create_token(event, "white")

class Myobj2:
	# instance attribute
	def __init__(self, canvas):
		self.name = "object2"
		self.canvas = canvas

	def click(self, event):
		print("click from object2")
		self.canvas.create_token(event, "black")



filename = '500.jpg'  # place path to your image here
app = MainWindow(tk.Tk(), path=filename)
app.mainloop()