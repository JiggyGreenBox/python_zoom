import tkinter as tk

from tkinter import ttk
from tkinter import *

# menus
from menus.uni_tib_val_menu import UNI_TIB_VAL_Menu
from menus.uni_fem_val_menu import UNI_FEM_VAL_Menu
from menus.alpha_menu import ALPHA_Menu
from menus.beta_menu import BETA_Menu

# objs
from objs.uni_tib_val import UNI_TIB_VAL
from objs.uni_fem_val import UNI_FEM_VAL
from objs.alpha import ALPHA
from objs.beta import BETA

# choose file
from tkinter import filedialog

# from gui_canvas import CanvasImage
from gui_draw_tools import DrawTools

# warning box for choose-side
from tkinter import messagebox

# get relpath
import os



class POST_AP_View(tk.Frame):

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
		# for x,text in enumerate(["UNI_TIB_VAL","UNI_FEM_VAL"]):
		for x,text in enumerate(["UNI_TIB_VAL","UNI_FEM_VAL","ALPHA","BETA"]):
			# print(text)
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
					UNI_TIB_VAL_Menu,
					UNI_FEM_VAL_Menu,
					ALPHA_Menu,
					BETA_Menu
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
					UNI_TIB_VAL,
					UNI_FEM_VAL,
					ALPHA,
					BETA
				):
			obj_name = Obj.__name__
			# print(obj_name)
			self.objects[obj_name] = Obj(self.canvas, self.master_dict, controller=self, op_type = "POST-OP")




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
		if self.canvas != "":
			try:
				self.canvas.cur_obj.escapeObjFunc()
			except Exception as e:
				raise e


	def is_set_med_image(self):
		if self.med_image != "":
			return True
		return False

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

			# save to json for future sessions
			# self.master_dict["IMAGES"]["PRE-AP"] = image
			self.master_dict["IMAGES"]["POST-AP"] = rel_path

			# save to pat.json
			self.controller.save_json()

	def menu_btn_click(self, obj_name, action):
		'''Route menu click to object page'''		
		self.objects[obj_name].menu_btn_click(action)


	def updateMenuLabel(self, label_text, menu_obj):
		'''Set label text for user instructions'''
		self.menus[menu_obj].setLabelText(label_text)


	def update_dict(self, master_dict):

		# update dictionaries
		self.master_dict = master_dict
		for obj in self.objects:
			self.objects[obj].update_dict(master_dict)		

		# found json data, load image from json
		if self.master_dict["IMAGES"]["POST-AP"] != None:

			self.med_image = self.controller.working_dir + "/" + self.master_dict["IMAGES"]["POST-AP"]
			self.canvas = DrawTools(self.content_frame, self.med_image)  # create widget
			self.canvas.grid(row=0, column=0)  # show widget

			# update canvas object for children
			for obj in self.objects:			
				self.objects[obj].update_canvas(self.canvas)


	def unsetObjs(self, obj_name):
		'''Reset variable for inactive objects'''
		for obj in self.objects:
			# except obj_name call unset
			if obj == obj_name: continue
			self.objects[obj].unset()

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
		return int(self.master_dict["POINT_SIZES"]["POST-AP"])

	def resizeRedraw(self):
		'''redraw with new point size'''
		print('resizeRedraw')
		for obj in self.objects:
			self.objects[obj].draw()
			self.objects[obj].unset()

			