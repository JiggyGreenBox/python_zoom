import tkinter as tk


from tkinter import ttk
from tkinter import *

class DETAILS_View(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller

		# choosen by user OR
		# loaded from pat.json
		self.med_image = ""		


	def is_set_med_image(self):
		if self.med_image != "":
			return True
		return False


	def set_med_image(self, image):
		if image != "":
			self.med_image = image
		else:
			print("image is blank")