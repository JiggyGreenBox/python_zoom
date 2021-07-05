import tkinter as tk


from tkinter import ttk
from tkinter import *

# identify mac os and flip keys
from sys import platform

class KJLO_Menu(tk.Frame):

	# def __init__(self, parent, controller):
	# 	tk.Frame.__init__(self, parent)
	# 	self.controller = controller
		
	# 	self.obj_name = "KJLO"
	# 	label = tk.Label(self, text=self.obj_name,font=("TkDefaultFont",20))
	# 	label.pack(side="top", fill="x", pady=20)



	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		self.obj_name = "KJLO"
		
		header_label = tk.Label(self, text=self.obj_name,font=("TkDefaultFont",20))
		header_label.grid(column=1, row=1,columnspan=2,pady=[20,0])

		self.label = tk.Label(self, text="CHOOSE SIDE")
		self.label.grid(column=1, row=2,columnspan=2,pady=[10,20])


		
		b_width = 8
		if platform == "darwin":

			button = ttk.Button(self, text="RIGHT", width=b_width, command=lambda: controller.menu_btn_click(self.obj_name, "SET-RIGHT"))
			button.grid(padx=[10,10],column=1, row=3)

			button = ttk.Button(self, text="LEFT", width=b_width,  command=lambda: controller.menu_btn_click(self.obj_name, "SET-LEFT"))
			button.grid(padx=[10,10],column=2, row=3)



			# delete menu
			del_label = tk.Label(self, text="DELETE MENU")
			del_label.grid(column=1, row=4,columnspan=2,pady=(100, 0),sticky=N)


			button = ttk.Button(self, text="JOINT LINE", width=b_width,  command=lambda: controller.menu_btn_click(self.obj_name, "DEL-RIGHT-JOINT-LINE"))
			button.grid(padx=[10,10],column=1, row=5)

			button = ttk.Button(self, text="JOINT LINE", width=b_width,  command=lambda: controller.menu_btn_click(self.obj_name, "DEL-LEFT-JOINT-LINE"))
			button.grid(padx=[10,10],column=2, row=5)

			button = ttk.Button(self, text="ANKLE", width=b_width,  command=lambda: controller.menu_btn_click(self.obj_name, "DEL-RIGHT-ANKLE"))
			button.grid(padx=[10,10],column=1, row=6)

			button = ttk.Button(self, text="ANKLE", width=b_width,  command=lambda: controller.menu_btn_click(self.obj_name, "DEL-LEFT-ANKLE"))
			button.grid(padx=[10,10],column=2, row=6)

		else:


			button = ttk.Button(self, text="RIGHT", command=lambda: controller.menu_btn_click(self.obj_name, "SET-RIGHT"))
			button.grid(padx=[10,10],column=1, row=3)

			button = ttk.Button(self, text="LEFT", command=lambda: controller.menu_btn_click(self.obj_name, "SET-LEFT"))
			button.grid(padx=[10,10],column=2, row=3)



			# delete menu
			del_label = tk.Label(self, text="DELETE MENU")
			del_label.grid(padx=[10,10],column=1, row=4,columnspan=2,pady=(100, 0),sticky=N)


			button = ttk.Button(self, text="JOINT LINE", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-RIGHT-JOINT-LINE"))
			button.grid(padx=[10,10],column=1, row=5)

			button = ttk.Button(self, text="JOINT LINE", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-LEFT-JOINT-LINE"))
			button.grid(column=2, row=5)

			button = ttk.Button(self, text="ANKLE", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-RIGHT-ANKLE"))
			button.grid(padx=[10,10],column=1, row=6)

			button = ttk.Button(self, text="ANKLE", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-LEFT-ANKLE"))
			button.grid(padx=[10,10],column=2, row=6)

		


	def setLabelText(self, label_text):
		self.label.config(text=label_text)	