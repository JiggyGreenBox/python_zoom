import tkinter as tk


from tkinter import ttk
from tkinter import *

# identify mac os and flip keys
from sys import platform

class P_TILT_Menu(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		self.obj_name = "P_TILT"


		self.label_var = IntVar(value=1)
		self.hover_var = IntVar(value=1)

		header_label = tk.Label(self, text=self.obj_name,font=("TkDefaultFont",20))
		header_label.grid(column=1, row=1,columnspan=2,pady=[20,0])

		self.label = tk.Label(self, text="CHOOSE SIDE")
		self.label.grid(column=1, row=2,columnspan=2,pady=[10,20])

		b_width = 8

		if platform == "darwin":

			button = ttk.Button(self, text="RIGHT", width=b_width, command=lambda: controller.menu_btn_click(self.obj_name, "SET-RIGHT"))
			button.grid(padx=[10,10], column=1, row=3)

			button = ttk.Button(self, text="LEFT", width=b_width, command=lambda: controller.menu_btn_click(self.obj_name, "SET-LEFT"))
			button.grid(padx=[10,10], column=2, row=3)

			

			# delete menu
			del_label = tk.Label(self, text="DELETE MENU")
			del_label.grid(column=1, row=4,columnspan=2,pady=(100, 0),sticky=N)

			

			button = ttk.Button(self, text="P1", width=b_width, command=lambda: controller.menu_btn_click(self.obj_name, "DEL-RIGHT-P1"))
			button.grid(padx=[10,10], column=1, row=5)
			button = ttk.Button(self, text="P1", width=b_width, command=lambda: controller.menu_btn_click(self.obj_name, "DEL-LEFT-P1"))
			button.grid(padx=[10,10], column=2, row=5)

			
			button = ttk.Button(self, text="P2", width=b_width, command=lambda: controller.menu_btn_click(self.obj_name, "DEL-RIGHT-P2"))
			button.grid(padx=[10,10], column=1, row=6)
			button = ttk.Button(self, text="P2", width=b_width, command=lambda: controller.menu_btn_click(self.obj_name, "DEL-LEFT-P2"))
			button.grid(padx=[10,10], column=2, row=6)


			button = ttk.Button(self, text="PAT P1", width=b_width, command=lambda: controller.menu_btn_click(self.obj_name, "DEL-RIGHT-PAT-P1"))
			button.grid(padx=[10,10], column=1, row=7)
			button = ttk.Button(self, text="PAT P1", width=b_width, command=lambda: controller.menu_btn_click(self.obj_name, "DEL-LEFT-PAT-P1"))
			button.grid(padx=[10,10], column=2, row=7)

			
			button = ttk.Button(self, text="PAT P2", width=b_width, command=lambda: controller.menu_btn_click(self.obj_name, "DEL-RIGHT-PAT-P2"))
			button.grid(padx=[10,10], column=1, row=8)
			button = ttk.Button(self, text="PAT P2", width=b_width, command=lambda: controller.menu_btn_click(self.obj_name, "DEL-LEFT-PAT-P2"))
			button.grid(padx=[10,10], column=2, row=8)

			label_cb = Checkbutton(self, text="LABELS", variable=self.label_var,command=lambda: controller.checkbox_click(self.obj_name, "TOGGLE_LABEL", self.label_var))
			label_cb.grid(padx=[5,0], pady=[10,0], sticky="W", column=1, row=9)

			hover_cb = Checkbutton(self, text="HOVER", variable=self.hover_var,command=lambda: controller.checkbox_click(self.obj_name, "TOGGLE_HOVER", self.hover_var))
			hover_cb.grid(padx=[5,0], pady=[10,0], sticky="W", column=2, row=9)

		else:


			button = ttk.Button(self, text="RIGHT", command=lambda: controller.menu_btn_click(self.obj_name, "SET-RIGHT"))
			button.grid(padx=[10,10], column=1, row=3)

			button = ttk.Button(self, text="LEFT", command=lambda: controller.menu_btn_click(self.obj_name, "SET-LEFT"))
			button.grid(padx=[10,10], column=2, row=3)

			

			# delete menu
			del_label = tk.Label(self, text="DELETE MENU")
			del_label.grid(column=1, row=4,columnspan=2,pady=(100, 0),sticky=N)

			

			button = ttk.Button(self, text="P1", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-RIGHT-P1"))
			button.grid(padx=[10,10], column=1, row=5)
			button = ttk.Button(self, text="P1", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-LEFT-P1"))
			button.grid(padx=[10,10], column=2, row=5)

			
			button = ttk.Button(self, text="P2", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-RIGHT-P2"))
			button.grid(padx=[10,10], column=1, row=6)
			button = ttk.Button(self, text="P2", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-LEFT-P2"))
			button.grid(padx=[10,10], column=2, row=6)


			button = ttk.Button(self, text="PAT P1", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-RIGHT-PAT-P1"))
			button.grid(padx=[10,10], column=1, row=7)
			button = ttk.Button(self, text="PAT P1", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-LEFT-PAT-P1"))
			button.grid(padx=[10,10], column=2, row=7)

			
			button = ttk.Button(self, text="PAT P2", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-RIGHT-PAT-P2"))
			button.grid(padx=[10,10], column=1, row=8)
			button = ttk.Button(self, text="PAT P2", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-LEFT-PAT-P2"))
			button.grid(padx=[10,10], column=2, row=8)

			label_cb = Checkbutton(self, text="LABELS", variable=self.label_var,command=lambda: controller.checkbox_click(self.obj_name, "TOGGLE_LABEL", self.label_var))
			label_cb.grid(padx=[5,0], pady=[10,0], sticky="W", column=1, row=9)

			hover_cb = Checkbutton(self, text="HOVER", variable=self.hover_var,command=lambda: controller.checkbox_click(self.obj_name, "TOGGLE_HOVER", self.hover_var))
			hover_cb.grid(padx=[5,0], pady=[10,0], sticky="W", column=2, row=9)


	def setLabelText(self, label_text):
		self.label.config(text=label_text)