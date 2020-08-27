import pandas as pd

# read json file
from pathlib import Path
import json


# def check_pat_json():

# 	ret = None

# 	my_file = Path("pat.json")
# 	if my_file.is_file():
# 		# file exists
# 		print("pat.json exists")

# 		with open(my_file) as f:
# 			ret = json.load(f)
# 			# print(d)

# 	return ret



# master_dict = check_pat_json()

# if master_dict != None:
# 	# print(master_dict)



# 	f_name 	= master_dict["DETAILS"]["F_NAME"]
# 	l_name 	= master_dict["DETAILS"]["L_NAME"]
# 	age 	= master_dict["DETAILS"]["AGE"]
# 	sex 	= master_dict["DETAILS"]["SEX"]

# 	row1 = [f_name,l_name,age,sex]

# 	for pre and post
# 		for left right
# 			if not null
				


# 	print_dict = {"NAME":	,"AGE":,"GENDER":,"SIDE":,"K_L_GRADE":,"TYPE":,"HKA":,"MAD":,"MNSA":,}

# 	df = pd.DataFrame(row1)

# 	print(df)




name 		= []
age 		= []
gender 		= []
side 		= []
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
			"SIDE"			:side,
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


for x in range(1,10):
	name.append(x)
	age.append(x)
	gender.append(x)
	side.append(x)
	k_l_grade.append(x)
	mtype.append(x)
	prosthesis.append(x)
	hka.append(x)
	mad.append(x)
	mnsa.append(x)
	vca.append(x)
	afta.append(x)
	mldfa.append(x)
	aldfa.append(x)
	eadfa.append(x)
	eadfps.append(x)
	eadfds.append(x)
	jda.append(x)
	tamd.append(x)
	mpta.append(x)
	kjlo.append(x)
	kaol.append(x)
	eadta.append(x)
	eadtps.append(x)
	eadtds.append(x)
	fflex.append(x)
	pcor.append(x)
	acor.append(x)
	tslope.append(x)
	isr.append(x)
	sa.append(x)
	ptilt.append(x)
	ppba.append(x)
	miscell.append(x)
	fvarval.append(x)
	tvarval.append(x)
	ffleext.append(x)
	tfleext.append(x)


df = pd.DataFrame(mdict) 

print(df)




