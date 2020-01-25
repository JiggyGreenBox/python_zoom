import tkinter as tk


from tkinter import ttk
from tkinter import *

class MAIN_Menu(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		self.label = tk.Label(self, text="CHOOSE SIDE")
		self.label.grid(column=1, row=1,columnspan=2,pady=50)
		self.obj_name = "MAIN"
		# label.pack(side="top", fill="x", pady=10)

		# button1 = tk.Button(self, text="LEFT",
		# 					command=lambda: controller.show_frame("Menu2"))
		# button2 = tk.Button(self, text="RIGHT",
		# 					command=lambda: controller.show_frame("Menu3"))
		# button1.pack()
		# button2.pack()



		button = ttk.Button(self, text="LEFT", command=lambda: controller.menu_btn_click(self.obj_name, "SET-LEFT"))
		button.grid(column=1, row=2)

		button = ttk.Button(self, text="RIGHT", command=lambda: controller.menu_btn_click(self.obj_name, "SET-RIGHT"))
		button.grid(column=2, row=2)



		# delete menu
		del_label = tk.Label(self, text="DELETE MENU")
		del_label.grid(column=1, row=3,columnspan=2,pady=(100, 0),sticky=N)

		button = ttk.Button(self, text="HIP", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-LEFT-HIP"))
		button.grid(column=1, row=4)

		button = ttk.Button(self, text="HIP", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-RIGHT-HIP"))
		button.grid(column=2, row=4)

		button = ttk.Button(self, text="KNEE", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-LEFT-HIP"))
		button.grid(column=1, row=5)

		button = ttk.Button(self, text="KNEE", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-RIGHT-HIP"))
		button.grid(column=2, row=5)


		button = ttk.Button(self, text="ANKLE", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-LEFT-HIP"))
		button.grid(column=1, row=6)

		button = ttk.Button(self, text="ANKLE", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-RIGHT-HIP"))
		button.grid(column=2, row=6)


		button = ttk.Button(self, text="FEM TOP", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-LEFT-HIP"))
		button.grid(column=1, row=7)

		button = ttk.Button(self, text="FEM TOP", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-RIGHT-HIP"))
		button.grid(column=2, row=7)


		button = ttk.Button(self, text="FEM BOT", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-LEFT-HIP"))
		button.grid(column=1, row=8)

		button = ttk.Button(self, text="FEM BOT", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-RIGHT-HIP"))
		button.grid(column=2, row=8)

	def setLabelText(self, label_text):
		self.label.config(text=label_text)		
