import tkinter as tk


from tkinter import ttk
from tkinter import *

class MAD_Menu(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		self.obj_name = "MAD"


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
		del_label.grid(column=1, row=4,columnspan=2,pady=(100, 0),sticky=N)


		button = ttk.Button(self, text="MAD LINE", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-RIGHT-MAD-LINE"))
		button.grid(column=1, row=5)

		button = ttk.Button(self, text="MAD LINE", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-LEFT-MAD-LINE"))
		button.grid(column=2, row=5)

		


	def setLabelText(self, label_text):
		self.label.config(text=label_text)