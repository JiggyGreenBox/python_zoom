import tkinter as tk


from tkinter import ttk
from tkinter import *



class DETAILS_View(tk.Frame):
	def __init__(self, parent, controller, master_dict):
		tk.Frame.__init__(self, parent)
		self.controller = controller

		self.master_dict = master_dict

		
		# to avoid iteration bugs
		self.med_image = ""


		vcmd = (self.register(self.callback))

		tk.Label(self, text="First Name").grid(row=0)
		tk.Label(self, text="Last Name").grid(row=1)
		tk.Label(self, text="Age").grid(row=2)
		tk.Label(self, text="Sex").grid(row=3)

		self.e_fname = tk.Entry(self)
		self.e_lname = tk.Entry(self)		
		self.e_age = tk.Entry(self, validate='all', validatecommand=(vcmd, '%P')) 



		self.e_fname.grid(row=0, column=1)
		self.e_lname.grid(row=1, column=1)
		self.e_age.grid(row=2, column=1)



		self.sex = tk.StringVar()
		m_btn = tk.Radiobutton(self, text='M', variable=self.sex, value="M")		
		m_btn.grid(row=3, column=1)
		f_btn = tk.Radiobutton(self, text='F', variable=self.sex, value="F")		
		f_btn.grid(row=4, column=1)


		submit_btn = ttk.Button(self, text="SAVE", command=lambda: self.save())
		submit_btn.grid(column=0, row=5)

	def callback(self, P):
		if str.isdigit(P) or P == "":
			return True
		else:
			return False

	def is_set_med_image(self):		
		# This class has no image related to it
		# exception for DETAILS_View
		return True

	def update_dict(self, master_dict):
		# update dictionaries
		self.master_dict = master_dict
		self.add_details_masterdict()


	def save(self):
		# print("save details")

		f_name 	= self.e_fname.get().strip()
		l_name 	= self.e_lname.get().strip()
		age 	= self.e_age.get().strip()
		sex 	= self.sex.get().strip()

		bool_save = False

		if f_name != "":
			self.master_dict["DETAILS"]["F_NAME"] = f_name
			bool_save = True

		if l_name != "":
			self.master_dict["DETAILS"]["L_NAME"] = l_name
			bool_save = True

		if age != "":
			self.master_dict["DETAILS"]["AGE"] = age
			bool_save = True

		if sex != "":
			self.master_dict["DETAILS"]["SEX"] = sex
			bool_save = True

		if bool_save:
			self.controller.save_json()

		


	def add_details_masterdict(self):
		
		if "DETAILS" not in self.master_dict.keys():		# details dont exist new patient
			# print("details reached")
			self.master_dict["DETAILS"] = 	{
										"F_NAME":None,
										"L_NAME":None,
										"AGE":None,
										"SEX":None										
									}
			self.controller.save_json()

		else:												# details exist, check if blank			

			f_name 	= self.master_dict["DETAILS"]["F_NAME"]
			l_name 	= self.master_dict["DETAILS"]["L_NAME"]
			age 	= self.master_dict["DETAILS"]["AGE"]
			sex 	= self.master_dict["DETAILS"]["SEX"]


			if f_name != None:				
				self.e_fname.delete(0, tk.END)
				self.e_fname.insert(0, f_name)

			if l_name != None:				
				self.e_lname.delete(0, tk.END)
				self.e_lname.insert(0, l_name)

			if age != None:				
				self.e_age.delete(0, tk.END)
				self.e_age.insert(0, age)

			if sex != None:				
				self.sex.set(sex)


	