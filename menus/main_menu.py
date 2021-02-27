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
		self.dissapear_var = IntVar(value=1)
		self.draw_fem_j_var = IntVar(value=1)
		self.draw_tib_j_var = IntVar(value=1)
		self.draw_kjlo_line = IntVar(value=1)
		self.draw_mad_line = IntVar(value=1)
		self.draw_tib_knee = IntVar(value=1)
		self.draw_fem_knee = IntVar(value=1)



		header_label = tk.Label(self, text=self.obj_name,font=("TkDefaultFont",20))
		header_label.grid(column=1, row=1, columnspan=2, pady=[20,0])

		self.label = tk.Label(self, text="CHOOSE SIDE")
		self.label.grid(column=1, row=2, columnspan=2, pady=[10,20])



		button = ttk.Button(self, text="RIGHT", command=lambda: controller.menu_btn_click(self.obj_name, "SET-RIGHT"))
		button.grid(padx=[10,10], sticky="W", column=1, row=3)

		button = ttk.Button(self, text="LEFT", command=lambda: controller.menu_btn_click(self.obj_name, "SET-LEFT"))
		button.grid(padx=[10,10], sticky="W", column=2, row=3)

		

		# delete menu
		del_label = tk.Label(self, text="DELETE MENU")
		# del_label.grid(column=1, row=4,columnspan=2,pady=(50, 10),sticky=N)
		del_label.grid(column=1, row=4,columnspan=2,pady=(25, 5),sticky=N)


		button = ttk.Button(self, text="HIP", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-RIGHT-HIP"))
		button.grid(padx=[10,10], sticky="W", column=1, row=5)
		button = ttk.Button(self, text="HIP", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-LEFT-HIP"))
		button.grid(padx=[10,10], sticky="W", column=2, row=5)

		button = ttk.Button(self, text="NECK AXIS", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-RIGHT-NECK-AXIS"))
		button.grid(padx=[10,10], sticky="W", column=1, row=6)
		button = ttk.Button(self, text="NECK AXIS", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-LEFT-NECK-AXIS"))
		button.grid(padx=[10,10], sticky="W", column=2, row=6)

		
		

		button = ttk.Button(self, text="FEM TOP", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-RIGHT-FEM-TOP"))
		button.grid(padx=[10,10], sticky="W", column=1, row=7)
		button = ttk.Button(self, text="FEM TOP", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-LEFT-FEM-TOP"))
		button.grid(padx=[10,10], sticky="W", column=2, row=7)
		
		button = ttk.Button(self, text="FEM BOT", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-RIGHT-FEM-BOT"))
		button.grid(padx=[10,10], sticky="W", column=1, row=8)
		button = ttk.Button(self, text="FEM BOT", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-LEFT-FEM-BOT"))
		button.grid(padx=[10,10], sticky="W", column=2, row=8)



		button = ttk.Button(self, text="FEM KNEE", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-RIGHT-FEM-KNEE"))
		button.grid(padx=[10,10], sticky="W", column=1, row=9)
		button = ttk.Button(self, text="FEM KNEE", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-LEFT-FEM-KNEE"))
		button.grid(padx=[10,10], sticky="W", column=2, row=9)

		button = ttk.Button(self, text="TIB KNEE", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-RIGHT-TIB-KNEE"))
		button.grid(padx=[10,10], sticky="W", column=1, row=10)
		button = ttk.Button(self, text="TIB KNEE", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-LEFT-TIB-KNEE"))
		button.grid(padx=[10,10], sticky="W", column=2, row=10)


		button = ttk.Button(self, text="FEM J LINE", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-RIGHT-FEM-JOINT-LINE"))
		button.grid(padx=[10,10], sticky="W", column=1, row=11)
		button = ttk.Button(self, text="FEM J LINE", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-LEFT-FEM-JOINT-LINE"))
		button.grid(padx=[10,10], sticky="W", column=2, row=11)

		button = ttk.Button(self, text="TIB J LINE", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-RIGHT-TIB-JOINT-LINE"))
		button.grid(padx=[10,10], sticky="W", column=1, row=12)
		button = ttk.Button(self, text="TIB J LINE", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-LEFT-TIB-JOINT-LINE"))
		button.grid(padx=[10,10], sticky="W", column=2, row=12)
		

		

		button = ttk.Button(self, text="TIB TOP", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-RIGHT-TIB-TOP"))
		button.grid(padx=[10,10], sticky="W", column=1, row=13)
		button = ttk.Button(self, text="TIB TOP", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-LEFT-TIB-TOP"))
		button.grid(padx=[10,10], sticky="W", column=2, row=13)
		
		button = ttk.Button(self, text="TIB BOT", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-RIGHT-TIB-BOT"))
		button.grid(padx=[10,10], sticky="W", column=1, row=14)
		button = ttk.Button(self, text="TIB BOT", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-LEFT-TIB-BOT"))
		button.grid(padx=[10,10], sticky="W", column=2, row=14)




		button = ttk.Button(self, text="ANKLE", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-RIGHT-ANKLE"))
		button.grid(padx=[10,10], sticky="W", column=1, row=15)
		button = ttk.Button(self, text="ANKLE", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-LEFT-ANKLE"))
		button.grid(padx=[10,10], sticky="W", column=2, row=15)


		button = ttk.Button(self, text="DIST FEM", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-RIGHT-DIST-FEM"))
		button.grid(padx=[10,10], sticky="W", column=1, row=16)
		button = ttk.Button(self, text="DIST FEM", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-LEFT-DIST-FEM"))
		button.grid(padx=[10,10], sticky="W", column=2, row=16)


		button = ttk.Button(self, text="KJLO LINE", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-RIGHT-KJLO-LINE"))
		button.grid(padx=[10,10], sticky="W", column=1, row=17)
		button = ttk.Button(self, text="KJLO LINE", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-LEFT-KJLO-LINE"))
		button.grid(padx=[10,10], sticky="W", column=2, row=17)

		button = ttk.Button(self, text="MAD LINE", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-RIGHT-MAD-LINE"))
		button.grid(padx=[10,10], sticky="W", column=1, row=18)
		button = ttk.Button(self, text="MAD LINE", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-LEFT-MAD-LINE"))
		button.grid(padx=[10,10], sticky="W", column=2, row=18)


		

		


		

		label_cb = Checkbutton(self, text="LABELS", variable=self.label_var,command=lambda: controller.checkbox_click(self.obj_name, "TOGGLE_LABEL", self.label_var))
		label_cb.grid(padx=[5,0], pady=[10,0], sticky="W", column=1, row=19)

		hover_cb = Checkbutton(self, text="HOVER", variable=self.hover_var,command=lambda: controller.checkbox_click(self.obj_name, "TOGGLE_HOVER", self.hover_var))
		hover_cb.grid(padx=[5,0], pady=[10,0], sticky="W", column=2, row=19)

		dissapear_cb = Checkbutton(self, text="DISSAPEAR MODE", variable=self.dissapear_var,command=lambda: controller.checkbox_click(self.obj_name, "TOGGLE_DISSAPEAR_MODE", self.dissapear_var))
		dissapear_cb.grid(padx=[5,0],sticky="W", column=1, row=20, columnspan=2)

		fem_j_cb = Checkbutton(self, text="FEM J LINE", variable=self.draw_fem_j_var,command=lambda: controller.checkbox_click(self.obj_name, "TOGGLE_FEM_J", self.draw_fem_j_var))
		fem_j_cb.grid(padx=[5,0],sticky="W", column=1, row=21)

		tib_j_cb = Checkbutton(self, text="TIB J LINE", variable=self.draw_tib_j_var,command=lambda: controller.checkbox_click(self.obj_name, "TOGGLE_TIB_J", self.draw_tib_j_var))
		tib_j_cb.grid(padx=[5,0],sticky="W", column=2, row=21)


		fem_j_cb = Checkbutton(self, text="KJLO LINE", variable=self.draw_kjlo_line,command=lambda: controller.checkbox_click(self.obj_name, "TOGGLE_KJLO_LINE", self.draw_kjlo_line))
		fem_j_cb.grid(padx=[5,0],sticky="W", column=1, row=22)

		tib_j_cb = Checkbutton(self, text="MAD LINE", variable=self.draw_mad_line,command=lambda: controller.checkbox_click(self.obj_name, "TOGGLE_MAD_LINE", self.draw_mad_line))
		tib_j_cb.grid(padx=[5,0],sticky="W", column=2, row=22)


		fem_knee_cb = Checkbutton(self, text="FEM KNEE", variable=self.draw_fem_knee,command=lambda: controller.checkbox_click(self.obj_name, "TOGGLE_FEM_KNEE", self.draw_fem_knee))
		fem_knee_cb.grid(padx=[5,0],sticky="W", column=1, row=23)

		tib_knee_cb = Checkbutton(self, text="TIB KNEE", variable=self.draw_tib_knee,command=lambda: controller.checkbox_click(self.obj_name, "TOGGLE_TIB_KNEE", self.draw_tib_knee))
		tib_knee_cb.grid(padx=[5,0],sticky="W", column=2, row=23)
		

		# dist line
		# fem tib joint line
		# distal vca and kjlo
		# mad


		# draw_hip_knee_cb = Checkbutton(self, text="ANAT AXIS", variable=self.anat_var,command=lambda: controller.checkbox_click(self.obj_name, "TOGGLE_ANAT_AXIS", self.anat_var))
		# anat_axis_cb.grid(sticky="W",column=1, row=16)

		# mech_axis_cb = Checkbutton(self, text="MECH AXIS", variable=self.mech_var,command=lambda: controller.checkbox_click(self.obj_name, "TOGGLE_MECH_AXIS", self.mech_var))
		# mech_axis_cb.grid(sticky="W",column=1, row=15)

		# anat_axis_cb = Checkbutton(self, text="ANAT AXIS", variable=self.anat_var,command=lambda: controller.checkbox_click(self.obj_name, "TOGGLE_ANAT_AXIS", self.anat_var))
		# anat_axis_cb.grid(sticky="W",column=1, row=16)

		
		


	def setLabelText(self, label_text):
		self.label.config(text=label_text)	
