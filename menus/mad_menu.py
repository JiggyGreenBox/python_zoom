import tkinter as tk


from tkinter import ttk
from tkinter import *

class MAD_Menu(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		self.obj_name = "MAD"

		label = tk.Label(self, text=self.obj_name,font=("TkDefaultFont",20))
		label.pack(side="top", fill="x", pady=20)		


		# deprecated, auto calculating MAD

		# -----------------MAD TEXT ENTRY---------------------------------------
		# header_label = tk.Label(self, text=self.obj_name,font=("TkDefaultFont",20))
		# header_label.grid(column=1, row=1,columnspan=2,pady=[20,0])

		# self.label = tk.Label(self, text="MAD VALUE")
		# self.label.grid(column=1, row=2,columnspan=2,pady=[10,20])

		# self.R_mad_entry = tk.Entry(self, width=10)
		# self.L_mad_entry = tk.Entry(self, width=10)

		# self.R_mad_entry.grid(row=3, column=1,padx=[5,5])
		# self.L_mad_entry.grid(row=3, column=2,padx=[5,5])



		# button = ttk.Button(self, text="SAVE", command=lambda: controller.menu_btn_click(self.obj_name, "SAVE-MAD"))
		# button.grid(column=1, row=4, columnspan=2, pady=[10,0])

		# --------------------------------------------------------






	# 	button = ttk.Button(self, text="LEFT", command=lambda: controller.menu_btn_click(self.obj_name, "SET-LEFT"))
	# 	button.grid(column=2, row=3)



	# 	# delete menu
	# 	del_label = tk.Label(self, text="DELETE MENU")
	# 	del_label.grid(column=1, row=4,columnspan=2,pady=(100, 0),sticky=N)


	# 	button = ttk.Button(self, text="MAD LINE", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-RIGHT-MAD-LINE"))
	# 	button.grid(column=1, row=5)

	# 	button = ttk.Button(self, text="MAD LINE", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-LEFT-MAD-LINE"))
	# 	button.grid(column=2, row=5)

		


	# def setLabelText(self, label_text):
	# 	self.label.config(text=label_text)




	# -----------------MAD TEXT ENTRY---------------------------------------
	# def getMadEntryVals(self):
	# 	'''return R-L vals'''
	# 	return self.R_mad_entry.get().strip(), self.L_mad_entry.get().strip()

	# def updateMadLabels(self, R_val, L_val):

	# 	if R_val != None:
	# 		self.R_mad_entry.delete(0, tk.END)
	# 		self.R_mad_entry.insert(0, R_val)

	# 	if L_val != None:
	# 		self.L_mad_entry.delete(0, tk.END)
	# 		self.L_mad_entry.insert(0, L_val)