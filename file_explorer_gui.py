from tkinter import *
from tkinter import ttk
from tkinter import filedialog

interface = Tk()

def opendir():
	working_dir = filedialog.askdirectory()
	print(working_dir)
	# return filedialog.askopenfilename()


def openfile():
	path = filedialog.askopenfilename()
	print(path)

button = ttk.Button(interface, text="Set Working Directory", command=opendir)  # <------
button.grid(column=1, row=1)

button = ttk.Button(interface, text="Open File", command=openfile)  # <------
button.grid(column=1, row=2)

interface.mainloop()