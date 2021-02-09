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
		# self.master.geometry('800x600')  # size of the main window
		self.master.geometry('900x700')  # size of the main window
		
		self.master.grid_rowconfigure(1, weight=1) # this needed to be added
		self.master.grid_columnconfigure(0, weight=1) # as did this

		self.master.bind('<Escape>', lambda event: self.master.after_idle(self.key_funct, event))

		# check for user prefs, if not found create user_prefs.json
		self.point_size_obj = "" 	# store json data view-wise of point sizes
		self.check_user_prefs()

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


		# remove for production
		# self.debugSetDir()

		if self.working_dir == "":
			self.topbar.grid_forget()
			self.show_view("SET_WORKING")
		# self.set_working_dir()


	# only escape key for now
	def key_funct(self, event):
		print("key press {}".format(event.keycode))
		if self.cur_view != "":
			self.views[self.cur_view].escapeFunc()
		

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


	def check_user_prefs(self):
		script_dir = os.path.dirname(os.path.realpath(__file__))
		file_prefs = Path(script_dir + "/user_prefs.json")

		
		try:
			# check if exists
			if file_prefs.is_file():
				print('exists')
				with open(file_prefs) as f:
					self.point_size_obj = json.load(f)
					print(self.point_size_obj)


			# create if not found
			else:				
				user_json = {}
				if "POINT_SIZES" not in user_json.keys():
					user_json["POINT_SIZES"] = 	{
												"PRE-SCANNO":7,
												"PRE-AP":7,
												"PRE-LAT":7,
												"PRE-SKY":7,
												"POST-SCANNO":7,
												"POST-AP":7,
												"POST-LAT":7,
												"POST-SKY":7
											}

				with open(script_dir + '/user_prefs.json', 'w', encoding='utf-8') as f:
					json.dump(user_json, f, ensure_ascii=False, indent=4)

				self.point_size_obj = json.loads(json.dumps(user_json))
				print(self.point_size_obj)


		except Exception as e:
			print(e)
			raise e
		



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


		if "POINT_SIZES" not in self.master_dict.keys():

			print('point val is {}'.format(self.point_size_obj["POINT_SIZES"]["PRE-SCANNO"]))

			if self.point_size_obj != "":
				self.master_dict["POINT_SIZES"] = 	{
											"PRE-SCANNO":	self.point_size_obj["POINT_SIZES"]["PRE-SCANNO"],
											"PRE-AP":		self.point_size_obj["POINT_SIZES"]["PRE-AP"],
											"PRE-LAT":		self.point_size_obj["POINT_SIZES"]["PRE-LAT"],
											"PRE-SKY":		self.point_size_obj["POINT_SIZES"]["PRE-SKY"],
											"POST-SCANNO":	self.point_size_obj["POINT_SIZES"]["POST-SCANNO"],
											"POST-AP":		self.point_size_obj["POINT_SIZES"]["POST-AP"],
											"POST-LAT":		self.point_size_obj["POINT_SIZES"]["POST-LAT"],
											"POST-SKY":		self.point_size_obj["POINT_SIZES"]["POST-SKY"]
										}
			else:				
				self.master_dict["POINT_SIZES"] = 	{
											"PRE-SCANNO":None,
											"PRE-AP":None,
											"PRE-LAT":None,
											"PRE-SKY":None,
											"POST-SCANNO":None,
											"POST-AP":None,
											"POST-LAT":None,
											"POST-SKY":None
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

		# prevent export before folder is selected
		# self.working_dir = ""
		# if self.cur_view == "SET_WORKING_View":
		if self.working_dir == "":			
			print('empty')
			return		

		# handle no name information case		
		l_name 		= ""
		f_name 		= ""
		disp_age 	= ""
		disp_sex 	= ""
		# "DETAILS": {
		#         "F_NAME": "kim",
		#         "L_NAME": "jong",
		#         "AGE": "45",
		#         "SEX": "M"
	
		# NAME
		if self.master_dict["DETAILS"]["L_NAME"] != None:
			l_name = self.master_dict["DETAILS"]["L_NAME"]
		else:
			print("lname not fpund")
		if self.master_dict["DETAILS"]["F_NAME"] != None:
			f_name = self.master_dict["DETAILS"]["F_NAME"]
		else:
			print("fname not fpund")
		disp_name 	= (l_name + " " + f_name).upper()
		print('disp_name = {}'.format(disp_name))

		# AGE
		if self.master_dict["DETAILS"]["AGE"] != None:
			disp_age = self.master_dict["DETAILS"]["AGE"]
		# SEX
		if self.master_dict["DETAILS"]["SEX"] != None:
			disp_sex = self.master_dict["DETAILS"]["SEX"]

		'''
		l_name = self.master_dict["DETAILS"]["L_NAME"]
		f_name = self.master_dict["DETAILS"]["F_NAME"]
		disp_name 	= (l_name + " " + f_name).upper()
		print('disp_name = {}'.format(disp_name))
		disp_age = self.master_dict["DETAILS"]["AGE"]		
		disp_sex = self.master_dict["DETAILS"]["SEX"]
		'''


		name 		= []
		age 		= []
		gender 		= []
		leg_side 	= []
		k_l_grade 	= []
		mdate 		= []
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
		post_hka	= []
		post_mad 	= []
		post_mnsa 	= []
		post_vca 	= []
		post_afta 	= []
		post_mldfa 	= []
		post_aldfa 	= []
		post_eadfa 	= []
		post_eadfps = []
		post_eadfds = []
		post_jda 	= []
		post_tamd 	= []
		post_mpta 	= []
		post_kjlo 	= []
		post_kaol 	= []
		post_eadta 	= []
		post_eadtps = []
		post_eadtds = []
		post_fflex  = []
		post_pcor 	= []
		post_acor 	= []
		post_tslope = []
		post_isr 	= []
		post_sa 	= []
		post_ptilt 	= []
		post_ppba 	= []
		post_miscel = []
		fvarval 	= []
		tvarval 	= []
		ffleext 	= []
		tfleext 	= []

		mdict = {
					"NAME"			:	name,
					"AGE"			:	age,
					"GENDER"		:	gender,
					"SIDE"			:	leg_side,
					"K-L GRADE"		:	k_l_grade,
					"DATE"			:	mdate,
					"PROSTHESIS"	:	prosthesis,
					"HKA"			:	hka,
					"MAD"			:	mad,
					"MNSA"			:	mnsa,
					"VCA"			:	vca,
					"aFTA"			:	afta,
					"mLDFA"			:	mldfa,
					"aLDFA"			:	aldfa,
					"EADFA"			:	eadfa,
					"EADFPS"		:	eadfps,
					"EADFDS"		:	eadfds,
					"JDA"			:	jda,
					"TAMD"			:	tamd,
					"MPTA"			:	mpta,
					"KJLO"			:	kjlo,
					"KAOL"			:	kaol,
					"EADTA"			:	eadta,
					"EADTPS"		:	eadtps,
					"EADTDS"		:	eadtds,
					"FFLEX"			:	fflex,
					"PCOR"			:	pcor,
					"ACOR"			:	acor,
					"TSLOPE"		:	tslope,
					"ISR"			:	isr,
					"SA"			:	sa,
					"PTILT"			:	ptilt,
					"PPBA"			:	ppba,
					"MISCELL"		:	miscell,
					"Post-HKA"		:	post_hka,
					"Post-MAD"		:	post_mad,
					"Post-MNSA"		:	post_mnsa,
					"Post-VCA"		:	post_vca,
					"Post-aFTA"		:	post_afta,
					"Post-mLDFA"	:	post_mldfa,
					"Post-aLDFA"	:	post_aldfa,
					"Post-EADFA"	:	post_eadfa,
					"Post-EADFPS"	:	post_eadfps,
					"Post-EADFDS"	:	post_eadfds,
					"Post-JDA"		:	post_jda,
					"Post-TAMD"		:	post_tamd,
					"Post-MPTA"		:	post_mpta,
					"Post-KJLO"		:	post_kjlo,
					"Post-KAOL"		:	post_kaol,
					"Post-EADTA"	:	post_eadta,
					"Post-EADTPS"	:	post_eadtps,
					"Post-EADTDS"	:	post_eadtds,
					"Post-FFLEX	"	:	post_fflex,
					"Post-PCOR"		:	post_pcor,
					"Post-ACOR"		:	post_acor,
					"Post-TSLOPE"	:	post_tslope,
					"Post-ISR"		:	post_isr,
					"Post-SA"		:	post_sa,
					"Post-PTILT"	:	post_ptilt,
					"Post-PPBA"		:	post_ppba,
					"Post-MISCELL"	:	post_miscel,
					"Post-F FLE/EXT"	:	ffleext,
					"Post-F VAR/VAL"	:	fvarval,
					"Post-T FLE/EXT"	:	tfleext,
					"Post-T VAR/VAL"	:	tvarval
				}



		# Iterate
		# for op_type in ["PRE-OP", "POST-OP"]:
		for side in ["RIGHT", "LEFT"]:

			# master list				
			# if self.master_dict["EXCEL"][op_type][side]["HASDATA"] == True:


			x = ""					

			name.append(disp_name)
			age.append(disp_age)
			gender.append(disp_sex)
			leg_side.append(side[0])
			k_l_grade.append(x)
			mdate.append(x)
			prosthesis.append(x)
			hka.append(self.master_dict["EXCEL"]["PRE-OP"][side]["HKA"])
			mad.append(self.master_dict["EXCEL"]["PRE-OP"][side]["MAD"])
			mnsa.append(self.master_dict["EXCEL"]["PRE-OP"][side]["MNSA"])
			vca.append(self.master_dict["EXCEL"]["PRE-OP"][side]["VCA"])
			afta.append(self.master_dict["EXCEL"]["PRE-OP"][side]["aFTA"])
			mldfa.append(self.master_dict["EXCEL"]["PRE-OP"][side]["mLDFA"])
			aldfa.append(self.master_dict["EXCEL"]["PRE-OP"][side]["aLDFA"])
			eadfa.append(x)
			eadfps.append(x)
			eadfds.append(x)
			jda.append(x)
			tamd.append(self.master_dict["EXCEL"]["PRE-OP"][side]["TAMD"])
			mpta.append(self.master_dict["EXCEL"]["PRE-OP"][side]["MPTA"])
			kjlo.append(self.master_dict["EXCEL"]["PRE-OP"][side]["KJLO"])
			kaol.append(self.master_dict["EXCEL"]["PRE-OP"][side]["KAOL"])
			eadta.append(x)
			eadtps.append(x)
			eadtds.append(x)
			fflex.append(self.master_dict["EXCEL"]["PRE-OP"][side]["FFLEX"])
			pcor.append(self.master_dict["EXCEL"]["PRE-OP"][side]["PCOR"])
			acor.append(self.master_dict["EXCEL"]["PRE-OP"][side]["ACOR"])
			tslope.append(self.master_dict["EXCEL"]["PRE-OP"][side]["TSLOPE"])
			isr.append(self.master_dict["EXCEL"]["PRE-OP"][side]["ISR"])
			sa.append(self.master_dict["EXCEL"]["PRE-OP"][side]["SA"])
			ptilt.append(self.master_dict["EXCEL"]["PRE-OP"][side]["PTILT"])
			ppba.append(self.master_dict["EXCEL"]["PRE-OP"][side]["PPBA"])
			miscell.append(x)

			
			post_hka.append(self.master_dict["EXCEL"]["POST-OP"][side]["HKA"])
			post_mad.append(x)
			post_mnsa.append(self.master_dict["EXCEL"]["POST-OP"][side]["MNSA"])
			post_vca.append(self.master_dict["EXCEL"]["POST-OP"][side]["VCA"])
			post_afta.append(self.master_dict["EXCEL"]["POST-OP"][side]["aFTA"])
			post_mldfa.append(self.master_dict["EXCEL"]["POST-OP"][side]["mLDFA"])
			post_aldfa.append(self.master_dict["EXCEL"]["POST-OP"][side]["aLDFA"])
			post_eadfa.append(x)
			post_eadfps.append(x)
			post_eadfds.append(x)
			post_jda.append(x)
			post_tamd.append(self.master_dict["EXCEL"]["POST-OP"][side]["TAMD"])
			post_mpta.append(self.master_dict["EXCEL"]["POST-OP"][side]["MPTA"])
			post_kjlo.append(self.master_dict["EXCEL"]["POST-OP"][side]["KJLO"])
			post_kaol.append(self.master_dict["EXCEL"]["POST-OP"][side]["KAOL"])
			post_eadta.append(x)
			post_eadtps.append(x)
			post_eadtds.append(x)
			post_fflex.append(self.master_dict["EXCEL"]["POST-OP"][side]["FFLEX"])
			post_pcor.append(self.master_dict["EXCEL"]["POST-OP"][side]["PCOR"])
			post_acor.append(self.master_dict["EXCEL"]["POST-OP"][side]["ACOR"])
			post_tslope.append(self.master_dict["EXCEL"]["POST-OP"][side]["TSLOPE"])
			post_isr.append(self.master_dict["EXCEL"]["POST-OP"][side]["ISR"])
			post_sa.append(self.master_dict["EXCEL"]["POST-OP"][side]["SA"])
			post_ptilt.append(self.master_dict["EXCEL"]["POST-OP"][side]["PTILT"])
			post_ppba.append(self.master_dict["EXCEL"]["POST-OP"][side]["PPBA"])
			post_miscel.append(x)

			fvarval.append(self.master_dict["EXCEL"]["POST-OP"][side]["FVAR/VAL"])
			tvarval.append(self.master_dict["EXCEL"]["POST-OP"][side]["TVAR/VAL"])
			ffleext.append(self.master_dict["EXCEL"]["POST-OP"][side]["FFLE/EXT"])
			tfleext.append(self.master_dict["EXCEL"]["POST-OP"][side]["TFLE/EXT"])

			



		# print(mtype)


		df = pd.DataFrame(mdict)
		# df.fillna(value=pd.np.nan, inplace=True)
		print(df)
		if not df.empty:
			excel_file = Path(self.working_dir + "/output.xlsx")
			df.to_excel(excel_file, index=False)


	def debugSetDir(self):

		self.working_dir = "/home/jiggy/Desktop/kim_jong"

		my_file = "/home/jiggy/Desktop/kim_jong/pat.json"


		with open(my_file) as f:
			d = json.load(f)
			self.master_dict = d						

		# update all dictionaries
		for view in self.views:
			self.views[view].update_dict(self.master_dict)


	def redrawNewPointSize(self, page_name):

		page_name = page_name.replace("-", "_")	+ "_View"			
		view = self.views[page_name]
		
		view.resizeRedraw()		


app = MainWindow(tk.Tk())
app.mainloop()