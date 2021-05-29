# pip install tkcalendar

try:
	import tkinter as tk
	from tkinter import ttk
except ImportError:
	import Tkinter as tk
	import ttk

from tkcalendar import Calendar, DateEntry


def print_sel(e):
	print(cal.get_date())

root = tk.Tk()
s = ttk.Style(root)
s.theme_use('clam')


ttk.Label(root, text='Choose date').pack(padx=10, pady=10)

cal = DateEntry(root, width=12, background='darkblue',
				foreground='white', borderwidth=2,
				date_pattern='dd/mm/yyyy')
cal.pack(padx=10, pady=10)
cal.bind("<<DateEntrySelected>>", print_sel)
def_date = cal.get_date()
print(def_date)


root.mainloop()