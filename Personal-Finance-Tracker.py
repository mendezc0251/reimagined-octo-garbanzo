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
        self.e_1 = ttk.Entry(frm).grid(column=0,row=1)
        self.e_1.pack()
        self.e_2 = ttk.Entry(frm).grid(column=1,row=1)
        self.e_2.pack()
        self.e_3 = ttk.Entry(frm).grid(column=2,row=1)
        self.e_3.pack()
        ttk.Button(frm, text="Add Income").grid(column=1,row=4)
        ttk.Entry(frm).grid(column=0,row=3)
        ttk.Entry(frm).grid(column=1,row=3)
        ttk.Entry(frm).grid(column=2,row=3)
    def all_expenses(self, *args):
        try:
            FinanceTracker.add_expense(self.e_1.get(), self.e_2.get(), self.e_3.get())
        except
root = Tk()
PersonalFinanceTracker(root)
root.mainloop()