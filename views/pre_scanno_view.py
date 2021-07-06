import tkinter as tk

from tkinter import ttk
from tkinter import *

# menus
from menus.afta_menu import AFTA_Menu
from menus.aldfa_menu import ALDFA_Menu
from menus.hka_menu import HKA_Menu
from menus.mldfa_menu import MLDFA_Menu
from menus.mnsa_menu import MNSA_Menu
from menus.tamd_menu import TAMD_Menu
from menus.mpta_menu import MPTA_Menu
from menus.jca_menu import JCA_Menu
from menus.vca_menu import VCA_Menu
from menus.kjlo_menu import KJLO_Menu
from menus.kaol_menu import KAOL_Menu
from menus.mad_menu import MAD_Menu
from menus.eadf_menu import EADF_Menu
from menus.eadt_menu import EADT_Menu
from menus.lpfa_menu import LPFA_Menu
from menus.vang_menu import VANG_Menu
from menus.draw_menu import DRAW_Menu
from menus.main_menu import MAIN_Menu

# objs
from objs.afta import AFTA
from objs.hka import HKA
from objs.mnsa import MNSA
from objs.aldfa import ALDFA
from objs.mldfa import MLDFA
from objs.tamd import TAMD
from objs.mpta import MPTA
from objs.jca import JCA
from objs.vca import VCA
from objs.kjlo import KJLO
from objs.kaol import KAOL
from objs.mad import MAD
from objs.eadf import EADF
from objs.eadt import EADT
from objs.lpfa import LPFA
from objs.vang import VANG
from objs.draw_obj import DRAW
from objs.main_anatomy import MAIN

# choose file
from tkinter import filedialog

# from gui_canvas import CanvasImage
from gui_draw_tools import DrawTools

# warning box for choose-side
from tkinter import messagebox

# get relpath
import os

# make export dir if not exist
from pathlib import Path

# identify mac os and flip keys
from sys import platform


