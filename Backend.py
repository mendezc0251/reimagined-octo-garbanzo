"""
Class that will take care of the backend of the finance tracker.
"""

import sqlite3


class FinanceTracker:
    def __init__(self):
        self.mydb = sqlite3.connector.connect('Finances.db')
        self.cursor = self.mydb.cursor()
        print('Database initialized')

    def add_expense(self, id, expense, amount):
        self.cursor.execute('INSERT INTO Expenses VALUES(id, expense, amount)')

    def remove_expense(self, id):
        self.cursor.execute('DELETE FROM Expenses WHERE id = id')

    def add_income(self, id, income, amount):
        self.cursor.execute('INSERT INTO Income VALUES(id, income, amount)')

    def remove_income(self, id):
        self.cursor.execute('DELETE FROM Income WHERE id = id')
