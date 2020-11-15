import tkinter as tk

from gui_canvas import CanvasImage

# angle import
import math

# # debug
# from itertools import count

class DrawTools(CanvasImage):
	""" Class of Polygons. Inherit CanvasImage class """

	# _ids = count(0)


	def __init__(self, placeholder, path):
		""" Initialize the Base Class """
		CanvasImage.__init__(self, placeholder, path)  # call __init__ of the CanvasImage class

		# self.id = next(self._ids)
		# self.path = path
		# print("instance no {}".format(self.id))

		# this data is used to keep track of an
		# item being dragged
		self._drag_data = {"x": 0, "y": 0, "item": None,"tags":None}
		self.cur_obj = None


		self.canvas.bind('<ButtonPress-1>', self.clickfunc)  # set new edge
		# self.canvas.bind('<ButtonPress-1>', print("clidked"))  # set new edge
		# self.canvas.bind('<Key>', self.clickfunc)  # set new edge
		self.canvas.tag_bind("token", "<ButtonPress-1>", self.drag_start)
		self.canvas.tag_bind("token", "<ButtonRelease-1>", self.drag_stop)
		self.canvas.tag_bind("token", "<B1-Motion>", self.drag)


		self.canvas.bind('<Motion>', self.hover)  # remember canvas position
		self.canvas.bind('<ButtonPress-3>', self.logme)

		self.isHover = False
		self.hover_label = ""


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
		
		# x_find = round(self.canvas.canvasx(event.x))
		# y_find = round(self.canvas.canvasy(event.y))
		x_find = self.canvas.canvasx(event.x)
		y_find = self.canvas.canvasy(event.y)
		
		if not self.outside(x_find, y_find):
			# item = self.canvas.find_closest(event.x, event.y)
			item = self.canvas.find_closest(x_find, y_find)		
			tags = self.canvas.itemcget(item, "tags")
			# print(item)
			# print(tags)
			if "token" not in tags:	
				# self.cur_obj.click(event)
				if self.cur_obj != None:
					self.cur_obj.click(event)
				# self.create_token2("red")
			else:
				print("no click")
				# self.drag_start(event)


	def clear_by_tag(self, tag):
		self.canvas.delete(tag)


	def create_token(self, event, color, mytag):
		"""Create a token at the given coordinate in the given color"""
		# x = round(self.canvas.canvasx(event.x))  # get coordinates of the event on the canvas
		# y = round(self.canvas.canvasy(event.y))
		x = self.canvas.canvasx(event.x)  # get coordinates of the event on the canvas
		y = self.canvas.canvasy(event.y)
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


	def create_mypoint(self, point, color, mytag, hover_point=False):
		"""Create a token at the given coordinate in the given color"""
		if not hover_point:
			mytag.append("token")
		p1 = self.getScaledCoords(point)
		x = p1[0]
		y = p1[1]
		thickness = 7 * self.imscale
		self.canvas.create_oval(
			x - thickness,
			y - thickness,
			x + thickness,
			y + thickness,
			outline="black",
			fill=color,
			tags=mytag,
		)
		# point
		# outline="#0a4680",			
		# fill="#1382eb",


	def create_mytext(self, point, mytext, mytag, x_offset=0, y_offset=0, color="white", font_size=8):
		"""Create a token at the given coordinate in the given color"""
		# font_size = 8
		# text='{0:.2f}'.format(t1)		
		p1 = self.getScaledCoords(point)
		x = p1[0]
		y = p1[1]
		x_off = x_offset * self.imscale
		y_off = y_offset * self.imscale
		# font_size = int(font_size/self.imscale)

		self.canvas.create_text(x+x_off, y+y_off, fill=color, text=mytext, font=("TkDefaultFont", font_size), tags=mytag)



	def create_midpoint(self, point, color, mytag):
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
			outline="black",
			fill=color,
			# tags=("mid","lines", mytag),
			tags=mytag,
		)

	def create_myline(self, point1, point2, mytag):

		p1 = self.getScaledCoords(point1)
		p2 = self.getScaledCoords(point2)

		# self.canvas.create_line(p1[0], p1[1], p2[0], p2[1], fill="red", width=2, tags=("del","lines", mytag))
		# self.canvas.create_line(p1[0], p1[1], p2[0], p2[1], fill="orange", width=2, tags=("del","lines", mytag))
		self.canvas.create_line(p1[0], p1[1], p2[0], p2[1], fill="orange", width=2, tags=mytag)


	def create_midpoint_line(self, point1, point2, mid1, mytag):

		p1 = self.getScaledCoords(point1)
		p2 = self.getScaledCoords(point2)
		m1 = self.getScaledCoords(mid1)

		# self.create_midpoint(m1,"red", mytag)
		# self.canvas.create_line(p1[0], p1[1], p2[0], p2[1], fill="red", width=2, tags=("del","lines", mytag))
		# 696969
		self.create_midpoint(m1,"#404040", mytag)
		# self.canvas.create_line(p1[0], p1[1], p2[0], p2[1], fill="orange", width=2, tags=("del","lines", mytag))
		self.canvas.create_line(p1[0], p1[1], p2[0], p2[1], fill="orange", width=2, tags=mytag)


	def midpoint(self, p1, p2):
		return ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)


	def getDistance(self, p1, p2):
		return math.hypot(p2[0] - p1[0], p2[1] - p1[1])



	def create_myAngle(self, point1, point2, point3, mytag, radius=50, width=3, outline="orange"):

		angle = self.getAnglePoints(point1, point2, point3)
		# print('angle: {}'.format(angle))

		arc_angle = self.getAnglePointsNeg(point3, point2, (self.imwidth, point2[1]))
		# print('arc_angle: {}'.format(arc_angle))
		
		# bot_left = self.getScaledCoords(((point2[0] - radius),(point2[1] - radius)))
		# top_right = self.getScaledCoords(((point2[0] + radius),(point2[1] + radius)))
		# self.canvas.create_arc(x-r, y-r, x+r, y+r, start=t0, extent=angle1, style='arc', width=width, tags="tag")
		p1 = self.getScaledCoords(point2)	
		x = p1[0]	
		y = p1[1]
		r = radius * self.imscale

		# self.canvas.create_arc(x-r, y-r, x+r, y+r, start=arc_angle, extent=angle, style='arc', width=width, tags=mytag)
		self.canvas.create_arc(x-r, y-r, x+r, y+r, start=arc_angle, extent=angle, outline=outline, width=width, tags=mytag)
		return angle


	def getAnglePoints(self, a, b, c):
		ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
		return ang + 360 if ang < 0 else ang

	def getAnglePointsNeg(self, a, b, c):
		ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
		return ang


	def getSmallestAngle(self, a, b, c):
		angle1 = self.getAnglePoints(a, b, c)
		angle2 = self.getAnglePoints(c, b, a)

		if angle1 < angle2:
			return angle1
		else:
			return angle2



	def retPointsLeftRight(self, p1, p2):
		if p1[0] < p2[0]:
			return p1, p2
		else:
			return p2, p1


	def retPointsUpDown(self, p1, p2):
		if p1[1] < p2[1]:
			return p1, p2
		else:
			return p2, p1




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
		# return int(x), int(y)
		return x, y


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
		# x1 = round((x - bbox[0]) / self.imscale)  # get real (x,y) on the image without zoom
		# y1 = round((y - bbox[1]) / self.imscale)
		x1 = (x - bbox[0]) / self.imscale  # get real (x,y) on the image without zoom
		y1 = (y - bbox[1]) / self.imscale

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

		print("drag start")

		# x_find = round(self.canvas.canvasx(event.x))
		# y_find = round(self.canvas.canvasy(event.y))
		x_find = self.canvas.canvasx(event.x)
		y_find = self.canvas.canvasy(event.y)


		self._drag_data["item"] = self.canvas.find_closest(x_find, y_find)[0]

		# self.canvas.delete("lines")
		coords = self.canvas.coords(self._drag_data["item"])
		print(coords)
		x = (coords[0] + coords[2])/2
		y = (coords[1] + coords[3])/2

		
		# self._drag_data["x"] = x_find
		# self._drag_data["y"] = y_find
		self._drag_data["x"] = x
		self._drag_data["y"] = y
		tags = list(self.canvas.gettags(self._drag_data["item"]))
		self._drag_data["tags"] = list(self.canvas.gettags(self._drag_data["item"]))
		self.cur_obj.drag_start(tags)



	def drag_stop(self, event):
		"""End drag of an object"""
		# reset the drag information
		
		# print(self._drag_data["item"])

		# tags = self.canvas.itemcget(self._drag_data["item"], "tags")		
		# tags = self.canvas.itemcget(self._drag_data["item"])	
		m = self._drag_data["tags"]

		# m = tags.split(' ')
		# m.remove('token')
		# m.remove('current')
		# print(m)

		# get real coords
		# bbox = self.canvas.coords(self.container)  # get image area
		# x1 = round((self._drag_data["x"] - bbox[0]) / self.imscale)  # get real (x,y) on the image without zoom
		# y1 = round((self._drag_data["y"] - bbox[1]) / self.imscale)		 

		# x1 = (self._drag_data["x"] - bbox[0]) / self.imscale  # get real (x,y) on the image without zoom
		# y1 = (self._drag_data["y"] - bbox[1]) / self.imscale

		# x1 = (self._drag_data["x"] - bbox[0]) / self.imscale  # get real (x,y) on the image without zoom
		# y1 = (self._drag_data["y"] - bbox[1]) / self.imscale		 
		
		# x_find = self.canvas.canvasx(event.x)
		# y_find = self.canvas.canvasy(event.y)
		

		# self.canvas.delete("main")
		# self.cur_obj.updatePosition(m,(x1, y1))
		# self.cur_obj.draw()
		self.canvas.delete("current")

		self._drag_data["item"] = None
		self._drag_data["x"] = 0
		self._drag_data["y"] = 0
		self._drag_data["tags"].clear()

		P_mouse = self.getRealCoords(event)
		self.cur_obj.drag_stop(P_mouse)



	def drag(self, event):
		"""Handle dragging of an object"""
		# x_find = round(self.canvas.canvasx(event.x))
		# y_find = round(self.canvas.canvasy(event.y))

		x_find = self.canvas.canvasx(event.x)
		y_find = self.canvas.canvasy(event.y)

		delta_x = x_find - self._drag_data["x"]
		delta_y = y_find - self._drag_data["y"]
		# move the object the appropriate amount
		self.canvas.move(self._drag_data["item"], delta_x, delta_y)
		# record the new position
		self._drag_data["x"] = x_find
		self._drag_data["y"] = y_find	

		P_mouse = self.getRealCoords(event)
		self.cur_obj.drag(P_mouse)
		# self.cur_obj.draw()



	def update_img(self, image):
		print("reached")
		self.jigjig(image)


	def hover(self, event):

		if self.cur_obj != None:
			P_mouse = self.getRealCoords(event)
			
			if self.getHoverBool() == True:

				P_stored = self.getHoverPoint()
				self.cur_obj.hover(P_mouse, P_stored, self.hover_label)
				
				# self.canvas.delete("hover_line")
				# self.create_myline(P_stored, P_mouse, "hover_line")


	def setHoverPoint(self, P):
		self.hoverPoint = P

	def getHoverPoint(self):
		try:
			return self.hoverPoint
		except Exception as e:
			return None
		

	def setHoverBool(self, hoverBool):
		if hoverBool == False:
			self.canvas.delete("hover_line")
			self.setHoverPoint(None)
			self.setHoverPointLabel(None)
		self.isHover = hoverBool

	def getHoverBool(self):
		return self.isHover

	# we pass hover information to the object
	# but the object needs a state variable to know which point is currently in use
	def setHoverPointLabel(self, label):
		self.hover_label = label

	def getHoverPointLabel(self):
		return self.hover_label

	# def __del__(self): 
	# 	print("deleted instance no {}".format(self.id))
	# 	print("deleted path {}".format(self.path))