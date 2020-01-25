import tkinter as tk


from tkinter import ttk
from tkinter import *

class VCA_Menu(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		label = tk.Label(self, text="VCA_Menu")
		label.pack(side="top", fill="x", pady=10)