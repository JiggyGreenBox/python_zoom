

class HKA():
	"""docstring for ClassName"""
	def __init__(self, draw_tools, master_dict, controller):
		self.name = "HKA"
		self.draw_tools = draw_tools
		self.dict = master_dict
		
	def click(self, event):
		print("click from "+self.name)

	def unset(self):
		print("unset from "+self.name)		

		