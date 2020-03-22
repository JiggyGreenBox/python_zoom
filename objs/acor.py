

class ACOR():
	"""docstring for ClassName"""
	def __init__(self, draw_tools, master_dict, controller):
		self.name = "ACOR"
		self.tag = "acor"
		self.draw_tools = draw_tools
		self.dict = master_dict
		self.controller = controller
		self.side = None

	def click(self, event):
		print("click from "+self.name)

	def draw(self):

		# loop left and right
		pass




	def unset(self):
		print("unset from "+self.name)
		self.draw_tools.clear_by_tag(self.tag)