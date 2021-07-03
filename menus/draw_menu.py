import tkinter as tk


from tkinter import ttk
from tkinter import *

class DRAW_Menu(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		self.obj_name = "DRAW"

		self.label_var = IntVar(value=1)
		self.hover_var = IntVar(value=1)

		self.sv_draw_options = tk.StringVar()	# DrawOptions
		self.sv_map_val 	 = tk.StringVar()	# MapVal


		


		header_label = tk.Label(self, text=self.obj_name,font=("TkDefaultFont",20))
		header_label.grid(column=1, row=1,columnspan=2,pady=[20,0])

		self.label = tk.Label(self, text="CHOOSE SIDE")
		self.label.grid(column=1, row=2,columnspan=2,pady=[10,20])

		rb1 = ttk.Radiobutton(self, text='LINE', value='LINE', variable=self.sv_draw_options, command=lambda: controller.menu_btn_click(self.obj_name, "SET-LINE"))
		rb2 = ttk.Radiobutton(self, text='ANGLE', value='ANGLE', variable=self.sv_draw_options, command=lambda: controller.menu_btn_click(self.obj_name, "SET-ANGLE"))
		rb3 = ttk.Radiobutton(self, text='MAP', value='MAP', variable=self.sv_draw_options, command=lambda: controller.menu_btn_click(self.obj_name, "SET-MAP"))
		rb1.grid(column=1, row=3,sticky="W")
		rb2.grid(column=1, row=4,sticky="W")
		rb3.grid(column=1, row=5,sticky="W")


		# map_btn = ttk.Button(self, text="DEL MAP", command=lambda: controller.menu_btn_click(self.obj_name, "DEL-MAP"))
		# map_btn.grid(column=1, row=6)
		map_btn = tk.Label(self, text="MAP LENGTH (cm)")
		map_btn.grid(column=1, row=6)

		self.map_val = ttk.Entry(self, width=8, textvariable=self.sv_map_val)
		self.map_val.grid(column=2, row=6)

		self.sv_map_val.trace_add("write", lambda name, index, mode, var=self.sv_map_val: self.entry_callback(self.sv_map_val))

		# put scroll div here
		self.draw_list = Example(self)
		self.draw_list.grid(column=1, row=7, columnspan=2)		
		


	def setLabelText(self, label_text):
		self.label.config(text=label_text)


	def entry_callback(self, val):
		print(val.get().strip())

		self.controller.menu_to_obj(self.obj_name, "MAP_VAL", val.get().strip())

	def obj_to_menu(self, key, val):
		# print('key: {} : val:{}'.format(key,val))


		self.draw_list.updateLocalDicts(key,val)

		



class Example(tk.Frame):
	def __init__(self, parent):

		# tk.Frame.__init__(self, parent)
		# self.canvas = tk.Canvas(self, borderwidth=0, background="#ffffff", width=170)
		# self.frame = tk.Frame(self.canvas, background="#ffffff", width=170)
		# self.vsb = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
		# self.canvas.configure(yscrollcommand=self.vsb.set)

		# self.vsb.pack(side="right", fill="y")
		# self.canvas.pack(side="left", fill="both", expand=True)
		# self.canvas.create_window((4,4), window=self.frame, anchor="nw", tags="self.frame")

		# self.frame.bind("<Configure>", self.onFrameConfigure)

		# self.btn_holder = tk.Frame(self, background="green", width=170, height=50)
		# self.btn_holder.pack(side="bottom", anchor="w")

		tk.Frame.__init__(self, parent)

		self.parent = parent

		self.main_frame = tk.Frame(self, width=170)

		# self.canvas = tk.Canvas(self.main_frame, borderwidth=0, background="#ffffff", width=170)
		# self.frame = tk.Frame(self.canvas, background="#ffffff", width=170)
		self.canvas = tk.Canvas(self.main_frame, borderwidth=0, width=170)
		self.frame = tk.Frame(self.canvas, width=170)
		self.vsb = ttk.Scrollbar(self.main_frame, orient="vertical", command=self.canvas.yview)
		self.canvas.configure(yscrollcommand=self.vsb.set)

		self.vsb.pack(side="right", fill="y")
		self.canvas.pack(side="left", fill="both", expand=True)
		self.canvas.create_window((4,4), window=self.frame, anchor="nw", tags="self.frame")

		self.frame.bind("<Configure>", self.onFrameConfigure)

		self.main_frame.grid(row=0,column=0)

		self.btn_holder = tk.Frame(self, background="green", width=170, height=50)
		self.btn_holder.grid(row=1,column=0)

		self.delete_btn = ttk.Button(self.btn_holder, text="DELETE", command=lambda: self.delete_from_dicts())
		self.delete_btn.grid(row=0,column=0)

		self.flip_btn = ttk.Button(self.btn_holder, text="FLIP", command=lambda: self.flip_angles())
		self.flip_btn.grid(row=1,column=0)

		self.populate()


		# storage for lines angle and map
		self.line_dict 	= {}
		self.angle_dict = {}
		self.map_dict 	= {}

		# store selected keys here 
		self.line_selected 	= []
		self.angle_selected = []
		self.map_selected 	= []

	def populate(self):
		'''Put in some fake data'''
		pass
		# for row in range(10):
		# 	tk.Label(self.frame, text="%s" % row, width=3, borderwidth="1",
		# 			 relief="solid").grid(row=row, column=0)
		# 	t="this is the second column for row %s" %row
		# 	tk.Label(self.frame, text=t).grid(row=row, column=1)

	def onFrameConfigure(self, event):
		'''Reset the scroll region to encompass the inner frame'''
		self.canvas.configure(scrollregion=self.canvas.bbox("all"))


	def myPopulate(self):
		#  empty the frame
		for widget in self.frame.winfo_children():
			widget.destroy()

		# clear the selected lists
		self.angle_selected.clear()
		self.line_selected.clear()
		self.map_selected.clear()

		# use the list information to populate
		row=0
		# line dict first
		for k in self.line_dict.keys():
			# tk.Label(self.frame, text=k).grid(row=row, column=0)

			cb = ttk.Checkbutton(self.frame, text=k, command=lambda k=k, mtype="LINE": self.draw_checkbox_click(mtype,k))
			cb.state(['!alternate'])
			cb.state(['!selected'])
			# cb.grid(padx=[5,0],sticky="W", column=2, row=21)
			cb.grid(row=row, column=0, sticky="W")

			if self.line_dict[k]['cm'] != None:
				cm_val = '{0:.2f}'.format(self.line_dict[k]['cm'])
				tk.Label(self.frame, text=cm_val).grid(row=row, column=1)

			row=row+1

		for k in self.angle_dict.keys():
			# tk.Label(self.frame, text=k).grid(row=row, column=0)

			cb = ttk.Checkbutton(self.frame, text=k, command=lambda k=k, mtype="ANGLE": self.draw_checkbox_click(mtype,k))
			cb.state(['!alternate'])
			cb.state(['!selected'])
			# cb.grid(padx=[5,0],sticky="W", column=2, row=21)
			cb.grid(row=row, column=0, sticky="W")

			if self.angle_dict[k]['angle'] != None:
				ang_val = '{0:.2f}'.format(self.angle_dict[k]['angle'])
				tk.Label(self.frame, text=ang_val).grid(row=row, column=1)

			row=row+1

		for k in self.map_dict.keys():
			# tk.Label(self.frame, text=k).grid(row=row, column=0)

			cb = ttk.Checkbutton(self.frame, text=k, command=lambda k=k, mtype="MAP": self.draw_checkbox_click(mtype,k))
			cb.state(['!alternate'])
			cb.state(['!selected'])
			# cb.grid(padx=[5,0],sticky="W", column=2, row=21)
			cb.grid(row=row, column=0)
			row=row+1

	def delete_from_dicts(self):
		print("delete")
		# print(self.angle_selected)
		# print(self.line_selected)

		for key in self.angle_selected:
			del self.angle_dict[key]

		for key in self.line_selected:
			del self.line_dict[key]

		for key in self.map_selected:
			del self.map_dict[key]

		self.angle_selected.clear()
		self.line_selected.clear()
		self.map_selected.clear()

		self.parent.controller.menu_to_obj("DRAW", "UPDATE_ANGLE", self.angle_dict)
		self.parent.controller.menu_to_obj("DRAW", "UPDATE_LINE", self.line_dict)
		self.parent.controller.menu_to_obj("DRAW", "UPDATE_MAP", self.map_dict)
		self.myPopulate()


	def flip_angles(self):

		# iterate through angle selected
		for key in self.angle_selected:
			self.angle_dict[key]['flip'] = not self.angle_dict[key]['flip']

		self.parent.controller.menu_to_obj("DRAW", "UPDATE_ANGLE", self.angle_dict)



	def updateLocalDicts(self, key, val):
		if key == "line_dict":
			self.line_dict = val
		elif key == "angle_dict":
			self.angle_dict = val
		elif key == "map_dict":		
			self.map_dict = val

		self.myPopulate()


	def draw_checkbox_click(self, dict_type, key):
		print('dict_type:{} key:{}'.format(dict_type, key))

		# if key found remove
		# else insert
		if dict_type == "ANGLE":
			if key in self.angle_selected:
				self.angle_selected.remove(key)
			else:
				self.angle_selected.append(key)	

		elif dict_type == "LINE":
			if key in self.line_selected:
				self.line_selected.remove(key)
			else:
				self.line_selected.append(key)

		elif dict_type == "MAP":
			if key in self.map_selected:
				self.map_selected.remove(key)
			else:
				self.map_selected.append(key)



