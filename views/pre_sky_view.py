import tkinter as tk
from tkinter import ttk
from tkinter import *

# menus
from menus.sa_menu import SA_Menu
from menus.p_tilt_menu import P_TILT_Menu

# objs
from objs.sa import SA
from objs.p_tilt import P_TILT

# choose file
from tkinter import filedialog

# from gui_canvas import CanvasImage
from gui_draw_tools import DrawTools

# warning box for choose-side
from tkinter import messagebox

class PRE_SKY_View(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller

		# choosen by user OR
		# loaded from pat.json
		self.med_image = ""
		self.canvas = ""
		self.master_dict = {}

		# topbar
		self.topbar = Frame(self, height=100)
		self.topbar.pack(anchor=E, fill=X, expand=False, side=TOP)

		# make buttons in the topbar
		for x,text in enumerate(["SA", "P_TILT"]):
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
					SA_Menu,
					P_TILT_Menu
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
					SA,
					P_TILT
				):
			obj_name = Obj.__name__
			print(obj_name)
			self.objects[obj_name] = Obj(self.canvas, self.master_dict, controller=self)

	def show_frame(self, page_name):
		'''Show a frame for the given page name'''
		frame = self.menus[page_name]
		frame.tkraise()

	def warningBox(self, message):
		'''Display a warning box with message'''
		messagebox.showwarning("Warning", message)		

	def is_set_med_image(self):
		if self.med_image != "":
			return True
		return False

	def open_image_loc(self):		
		image = filedialog.askopenfilename(initialdir=self.controller.working_dir)

		if image != "":
			self.med_image = image
			self.canvas = DrawTools(self.content_frame, image)  # create widget
			self.canvas.grid(row=0, column=0)  # show widget

			for obj in self.objects:			
				self.objects[obj].update_canvas(self.canvas)

	def menu_btn_click(self, obj_name, action):
		'''Route menu click to object page'''		
		self.objects[obj_name].menu_btn_click(action)


	def updateMenuLabel(self, label_text, menu_obj):
		'''Set label text for user instructions'''
		self.frames[menu_obj].setLabelText(label_text)


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