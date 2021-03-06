# -*- coding: utf-8 -*-
# Advanced zoom for images of various types from small to huge up to several GB
import math
import warnings
import tkinter as tk

from tkinter import messagebox

from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk

# from gui_canvas import CanvasImage
from gui_draw_tools import DrawTools

from menus.acor_menu import ACOR_Menu
from menus.isr_menu import ISR_Menu
from menus.tslope_menu import TSLOPE_Menu


from objs.acor import ACOR
from objs.isr import ISR
from objs.tslope import TSLOPE

# read json file
from pathlib import Path
import json

class MainWindow(ttk.Frame):
	""" Main window class """
	def __init__(self, mainframe, path):
		""" Initialize the main Frame """
		ttk.Frame.__init__(self, master=mainframe)
		self.master.title('Advanced Zoom v3.0')
		self.master.geometry('800x600')  # size of the main window
		# self.master.rowconfigure(0, weight=1)  # make the CanvasImage widget expandable
		# self.master.columnconfigure(0, weight=1)


		# topbar
		topbar = Frame(self.master, height=100,bg="red")
		topbar.pack(anchor=E, fill=X, expand=False, side=TOP)  # <----

		# make buttons in the topbar
		for x,text in enumerate(["ACOR","ISR","TSLOPE"]):
			# print(text)
			button = ttk.Button(topbar, text=text, command=lambda text=text: self.show_menu(text))
			button.grid(column=x, row=1)


		# left navbar
		navbar = Frame(self.master, width=100)
		navbar.pack(anchor=W, fill=Y, expand=False, side=LEFT)  # <----


		# create menus
		self.frames = {}
		for F in (
					ACOR_Menu,
					ISR_Menu,
					TSLOPE_Menu
				):
			page_name = F.__name__
			frame = F(parent=navbar, controller=self)
			self.frames[page_name] = frame

			# put all of the pages in the same location;
			# the one on the top of the stacking order
			# will be the one that is visible.
			frame.grid(row=0, column=0, sticky="nsew")


		# button = ttk.Button(navbar, text="object 1", command=self.btn1)
		# button.grid(column=1, row=1)

		# button = ttk.Button(navbar, text="object 2", command=self.btn2)
		# button.grid(column=1, row=2)


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

		content_frame = Frame(self.master)
		content_frame.pack(anchor=N, fill=BOTH, expand=True, side=LEFT )
		content_frame.rowconfigure(0, weight=1)  # make the CanvasImage widget expandable
		content_frame.columnconfigure(0, weight=1)

		


		self.canvas = DrawTools(content_frame, path)  # create widget
		self.canvas.grid(row=0, column=0)  # show widget
		

		self.master_dict = {}
		
		# =========== PUT IN A FUNCTION ==============================
		try:
			my_file = Path("patient.json")
			if my_file.is_file():
				# file exists
				print("fil exists")

				with open(my_file) as f:
					d = json.load(f)
					self.master_dict = d
					print(d)


		except Exception as e:
			raise e
		# =========================================

		self.objects = {}
		for Obj in (
					ACOR,
					ISR,
					TSLOPE
				):
			obj_name = Obj.__name__			
			print(obj_name)
			self.objects[obj_name] = Obj(self.canvas, self.master_dict, controller=self)


	def donothing(self):
		x = 0


	def show_menu(self, obj_name):
		'''Show corresponding menu to the object and set cur_object in drawtools'''
		menu = obj_name+"_Menu"
		self.canvas.setObject(self.objects[obj_name])
		self.objects[obj_name].draw()
		self.unsetObjs(obj_name)
		self.show_frame(menu)


	def show_frame(self, page_name):
		'''Show a frame for the given page name'''
		frame = self.frames[page_name]
		frame.tkraise()


	def menu_btn_click(self, obj_name, action):
		'''Route menu click to object page'''		
		self.objects[obj_name].menu_btn_click(action)


	def updateMenuLabel(self, label_text, menu_obj):
		'''Set label text for user instructions'''
		self.frames[menu_obj].setLabelText(label_text)


	def warningBox(self, message):
		'''Display a warning box with message'''
		messagebox.showwarning("Warning", message)



	def unsetObjs(self, obj_name):
		'''Reset variable for inactive objects'''
		for obj in self.objects:
			# except obj_name call unset
			if obj == obj_name: continue
			self.objects[obj].unset()



# filename = '500.jpg'  # place path to your image here
filename = 'lateral_view.jpeg'  # place path to your image here
app = MainWindow(tk.Tk(), path=filename)
app.mainloop()