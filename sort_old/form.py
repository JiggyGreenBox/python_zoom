from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')


lbl = Label(window, text="First Name")
lbl.grid(column=0, row=0)


txt = Entry(window, width=10)
txt.grid(column=0, row=1)


# def clicked():
# 	lbl.configure(text="Button was clicked !!")


# import pandas as pd
import pandas as pd
 
# list of strings
lst = ['Geeks', 'For', 'Geeks', 'is', 
			'portal', 'for', 'Geeks']
 
# Calling DataFrame constructor on list
df = pd.DataFrame(lst)
print(df)


# btn = Button(window, text="Click Me", command=clicked)
# btn.grid(column=2, row=0)



lbl2 = Label(window, text="Last Name")
lbl2.grid(column=0, row=2)


txt2 = Entry(window, width=10)
txt2.grid(column=0, row=3)


def clicked():
	lbl2.configure(text="Button was clicked !!")



btn = ttk.Button(window, text="Submit", command=clicked)
btn.grid(column=0, row=4)


window.mainloop()