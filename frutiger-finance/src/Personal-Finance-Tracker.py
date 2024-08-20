"""
Class that will handle the gui and all of the Finance Trackers frontend.
"""
from Backend import FinanceTracker
from tkinter import *
from tkinter import ttk

class PersonalFinanceTracker:
    # This function initializes the Finance Trackers frontend
    def __init__(self, root):
        frm = ttk.Frame(root, padding=100)
        frm.grid()
        root.title("Personal Finance Tracker")
        ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1,row=5)
        ttk.Button(frm, text="Add Expense", command=self.all_expenses).grid(column=1,row=2)
        self.e_2 = ttk.Entry(frm)
        self.e_2.grid(column=1,row=1)
        self.e_3 = ttk.Entry(frm)
        self.e_3.grid(column=2,row=1)
        ttk.Button(frm, text="Add Income", command=self.all_incomes).grid(column=1,row=4)
        self.i_2 = ttk.Entry(frm)
        self.i_2.grid(column=1,row=3)
        self.i_3 = ttk.Entry(frm)
        self.i_3.grid(column=2,row=3)
    # This function adds a users input expense to the Finances database
    def all_expenses(self, *args):
        try:
            f = FinanceTracker()
            f.add_expense(self.e_1.get(), self.e_2.get(), self.e_3.get())
        except Exception as e:
            print(f"An error occurred: {e}")
    # This function adss a users input income to the Finances database
    def all_incomes(self, *args):
        try:
            f = FinanceTracker()
            f.add_income(self.i_1.get(), self.i_2.get(), self.i_3.get())
        except Exception as e:
            print(f"An error occured: {e}")
root = Tk()
PersonalFinanceTracker(root)
root.mainloop()