# read json file
from pathlib import Path
import json

from copy import deepcopy

import pprint

master_dict = {}

my_file = Path("pat.json")
if my_file.is_file():
	# file exists
	print("pat.json exists")

	with open(my_file) as f:
		master_dict = json.load(f)
		# pprint.pprint(master_dict)



# local_dict = deepcopy(master_dict)
local_dict = deepcopy(master_dict["MAIN"]["PRE-OP"]["RIGHT"]["FEM_KNEE"]["P1"])

print(local_dict)