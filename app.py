# -*- coding: utf-8 -*-
# Advanced zoom for images of various types from small to huge up to several GB
import math
import warnings
import tkinter as tk



from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk


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


# read json file
from pathlib import Path
import json

# choose file
from tkinter import filedialog




class DETAILS_View(tk.Frame):
	def __init__(self, parent, controller, master_dict):
		tk.Frame.__init__(self, parent)
		self.controller = controller

		self.master_dict = master_dict

		



		vcmd = (self.register(self.callback))

		tk.Label(self, text="First Name").grid(row=0)
		tk.Label(self, text="Last Name").grid(row=1)
		tk.Label(self, text="Age").grid(row=2)
		tk.Label(self, text="Sex").grid(row=3)

		self.e_fname = tk.Entry(self)
		self.e_lname = tk.Entry(self)		
		self.e_age = tk.Entry(self, validate='all', validatecommand=(vcmd, '%P')) 



		self.e_fname.grid(row=0, column=1)
		self.e_lname.grid(row=1, column=1)
		self.e_age.grid(row=2, column=1)



		self.sex = tk.StringVar()
		m_btn = tk.Radiobutton(self, text='M', variable=self.sex, value="M")		
		m_btn.grid(row=3, column=1)
		f_btn = tk.Radiobutton(self, text='F', variable=self.sex, value="F")		
		f_btn.grid(row=4, column=1)


		submit_btn = ttk.Button(self, text="SAVE", command=lambda: self.save())
		submit_btn.grid(column=0, row=5)

	def callback(self, P):
		if str.isdigit(P) or P == "":
			return True
		else:
			return False

	def is_set_med_image(self):		
		# This class has no image related to it
		# exception for DETAILS_View
		return True

	def update_dict(self, master_dict):
		# update dictionaries
		self.master_dict = master_dict
		self.add_details_masterdict()


	def save(self):
		# print("save details")

		f_name 	= self.e_fname.get().strip()
		l_name 	= self.e_lname.get().strip()
		age 	= self.e_age.get().strip()
		sex 	= self.sex.get().strip()

		bool_save = False

		if f_name != "":
			self.master_dict["DETAILS"]["F_NAME"] = f_name
			bool_save = True

		if l_name != "":
			self.master_dict["DETAILS"]["L_NAME"] = l_name
			bool_save = True

		if age != "":
			self.master_dict["DETAILS"]["AGE"] = age
			bool_save = True

		if sex != "":
			self.master_dict["DETAILS"]["SEX"] = sex
			bool_save = True

		if bool_save:
			self.controller.save_json()

		


	def add_details_masterdict(self):
		
		if "DETAILS" not in self.master_dict.keys():		# details dont exist new patient
			# print("details reached")
			self.master_dict["DETAILS"] = 	{
										"F_NAME":None,
										"L_NAME":None,
										"AGE":None,
										"SEX":None										
									}
			self.controller.save_json()

		else:												# details exist, check if blank			

			f_name 	= self.master_dict["DETAILS"]["F_NAME"]
			l_name 	= self.master_dict["DETAILS"]["L_NAME"]
			age 	= self.master_dict["DETAILS"]["AGE"]
			sex 	= self.master_dict["DETAILS"]["SEX"]


			if f_name != None:				
				self.e_fname.delete(0, tk.END)
				self.e_fname.insert(0, f_name)

			if l_name != None:				
				self.e_lname.delete(0, tk.END)
				self.e_lname.insert(0, l_name)

			if age != None:				
				self.e_age.delete(0, tk.END)
				self.e_age.insert(0, age)

			if sex != None:				
				self.sex.set(sex)										



				







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
		self.master_dict = {}
		self.add_image_path_masterdict()

		
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
			view = V(parent=self.master, controller=self, master_dict=self.master_dict)
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

			try:
				my_file = Path("pat.json")
				if my_file.is_file():
					# file exists
					print("pat.json exists")

					with open(my_file) as f:
						d = json.load(f)
						self.master_dict = d
						# print(d)

				# update all dictionaries
				for view in self.views:
					self.views[view].update_dict(self.master_dict)


			except Exception as e:
				raise e


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


	def save_json(self):
		# print("successfully bubbled to the top")
		# print(self.master_dict)

		with open('pat.json', 'w', encoding='utf-8') as f:
			json.dump(self.master_dict, f, ensure_ascii=False, indent=4)



	def add_image_path_masterdict(self):
		if "IMAGES" not in self.master_dict.keys():
			self.master_dict["IMAGES"] = 	{
										"DETAILS":None,
										"PRE-SCANNO":None,
										"PRE-AP":None,
										"PRE-LAT":None,
										"PRE-SKY":None,
										"POST-SCANNO":None,
										"POST-AP":None,
										"POST-LAT":None,
										"POST-SKY":None
									}



filename = '500.jpg'  # place path to your image here
app = MainWindow(tk.Tk(), path=filename)
app.mainloop()