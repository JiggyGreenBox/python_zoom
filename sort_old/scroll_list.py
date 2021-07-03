# from tkinter import *


# # Creating the root window
# root = Tk()

# # Creating a Listbox and
# # attaching it to root window
# listbox = Listbox(root)

# # Adding Listbox to the left
# # side of root window
# listbox.pack(side = LEFT, fill = BOTH)

# # Creating a Scrollbar and 
# # attaching it to root window
# scrollbar = Scrollbar(root)

# # Adding Scrollbar to the right
# # side of root window
# scrollbar.pack(side = RIGHT, fill = BOTH)

# # Insert elements into the listbox
# for values in range(100):
# 	listbox.insert(END, values)

# # Attaching Listbox to Scrollbar
# # Since we need to have a vertical 
# # scroll we use yscrollcommand
# listbox.config(yscrollcommand = scrollbar.set)

# # setting scrollbar command parameter 
# # to listbox.yview method its yview because
# # we need to have a vertical view
# scrollbar.config(command = listbox.yview)

# root.mainloop()




from tkinter import *
from tkinter import ttk

ws = Tk()
ws.title('PythonGuides')
ws.geometry('400x300')
ws['bg']='#fb0'

tv = ttk.Treeview(ws)
tv['columns']=('Rank', 'Name', 'Badge')
tv.column('#0', width=0, stretch=NO)
tv.column('Rank', anchor=CENTER, width=80)
tv.column('Name', anchor=CENTER, width=80)
tv.column('Badge', anchor=CENTER, width=80)

tv.heading('#0', text='', anchor=CENTER)
tv.heading('Rank', text='Id', anchor=CENTER)
tv.heading('Name', text='rank', anchor=CENTER)
tv.heading('Badge', text='Badge', anchor=CENTER)

tv.insert(parent='', index=0, iid=0, text='', values=('1','Vineet','Alpha'))
tv.insert(parent='', index=1, iid=1, text='', values=('2','Anil','Bravo'))
tv.insert(parent='', index=2, iid=2, text='', values=('3','Vinod','Charlie'))
tv.insert(parent='', index=3, iid=3, text='', values=('4','Vimal','Delta'))
tv.insert(parent='', index=4, iid=4, text='', values=('5','Manjeet','Echo'))
tv.pack()


ws.mainloop()