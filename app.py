# -*- coding: utf-8 -*-
# Advanced zoom for images of various types from small to huge up to several GB
import math
import warnings
import tkinter as tk



from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk


from views.pre_scanno_view import PRE_SCANNO_View
from views.post_scanno_view import POST_SCANNO_View
from views.pre_lat_view import PRE_LAT_View
from views.post_lat_view import POST_LAT_View
from views.pre_ap_view import PRE_AP_View
from views.post_ap_view import POST_AP_View
from views.pre_sky_view import PRE_SKY_View
from views.post_sky_view import POST_SKY_View

from views.details_view import DETAILS_View
from views.set_working_view import SET_WORKING_View


# read json file
from pathlib import Path
import json

# choose file
from tkinter import filedialog

# get relpath
import os

import pandas as pd


class MainWindow(ttk.Frame):
	""" Main window class """

	def __init__(self, mainframe):
		""" Initialize the main Frame """
		ttk.Frame.__init__(self, master=mainframe)
		self.master.title('Advanced Zoom v3.0')
		self.master.geometry('800x600')  # size of the main window
		
		self.master.grid_rowconfigure(1, weight=1) # this needed to be added
		self.master.grid_columnconfigure(0, weight=1) # as did this

		self.working_dir = ""		
		self.master_dict = {}
		self.add_image_path_masterdict()

		# used for image rotate
		# rotate call will rotate current view
		self.cur_view = ""

		# menubar for image rotate
		# can add more functionality here later
		menubar = Menu(self.master)
		filemenu = Menu(menubar,tearoff=0)
		filemenu.add_command(label="Rotate 90", command=self.rotateImage)
		filemenu.add_command(label="Reset Image", command=self.resetImage)
		filemenu.add_command(label="Export Excel", command=self.exportExcel)
		menubar.add_cascade(label="File", menu=filemenu)
		self.master.config(menu=menubar)


		# topbar
		self.topbar = Frame(self.master, height=100)				
		self.topbar.grid(row=0, column=0, sticky="nwe") # stick to the top

		# make buttons in the topbar
		for x,text in enumerate(["DETAILS","PRE-SCANNO","PRE-AP","PRE-LAT","PRE-SKY","POST-SCANNO","POST-AP","POST-LAT","POST-SKY"]):		
			button = ttk.Button(self.topbar, text=text, command=lambda text=text: self.show_view(text))
			button.grid(column=x, row=1)



		# create menus
		self.views = {}
		for V in (					
					PRE_SCANNO_View,
					POST_SCANNO_View,
					PRE_LAT_View,
					POST_LAT_View,
					PRE_AP_View,
					POST_AP_View,
					PRE_SKY_View,
					POST_SKY_View,
					DETAILS_View,
					SET_WORKING_View
				):
			page_name = V.__name__
			view = V(parent=self.master, controller=self, master_dict=self.master_dict)
			# view = V(parent=place_holder, controller=self)
			self.views[page_name] = view

			# put all of the pages in the same location;
			# the one on the top of the stacking order
			# will be the one that is visible.
			view.grid(row=1, column=0, sticky="nsew")


		if self.working_dir == "":
			self.topbar.grid_forget()
			self.show_view("SET_WORKING")
		# self.set_working_dir()

	
	def set_working_dir(self):
		self.working_dir = filedialog.askdirectory()
		print(type(self.working_dir))

		if isinstance(self.working_dir, str) and self.working_dir != "":

			self.topbar.grid(row=0, column=0, sticky="we")
			self.show_view("DETAILS")

			try:
				my_file = Path(self.working_dir + "/pat.json")
				if my_file.is_file():
					# file exists
					print("pat.json exists")

					with open(my_file) as f:
						d = json.load(f)
						self.master_dict = d
						# print(d)

				# update all dictionaries
				for view in self.views:
					self.views[view].update_dict(self.master_dict)


			except Exception as e:
				raise e

		else:
			self.show_view("SET_WORKING")


	def show_view(self, page_name):
		'''Show a view for the given page name'''
		page_name = page_name.replace("-", "_")	+ "_View"			
		view = self.views[page_name]
		self.cur_view = page_name		# store for image rotate

		if self.views[page_name].is_set_med_image():
			print("image is set")
			# pass
		else:
			try:
				self.views[page_name].open_image_loc()
			except Exception as e:
				# print(e)
				raise e
			# print("image is NOT set")

		view.tkraise()


	def save_json(self):
		# print("successfully bubbled to the top")
		# print(self.master_dict)
		print('saving json')

		with open(self.working_dir + '/pat.json', 'w', encoding='utf-8') as f:
			json.dump(self.master_dict, f, ensure_ascii=False, indent=4)


	def add_image_path_masterdict(self):
		
		if "IMAGES" not in self.master_dict.keys():
			self.master_dict["IMAGES"] = 	{
										"DETAILS":None,
										"PRE-SCANNO":None,
										"PRE-AP":None,
										"PRE-LAT":None,
										"PRE-SKY":None,
										"POST-SCANNO":None,
										"POST-AP":None,
										"POST-LAT":None,
										"POST-SKY":None
									}

		if "EXCEL" not in self.master_dict.keys():

			self.master_dict["EXCEL"] = 	{
												"PRE-OP":{
													"RIGHT":{
														"HASDATA"		:False,
														"HKA"			:None,
														"MAD"			:None,
														"MNSA"			:None,
														"VCA"			:None,
														"aFTA"			:None,
														"mLDFA"			:None,
														"aLDFA"			:None,
														"EADFA"			:None,
														"EADFPS"		:None,
														"EADFDS"		:None,
														"JDA"			:None,
														"TAMD"			:None,
														"MPTA"			:None,
														"KJLO"			:None,
														"KAOL"			:None,
														"EADTA"			:None,
														"EADTPS"		:None,
														"EADTDS"		:None,
														"FFLEX"			:None,
														"PCOR"			:None,
														"ACOR"			:None,
														"TSLOPE"		:None,
														"ISR"			:None,
														"SA"			:None,
														"PTILT"			:None,
														"PPBA"			:None,
														"MISCELL"		:None,
														"FVAR/VAL"		:None,
														"TVAR/VAL"		:None,
														"FFLE/EXT"		:None,
														"TFLE/EXT"		:None
													},
													"LEFT":{
														"HASDATA"		:False,
														"HKA"			:None,
														"MAD"			:None,
														"MNSA"			:None,
														"VCA"			:None,
														"aFTA"			:None,
														"mLDFA"			:None,
														"aLDFA"			:None,
														"EADFA"			:None,
														"EADFPS"		:None,
														"EADFDS"		:None,
														"JDA"			:None,
														"TAMD"			:None,
														"MPTA"			:None,
														"KJLO"			:None,
														"KAOL"			:None,
														"EADTA"			:None,
														"EADTPS"		:None,
														"EADTDS"		:None,
														"FFLEX"			:None,
														"PCOR"			:None,
														"ACOR"			:None,
														"TSLOPE"		:None,
														"ISR"			:None,
														"SA"			:None,
														"PTILT"			:None,
														"PPBA"			:None,
														"MISCELL"		:None,
														"FVAR/VAL"		:None,
														"TVAR/VAL"		:None,
														"FFLE/EXT"		:None,
														"TFLE/EXT"		:None
													}
												},
												"POST-OP":{
													"RIGHT":{
														"HASDATA"		:False,
														"HKA"			:None,
														"MAD"			:None,
														"MNSA"			:None,
														"VCA"			:None,
														"aFTA"			:None,
														"mLDFA"			:None,
														"aLDFA"			:None,
														"EADFA"			:None,
														"EADFPS"		:None,
														"EADFDS"		:None,
														"JDA"			:None,
														"TAMD"			:None,
														"MPTA"			:None,
														"KJLO"			:None,
														"KAOL"			:None,
														"EADTA"			:None,
														"EADTPS"		:None,
														"EADTDS"		:None,
														"FFLEX"			:None,
														"PCOR"			:None,
														"ACOR"			:None,
														"TSLOPE"		:None,
														"ISR"			:None,
														"SA"			:None,
														"PTILT"			:None,
														"PPBA"			:None,
														"MISCELL"		:None,
														"FVAR/VAL"		:None,
														"TVAR/VAL"		:None,
														"FFLE/EXT"		:None,
														"TFLE/EXT"		:None
													},
													"LEFT":{
														"HASDATA"		:False,
														"HKA"			:None,
														"MAD"			:None,
														"MNSA"			:None,
														"VCA"			:None,
														"aFTA"			:None,
														"mLDFA"			:None,
														"aLDFA"			:None,
														"EADFA"			:None,
														"EADFPS"		:None,
														"EADFDS"		:None,
														"JDA"			:None,
														"TAMD"			:None,
														"MPTA"			:None,
														"KJLO"			:None,
														"KAOL"			:None,
														"EADTA"			:None,
														"EADTPS"		:None,
														"EADTDS"		:None,
														"FFLEX"			:None,
														"PCOR"			:None,
														"ACOR"			:None,
														"TSLOPE"		:None,
														"ISR"			:None,
														"SA"			:None,
														"PTILT"			:None,
														"PPBA"			:None,
														"MISCELL"		:None,
														"FVAR/VAL"		:None,
														"TVAR/VAL"		:None,
														"FFLE/EXT"		:None,
														"TFLE/EXT"		:None
													}
												}
											}

	def rotateImage(self):
		
		# ignore these views
		# SET_WORKING_View
		# DETAILS_View
		if self.cur_view not in ('SET_WORKING_View', 'DETAILS_View'):
			# print(self.cur_view)

			# check if image is set
			img = self.views[self.cur_view].med_image
			if img != "":
				img_rt_90 = self.rotate_img(img, 90)
				img_rt_90.save(img)

				# reset the image in the current view
				self.views[self.cur_view].resetImg(img)


				# images can be shared between views
				# if shared views found reset image for shared view
				for view in self.views:
					# except cur_view check duplicate
					if self.cur_view == view: continue
					if img == self.views[view].med_image:
						print("duplicate img found for {}".format(view))
						self.views[view].resetImg(img)

	def resetImage(self):
		# ignore these views
		# SET_WORKING_View
		# DETAILS_View
		if self.cur_view not in ('SET_WORKING_View', 'DETAILS_View'):

			# check if image is set
			img = self.views[self.cur_view].med_image
			if img != "":
				print("reset image")
				self.views[self.cur_view].open_image_loc()

	def rotate_img(self, img_path, rt_degr):
		img = Image.open(img_path)
		return img.rotate(rt_degr, expand=1)



	def exportExcel(self):
		print("export")

		disp_name 	= (self.master_dict["DETAILS"]["L_NAME"] + " " + self.master_dict["DETAILS"]["F_NAME"]).upper()
		disp_age 	= self.master_dict["DETAILS"]["AGE"]
		disp_sex 	= self.master_dict["DETAILS"]["SEX"]


		name 		= []
		age 		= []
		gender 		= []
		leg_side 	= []
		k_l_grade 	= []
		mtype 		= []
		prosthesis 	= []
		hka 		= []
		mad 		= []
		mnsa 		= []
		vca 		= []
		afta 		= []
		mldfa 		= []
		aldfa 		= []
		eadfa 		= []
		eadfps 		= []
		eadfds 		= []
		jda 		= []
		tamd 		= []
		mpta 		= []
		kjlo 		= []
		kaol 		= []
		eadta 		= []
		eadtps 		= []
		eadtds 		= []
		fflex 		= []
		pcor 		= []
		acor 		= []
		tslope 		= []
		isr 		= []
		sa 			= []
		ptilt 		= []
		ppba 		= []
		miscell 	= []
		fvarval 	= []
		tvarval 	= []
		ffleext 	= []
		tfleext 	= []

		mdict = {
					"NAME"			:name,
					"AGE"			:age,
					"GENDER"		:gender,
					"SIDE"			:leg_side,
					"K-L GRADE"		:k_l_grade,
					"TYPE"			:mtype,
					"PROSTHESIS"	:prosthesis,
					"HKA"			:hka,
					"MAD"			:mad,
					"MNSA"			:mnsa,
					"VCA"			:vca,
					"aFTA"			:afta,
					"mLDFA"			:mldfa,
					"aLDFA"			:aldfa,
					"EADFA"			:eadfa,
					"EADFPS"		:eadfps,
					"EADFDS"		:eadfds,
					"JDA"			:jda,
					"TAMD"			:tamd,
					"MPTA"			:mpta,
					"KJLO"			:kjlo,
					"KAOL"			:kaol,
					"EADTA"			:eadta,
					"EADTPS"		:eadtps,
					"EADTDS"		:eadtds,
					"FFLEX"			:fflex,
					"PCOR"			:pcor,
					"ACOR"			:acor,
					"TSLOPE"		:tslope,
					"ISR"			:isr,
					"SA"			:sa,
					"PTILT"			:ptilt,
					"PPBA"			:ppba,
					"MISCELL"		:miscell,
					"FVAR/VAL"		:fvarval,
					"TVAR/VAL"		:tvarval,
					"FFLE/EXT"		:ffleext,
					"TFLE/EXT"		:tfleext
				}



		# Iterate
		for op_type in ["PRE-OP", "POST-OP"]:
			for side in ["RIGHT", "LEFT"]:

				# master list
				# m_list = []

				# data for leg exists
				# print('{} {}'.format(op_type,side))
				# print(self.master_dict["EXCEL"][op_type][side]["HASDATA"])
				if self.master_dict["EXCEL"][op_type][side]["HASDATA"] == True:

					# # local list
					# l_list = []

					# # iterate over fields
					# for obj in self.master_dict["EXCEL"][op_type][side]:

					# 	# ignore bool fields
					# 	if obj == "HASDATA": continue

					# 	if self.master_dict["EXCEL"][op_type][side][obj] == None:
					# 		l_list.append("")
					# 	else:
					# 		l_list.append(self.master_dict["EXCEL"][op_type][side][obj])
					x = ""					

					name.append(disp_name)
					age.append(disp_age)
					gender.append(disp_sex)
					leg_side.append(side[0])
					k_l_grade.append(x)
					mtype.append(x)
					prosthesis.append(x)
					hka.append(self.master_dict["EXCEL"][op_type][side]["HKA"])
					mad.append(self.master_dict["EXCEL"][op_type][side]["MAD"])
					mnsa.append(self.master_dict["EXCEL"][op_type][side]["MNSA"])
					vca.append(self.master_dict["EXCEL"][op_type][side]["VCA"])
					afta.append(self.master_dict["EXCEL"][op_type][side]["aFTA"])
					mldfa.append(self.master_dict["EXCEL"][op_type][side]["mLDFA"])
					aldfa.append(self.master_dict["EXCEL"][op_type][side]["aLDFA"])
					eadfa.append(x)
					eadfps.append(x)
					eadfds.append(x)
					jda.append(x)
					tamd.append(self.master_dict["EXCEL"][op_type][side]["TAMD"])
					mpta.append(self.master_dict["EXCEL"][op_type][side]["MPTA"])
					kjlo.append(self.master_dict["EXCEL"][op_type][side]["KJLO"])
					kaol.append(self.master_dict["EXCEL"][op_type][side]["KAOL"])
					eadta.append(x)
					eadtps.append(x)
					eadtds.append(x)
					fflex.append(x)
					pcor.append(x)
					acor.append(x)
					tslope.append(self.master_dict["EXCEL"][op_type][side]["TSLOPE"])
					isr.append(x)
					sa.append(self.master_dict["EXCEL"][op_type][side]["SA"])
					ptilt.append(self.master_dict["EXCEL"][op_type][side]["PTILT"])
					ppba.append(x)
					miscell.append(x)
					fvarval.append(x)
					tvarval.append(x)
					ffleext.append(x)
					tfleext.append(x)


