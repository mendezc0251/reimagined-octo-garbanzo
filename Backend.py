"""
Class that will take care of the backend of the finance tracker.
"""

import sqlite3


class FinanceTracker:
    # This function initializes the Finance Trackers backend
    def __init__(self):
        self.mydb = sqlite3.connect('Finances.db')
        self.cursor = self.mydb.cursor()
        print('Database initialized')
    # This function adds an expense to the Finances databases Expenses Table
    def add_expense(self, id, expense, amount):
        self.cursor.execute('INSERT INTO Expenses VALUES(?, ?, ?)',(id,expense,amount))
        self.mydb.commit()
    # This function removes an expense from the Expenses Table
    def remove_expense(self, id):
        self.cursor.execute('DELETE FROM Expenses WHERE id = ?'(id))
        self.mydb.commit()
    # This function adds and income to the Finances databases Incomes Table
    def add_income(self, id, income, amount):
        self.cursor.execute('INSERT INTO Income VALUES(?, ?, ?)'(id,income,amount))
        self.mydb.commit()
    # This function removes an income from the Incomes Table
    def remove_income(self, id):
        self.cursor.execute('DELETE FROM Income WHERE id = ?'(id))
        self.mydb.commit()