import tkinter as tk


from tkinter import ttk
from tkinter import *

class KAOL_Menu(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		self.obj_name = "KAOL"

		label = tk.Label(self, text=self.obj_name,font=("TkDefaultFont",20))
		label.pack(side="top", fill="x", pady=20)