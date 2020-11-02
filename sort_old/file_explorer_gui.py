from tkinter import *
from tkinter import ttk
from tkinter import filedialog

interface = Tk()

working_dir = ""

def opendir():
	global working_dir
	working_dir = filedialog.askdirectory()
	print(working_dir)
	# return filedialog.askopenfilename()

def openseldir():
	global working_dir
	working_dir = filedialog.askopenfilename(initialdir=working_dir)


def openfile():
	path = filedialog.askopenfilename()
	print(path)

button = ttk.Button(interface, text="Set Working Directory", command=opendir)  # <------
button.grid(column=1, row=1)


button = ttk.Button(interface, text="Open File", command=openfile)  # <------
button.grid(column=1, row=2)


button = ttk.Button(interface, text="Get from sel Directory", command=openseldir)  # <------
button.grid(column=1, row=3)

interface.mainloop()