# self.master_dict["EXCEL"][op_type][side]["MAD"]
# self.master_dict["EXCEL"][op_type][side]["VCA"]
# self.master_dict["EXCEL"][op_type][side]["aFTA"]

# self.master_dict["EXCEL"][op_type][side]["EADFA"]
# self.master_dict["EXCEL"][op_type][side]["EADFPS"]
# self.master_dict["EXCEL"][op_type][side]["EADFDS"]
# self.master_dict["EXCEL"][op_type][side]["JDA"]

# self.master_dict["EXCEL"][op_type][side]["EADTA"]
# self.master_dict["EXCEL"][op_type][side]["EADTPS"]
# self.master_dict["EXCEL"][op_type][side]["EADTDS"]
# self.master_dict["EXCEL"][op_type][side]["FFLEX"]
# self.master_dict["EXCEL"][op_type][side]["PCOR"]
# self.master_dict["EXCEL"][op_type][side]["ACOR"]

# self.master_dict["EXCEL"][op_type][side]["ISR"]

# self.master_dict["EXCEL"][op_type][side]["PPBA"]
# self.master_dict["EXCEL"][op_type][side]["MISCELL"]
# self.master_dict["EXCEL"][op_type][side]["FVAR/VAL"]
# self.master_dict["EXCEL"][op_type][side]["TVAR/VAL"]
# self.master_dict["EXCEL"][op_type][side]["FFLE/EXT"]
# self.master_dict["EXCEL"][op_type][side]["TFLE/EXT"]


		# print(l_list)


		df = pd.DataFrame(mdict)
		# df.fillna(value=pd.np.nan, inplace=True)
		print(df)
		excel_file = Path(self.working_dir + "/output.xlsx")
		df.to_excel(excel_file, index=False)








app = MainWindow(tk.Tk())
app.mainloop()