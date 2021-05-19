import tkinter as tk


from tkinter import ttk
from tkinter import *

# choose file
from tkinter import filedialog

# warning box for choose-side
from tkinter import messagebox

# get relpath
import os

# stitch images
import sys
from PIL import Image


class DETAILS_View(tk.Frame):
	def __init__(self, parent, controller, master_dict):
		tk.Frame.__init__(self, parent)
		self.controller = controller

		self.master_dict = master_dict

		
		# to avoid iteration bugs
		self.med_image = ""

		# for stitching images
		self.im1 = ""
		self.im2 = ""
		self.im_result_name = ""


		self.sex 		= tk.StringVar()
		self.sv_fname 	= tk.StringVar()
		self.sv_lname 	= tk.StringVar()
		self.sv_age 	= tk.StringVar()
		

		tk.Label(self, text="PATIENT DETAILS", font=("TkDefaultFont", 12)).grid(sticky="W", column=0, row=0, pady=(30, 10), padx=(10,0))

		tk.Label(self, text="First Name").grid(sticky="W", row=1, padx=(10,0))
		tk.Label(self, text="Last Name").grid(sticky="W", row=2, padx=(10,0))
		tk.Label(self, text="Age").grid(sticky="W", row=3, padx=(10,0))
		tk.Label(self, text="Sex").grid(sticky="W", row=4, padx=(10,0))

		self.e_fname 	= tk.Entry(self, textvariable=self.sv_fname)
		self.e_lname	= tk.Entry(self, textvariable=self.sv_lname)
		self.e_age 		= tk.Entry(self, textvariable=self.sv_age)



		self.e_fname.grid(row=1, column=1)
		self.e_lname.grid(row=2, column=1)
		self.e_age.grid(row=3, column=1)



		
		m_btn = tk.Radiobutton(self, text='M', variable=self.sex, value="M",tristatevalue="x")
		m_btn.grid(sticky="W", row=4, column=1)
		f_btn = tk.Radiobutton(self, text='F', variable=self.sex, value="F",tristatevalue="x")
		f_btn.grid(sticky="W", row=5, column=1)


		# submit_btn = ttk.Button(self, text="SAVE", command=lambda: self.save())
		# submit_btn.grid(column=0, row=6)



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

		# tk.Label(self, text="v0.4").grid(sticky="W", row=16, pady=(30,0), padx=(10,0))
		tk.Label(self, text=self.controller.app_version).grid(sticky="W", row=16, pady=(30,0), padx=(10,0))




		tk.Label(self, text="IMAGE STITCH", font=("TkDefaultFont", 12)).grid(sticky="W", column=3, row=0, pady=(30, 10), padx=(80,0), columnspan=3)
		
		btn_set_im1 = ttk.Button(self, text="IMG 1", width=10, command=lambda: self.set_stitch_images("im1"))
		btn_set_im1.grid(sticky="W", column=3, row=3, padx=(80,0))
		btn_set_im2 = ttk.Button(self, text="IMG 2", width=10, command=lambda: self.set_stitch_images("im2"))
		btn_set_im2.grid(sticky="W", column=4, row=3)
		btn_stitch 	= ttk.Button(self, text="GO", width=10, command=lambda: self.set_stitch_images("go"))
		btn_stitch.grid(sticky="W", column=5, row=3)


		btn_rot_im1 = ttk.Button(self, text="ROT 1", width=10, command=lambda: self.rotateStichImage("im1"))
		btn_rot_im1.grid(sticky="W", column=3, row=4, padx=(80,0))
		btn_rot_im2 = ttk.Button(self, text="ROT 2", width=10, command=lambda: self.rotateStichImage("im2"))
		btn_rot_im2.grid(sticky="W", column=4, row=4)

		# btn_stitch 	= ttk.Button(self, text="GO", width=10, command=lambda: self.draw_presentation_images())
		# btn_stitch.grid(sticky="W", column=5, row=3)

		# btn_go2 = ttk.Button(self, text="GO 2", width=10, command=lambda: self.draw_presentation_images())
		# btn_go2.grid(sticky="W", column=3, row=4, padx=(80,0))


		self.label1 = tk.Label(self, text="Img Name:").grid(sticky="W", column=3, row=1, padx=(80,0))
		self.img_stitch_name = tk.Entry(self)
		self.img_stitch_name.grid(sticky="W", column=3, row=2, padx=(80,0), columnspan=3)

		# self.label2 = tk.Label(self, text="No Image Selected").grid(sticky="W", column=3, row=3, padx=(10,0))

		

		# tk.Label(self, text="IMAGE EXPORT", font=("TkDefaultFont", 12)).grid(sticky="W", column=3, row=4, pady=(60, 10), padx=(10,0), columnspan=3)


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

	def callback2(self, sv):
		print(sv.get())

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

		if self.master_dict["DETAILS"]["F_NAME"] != None:
			self.sv_fname.set(self.master_dict["DETAILS"]["F_NAME"])
		if self.master_dict["DETAILS"]["L_NAME"] != None:
			self.sv_lname.set(self.master_dict["DETAILS"]["L_NAME"])
		if self.master_dict["DETAILS"]["AGE"] != None:
			self.sv_age.set(self.master_dict["DETAILS"]["AGE"])

		if self.master_dict["DETAILS"]["SEX"] != None:
			self.sex.set(self.master_dict["DETAILS"]["SEX"])

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


		# trace entrys
		self.sv_fname.trace_add("write", lambda name, index, mode, entry_type="F-NAME", var=self.sv_fname: self.entry_callback(entry_type, self.sv_fname))
		self.sv_lname.trace_add("write", lambda name, index, mode, entry_type="L-NAME", var=self.sv_lname: self.entry_callback(entry_type, self.sv_lname))
		self.sv_age.trace_add("write", lambda name, index, mode, entry_type="AGE", var=self.sv_age: self.entry_callback(entry_type, self.sv_age))


		self.sex.trace_add("write", lambda name, index, mode, var=self.sex: self.radio_callback(self.sex))



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



	def entry_callback(self, entry_type, var):
		print('{} entry_type update {}'.format(entry_type, var.get()))


		val = var.get().strip()
		if val != "":
			if entry_type == "F-NAME":
				self.master_dict["DETAILS"]["F_NAME"] = val
				self.controller.save_json()
			elif entry_type == "L-NAME":
				self.master_dict["DETAILS"]["L_NAME"] = val
				self.controller.save_json()
			elif entry_type == "AGE":
				self.master_dict["DETAILS"]["AGE"] = val
				self.controller.save_json()


	def radio_callback(self, var):

		sex = var.get().strip()

		if sex != None:
			self.master_dict["DETAILS"]["SEX"] = sex
			self.controller.save_json()

		print('radio callback {}'.format(sex))



	def set_stitch_images(self, btn_type):
		if btn_type == "im1" or btn_type == "im2":
			print("set images")


			# get image
			image = filedialog.askopenfilename(initialdir=self.controller.working_dir)

			if isinstance(image, str) and image != "":

				dir_name = os.path.dirname(image)
				rel_path = os.path.relpath(image, dir_name)

				# only allow images from the working dir
				if self.controller.working_dir != dir_name:
					print("mis-match")
					self.warningBox("Image not from working directory")
					return

				if btn_type == "im1":
					self.im1 = rel_path
				elif btn_type == "im2":
					self.im2 = rel_path

		if btn_type == "go":
			# check if images are set
			if self.im1 == "":
				self.warningBox("Image 1 Not Selected")
				return
			if self.im2 == "":
				self.warningBox("Image 2 Not Selected")
				return

			# check if result image name is set
			im_name = self.img_stitch_name.get().strip()
			im_name = self.controller.working_dir + "/" + im_name + '.jpg'
			if im_name == "":
				self.warningBox("Stitched Image-name not set")
				return


			images = [Image.open(x) for x in [(self.controller.working_dir + "/" + self.im1), (self.controller.working_dir + "/" + self.im2)]]
			# images = [Image.open(x) for x in ['post_ap.jpg','post_lat.jpg']]

			
			widths, heights = zip(*(i.size for i in images))

			total_width = sum(widths)
			max_height = max(heights)

			new_im = Image.new('RGB', (total_width, max_height))

			x_offset = 0
			for im in images:
				new_im.paste(im, (x_offset,0))
				x_offset += im.size[0]

			new_im.save(im_name)
			self.im1 = ""
			self.im2 = ""
			self.img_stitch_name.delete(0, tk.END)
			self.warningBox("Success")


	def rotateStichImage(self, btn_type):
		im_path = ""
		if btn_type == "im1":
			if self.im1 == "":
				self.warningBox("Image 1 Not Selected")
				return
			im_path = self.controller.working_dir + "/" + self.im1

		elif btn_type == "im2":
			if self.im2 == "":
				self.warningBox("Image 2 Not Selected")
				return
			im_path = self.controller.working_dir + "/" + self.im2

		if im_path != "":
			img_rt_90 = self.rotate_img(im_path, 90)
			img_rt_90.save(im_path)
			self.warningBox("Rotated 90")


	def rotate_img(self, img_path, rt_degr):
		img = Image.open(img_path)
		return img.rotate(rt_degr, expand=1)



	def warningBox(self, message):
		'''Display a warning box with message'''
		messagebox.showwarning("Warning", message)


	def draw_presentation_images(self):
		print('draw_presentation_images')
		# pass
		self.controller.app_draw_pil()


	def details_tryPsFile(self):
		print('details_tryPsFile')
		# get into the view to access canvas
		self.controller.app_tryPsFile()



	def escapeFunc(self):
		pass
	def keySetRight(self):
		pass
	def keySetLeft(self):
		pass

				
				


		



	