# -*- coding: utf-8 -*-
# Advanced zoom for images of various types from small to huge up to several GB
import math
import warnings
import tkinter as tk

from tkinter import ttk
from PIL import Image, ImageTk

# angle import
import math
point_counter = 0
point_list = []

class AutoScrollbar(ttk.Scrollbar):
	""" A scrollbar that hides itself if it's not needed. Works only for grid geometry manager """
	def set(self, lo, hi):
		if float(lo) <= 0.0 and float(hi) >= 1.0:
			self.grid_remove()
		else:
			self.grid()
			ttk.Scrollbar.set(self, lo, hi)

	def pack(self, **kw):
		raise tk.TclError('Cannot use pack with the widget ' + self.__class__.__name__)

	def place(self, **kw):
		raise tk.TclError('Cannot use place with the widget ' + self.__class__.__name__)

class CanvasImage:
	""" Display and zoom image """
	def __init__(self, placeholder, path):
		""" Initialize the ImageFrame """
		self.imscale = 1.0  # scale for the canvas image zoom, public for outer classes
		self.__delta = 1.3  # zoom magnitude
		self.__filter = Image.ANTIALIAS  # could be: NEAREST, BILINEAR, BICUBIC and ANTIALIAS
		self.__previous_state = 0  # previous state of the keyboard
		self.path = path  # path to the image, should be public for outer classes
		# Create ImageFrame in placeholder widget
		self.__imframe = ttk.Frame(placeholder)  # placeholder of the ImageFrame object
		# Vertical and horizontal scrollbars for canvas
		hbar = AutoScrollbar(self.__imframe, orient='horizontal')
		vbar = AutoScrollbar(self.__imframe, orient='vertical')
		hbar.grid(row=1, column=0, sticky='we')
		vbar.grid(row=0, column=1, sticky='ns')
		# Create canvas and bind it with scrollbars. Public for outer classes
		self.canvas = tk.Canvas(self.__imframe, highlightthickness=0,
								xscrollcommand=hbar.set, yscrollcommand=vbar.set)
		self.canvas.grid(row=0, column=0, sticky='nswe')
		self.canvas.update()  # wait till canvas is created
		hbar.configure(command=self.__scroll_x)  # bind scrollbars to the canvas
		vbar.configure(command=self.__scroll_y)
		# Bind events to the Canvas
		self.canvas.bind('<Configure>', lambda event: self.__show_image())  # canvas is resized
		self.canvas.bind('<ButtonPress-1>', self.jiggy_click)  # remember canvas position
		self.canvas.bind('<ButtonPress-2>', self.__move_from)  # remember canvas position
		self.canvas.bind('<ButtonPress-3>', self.jiggy)  # remember canvas position
		self.canvas.bind('<B2-Motion>',     self.__move_to)  # move canvas to the new position
		self.canvas.bind('<MouseWheel>', self.__wheel)  # zoom for Windows and MacOS, but not Linux
		self.canvas.bind('<Button-5>',   self.__wheel)  # zoom for Linux, wheel scroll down
		self.canvas.bind('<Button-4>',   self.__wheel)  # zoom for Linux, wheel scroll up
		# Handle keystrokes in idle mode, because program slows down on a weak computers,
		# when too many key stroke events in the same time
		self.canvas.bind('<Key>', lambda event: self.canvas.after_idle(self.__keystroke, event))
		# Decide if this image huge or not
		self.__huge = False  # huge or not
		self.__huge_size = 14000  # define size of the huge image
		self.__band_width = 1024  # width of the tile band
		Image.MAX_IMAGE_PIXELS = 1000000000  # suppress DecompressionBombError for the big image
		with warnings.catch_warnings():  # suppress DecompressionBombWarning
			warnings.simplefilter('ignore')
			self.__image = Image.open(self.path)  # open image, but down't load it
		self.imwidth, self.imheight = self.__image.size  # public for outer classes
		if self.imwidth * self.imheight > self.__huge_size * self.__huge_size and \
		   self.__image.tile[0][0] == 'raw':  # only raw images could be tiled
			self.__huge = True  # image is huge
			self.__offset = self.__image.tile[0][2]  # initial tile offset
			self.__tile = [self.__image.tile[0][0],  # it have to be 'raw'
						   [0, 0, self.imwidth, 0],  # tile extent (a rectangle)
						   self.__offset,
						   self.__image.tile[0][3]]  # list of arguments to the decoder
		self.__min_side = min(self.imwidth, self.imheight)  # get the smaller image side
		# Create image pyramid
		self.__pyramid = [self.smaller()] if self.__huge else [Image.open(self.path)]
		# Set ratio coefficient for image pyramid
		self.__ratio = max(self.imwidth, self.imheight) / self.__huge_size if self.__huge else 1.0
		self.__curr_img = 0  # current image from the pyramid
		self.__scale = self.imscale * self.__ratio  # image pyramide scale
		self.__reduction = 2  # reduction degree of image pyramid
		w, h = self.__pyramid[-1].size
		while w > 512 and h > 512:  # top pyramid image is around 512 pixels in size
			w /= self.__reduction  # divide on reduction degree
			h /= self.__reduction  # divide on reduction degree
			self.__pyramid.append(self.__pyramid[-1].resize((int(w), int(h)), self.__filter))
		# Put image into container rectangle and use it to set proper coordinates to the image
		self.container = self.canvas.create_rectangle((0, 0, self.imwidth, self.imheight), width=0)
		self.__show_image()  # show image on the canvas
		self.canvas.focus_set()  # set focus on the canvas

	def jiggy(self, event):
		global point_counter
		global point_list

		point_list.clear()
		point_counter = 0			
		self.canvas.delete("tag")

		# x = self.canvas.canvasx(event.x)  # get coordinates of the event on the canvas
		# y = self.canvas.canvasy(event.y)
		# print("click:"+str(x)+","+str(y))

		# if(self.outside(x, y)):
		# 	print("outside")
		# else:
		# 	bbox = self.canvas.coords(self.container)  # get image area
		# 	x1 = round((x - bbox[0]) / self.imscale)  # get real (x,y) on the image without zoom
		# 	y1 = round((y - bbox[1]) / self.imscale)
		# 	print("real:"+str(x1)+","+str(y1))


	def create_mypoint(self, point, color, mytag):
		"""Create a token at the given coordinate in the given color"""
		p1 = self.getScaledCoords(point)
		x = p1[0]
		y = p1[1]
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


	def getRealCoords(self, event):		
		"""scale and pan invariant coords"""
		x = self.canvas.canvasx(event.x)  # get coordinates of the event on the canvas
		y = self.canvas.canvasy(event.y)

		bbox = self.canvas.coords(self.container)  # get image area
		x1 = round((x - bbox[0]) / self.imscale)  # get real (x,y) on the image without zoom
		y1 = round((y - bbox[1]) / self.imscale)

		return (x1, y1)
 
	def getAngle(self, a, b, c):
		ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
		return ang + 360 if ang < 0 else ang




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


	def getScaledCoords(self, point):		
		"""scale and pan invariant coords"""
		bbox = self.canvas.coords(self.container)  # get image area
		x = point[0] * self.imscale + bbox[0]
		y = point[1] * self.imscale + bbox[1]
		return (x, y)

	def retLeftPoint(self, p1, p2):
		if p1[0] < p2[0]:
			return p1
		return p2


	def create_myline(self, point1, point2, mytag):

		p1 = self.getScaledCoords(point1)
		p2 = self.getScaledCoords(point2)

		self.canvas.create_line(p1[0], p1[1], p2[0], p2[1], fill="red",width=2, tags=("del","lines", mytag))


	def circular_arc(self, canvas, x, y, r, t0, t1, width):
		return canvas.create_arc(x-r, y-r, x+r, y+r, start=t0, extent=t1-t0,
			style='arc', width=width)

	def jiggy_click(self, event):
		x = self.canvas.canvasx(event.x)  # get coordinates of the event on the canvas
		y = self.canvas.canvasy(event.y)
		# print("click:"+str(x)+","+str(y))

		global point_counter
		global point_list

		thickness = 10 * self.imscale

		# xy = 20, 20, 300, 300


		# self.canvas.create_oval(	300 - thickness, 300 - thickness,
		# 									180 + thickness, 180 + thickness,
		# 									width=0, fill="red",
		# 									tags=("del"))

		# self.canvas.create_arc(xy, start=0, extent=270, fill="rounded")
		# self.canvas.create_arc(xy, start=270, extent=60, fill="blue")
		# self.canvas.create_arc(xy, start=330, extent=30, fill="green")

		# self.circular_arc(self.canvas, 20, 20, 10, 90, 180, 5)
		

		if(self.outside(x, y)):
			# print("outside")
			pass
		else:
			P = self.getRealCoords(event)
			print(point_counter)
			

			if( point_counter < 4):

				point_list.append(P)
				self.create_mypoint(P, "white", "tag")

				

			
			if( point_counter == 3):

				p1 = point_list[0]
				p2 = point_list[1]
				p3 = point_list[2]
				p4 = point_list[3]

				self.create_myline(p1, p2, "tag")
				self.create_myline(p3, p4, "tag")

				p_int = self.line_intersection((p1, p2), (p3, p4))

				angle = self.create_myAngle(p1, p_int, p3, "tag")
				print(angle)

			# increment point counter
			point_counter = point_counter+1

	def smaller(self):
		""" Resize image proportionally and return smaller image """
		w1, h1 = float(self.imwidth), float(self.imheight)
		w2, h2 = float(self.__huge_size), float(self.__huge_size)
		aspect_ratio1 = w1 / h1
		aspect_ratio2 = w2 / h2  # it equals to 1.0
		if aspect_ratio1 == aspect_ratio2:
			image = Image.new('RGB', (int(w2), int(h2)))
			k = h2 / h1  # compression ratio
			w = int(w2)  # band length
		elif aspect_ratio1 > aspect_ratio2:
			image = Image.new('RGB', (int(w2), int(w2 / aspect_ratio1)))
			k = h2 / w1  # compression ratio
			w = int(w2)  # band length
		else:  # aspect_ratio1 < aspect_ration2
			image = Image.new('RGB', (int(h2 * aspect_ratio1), int(h2)))
			k = h2 / h1  # compression ratio
			w = int(h2 * aspect_ratio1)  # band length
		i, j, n = 0, 1, round(0.5 + self.imheight / self.__band_width)
		while i < self.imheight:
			print('\rOpening image: {j} from {n}'.format(j=j, n=n), end='')
			band = min(self.__band_width, self.imheight - i)  # width of the tile band
			self.__tile[1][3] = band  # set band width
			self.__tile[2] = self.__offset + self.imwidth * i * 3  # tile offset (3 bytes per pixel)
			self.__image.close()
			self.__image = Image.open(self.path)  # reopen / reset image
			self.__image.size = (self.imwidth, band)  # set size of the tile band
			self.__image.tile = [self.__tile]  # set tile
			cropped = self.__image.crop((0, 0, self.imwidth, band))  # crop tile band
			image.paste(cropped.resize((w, int(band * k)+1), self.__filter), (0, int(i * k)))
			i += band
			j += 1
		print('\r' + 30*' ' + '\r', end='')  # hide printed string
		return image

	def redraw_figures(self):
		""" Dummy function to redraw figures in the children classes """
		pass

	def create_myAngle(self, point1, point2, point3, mytag, radius = 50, width = 3, outline="red"):

		angle = self.getAnglePoints(point1, point2, point3)
		print('angle: {}'.format(angle))

		arc_angle = self.getAnglePointsNeg(point3, point2, (self.imwidth, point2[1]))
		print('arc_angle: {}'.format(arc_angle))
		
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


	def grid(self, **kw):
		""" Put CanvasImage widget on the parent widget """
		self.__imframe.grid(**kw)  # place CanvasImage widget on the grid
		self.__imframe.grid(sticky='nswe')  # make frame container sticky
		self.__imframe.rowconfigure(0, weight=1)  # make canvas expandable
		self.__imframe.columnconfigure(0, weight=1)

	def pack(self, **kw):
		""" Exception: cannot use pack with this widget """
		raise Exception('Cannot use pack with the widget ' + self.__class__.__name__)

	def place(self, **kw):
		""" Exception: cannot use place with this widget """
		raise Exception('Cannot use place with the widget ' + self.__class__.__name__)

	# noinspection PyUnusedLocal
	def __scroll_x(self, *args, **kwargs):
		""" Scroll canvas horizontally and redraw the image """
		self.canvas.xview(*args)  # scroll horizontally
		self.__show_image()  # redraw the image

	# noinspection PyUnusedLocal
	def __scroll_y(self, *args, **kwargs):
		""" Scroll canvas vertically and redraw the image """
		self.canvas.yview(*args)  # scroll vertically
		self.__show_image()  # redraw the image

	def __show_image(self):
		""" Show image on the Canvas. Implements correct image zoom almost like in Google Maps """
		box_image = self.canvas.coords(self.container)  # get image area
		box_canvas = (self.canvas.canvasx(0),  # get visible area of the canvas
					  self.canvas.canvasy(0),
					  self.canvas.canvasx(self.canvas.winfo_width()),
					  self.canvas.canvasy(self.canvas.winfo_height()))
		box_img_int = tuple(map(int, box_image))  # convert to integer or it will not work properly
		# Get scroll region box
		box_scroll = [min(box_img_int[0], box_canvas[0]), min(box_img_int[1], box_canvas[1]),
					  max(box_img_int[2], box_canvas[2]), max(box_img_int[3], box_canvas[3])]
		# Horizontal part of the image is in the visible area
		if  box_scroll[0] == box_canvas[0] and box_scroll[2] == box_canvas[2]:
			box_scroll[0]  = box_img_int[0]
			box_scroll[2]  = box_img_int[2]
		# Vertical part of the image is in the visible area
		if  box_scroll[1] == box_canvas[1] and box_scroll[3] == box_canvas[3]:
			box_scroll[1]  = box_img_int[1]
			box_scroll[3]  = box_img_int[3]
		# Convert scroll region to tuple and to integer
		self.canvas.configure(scrollregion=tuple(map(int, box_scroll)))  # set scroll region
		x1 = max(box_canvas[0] - box_image[0], 0)  # get coordinates (x1,y1,x2,y2) of the image tile
		y1 = max(box_canvas[1] - box_image[1], 0)
		x2 = min(box_canvas[2], box_image[2]) - box_image[0]
		y2 = min(box_canvas[3], box_image[3]) - box_image[1]
		if int(x2 - x1) > 0 and int(y2 - y1) > 0:  # show image if it in the visible area
			if self.__huge and self.__curr_img < 0:  # show huge image
				h = int((y2 - y1) / self.imscale)  # height of the tile band
				self.__tile[1][3] = h  # set the tile band height
				self.__tile[2] = self.__offset + self.imwidth * int(y1 / self.imscale) * 3
				self.__image.close()
				self.__image = Image.open(self.path)  # reopen / reset image
				self.__image.size = (self.imwidth, h)  # set size of the tile band
				self.__image.tile = [self.__tile]
				image = self.__image.crop((int(x1 / self.imscale), 0, int(x2 / self.imscale), h))
			else:  # show normal image
				image = self.__pyramid[max(0, self.__curr_img)].crop(  # crop current img from pyramid
									(int(x1 / self.__scale), int(y1 / self.__scale),
									 int(x2 / self.__scale), int(y2 / self.__scale)))
			#
			imagetk = ImageTk.PhotoImage(image.resize((int(x2 - x1), int(y2 - y1)), self.__filter))
			imageid = self.canvas.create_image(max(box_canvas[0], box_img_int[0]),
											   max(box_canvas[1], box_img_int[1]),
											   anchor='nw', image=imagetk)
			self.canvas.lower(imageid)  # set image into background
			self.canvas.imagetk = imagetk  # keep an extra reference to prevent garbage-collection

	def __move_from(self, event):
		""" Remember previous coordinates for scrolling with the mouse """
		self.canvas.scan_mark(event.x, event.y)

	def __move_to(self, event):
		""" Drag (move) canvas to the new position """
		self.canvas.scan_dragto(event.x, event.y, gain=1)
		self.__show_image()  # zoom tile and show it on the canvas

	def outside(self, x, y):
		""" Checks if the point (x,y) is outside the image area """
		bbox = self.canvas.coords(self.container)  # get image area
		if bbox[0] < x < bbox[2] and bbox[1] < y < bbox[3]:
			return False  # point (x,y) is inside the image area
		else:
			return True  # point (x,y) is outside the image area

	def __wheel(self, event):
		""" Zoom with mouse wheel """
		x = self.canvas.canvasx(event.x)  # get coordinates of the event on the canvas
		y = self.canvas.canvasy(event.y)
		if self.outside(x, y): return  # zoom only inside image area
		scale = 1.0
		# Respond to Linux (event.num) or Windows (event.delta) wheel event
		if event.num == 5 or event.delta == -120:  # scroll down, smaller
			if round(self.__min_side * self.imscale) < 30: return  # image is less than 30 pixels
			self.imscale /= self.__delta
			scale        /= self.__delta
		if event.num == 4 or event.delta == 120:  # scroll up, bigger
			i = min(self.canvas.winfo_width(), self.canvas.winfo_height()) >> 1
			if i < self.imscale: return  # 1 pixel is bigger than the visible area
			self.imscale *= self.__delta
			scale        *= self.__delta
		# Take appropriate image from the pyramid
		k = self.imscale * self.__ratio  # temporary coefficient
		self.__curr_img = min((-1) * int(math.log(k, self.__reduction)), len(self.__pyramid) - 1)
		self.__scale = k * math.pow(self.__reduction, max(0, self.__curr_img))
		#
		self.canvas.scale('all', x, y, scale, scale)  # rescale all objects
		# Redraw some figures before showing image on the screen
		self.redraw_figures()  # method for child classes
		self.__show_image()

	def __keystroke(self, event):
		""" Scrolling with the keyboard.
			Independent from the language of the keyboard, CapsLock, <Ctrl>+<key>, etc. """
		if event.state - self.__previous_state == 4:  # means that the Control key is pressed
			pass  # do nothing if Control key is pressed
		else:
			self.__previous_state = event.state  # remember the last keystroke state
			# Up, Down, Left, Right keystrokes
			if event.keycode in [68, 39, 102]:  # scroll right, keys 'd' or 'Right'
				self.__scroll_x('scroll',  1, 'unit', event=event)
			elif event.keycode in [65, 37, 100]:  # scroll left, keys 'a' or 'Left'
				self.__scroll_x('scroll', -1, 'unit', event=event)
			elif event.keycode in [87, 38, 104]:  # scroll up, keys 'w' or 'Up'
				self.__scroll_y('scroll', -1, 'unit', event=event)
			elif event.keycode in [83, 40, 98]:  # scroll down, keys 's' or 'Down'
				self.__scroll_y('scroll',  1, 'unit', event=event)

	def crop(self, bbox):
		""" Crop rectangle from the image and return it """
		if self.__huge:  # image is huge and not totally in RAM
			band = bbox[3] - bbox[1]  # width of the tile band
			self.__tile[1][3] = band  # set the tile height
			self.__tile[2] = self.__offset + self.imwidth * bbox[1] * 3  # set offset of the band
			self.__image.close()
			self.__image = Image.open(self.path)  # reopen / reset image
			self.__image.size = (self.imwidth, band)  # set size of the tile band
			self.__image.tile = [self.__tile]
			return self.__image.crop((bbox[0], 0, bbox[2], band))
		else:  # image is totally in RAM
			return self.__pyramid[0].crop(bbox)

	def destroy(self):
		""" ImageFrame destructor """
		self.__image.close()
		map(lambda i: i.close, self.__pyramid)  # close all pyramid images
		del self.__pyramid[:]  # delete pyramid list
		del self.__pyramid  # delete pyramid variable
		self.canvas.destroy()
		self.__imframe.destroy()

