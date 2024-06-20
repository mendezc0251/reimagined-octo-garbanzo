from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=100)
frm.grid()
ttk.Label(frm, text="Personal Finance Tracker").grid(column=0,row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1,row=0)
ttk.Button(frm, text="Add Expense").grid(column=0,row=2)
ttk.Entry(frm).grid(column=0,row=1)
ttk.Button(frm, text="Add Income").grid(column=0,row=4)
ttk.Entry(frm).grid(column=0,row=3)
root.mainloop()