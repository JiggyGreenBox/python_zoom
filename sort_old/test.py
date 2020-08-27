# s = 5

# print("instance no {}".format(s))

# master_dict = {}

# master_dict["EXCEL"] = 	{
# 												"PRE_OP":{
# 													"RIGHT":{
# 														"HASDATA"		:False,
# 														"HKA"			:None,
# 														"MAD"			:None}}}


# print(master_dict)

# if master_dict["EXCEL"]["PRE_OP"]["RIGHT"]["HASDATA"] == False:
# 	print("make true")
# 	master_dict["EXCEL"]["PRE_OP"]["RIGHT"]["HASDATA"] = True

# if master_dict["EXCEL"]["PRE_OP"]["RIGHT"]["HASDATA"] != False:
# 	print("has become true")

# print(master_dict)

from modulefinder import ModuleFinder
finder = ModuleFinder()
finder.run_script("app.py")
for name, mod in finder.modules.items():
	print(name)