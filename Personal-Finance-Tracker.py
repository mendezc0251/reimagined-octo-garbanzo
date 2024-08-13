from Backend import FinanceTracker
from tkinter import *
from tkinter import ttk
class PersonalFinanceTracker:
    def __init__(self, root):
        frm = ttk.Frame(root, padding=100)
        frm.grid()
        root.title("Personal Finance Tracker")
        ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1,row=5)
        ttk.Button(frm, text="Add Expense").grid(column=1,row=2)
        e_1 = ttk.Entry(frm).grid(column=0,row=1)
        e_1.pack()
        e_2 = ttk.Entry(frm).grid(column=1,row=1)
        e_2.pack()
        e_3 = ttk.Entry(frm).grid(column=2,row=1)
        e_3.pack()
        ttk.Button(frm, text="Add Income").grid(column=1,row=4)
        ttk.Entry(frm).grid(column=0,row=3)
        ttk.Entry(frm).grid(column=1,row=3)
        ttk.Entry(frm).grid(column=2,row=3)
    def all_expenses():

root = Tk()
PersonalFinanceTracker(root)
root.mainloop()