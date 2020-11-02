import tkinter as tk     # python 3
# import Tkinter as tk   # python 2

class Example(tk.Frame):
	"""Illustrate how to drag items on a Tkinter canvas"""

	def __init__(self, parent):
		tk.Frame.__init__(self, parent)

		# create a canvas
		self.canvas = tk.Canvas(width=400, height=400, background="bisque")
		self.canvas.pack(fill="both", expand=True)

		# this data is used to keep track of an
		# item being dragged
		self._drag_data = {"x": 0, "y": 0, "item": None}

		# create a couple of movable objects
		self.create_token(100, 100, "white")
		self.create_token(200, 100, "black")

		# add bindings for clicking, dragging and releasing over
		# any object with the "token" tag
		self.canvas.tag_bind("token", "<ButtonPress-1>", self.drag_start)
		self.canvas.tag_bind("token", "<ButtonRelease-1>", self.drag_stop)
		self.canvas.tag_bind("token", "<B1-Motion>", self.drag)

		self.canvas.bind('<ButtonPress-1>', self.jiggy_click)  # remember canvas position

	def create_token(self, x, y, color):
		"""Create a token at the given coordinate in the given color"""
		thickness = 7
		self.canvas.create_oval(
			x - thickness,
			y - thickness,
			x + thickness,
			y + thickness,
			outline=color,
			fill=color,
			tags=("token","abcd"),
		)

	def drag_start(self, event):
		"""Begining drag of an object"""
		# record the item and its location
		self._drag_data["item"] = self.canvas.find_closest(event.x, event.y)[0]
		self._drag_data["x"] = event.x
		self._drag_data["y"] = event.y

	def drag_stop(self, event):
		"""End drag of an object"""
		# reset the drag information
		self._drag_data["item"] = None
		self._drag_data["x"] = 0
		self._drag_data["y"] = 0


	def jiggy_click(self, event):
		item = self.canvas.find_closest(event.x, event.y)
		tags = self.canvas.itemcget(item, "tags")
		# print(item)
		if "current" not in tags:		
			x = self.canvas.canvasx(event.x)  # get coordinates of the event on the canvas
			y = self.canvas.canvasy(event.y)
			self.create_token(x, y, "red")

	def drag(self, event):
		"""Handle dragging of an object"""
		# compute how much the mouse has moved
		delta_x = event.x - self._drag_data["x"]
		delta_y = event.y - self._drag_data["y"]
		# move the object the appropriate amount
		self.canvas.move(self._drag_data["item"], delta_x, delta_y)
		# record the new position
		self._drag_data["x"] = event.x
		self._drag_data["y"] = event.y

if __name__ == "__main__":
	root = tk.Tk()
	Example(root).pack(fill="both", expand=True)
	root.mainloop()