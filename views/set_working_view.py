import tkinter as tk


from tkinter import ttk
from tkinter import *

class SET_WORKING_View(tk.Frame):
	def __init__(self, parent, controller, master_dict):
		tk.Frame.__init__(self, parent)
		self.controller = controller

		# choosen by user OR
		# loaded from pat.json
		self.med_image = ""

		self.grid_columnconfigure(0, weight=1)
		# self.grid_rowconfigure(0, weight=1)
		# self.grid_columnconfigure(1, weight=1)
		# self.grid_rowconfigure(1, weight=1)		

		
		self.label = tk.Label(self, text="WORKING DIRECTORY NOT SET")
		self.label.grid(column=0, row=0,pady=100)

		button = ttk.Button(self, text="SET WORKING DIRECTORY", command=self.controller.set_working_dir)
		button.grid(column=0, row=1)



	def is_set_med_image(self):		
		# This class has no image related to it
		# exception for SET_WORKING_View
		return True			


	def update_dict(self, master_dict):
		pass
