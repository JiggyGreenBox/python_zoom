from tkinter import *

root = Tk()
root.geometry("800x600")

navbar = Frame(root, width=100)
navbar.pack(anchor=W, fill=Y, expand=False, side=LEFT)  # <----

content_frame = Frame(root, bg="orange")
content_frame.pack(anchor=N, fill=BOTH, expand=True, side=LEFT )

root.mainloop()