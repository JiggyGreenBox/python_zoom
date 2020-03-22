import tkinter as tk


from tkinter import ttk
from tkinter import *

class ISR_Menu(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		self.obj_name = "ISR"

		self.label = tk.Label(self, text="CHOOSE SIDE")
		self.label.grid(column=1, row=1,columnspan=2,pady=50)


		button = ttk.Button(self, text="LEFT", command=lambda: controller.menu_btn_click(self.obj_name, "SET-LEFT"))
		button.grid(column=1, row=2)

		button = ttk.Button(self, text="RIGHT", command=lambda: controller.menu_btn_click(self.obj_name, "SET-RIGHT"))
		button.grid(column=2, row=2)