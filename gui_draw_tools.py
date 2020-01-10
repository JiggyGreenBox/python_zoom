import tkinter as tk

from gui_canvas import CanvasImage

class DrawTools(CanvasImage):
	""" Class of Polygons. Inherit CanvasImage class """
	def __init__(self, placeholder, path):
		""" Initialize the Polygons """
		CanvasImage.__init__(self, placeholder, path)  # call __init__ of the CanvasImage class

		# this data is used to keep track of an
		# item being dragged
		self._drag_data = {"x": 0, "y": 0, "item": None}
		self.cur_obj = None


		self.canvas.bind('<ButtonPress-1>', self.clickfunc)  # set new edge
		self.canvas.tag_bind("token", "<ButtonPress-1>", self.drag_start)
		self.canvas.tag_bind("token", "<ButtonRelease-1>", self.drag_stop)
		self.canvas.tag_bind("token", "<B1-Motion>", self.drag)

		self.canvas.bind('<ButtonPress-3>', self.logme)


	def setObject(self, myobject):
		# print("set" + str(myobject))
		self.cur_obj = myobject


	def logme(self, event):
		# print("set" + str(myobject))
		obj = self.canvas.find_withtag("token")
		for o in obj:
			print(self.canvas.coords(o))

	def clickfunc(self, event):
	
		x_find = round(self.canvas.canvasx(event.x))
		y_find = round(self.canvas.canvasy(event.y))
		
		if not self.outside(x_find, y_find):
			# item = self.canvas.find_closest(event.x, event.y)
			item = self.canvas.find_closest(x_find, y_find)		
			tags = self.canvas.itemcget(item, "tags")
			print(item)
			print(tags)
			if "token" not in tags:	
				# self.cur_obj.click(event)
				if self.cur_obj != None:
					self.cur_obj.click(event)
				# self.create_token2("red")
			else:
				print("no click")


	def create_token(self, event, color):
		"""Create a token at the given coordinate in the given color"""
		x = round(self.canvas.canvasx(event.x))  # get coordinates of the event on the canvas
		y = round(self.canvas.canvasy(event.y))
		print("points: "+str(x)+" "+str(y))
		thickness = 7 * self.imscale
		self.canvas.create_oval(
			x - thickness,
			y - thickness,
			x + thickness,
			y + thickness,
			outline=color,
			fill=color,
			tags=("token",),
		)


	def drag_start(self, event):
		"""Begining drag of an object"""
		# record the item and its location

		# print("drag")

		x_find = round(self.canvas.canvasx(event.x))
		y_find = round(self.canvas.canvasy(event.y))


		# self._drag_data["item"] = self.canvas.find_closest(event.x, event.y)[0]
		# self._drag_data["x"] = event.x
		# self._drag_data["y"] = event.y

		self._drag_data["item"] = self.canvas.find_closest(x_find, y_find)[0]
		self._drag_data["x"] = x_find
		self._drag_data["y"] = y_find

	def drag_stop(self, event):
		"""End drag of an object"""
		# reset the drag information
		self._drag_data["item"] = None
		self._drag_data["x"] = 0
		self._drag_data["y"] = 0		


	def drag(self, event):
		"""Handle dragging of an object"""
		# compute how much the mouse has moved
		# delta_x = event.x - self._drag_data["x"]
		# delta_y = event.y - self._drag_data["y"]
		# # move the object the appropriate amount
		# self.canvas.move(self._drag_data["item"], delta_x, delta_y)
		# # record the new position
		# self._drag_data["x"] = event.x
		# self._drag_data["y"] = event.y


		x_find = round(self.canvas.canvasx(event.x))
		y_find = round(self.canvas.canvasy(event.y))

		delta_x = x_find - self._drag_data["x"]
		delta_y = y_find - self._drag_data["y"]
		# move the object the appropriate amount
		self.canvas.move(self._drag_data["item"], delta_x, delta_y)
		# record the new position
		self._drag_data["x"] = x_find
		self._drag_data["y"] = y_find		