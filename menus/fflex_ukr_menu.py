import tkinter as tk


from tkinter import ttk
from tkinter import *

class FFLEX_UKR_Menu(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		self.obj_name = "FFLEX_UKR"

		header_label = tk.Label(self, text=self.obj_name,font=("TkDefaultFont",20))
		header_label.grid(column=1, row=1,columnspan=2,pady=[20,0])

		self.label = tk.Label(self, text="CHOOSE SIDE")
		self.label.grid(column=1, row=2,columnspan=2,pady=[10,20])



		button = ttk.Button(self, text="RIGHT", command=lambda: controller.menu_btn_click(self.obj_name, "SET-RIGHT"))
		button.grid(column=1, row=3)

		button = ttk.Button(self, text="LEFT", command=lambda: controller.menu_btn_click(self.obj_name, "SET-LEFT"))
		button.grid(column=2, row=3)

		

		# delete menu
		del_label = tk.Label(self, text="DELETE MENU")
		del_label.grid(column=1, row=4,columnspan=2,pady=(110, 10),sticky=N)


		
		button = ttk.Button(self, text="FEM TOP", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-RIGHT-FEM-TOP"))
		button.grid(column=1, row=5)
		button = ttk.Button(self, text="FEM TOP", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-LEFT-FEM-TOP"))
		button.grid(column=2, row=5)


		button = ttk.Button(self, text="FEM BOT", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-RIGHT-FEM-BOT"))
		button.grid(column=1, row=6)
		button = ttk.Button(self, text="FEM BOT", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-LEFT-FEM-BOT"))
		button.grid(column=2, row=6)

		button = ttk.Button(self, text="PEG TOP", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-RIGHT-PEG-TOP"))
		button.grid(column=1, row=7)
		button = ttk.Button(self, text="PEG TOP", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-LEFT-PEG-TOP"))
		button.grid(column=2, row=7)

		button = ttk.Button(self, text="PEG BOT", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-RIGHT-PEG-BOT"))
		button.grid(column=1, row=8)
		button = ttk.Button(self, text="PEG BOT", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-LEFT-PEG-BOT"))
		button.grid(column=2, row=8)


	def setLabelText(self, label_text):
		self.label.config(text=label_text)