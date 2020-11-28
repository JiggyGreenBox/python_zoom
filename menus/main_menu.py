import tkinter as tk


from tkinter import ttk
from tkinter import *

class MAIN_Menu(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller		
		self.obj_name = "MAIN"

		# daw axis vars
		# self.mech_var = StringVar(self)
		# self.anat_var = StringVar(self)

		self.label_var = IntVar(value=1)
		self.hover_var = IntVar(value=1)
		self.mech_var = IntVar()
		self.anat_var = IntVar()



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


		button = ttk.Button(self, text="HIP", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-RIGHT-HIP"))
		button.grid(column=1, row=5)
		button = ttk.Button(self, text="HIP", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-LEFT-HIP"))
		button.grid(column=2, row=5)

		


		button = ttk.Button(self, text="FEM KNEE", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-RIGHT-FEM-KNEE"))
		button.grid(column=1, row=6)
		button = ttk.Button(self, text="FEM KNEE", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-LEFT-FEM-KNEE"))
		button.grid(column=2, row=6)

		button = ttk.Button(self, text="TIB KNEE", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-RIGHT-TIB-KNEE"))
		button.grid(column=1, row=7)
		button = ttk.Button(self, text="TIB KNEE", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-LEFT-TIB-KNEE"))
		button.grid(column=2, row=7)

		

		button = ttk.Button(self, text="ANKLE", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-RIGHT-ANKLE"))
		button.grid(column=1, row=8)
		button = ttk.Button(self, text="ANKLE", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-LEFT-ANKLE"))
		button.grid(column=2, row=8)
		

		button = ttk.Button(self, text="FEM TOP", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-RIGHT-FEM-TOP"))
		button.grid(column=1, row=9)
		button = ttk.Button(self, text="FEM TOP", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-LEFT-FEM-TOP"))
		button.grid(column=2, row=9)

		
		button = ttk.Button(self, text="FEM BOT", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-RIGHT-FEM-BOT"))
		button.grid(column=1, row=10)
		button = ttk.Button(self, text="FEM BOT", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-LEFT-FEM-BOT"))
		button.grid(column=2, row=10)



		button = ttk.Button(self, text="TIB TOP", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-RIGHT-TIB-TOP"))
		button.grid(column=1, row=11)
		button = ttk.Button(self, text="TIB TOP", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-LEFT-TIB-TOP"))
		button.grid(column=2, row=11)

		
		button = ttk.Button(self, text="TIB BOT", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-RIGHT-TIB-BOT"))
		button.grid(column=1, row=12)
		button = ttk.Button(self, text="TIB BOT", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-LEFT-TIB-BOT"))
		button.grid(column=2, row=12)


		# CheckVar1 = IntVar()
		# CheckVar2 = IntVar()
		'''
		mech_axis_cb = Checkbutton(self, text="MECH AXIS", variable=self.mech_var,onvalue="checked", offvalue="unchecked",command=self.meme)
		mech_axis_cb.grid(column=1, row=12)

		anat_axis_cb = Checkbutton(self, text="ANAT AXIS", variable=self.anat_var,onvalue="checked", offvalue="unchecked",command=self.meme)
		anat_axis_cb.grid(column=1, row=13)
		'''


		# mech_axis_cb = Checkbutton(self, text="MECH AXIS", variable=self.mech_var,command=self.meme)
		# mech_axis_cb.grid(column=1, row=13)

		# anat_axis_cb = Checkbutton(self, text="ANAT AXIS", variable=self.anat_var,command=self.meme)
		# anat_axis_cb.grid(column=1, row=14)

		mech_axis_cb = Checkbutton(self, text="LABELS", variable=self.label_var,command=lambda: controller.checkbox_click(self.obj_name, "TOGGLE_LABEL", self.label_var))
		mech_axis_cb.grid(sticky="W",column=1, row=13)

		mech_axis_cb = Checkbutton(self, text="HOVER", variable=self.hover_var,command=lambda: controller.checkbox_click(self.obj_name, "TOGGLE_HOVER", self.hover_var))
		mech_axis_cb.grid(sticky="W",column=1, row=14)

		mech_axis_cb = Checkbutton(self, text="MECH AXIS", variable=self.mech_var,command=lambda: controller.checkbox_click(self.obj_name, "TOGGLE_MECH_AXIS", self.mech_var))
		mech_axis_cb.grid(sticky="W",column=1, row=15)

		anat_axis_cb = Checkbutton(self, text="ANAT AXIS", variable=self.anat_var,command=lambda: controller.checkbox_click(self.obj_name, "TOGGLE_ANAT_AXIS", self.anat_var))
		anat_axis_cb.grid(sticky="W",column=1, row=16)

		
		


	def setLabelText(self, label_text):
		self.label.config(text=label_text)

	def meme(self):
		print('mech {}'.format(self.mech_var.get()))
		print('anat {}'.format(self.anat_var.get()))
		print("\n")
