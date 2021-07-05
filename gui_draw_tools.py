import tkinter as tk

from gui_canvas import CanvasImage

# angle import
import math

# # debug
# from itertools import count

# for PIL draw
from PIL import Image, ImageDraw, ImageFont

# identify mac os and flip keys
from sys import platform

# resource path
import os
import sys


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
		# self.canvas.bind('<ButtonPress-3>', self.righclickfunc)  # set new edge
		# self.canvas.bind('<ButtonPress-1>', print("clidked"))  # set new edge
		# self.canvas.bind('<Key>', self.clickfunc)  # set new edge
		self.canvas.tag_bind("token", "<ButtonPress-1>", self.drag_start)
		self.canvas.tag_bind("token", "<ButtonRelease-1>", self.drag_stop)
		self.canvas.tag_bind("token", "<B1-Motion>", self.drag)


		self.canvas.bind('<Motion>', self.hover)  # remember canvas position

		if platform == "darwin":
			# right click is btn 2 on mac
			self.canvas.bind('<ButtonPress-2>', self.righclickfunc)
		else:
			self.canvas.bind('<ButtonPress-3>', self.righclickfunc)



		self.isHover = False
		self.hover_label = ""

		# for PIL image
		self.pil_image = None
		self.pil_draw = None
		# self.pil_font = None
		# self.pil_font = ImageFont.truetype('Roboto-Medium.ttf', 30)
		self.pil_font = ImageFont.truetype(self.resource_path('Roboto-Medium.ttf'), 30)
		# self.resource_path('Roboto-Medium.ttf')
		# self.pil_font = (self.resource_path('Roboto-Medium.ttf'), 30)
		# ImageFont.load_default()


	def setObject(self, myobject):
		# print("set" + str(myobject))
		self.cur_obj = myobject



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

	def righclickfunc(self, event):
		if self.cur_obj != None:
			self.cur_obj.right_click(event)



	def clear_by_tag(self, tag):
		self.canvas.delete(tag)


	def create_token(self, event, color, mytag, point_thickness=7):
		"""Create a token at the given coordinate in the given color"""
		# x = round(self.canvas.canvasx(event.x))  # get coordinates of the event on the canvas
		# y = round(self.canvas.canvasy(event.y))
		x = self.canvas.canvasx(event.x)  # get coordinates of the event on the canvas
		y = self.canvas.canvasy(event.y)
		# print("points: "+str(x)+" "+str(y))
		# thickness = 7 * self.imscale
		thickness = point_thickness * self.imscale
		self.canvas.create_oval(
			x - thickness,
			y - thickness,
			x + thickness,
			y + thickness,
			outline=color,
			fill=color,
			tags=("token", mytag),
		)


	def create_mypoint(self, point, color, mytag, hover_point=False, point_thickness=7):
		"""Create a token at the given coordinate in the given color"""
		if not hover_point:
			mytag.append("token")
		p1 = self.getScaledCoords(point)
		x = p1[0]
		y = p1[1]
		# thickness = 7 * self.imscale
		thickness = point_thickness * self.imscale
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



	def create_midpoint(self, point, color, mytag, point_thickness=7):
		"""Create a token at the given coordinate in the given color"""
		# x = round(self.canvas.canvasx(event.x))  # get coordinates of the event on the canvas
		# y = round(self.canvas.canvasy(event.y))
		x = point[0]
		y = point[1]
		# print("points: "+str(x)+" "+str(y))
		# thickness = 7 * self.imscale
		thickness = point_thickness * self.imscale
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


	def create_midpoint_line(self, point1, point2, mid1, mytag, point_thickness=7):

		p1 = self.getScaledCoords(point1)
		p2 = self.getScaledCoords(point2)
		m1 = self.getScaledCoords(mid1)

		# self.create_midpoint(m1,"red", mytag)
		# self.canvas.create_line(p1[0], p1[1], p2[0], p2[1], fill="red", width=2, tags=("del","lines", mytag))
		# 696969
		self.create_midpoint(m1,"#404040", mytag, point_thickness)
		# self.canvas.create_line(p1[0], p1[1], p2[0], p2[1], fill="orange", width=2, tags=("del","lines", mytag))
		self.canvas.create_line(p1[0], p1[1], p2[0], p2[1], fill="orange", width=2, tags=mytag)


	def midpoint(self, p1, p2):
		return ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)


	def getDistance(self, p1, p2):
		return math.hypot(p2[0] - p1[0], p2[1] - p1[1])



	def slope(self, point1, point2):
		x1 = point1[0]
		y1 = point1[1]
		x2 = point2[0]
		y2 = point2[1]
		return (y2-y1)/(x2-x1)



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

	def retPointsUpDownList(self, p1, p2):
		if p1[1] < p2[1]:
			return p1, p2
		else:
			return (p2, p1)


	def retIsPointUp(self, p1, p2):
		if p1[1] < p2[1]:
			return True
		else:
			return False


	def retIsPointDown(self, p1, p2):
		if p1[1] > p2[1]:
			return True
		else:
			return False

	def retIsPointLeft(self, p1, p2):
		if p1[0] < p2[0]:
			return True
		else:
			return False

	def retIsPointRight(self, p1, p2):
		if p1[0] > p2[0]:
			return True
		else:
			return False





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

		if self.cur_obj != None:
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
		if self.cur_obj != None:
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
		if self.cur_obj != None:
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


	def getLineSegmentByPercentage(self, percent, p1, p2):
		# Cx = Ax * (1-t) + Bx * t
		# Cy = Ay * (1-t) + By * t

		
		# Cx = Ax * (1-t) + Bx * t
		# X = (x1*(1-percent)) + (x2*percent)
		# X = p1[0]*(1-percent) + p2[0] * percent

		# Cy = Ay * (1-t) + By * t  
		# Y = (y1*(1-percent)) + (y2*percent)
		# Y = p1[1]*(1-percent) + p2[1]*percent
		
		return (p1[0]*(1-percent) + p2[0]*percent, p1[1]*(1-percent) + p2[1]*percent)

	# def __del__(self): 
	# 	print("deleted instance no {}".format(self.id))
	# 	print("deleted path {}".format(self.path))


	# ------------------------------------------------------------------------
	# create methods for PIL drawing
	# to save for presentation mode

	# create the PIL image instance
	def createPIL(self, path):
		self.pil_image = Image.open(self.path)
		self.pil_draw = ImageDraw.Draw(self.pil_image)


	# save the image
	def savePIL(self, path):
		self.pil_image.save(path)


	# draw point
	def pil_create_mypoint(self, point, color=(255,165,0), point_thickness=7):
		x = point[0]
		y = point[1]
		self.pil_draw.ellipse(
			[x - point_thickness,
			y - point_thickness,
			x + point_thickness,
			y + point_thickness],
			fill=color,
			outline=(0,0,0)
		)
		# self.pilu_draw.ellipse(
		# 			[x2 - 7,
		# 			y2 - 7,
		# 			x2 + 7,
		# 			y2 + 7])

	# draw line
	def pil_create_myline(self, p1, p2):

		# p1 = self.getScaledCoords(point1)
		# p2 = self.getScaledCoords(point2)

		# self.canvas.create_line(p1[0], p1[1], p2[0], p2[1], fill="red", width=2, tags=("del","lines", mytag))
		# self.canvas.create_line(p1[0], p1[1], p2[0], p2[1], fill="orange", width=2, tags=("del","lines", mytag))
		self.pil_draw.line([p1[0], p1[1], p2[0], p2[1]], fill=(255,165,0), width=7)

	# draw angle
	def pil_create_myAngle(self, point1, point2, point3, radius=50, width=3, outline="orange"):
		# angle = self.getAnglePoints(point1, point2, point3)
		# # print('angle: {}'.format(angle))

		# arc_angle = self.getAnglePointsNeg(point3, point2, (self.imwidth, point2[1]))
		# # print('arc_angle: {}'.format(arc_angle))
		
		# # bot_left = self.getScaledCoords(((point2[0] - radius),(point2[1] - radius)))
		# # top_right = self.getScaledCoords(((point2[0] + radius),(point2[1] + radius)))
		# # self.canvas.create_arc(x-r, y-r, x+r, y+r, start=t0, extent=angle1, style='arc', width=width, tags="tag")
		# p1 = self.getScaledCoords(point2)	
		# x = p1[0]	
		# y = p1[1]
		# r = radius

		# # self.canvas.create_arc(x-r, y-r, x+r, y+r, start=arc_angle, extent=angle, style='arc', width=width, tags=mytag)
		# # self.canvas.create_arc(x-r, y-r, x+r, y+r, start=arc_angle, extent=angle, outline=outline, width=width, tags=mytag)
		# self.pil_draw.arc([x-r, y-r, x+r, y+r], start=arc_angle, end=angle, fill=(255,165,0), width=7)


		# angle rubbish begins
		angle1 = self.getAnglePoints(point1, point2, point3)
		angle2 = self.getAnglePoints(point3, point2, point1)
		print('angle1: {}, angle2: {}'.format(angle1, angle2))

		# co ord system begins with respect to x-axis
		# (self.imwidth, point2[1]) is horizontal X-Axis at point2

		p_arc_angle = self.getAnglePointsNeg(point3, point2, (self.imwidth,point2[1]))
		print('angle with x-axis: {}'.format(p_arc_angle))

		arc_angle = -1*p_arc_angle + angle2
		angle = -1*p_arc_angle

		print('arc_angle, angle: {} {}'.format(arc_angle, angle))

		x = point2[0]
		y = point2[1]
		r = 50

		self.pil_draw.arc([x-r, y-r, x+r, y+r], start=arc_angle, end=angle, fill=(255,165,0), width=5)

		return angle1

	# draw text
	def pil_create_mytext(self, point, mytext, x_offset=0, y_offset=0, color="white", font_size=8):

		x = point[0]
		y = point[1]
		x_off = x_offset
		y_off = y_offset
		# print('xoff: {}'.format(x_off))

		# font = ImageFont.load_default()
		# if self.pil_font == None:
			# self.pil_font = ImageFont.truetype('Roboto-Medium.ttf', 30)

		# self.canvas.create_text(x+x_off, y+y_off, fill=color, text=mytext, font=("TkDefaultFont", font_size), tags=mytag)
		self.pil_draw.text((x+x_off,y+y_off), mytext, font=self.pil_font, fill=(0,0,255,255))
		# self.pil_draw.text((x+x_off,y+y_off), mytext, font=self.pil_font, fill=(0,0,255,255),stroke_width=1, stroke_fill=(0,0,0,255))
		

	def pil_create_multiline_text(self, point, mytext, x_offset=0, y_offset=0, color=(0,0,255,255), font_size=8):

		x = point[0]		
		y = point[1]
		x_off = x_offset
		y_off = y_offset

		self.pil_draw.multiline_text((x+x_off,y+y_off), mytext, font=self.pil_font, fill=color)


	def pil_get_text_size(self, text):
		width  = self.pil_draw.textlength(text, font=self.pil_font)
		print('textlength: {}'.format(width))
		print('imscale: {}'.format(self.imscale))
		width, height = self.pil_draw.textsize(text, font=self.pil_font)
		print('width: {}'.format(width))
		return width


	def pil_get_multiline_text_size(self, text):
		
		width, height = self.pil_draw.multiline_textsize(text, font=self.pil_font)
		print('width: {}'.format(width))
		return width


	def pil_get_text_bbox(self, point, text, x_offset=0, y_offset=0):

		x = point[0]
		y = point[1]
		x_off = x_offset
		y_off = y_offset

		# x1,y1,x2,y2 = self.pil_draw.textbbox([x,y], text, font=self.pil_font)
		return self.pil_draw.textbbox((x+x_off,y+y_off), text, font=self.pil_font)

	def pil_draw_rect(self, xy, fill=(0,0,0,255), padding=0):

		xy[0] = xy[0] - padding
		xy[1] = xy[1] - padding
		xy[2] = xy[2] + padding
		xy[3] = xy[3] + padding

		self.pil_draw.rectangle(xy, fill=fill)

	# required when images are of low resolution
	def changePILfontsize(self, newfontsize):
		self.pil_font = ImageFont.truetype('Roboto-Medium.ttf', newfontsize)



	# ps file attempt
	def my_postscript(self, path):
		self.canvas.postscript(file=path, colormode='color')

	# returns adjusted but with L R  
	def get_yaxis_adjusted_points(self, point1, point2):

		point1 = list(point1)
		# print(point1)
		# print(type(point1))

		# print(point2)
		# print(type(point2))

		point2 = list(point2)

		U, D = self.retPointsUpDownList(point1, point2)

		ydiff = (D[1] - U[1])/2

		U[1] = U[1] + ydiff

		D[1] = D[1] - ydiff

		return self.retPointsLeftRight(U, D)

	def get_yaxis_midpoint(self, point1, point2):

		U, D = self.retPointsUpDown(point1, point2)

		ydiff = (D[1] - U[1])/2

		return ydiff

	# for fonts
	def resource_path(self, relative_path):
		try:
			base_path = sys._MEIPASS
		except Exception:
			base_path = os.path.abspath(".")

		return os.path.join(base_path, relative_path)






