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

# from menus.afta_menu import AFTA_Menu
# from menus.aldfa_menu import ALDFA_Menu
# from menus.hka_menu import HKA_Menu
# from menus.mldfa_menu import MLDFA_Menu
# from menus.mnsa_menu import MNSA_Menu
# from menus.tamd_menu import TAMD_Menu
# from menus.mpta_menu import MPTA_Menu
# from menus.vca_menu import VCA_Menu
# from menus.kjlo_menu import KJLO_Menu
# from menus.kaol_menu import KAOL_Menu
# from menus.main_menu import MAIN_Menu


from views.pre_scanno_view import PRE_SCANNO_View
from views.post_scanno_view import POST_SCANNO_View
from views.pre_lat_view import PRE_LAT_View
from views.post_lat_view import POST_LAT_View
from views.pre_ap_view import PRE_AP_View
from views.post_ap_view import POST_AP_View
from views.pre_sky_view import PRE_SKY_View
from views.post_sky_view import POST_SKY_View

from views.details_view import DETAILS_View
from views.set_working_view import SET_WORKING_View


from objs.afta import AFTA
from objs.hka import HKA
from objs.mnsa import MNSA
from objs.aldfa import ALDFA
from objs.mldfa import MLDFA
from objs.tamd import TAMD
from objs.mpta import MPTA
from objs.vca import VCA
from objs.kjlo import KJLO
from objs.kaol import KAOL
from objs.main_anatomy import MAIN

# read json file
from pathlib import Path
import json

# choose file
from tkinter import filedialog




class DETAILS_View(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller		


	def is_set_med_image(self):		
		# This class has no image related to it
		# exception for DETAILS_View
		return True




class MainWindow(ttk.Frame):
	""" Main window class """

	def __init__(self, mainframe, path):
		""" Initialize the main Frame """
		ttk.Frame.__init__(self, master=mainframe)
		self.master.title('Advanced Zoom v3.0')
		self.master.geometry('800x600')  # size of the main window
		
		self.master.grid_rowconfigure(1, weight=1) # this needed to be added
		self.master.grid_columnconfigure(0, weight=1) # as did this

		self.working_dir = ""

		
		# topbar
		self.topbar = Frame(self.master, height=100)				
		self.topbar.grid(row=0, column=0, sticky="nwe") # stick to the top

		# make buttons in the topbar
		for x,text in enumerate(["DETAILS","PRE-SCANNO","PRE-AP","PRE-LAT","PRE-SKY","POST-SCANNO","POST-AP","POST-LAT","POST-SKY"]):		
			button = ttk.Button(self.topbar, text=text, command=lambda text=text: self.show_view(text))
			button.grid(column=x, row=1)



		# create menus
		self.views = {}
		for V in (					
					PRE_SCANNO_View,
					POST_SCANNO_View,
					PRE_LAT_View,
					POST_LAT_View,
					PRE_AP_View,
					POST_AP_View,
					PRE_SKY_View,
					POST_SKY_View,
					DETAILS_View,
					SET_WORKING_View
				):
			page_name = V.__name__
			view = V(parent=self.master, controller=self)
			# view = V(parent=place_holder, controller=self)
			self.views[page_name] = view

			# put all of the pages in the same location;
			# the one on the top of the stacking order
			# will be the one that is visible.
			view.grid(row=1, column=0, sticky="nsew")


		if self.working_dir == "":
			self.topbar.grid_forget()
			self.show_view("SET_WORKING")
		# self.set_working_dir()

	
	def set_working_dir(self):
		self.working_dir = filedialog.askdirectory()		
		if self.working_dir == "":
			self.show_view("SET_WORKING")
		else:
			self.topbar.grid(row=0, column=0, sticky="we")
			self.show_view("DETAILS")


	def show_view(self, page_name):
		'''Show a view for the given page name'''
		page_name = page_name.replace("-", "_")	+ "_View"		
		view = self.views[page_name]	

		if self.views[page_name].is_set_med_image():
			print("image is set")
		else:
			try:
				self.views[page_name].open_image_loc()
			except Exception as e:
				# print(e)
				raise e
			print("image is NOT set")

		view.tkraise()


	def test_excel(self):
		print("successfully bubbled to the top")



filename = '500.jpg'  # place path to your image here
app = MainWindow(tk.Tk(), path=filename)
app.mainloop()