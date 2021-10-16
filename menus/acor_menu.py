import tkinter as tk


from tkinter import ttk
from tkinter import *

# identify mac os and flip keys
from sys import platform

class ACOR_Menu(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		self.obj_name = "ACOR"		

		self.flip_left = IntVar(value=0)
		self.flip_right = IntVar(value=0)

		header_label = tk.Label(self, text=self.obj_name, font=("TkDefaultFont",20))
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


			button = ttk.Button(self, text="FEM LINE", width=b_width, command=lambda: controller.menu_btn_click(self.obj_name, "DEL-RIGHT-FEM-LINE"))
			button.grid(padx=[10,10], column=1, row=5)
			button = ttk.Button(self, text="FEM LINE", width=b_width, command=lambda: controller.menu_btn_click(self.obj_name, "DEL-LEFT-FEM-LINE"))
			button.grid(padx=[10,10], column=2, row=5)

			
			button = ttk.Button(self, text="P1", width=b_width, command=lambda: controller.menu_btn_click(self.obj_name, "DEL-RIGHT-P1"))
			button.grid(padx=[10,10], column=1, row=6)
			button = ttk.Button(self, text="P1", width=b_width, command=lambda: controller.menu_btn_click(self.obj_name, "DEL-LEFT-P1"))
			button.grid(padx=[10,10], column=2, row=6)

			
			button = ttk.Button(self, text="P2", width=b_width, command=lambda: controller.menu_btn_click(self.obj_name, "DEL-RIGHT-P2"))
			button.grid(padx=[10,10], column=1, row=7)
			button = ttk.Button(self, text="P2", width=b_width, command=lambda: controller.menu_btn_click(self.obj_name, "DEL-LEFT-P2"))
			button.grid(padx=[10,10], column=2, row=7)

			button = ttk.Button(self, text="P3", width=b_width, command=lambda: controller.menu_btn_click(self.obj_name, "DEL-RIGHT-P3"))
			button.grid(padx=[10,10], column=1, row=8)
			button = ttk.Button(self, text="P3", width=b_width, command=lambda: controller.menu_btn_click(self.obj_name, "DEL-LEFT-P3"))
			button.grid(padx=[10,10], column=2, row=8)

			flip_r_cb = Checkbutton(self, text="FLIP", variable=self.flip_right,command=lambda: controller.checkbox_click(self.obj_name, "FLIP_RIGHT", self.flip_right))
			flip_r_cb.grid(padx=[5,0], pady=[10,0], sticky="W", column=1, row=9)

			flip_l_cb = Checkbutton(self, text="FLIP", variable=self.flip_left,command=lambda: controller.checkbox_click(self.obj_name, "FLIP_LEFT", self.flip_left))
			flip_l_cb.grid(padx=[5,0], pady=[10,0], sticky="W", column=2, row=9)

			tk.Label(self, text="ACOR = P1P2 / P1P3").grid(sticky="W", column=1, row=10,columnspan=2, padx=[10,10], pady=[10,10])
			tk.Label(self, text="PCOR = XP3 / P1P3").grid(sticky="W", column=1, row=11,columnspan=2, padx=[10,10], pady=[10,10])

		else:

			button = ttk.Button(self, text="RIGHT", command=lambda: controller.menu_btn_click(self.obj_name, "SET-RIGHT"))
			button.grid(padx=[10,10], column=1, row=3)

			button = ttk.Button(self, text="LEFT", command=lambda: controller.menu_btn_click(self.obj_name, "SET-LEFT"))
			button.grid(padx=[10,10], column=2, row=3)
			
			# delete menu
			del_label = tk.Label(self, text="DELETE MENU")
			del_label.grid(column=1, row=4,columnspan=2,pady=(100, 0),sticky=N)


			button = ttk.Button(self, text="FEM LINE", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-RIGHT-FEM-LINE"))
			button.grid(padx=[10,10], column=1, row=5)
			button = ttk.Button(self, text="FEM LINE", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-LEFT-FEM-LINE"))
			button.grid(padx=[10,10], column=2, row=5)

			
			button = ttk.Button(self, text="P1", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-RIGHT-P1"))
			button.grid(padx=[10,10], column=1, row=6)
			button = ttk.Button(self, text="P1", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-LEFT-P1"))
			button.grid(padx=[10,10], column=2, row=6)

			
			button = ttk.Button(self, text="P2", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-RIGHT-P2"))
			button.grid(padx=[10,10], column=1, row=7)
			button = ttk.Button(self, text="P2", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-LEFT-P2"))
			button.grid(padx=[10,10], column=2, row=7)

			button = ttk.Button(self, text="P3", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-RIGHT-P3"))
			button.grid(padx=[10,10], column=1, row=8)
			button = ttk.Button(self, text="P3", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-LEFT-P3"))
			button.grid(padx=[10,10], column=2, row=8)

			flip_r_cb = Checkbutton(self, text="FLIP", variable=self.flip_right,command=lambda: controller.checkbox_click(self.obj_name, "FLIP_RIGHT", self.flip_right))
			flip_r_cb.grid(padx=[5,0], pady=[10,0], sticky="W", column=1, row=9)

			flip_l_cb = Checkbutton(self, text="FLIP", variable=self.flip_left,command=lambda: controller.checkbox_click(self.obj_name, "FLIP_LEFT", self.flip_left))
			flip_l_cb.grid(padx=[5,0], pady=[10,0], sticky="W", column=2, row=9)

			tk.Label(self, text="ACOR = P1P2 / P1P3").grid(sticky="W", column=1, row=10,columnspan=2, padx=[10,10], pady=[10,10])
			tk.Label(self, text="PCOR = XP3 / P1P3").grid(sticky="W", column=1, row=11,columnspan=2, padx=[10,10], pady=[10,10])
			
			

		
	def setLabelText(self, label_text):
		self.label.config(text=label_text)


	def obj_to_menu(self, key, val):
		print('key: {} : val:{}'.format(key,val))

		if key == "flip_left":
			self.flip_left.set(1)

		if key == "flip_right":
			self.flip_right.set(1)