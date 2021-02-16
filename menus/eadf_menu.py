import tkinter as tk


from tkinter import ttk
from tkinter import *

class EADF_Menu(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		self.obj_name = "EADF"

		self.label_var = IntVar(value=1)
		self.hover_var = IntVar(value=1)


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


		button = ttk.Button(self, text="EADF LINE", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-RIGHT-EADF-LINE"))
		button.grid(column=1, row=5)

		button = ttk.Button(self, text="EADF LINE", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-LEFT-EADF-LINE"))
		button.grid(column=2, row=5)


		# hover-label checkboxes
		labels_cb = Checkbutton(self, text="LABELS", variable=self.label_var,command=lambda: controller.checkbox_click(self.obj_name, "TOGGLE_LABEL", self.label_var))
		labels_cb.grid(sticky="W",column=1, row=6)

		hover_cb = Checkbutton(self, text="HOVER", variable=self.hover_var,command=lambda: controller.checkbox_click(self.obj_name, "TOGGLE_HOVER", self.hover_var))
		hover_cb.grid(sticky="W",column=1, row=7)

		


	def setLabelText(self, label_text):
		self.label.config(text=label_text)