class PRE_SCANNO_View(tk.Frame):

	def __init__(self, parent, controller, master_dict):
		tk.Frame.__init__(self, parent)
		self.controller = controller

		# choosen by user OR
		# loaded from pat.json
		self.med_image = ""
		self.canvas = ""		
		self.master_dict = master_dict

		# topbar
		self.topbar = Frame(self, height=100)
		self.topbar.pack(anchor=E, fill=X, expand=False, side=TOP)

		# make buttons in the topbar
		# for x,text in enumerate(["DRAW","HKA","MNSA","VCA","AFTA","MLDFA","ALDFA","TAMD","MPTA","JCA","KJLO","KAOL","MAD","EADF","EADT","LPFA", "MAIN"]):
		# for x,text in enumerate(["MAIN","HKA","MNSA","VCA","AFTA","MLDFA","ALDFA","TAMD","MPTA","JCA","KJLO","KAOL","MAD","EADF","EADT","LPFA", "DRAW"]):
		for x,text in enumerate(["MAIN","HKA","MNSA","VCA","AFTA","MLDFA","ALDFA","TAMD","MPTA","JCA","KJLO","KAOL","MAD", "VANG","EADF","EADT","LPFA", "DRAW"]):
		# for x,text in enumerate(["MAIN","HKA","MNSA","VCA","AFTA","ALDFA","MLDFA","TAMD","MPTA","KJLO", "KAOL"]):
			# print(text)

			if platform == "darwin":
				if x < 9:
					button = ttk.Button(self.topbar, text=text, command=lambda text=text: self.show_menu(text))
					button.grid(column=x, row=1)
				else:
					button = ttk.Button(self.topbar, text=text, command=lambda text=text: self.show_menu(text))
					button.grid(column=x-9, row=2)
			else:
				button = ttk.Button(self.topbar, text=text, command=lambda text=text: self.show_menu(text))
				button.grid(column=x, row=1)


		# left navbar
		self.navbar = Frame(self, width=100)
		self.navbar.pack(anchor=W, fill=Y, expand=False, side=LEFT)

		self.content_frame = Frame(self,bg="red")
		self.content_frame.pack(anchor=N, fill=BOTH, expand=True, side=LEFT )
		self.content_frame.rowconfigure(0, weight=1)  # make the CanvasImage widget expandable
		self.content_frame.columnconfigure(0, weight=1)



		# create menus
		self.menus = {}
		for M in (
					AFTA_Menu,
					ALDFA_Menu,
					HKA_Menu,
					MLDFA_Menu,
					MNSA_Menu,
					MPTA_Menu,
					JCA_Menu,
					TAMD_Menu,
					VCA_Menu,
					KJLO_Menu,
					KAOL_Menu,
					MAD_Menu,
					VANG_Menu,
					EADF_Menu,
					EADT_Menu,
					LPFA_Menu,
					DRAW_Menu,
					MAIN_Menu
				):
			page_name = M.__name__
			menu = M(parent=self.navbar, controller=self)
			self.menus[page_name] = menu

			# put all of the pages in the same location;
			# the one on the top of the stacking order
			# will be the one that is visible.
			menu.grid(row=0, column=0, sticky="nsew")			


		self.objects = {}
		for Obj in (
					AFTA,
					HKA,
					MNSA,
					ALDFA,
					MLDFA,
					MPTA,
					JCA,
					TAMD,
					VCA,
					KJLO,
					KAOL,
					MAD,
					VANG,
					EADF,
					EADT,
					LPFA,
					DRAW,
					MAIN
				):
			obj_name = Obj.__name__
			# print(obj_name)
			self.objects[obj_name] = Obj(self.canvas, self.master_dict, controller=self, op_type = "PRE-OP")


	def show_frame(self, page_name):
		'''Show a frame for the given page name'''
		frame = self.menus[page_name]
		frame.tkraise()


	def warningBox(self, message):
		'''Display a warning box with message'''
		messagebox.showwarning("Warning", message)

	def save_json(self):
		'''bubble to top'''
		self.controller.save_json()

	def escapeFunc(self):
		# escape keypress from app.py
		if self.canvas != "":
			try:
				self.canvas.cur_obj.escapeObjFunc()
			except Exception as e:
				raise e

	def keySetRight(self):
		# num 1 keypress from app.py
		if self.canvas != "":
			try:
				self.canvas.cur_obj.keyRightObjFunc()
			except Exception as e:
				raise e

	def keySetLeft(self):
		# num 2 keypress from app.py
		if self.canvas != "":
			try:
				self.canvas.cur_obj.keyLeftObjFunc()
			except Exception as e:
				raise e
			
	

	def update_dict(self, master_dict):

		# update dictionaries
		self.master_dict = master_dict
		for obj in self.objects:
			self.objects[obj].update_dict(master_dict)

		# found json data, load image from json
		if self.master_dict["IMAGES"]["PRE-SCANNO"] != None:

			# self.med_image = self.master_dict["IMAGES"]["PRE-SCANNO"]
			self.med_image = self.controller.working_dir + "/" + self.master_dict["IMAGES"]["PRE-SCANNO"]
			self.canvas = DrawTools(self.content_frame, self.med_image)  # create widget
			self.canvas.grid(row=0, column=0)  # show widget

			# update canvas object for children
			for obj in self.objects:			
				self.objects[obj].update_canvas(self.canvas)

			# auto-set curObject to MAIN
			self.canvas.setObject(self.objects["MAIN"])

		# deprecated, MAD is auto calculated now
		# update mad value
		# self.menus["MAD_Menu"].updateMadLabels(self.master_dict["EXCEL"]["PRE-OP"]["RIGHT"]["MAD"],self.master_dict["EXCEL"]["PRE-OP"]["LEFT"]["MAD"])


	def is_set_med_image(self):
		if self.med_image != "":
			return True		
		return False


	def set_med_image(self, image):
		if image != "":
			self.med_image = image
		else: 
			print("image is blank")

	def open_image_loc(self):

		image = filedialog.askopenfilename(initialdir=self.controller.working_dir)


		if isinstance(image, str) and image != "":

			dir_name = os.path.dirname(image)
			rel_path = os.path.relpath(image, dir_name)

			# only allow images from the working dir
			if self.controller.working_dir != dir_name:
				print("mis-match")
				self.warningBox("Image not from working directory")
				return

			# current session
			self.med_image = image			
			self.canvas = DrawTools(self.content_frame, image)  # create widget
			self.canvas.grid(row=0, column=0)  # show widget

			# update canvas object for children
			for obj in self.objects:			
				self.objects[obj].update_canvas(self.canvas)

			# auto-set curObject to MAIN
			self.canvas.setObject(self.objects["MAIN"])

			# save to json for future sessions
			# self.master_dict["IMAGES"]["PRE-SCANNO"] = image
			self.master_dict["IMAGES"]["PRE-SCANNO"] = rel_path

			# save to pat.json
			self.controller.save_json()
			

	def menu_btn_click(self, obj_name, action):
		'''Route menu click to object page'''		
		self.objects[obj_name].menu_btn_click(action)


	def menu_to_obj(self, obj_name, key, val):
		'''Route menu click to object page'''		
		try:
			self.objects[obj_name].menu_to_obj(key, val)
		except Exception as e:
			print(e)

	def obj_to_menu(self, menu_name, key, val):
		'''update menu from object'''		
		try:
			self.menus[menu_name].obj_to_menu(key, val)
		except Exception as e:
			print(e)

		


	def unsetObjs(self, obj_name):
		'''Reset variable for inactive objects'''
		for obj in self.objects:
			# except obj_name call unset
			if obj == obj_name: continue
			self.objects[obj].unset()


	def updateMenuLabel(self, label_text, menu_obj):
		'''Set label text for user instructions'''
		self.menus[menu_obj].setLabelText(label_text)


	def show_menu(self, obj_name):
		'''Show corresponding menu to the object and set cur_object in drawtools'''
		menu = obj_name+"_Menu"
		self.canvas.setObject(self.objects[obj_name])
		self.objects[obj_name].draw()
		self.unsetObjs(obj_name)
		self.show_frame(menu)

	def resetImg(self, image):
		self.canvas.destroy()		
		self.canvas = DrawTools(self.content_frame, image)  # create widget
		self.canvas.grid(row=0, column=0)  # show widget

		# update canvas object for children
		for obj in self.objects:
			self.objects[obj].update_canvas(self.canvas)


	def checkbox_click(self, obj_name, action, val):
		try:
			self.objects[obj_name].checkbox_click(action,val)
		except Exception as e:
			raise e

	# point resize functs
	def getViewPointSize(self):
		return int(self.master_dict["POINT_SIZES"]["PRE-SCANNO"])

	def resizeRedraw(self):
		'''redraw with new point size'''
		print('resizeRedraw')
		for obj in self.objects:			
			self.objects[obj].draw()
			self.objects[obj].unset()

	# calls the draw function without drawing the points on the canvas
	def calculateExcel(self, excel_list=None):

		# called when Left Done or Right Done
		if excel_list == None:
			print('normal excel')
			for obj in self.objects:
				if obj in ["HKA","MNSA","VCA","AFTA","MLDFA","ALDFA","TAMD","MPTA","KJLO","KAOL","MAD","EADF","JCA","VANG"]:
					print("{} draw".format(obj))
					self.objects[obj].updateExcelValues()

		# called when drag stop is called
		else:
			print('drag excel')
			for obj in excel_list:
				print(obj)
				self.objects[obj].updateExcelValues()



	# unique for MAD
	def getMadVals(self):
		return self.menus["MAD_Menu"].getMadEntryVals()

	# unique for MAIN
	def toggleDissapearMode(self):
		self.menus["MAIN_Menu"].toggleDissapearCheckbox()



	def view_draw_pil(self):

		print('pre_scanno_view.py draw_pil')

		if self.canvas == "":
			print("no canvas")
			return

		# create the pil image
		# self.draw_tools.createPIL()
		self.canvas.createPIL(self.med_image)

		# draw from HKA
		self.objects["HKA"].obj_draw_pil()

		# check if export dir exists, create if not
		Path(self.controller.working_dir +'/export').mkdir(parents=True, exist_ok=True)

		# create platform independent file path
		file = Path(self.controller.working_dir + '/export/export_pre_scanno.jpg')
		# file = Path(self.controller.working_dir + '/export/resize.jpg')

		# save to path
		self.canvas.savePIL(file)


	def view_tryPsFile(self):
		print('view_tryPsFile')

		try:
			# self.canvas.postscript(file="try_ps.ps", colormode='color')	
			self.canvas.my_postscript("try_ps.ps")
		except Exception as e:
			raise e
		