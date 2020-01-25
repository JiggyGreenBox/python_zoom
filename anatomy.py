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


from objs.main_anatomy import MainAnatomy

from objs.afta import AFTA
from objs.hka import HKA
from objs.mnsa import MNSA
from objs.aldfa import ALDFA
from objs.mldfa import MLDFA
from objs.mpta import MPTA
from objs.vca import VCA

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

		
		self.master_dict = {}
		

		# for F in (Menu1, Menu2, Menu3):
		# 	page_name = F.__name__


		# obj11 = AFTA()
		# print(obj11.name)
		# obj22 = HKA()
		# print(obj22.name)
		# obj3 = MNSA()
		# print(obj3.name)
		# obj4 = ALDFA()
		# print(obj4.name)
		# obj5 = MLDFA()
		# print(obj5.name)
		# obj6 = MPTA()
		# print(obj6.name)
		# obj7 = VCA()
		# print(obj7.name)



		self.draw_tools = DrawTools(content_frame, path)  # create widget
		self.draw_tools.grid(row=0, column=0)  # show widget

		self.obj1 = MainAnatomy(self.draw_tools, self.master_dict)
		self.obj2 = Myobj2(self.draw_tools)


	def btn1(self):
		# global cur_obj
		# cur_obj = self.obj1
		print("set obj1")
		self.draw_tools.setObject(self.obj1)

	def btn2(self):
		# global cur_obj
		# cur_obj = self.obj2
		# print("set obj2")
		print(self.master_dict)
		self.draw_tools.setObject(self.obj2)



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