class MainWindow(ttk.Frame):
	""" Main window class """
	def __init__(self, mainframe, path):
		""" Initialize the main Frame """
		ttk.Frame.__init__(self, master=mainframe)
		self.master.title('Advanced Zoom v3.0')
		self.master.geometry('800x600')  # size of the main window
		self.master.rowconfigure(0, weight=1)  # make the CanvasImage widget expandable
		self.master.columnconfigure(0, weight=1)
		canvas = CanvasImage(self.master, path)  # create widget
		canvas.grid(row=0, column=0)  # show widget

# filename = './data/img_plg5.png'  # place path to your image here
# filename = 'harold.jpg'  # place path to your image here
# filename = 'legit2.jpg'  # place path to your image here
filename = '500.jpg'  # place path to your image here
#filename = 'd:/Data/yandex_z18_1-1.tif'  # huge TIFF file 1.4 GB
#filename = 'd:/Data/The_Garden_of_Earthly_Delights_by_Bosch_High_Resolution.jpg'
#filename = 'd:/Data/The_Garden_of_Earthly_Delights_by_Bosch_High_Resolution.tif'
#filename = 'd:/Data/heic1502a.tif'
#filename = 'd:/Data/land_shallow_topo_east.tif'
#filename = 'd:/Data/X1D5_B0002594.3FR'
app = MainWindow(tk.Tk(), path=filename)
app.mainloop()