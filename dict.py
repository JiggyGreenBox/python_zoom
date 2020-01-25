myDict = {}

myorder = ["L1","L2","L3","L4"]

counter = 0


myDict = {}
myDict["L1"] = {"type":"normal","P1":None,"P2":None}
myDict["L2"] = {"type":"midline","P1":None,"P2":None}


# print(len(myDict[myorder[counter]]))

# if myorder[counter] in myDict:
# 	print("key exists")
# else:
# 	myDict[myorder[counter]] = [1,2,3]

print(myDict)





if "MAIN" in myDict.keys():
	print("exists")
else:
	print("doesnt")


	# myDict["MAIN"] = 	{
	# 						"LEFT":	{
	# 								"HIP":		{"type":"point","P1":None},
	# 								"KNEE":		{"type":"point","P1":None},
	# 								"ANKLE":	{"type":"point","P1":None},
	# 								"AXIS_FEM":	{
	# 												"type":	"axis",
	# 												"TOP":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
	# 												"BOT":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
	# 											},
	# 								"AXIS_TIB":	{
	# 												"type":	"axis",
	# 												"TOP":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
	# 												"BOT":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
	# 											}
	# 								},
	# 						"RIGHT":{
	# 								"HIP":		{"type":"point","P1":None},
	# 								"KNEE":		{"type":"point","P1":None},
	# 								"ANKLE":	{"type":"point","P1":None},
	# 								"AXIS_FEM":	{
	# 												"type":	"axis",
	# 												"TOP":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
	# 												"BOT":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
	# 											},
	# 								"AXIS_TIB":	{
	# 												"type":	"axis",
	# 												"TOP":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
	# 												"BOT":	{"type":"midpoint","P1":None,"P2":None, "M1":None}
	# 											}
	# 								}
	# 					}



print(myDict)