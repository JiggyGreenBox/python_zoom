from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("800x600")

navbar = Frame(root, width=100)
navbar.pack(anchor=W, fill=Y, expand=False, side=LEFT)  # <----

def object1():
	print("object 1")

def object2():
	print("object 2")

button = ttk.Button(navbar, text="object 1", command=object1)
button.grid(column=1, row=1)

button = ttk.Button(navbar, text="object 2", command=object2)
button.grid(column=1, row=2)



content_frame = Frame(root, bg="orange")
content_frame.pack(anchor=N, fill=BOTH, expand=True, side=LEFT )

root.mainloop()