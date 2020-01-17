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
		# xtop, ytop, xbot, ybot = self.getImageCorners()
		print(self.imwidth, self.imheight)

		# self.create_midpoint(xtop, "red")
		# self.create_midpoint(ytop, "red")
		# self.create_midpoint(xbot, "red")
		# self.create_midpoint(ybot, "red")

		# obj = self.canvas.find_withtag("token")
		# for o in obj:
		# 	print(self.canvas.coords(o))

	def clickfunc(self, event):
		
		x_find = round(self.canvas.canvasx(event.x))
		y_find = round(self.canvas.canvasy(event.y))
		
		if not self.outside(x_find, y_find):
			# item = self.canvas.find_closest(event.x, event.y)
			item = self.canvas.find_closest(x_find, y_find)		
			tags = self.canvas.itemcget(item, "tags")
			# print(item)
			print(tags)
			if "token" not in tags:	
				# self.cur_obj.click(event)
				if self.cur_obj != None:
					self.cur_obj.click(event)
				# self.create_token2("red")
			else:
				print("no click")


	def create_token(self, event, color, mytag):
		"""Create a token at the given coordinate in the given color"""
		x = round(self.canvas.canvasx(event.x))  # get coordinates of the event on the canvas
		y = round(self.canvas.canvasy(event.y))
		# print("points: "+str(x)+" "+str(y))
		thickness = 7 * self.imscale
		self.canvas.create_oval(
			x - thickness,
			y - thickness,
			x + thickness,
			y + thickness,
			outline=color,
			fill=color,
			tags=("token", mytag),
		)


	def create_midpoint(self, point, color):
		"""Create a token at the given coordinate in the given color"""
		# x = round(self.canvas.canvasx(event.x))  # get coordinates of the event on the canvas
		# y = round(self.canvas.canvasy(event.y))
		x = point[0]
		y = point[1]
		# print("points: "+str(x)+" "+str(y))
		thickness = 7 * self.imscale
		self.canvas.create_oval(
			x - thickness,
			y - thickness,
			x + thickness,
			y + thickness,
			outline=color,
			fill=color,
			tags=("mid","lines"),
		)

	def create_myline(self, point1, point2):

		p1 = self.getScaledCoords(point1)
		p2 = self.getScaledCoords(point2)

		self.canvas.create_line(p1[0], p1[1], p2[0], p2[1], fill="red",width=2, tags=("del","lines"))


	def create_midpoint_line(self, point1, point2, mid1):

		p1 = self.getScaledCoords(point1)
		p2 = self.getScaledCoords(point2)
		m1 = self.getScaledCoords(mid1)

		self.create_midpoint(m1,"red")
		self.canvas.create_line(p1[0], p1[1], p2[0], p2[1], fill="red",width=2, tags=("del","lines"))


	def midpoint(self, p1, p2):
		return ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)


	def line_intersection(self, line1, line2):
		xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
		ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

		def det(a, b):
			return a[0] * b[1] - a[1] * b[0]

		div = det(xdiff, ydiff)
		if div == 0:
			raise Exception('lines do not intersect')

		d = (det(*line1), det(*line2))
		x = det(d, xdiff) / div
		y = det(d, ydiff) / div
		return int(x), int(y)


	def getImageCorners(self):
		"""get all corners of the image, used for ray calculations"""
		# box_image = self.canvas.coords(self.container)
		# box_img_int = tuple(map(int, box_image))		
		# return (box_img_int[0], box_img_int[1]), (box_img_int[2], box_img_int[1]), (box_img_int[0], box_img_int[3]), (box_img_int[2], box_img_int[3])

		return (0, 0), (self.imwidth, 0), (0, self.imheight), (self.imwidth, self.imheight)


	def getRealCoords(self, event):		
		"""scale and pan invariant coords"""
		x = self.canvas.canvasx(event.x)  # get coordinates of the event on the canvas
		y = self.canvas.canvasy(event.y)

		bbox = self.canvas.coords(self.container)  # get image area
		x1 = round((x - bbox[0]) / self.imscale)  # get real (x,y) on the image without zoom
		y1 = round((y - bbox[1]) / self.imscale)

		return (x1, y1)


	def getScaledCoords(self, point):		
		"""scale and pan invariant coords"""
		bbox = self.canvas.coords(self.container)  # get image area
		x = point[0] * self.imscale + bbox[0]
		y = point[1] * self.imscale + bbox[1]
		return (x, y)
			
	def drag_start(self, event):
		"""Begining drag of an object"""
		# record the item and its location
		x_find = round(self.canvas.canvasx(event.x))
		y_find = round(self.canvas.canvasy(event.y))

		self.canvas.delete("lines")

		self._drag_data["item"] = self.canvas.find_closest(x_find, y_find)[0]
		self._drag_data["x"] = x_find
		self._drag_data["y"] = y_find

	def drag_stop(self, event):
		"""End drag of an object"""
		# reset the drag information
		
		tags = self.canvas.itemcget(self._drag_data["item"], "tags")		
		m = tags.split(' ')
		m.remove('token')
		m.remove('current')
		print(m)

		# get real coords
		bbox = self.canvas.coords(self.container)  # get image area
		x1 = round((self._drag_data["x"] - bbox[0]) / self.imscale)  # get real (x,y) on the image without zoom
		y1 = round((self._drag_data["y"] - bbox[1]) / self.imscale)		 

		# x1 = (self._drag_data["x"] - bbox[0]) / self.imscale  # get real (x,y) on the image without zoom
		# y1 = (self._drag_data["y"] - bbox[1]) / self.imscale		 
		

		self.cur_obj.updateDict(m[0],(x1, y1))

		self.cur_obj.drawLines()

		self._drag_data["item"] = None
		self._drag_data["x"] = 0
		self._drag_data["y"] = 0


	def drag(self, event):
		"""Handle dragging of an object"""
		x_find = round(self.canvas.canvasx(event.x))
		y_find = round(self.canvas.canvasy(event.y))

		delta_x = x_find - self._drag_data["x"]
		delta_y = y_find - self._drag_data["y"]
		# move the object the appropriate amount
		self.canvas.move(self._drag_data["item"], delta_x, delta_y)
		# record the new position
		self._drag_data["x"] = x_find
		self._drag_data["y"] = y_find		