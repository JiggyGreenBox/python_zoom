import tkinter as tk


from tkinter import ttk
from tkinter import *

class AFTA_Menu(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		label = tk.Label(self, text="AFTA_Menu")
		label.pack(side="top", fill="x", pady=10)

		button1 = tk.Button(self, text="Go to Page One",
							command=lambda: controller.show_frame("Menu2"))
		button2 = tk.Button(self, text="Go to Page Two",
							command=lambda: controller.show_frame("Menu3"))
		button1.pack()
		button2.pack()