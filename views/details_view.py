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

		tk.Label(self, text="PATIENT DETAILS", font=("TkDefaultFont", 12)).grid(sticky="W", column=0, row=0, pady=(30, 10), padx=(10,0))

		tk.Label(self, text="First Name").grid(sticky="W", row=1, padx=(10,0))
		tk.Label(self, text="Last Name").grid(sticky="W", row=2, padx=(10,0))
		tk.Label(self, text="Age").grid(sticky="W", row=3, padx=(10,0))
		tk.Label(self, text="Sex").grid(sticky="W", row=4, padx=(10,0))

		self.e_fname = tk.Entry(self)
		self.e_lname = tk.Entry(self)		
		self.e_age = tk.Entry(self, validate='all', validatecommand=(vcmd, '%P')) 



		self.e_fname.grid(row=1, column=1)
		self.e_lname.grid(row=2, column=1)
		self.e_age.grid(row=3, column=1)



		self.sex = tk.StringVar()
		m_btn = tk.Radiobutton(self, text='M', variable=self.sex, value="M",tristatevalue="x")
		m_btn.grid(sticky="W", row=4, column=1)
		f_btn = tk.Radiobutton(self, text='F', variable=self.sex, value="F",tristatevalue="x")
		f_btn.grid(sticky="W", row=5, column=1)


		submit_btn = ttk.Button(self, text="SAVE", command=lambda: self.save())
		submit_btn.grid(column=0, row=6)



		tk.Label(self, text="POINT SIZES", font=("TkDefaultFont", 12)).grid(sticky="W", column=0, row=7, pady=(60, 10), padx=(10,0))

		
		self.pre_scanno_var		= StringVar()
		self.pre_ap_var	 		= StringVar()
		self.pre_lat_var	 	= StringVar()
		self.pre_sky_var		= StringVar()
		self.post_scanno_var	= StringVar()
		self.post_ap_var	 	= StringVar()
		self.post_lat_var		= StringVar()
		self.post_sky_var		= StringVar()



		tk.Label(self, text="PRE-SCANNO").grid(sticky="W", column=0, row=8, padx=(10,0))
		sp1 = Spinbox(self, textvariable=self.pre_scanno_var, from_= 1, to = 30, width=10).grid(column=1, row=8)

		tk.Label(self, text="PRE-AP").grid(sticky="W", column=0, row=9, padx=(10,0))
		sp2 = Spinbox(self, textvariable=self.pre_ap_var, from_= 1, to = 30, width=10).grid(column=1, row=9)

		tk.Label(self, text="PRE-LAT").grid(sticky="W", column=0, row=10, padx=(10,0))
		sp3 = Spinbox(self, textvariable=self.pre_lat_var, from_= 1, to = 30, width=10).grid(column=1, row=10)

		tk.Label(self, text="PRE-SKY").grid(sticky="W", column=0, row=11, padx=(10,0))
		sp4 = Spinbox(self, textvariable=self.pre_sky_var, from_= 1, to = 30, width=10).grid(column=1, row=11)

		tk.Label(self, text="POST-SCANNO").grid(sticky="W", column=0, row=12, padx=(10,0), pady=(20, 0))
		sp5 = Spinbox(self, textvariable=self.post_scanno_var, from_= 1, to = 30, width=10).grid(column=1, row=12, pady=(20, 0))

		tk.Label(self, text="POST-AP").grid(sticky="W", column=0, row=13, padx=(10,0))
		sp6 = Spinbox(self, textvariable=self.post_ap_var, from_= 1, to = 30, width=10).grid(column=1, row=13)

		tk.Label(self, text="POST-LAT").grid(sticky="W", column=0, row=14, padx=(10,0))
		sp7 = Spinbox(self, textvariable=self.post_lat_var, from_= 1, to = 30, width=10).grid(column=1, row=14)

		tk.Label(self, text="POST-SKY").grid(sticky="W", column=0, row=15, padx=(10,0))
		sp8 = Spinbox(self, textvariable=self.post_sky_var, from_= 1, to = 30, width=10).grid(column=1, row=15)



		tk.Label(self, text="v0.3").grid(sticky="W", row=16, pady=(30,0), padx=(10,0))


		# self.pre_scanno_var.set(self.master_dict["POINT_SIZES"]["PRE-SCANNO"])
		# self.pre_ap_var.set(self.master_dict["POINT_SIZES"]["PRE-AP"])
		# self.pre_lat_var.set(self.master_dict["POINT_SIZES"]["PRE-LAT"])
		# self.pre_sky_var.set(self.master_dict["POINT_SIZES"]["PRE-SKY"])
		# self.post_scanno_var.set(self.master_dict["POINT_SIZES"]["POST-SCANNO"])
		# self.post_ap_var.set(self.master_dict["POINT_SIZES"]["POST-AP"])
		# self.post_lat_var.set(self.master_dict["POINT_SIZES"]["POST-LAT"])
		# self.post_sky_var.set(self.master_dict["POINT_SIZES"]["POST-SKY"])

		# self.pre_scanno_var.trace('w', self.spinnerValUpdate)
		


				

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
		self.updateSpinboxes()


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


	def updateSpinboxes(self):
		self.pre_scanno_var.set(self.master_dict["POINT_SIZES"]["PRE-SCANNO"])
		self.pre_ap_var.set(self.master_dict["POINT_SIZES"]["PRE-AP"])
		self.pre_lat_var.set(self.master_dict["POINT_SIZES"]["PRE-LAT"])
		self.pre_sky_var.set(self.master_dict["POINT_SIZES"]["PRE-SKY"])
		self.post_scanno_var.set(self.master_dict["POINT_SIZES"]["POST-SCANNO"])
		self.post_ap_var.set(self.master_dict["POINT_SIZES"]["POST-AP"])
		self.post_lat_var.set(self.master_dict["POINT_SIZES"]["POST-LAT"])
		self.post_sky_var.set(self.master_dict["POINT_SIZES"]["POST-SKY"])

		# self.pre_scanno_var.trace("w", lambda name, index, mode, dict_key="PRE-SCANNO", var=self.pre_scanno_var: self.update_pointsize_dict(dict_key, var))
		# self.post_scanno_var.trace("w", lambda name, index, mode, dict_key="POST-SCANNO", var=self.post_scanno_var: self.update_pointsize_dict(dict_key, var))

		self.pre_scanno_var.trace("w", lambda name, index, mode, dict_key="PRE-SCANNO", var=self.pre_scanno_var: self.update_pointsize_dict(dict_key, var))
		self.pre_ap_var.trace("w", lambda name, index, mode, dict_key="PRE-AP", var=self.pre_ap_var: self.update_pointsize_dict(dict_key, var))
		self.pre_lat_var.trace("w", lambda name, index, mode, dict_key="PRE-LAT", var=self.pre_lat_var: self.update_pointsize_dict(dict_key, var))
		self.pre_sky_var.trace("w", lambda name, index, mode, dict_key="PRE-SKY", var=self.pre_sky_var: self.update_pointsize_dict(dict_key, var))
		self.post_scanno_var.trace("w", lambda name, index, mode, dict_key="POST-SCANNO", var=self.post_scanno_var: self.update_pointsize_dict(dict_key, var))
		self.post_ap_var.trace("w", lambda name, index, mode, dict_key="POST-AP", var=self.post_ap_var: self.update_pointsize_dict(dict_key, var))
		self.post_lat_var.trace("w", lambda name, index, mode, dict_key="POST-LAT", var=self.post_lat_var: self.update_pointsize_dict(dict_key, var))
		self.post_sky_var.trace("w", lambda name, index, mode, dict_key="POST-SKY", var=self.post_sky_var: self.update_pointsize_dict(dict_key, var))



	def update_pointsize_dict(self, dict_key, var):
		print('{} key update {}'.format(dict_key, var.get()))

		# no blank vals
		if var.get() != "":
			# try int cast
			try: 
				# make sure positive
				# and in range of 5 - 30
				int_check = int(var.get())
				# int_check = float(var.get())
				if int_check > 0 and int_check < 31:
					self.master_dict["POINT_SIZES"][dict_key] = int_check

					# pass the dictkey which is also the view(page_name) which updates all objects with new point size
					self.controller.redrawNewPointSize(dict_key)
					
					# save the new point size to disk
					self.controller.save_json()

			# int cast failed, must be text entry
			except Exception as e:
				print(e)
				# raise e
				
				


		



	