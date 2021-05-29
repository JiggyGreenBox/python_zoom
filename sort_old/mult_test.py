# -*- coding: utf-8 -*-
# Advanced zoom for images of various types from small to huge up to several GB
import math
import warnings
import tkinter as tk


from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk

# from gui_canvas import CanvasImage
from gui_draw_tools import DrawTools

# multithreading
import threading
import queue
# from queue import Queue
import time # sleep

class MainWindow(ttk.Frame):
	""" Main window class """
	def __init__(self, mainframe, path):
		""" Initialize the main Frame """
		ttk.Frame.__init__(self, master=mainframe)
		self.master.title('Advanced Zoom v3.0')
		self.master.geometry('800x600')  # size of the main window
		# self.master.rowconfigure(0, weight=1)  # make the CanvasImage widget expandable
		# self.master.columnconfigure(0, weight=1)


		navbar = Frame(self.master, width=100)
		navbar.pack(anchor=W, fill=Y, expand=False, side=LEFT)  # <----



		button = ttk.Button(navbar, text="object 1", command=self.btn1)
		button.grid(column=1, row=1)

		self.button2 = ttk.Button(navbar, text="object 2", command=self.btn2)
		self.button2.grid(column=1, row=2)



		content_frame = Frame(self.master)
		content_frame.pack(anchor=N, fill=BOTH, expand=True, side=LEFT )
		content_frame.rowconfigure(0, weight=1)  # make the CanvasImage widget expandable
		content_frame.columnconfigure(0, weight=1)

		


		self.canvas = DrawTools(content_frame, path)  # create widget
		self.canvas.grid(row=0, column=0)  # show widget

		self.obj1 = Myobj1(self.canvas)
		self.obj2 = Myobj2(self.canvas)


	def btn1(self):
		# global cur_obj
		# cur_obj = self.obj1
		print("set obj1")
		self.canvas.setObject(self.obj1)

	def btn2(self):
		# global cur_obj
		# cur_obj = self.obj2
		print("set obj2")
		# self.canvas.setObject(self.obj2)

		self.button2.configure(state=DISABLED)

		self.queue = queue.Queue()
		ThreadedTask(self.queue).start()
		self.master.after(100, self.process_queue)

	def process_queue(self):
		try:
			msg = self.queue.get(0)
			# Show result of the task if needed
			print(msg)
			self.button2.configure(state=NORMAL)
			# self.prog_bar.stop()
		except queue.Empty:
			self.master.after(100, self.process_queue)


class Myobj1:
	# instance attribute
	def __init__(self, canvas):
		self.name = "object1"
		self.canvas = canvas

	def click(self, event):
		print("click from object1")			
		# self.canvas.create_token(event, "white")

class Myobj2:
	# instance attribute
	def __init__(self, canvas):
		self.name = "object2"
		self.canvas = canvas

	def click(self, event):
		print("click from object2")
		# self.canvas.create_token(event, "black")


		# self.queue = queue.Queue()
		# ThreadedTask(self.queue).start()
		# self.master.after(100, self.process_queue)


	



class ThreadedTask(threading.Thread):
	def __init__(self, queue):
		threading.Thread.__init__(self)
		self.queue = queue
	def run(self):
		time.sleep(5)  # Simulate long running process
		self.queue.put("Task finished")



filename = '500.jpg'  # place path to your image here
app = MainWindow(tk.Tk(), path=filename)
app.mainloop()