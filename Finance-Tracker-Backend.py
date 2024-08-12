"""
Class that will take care of the backend of the finance tracker.
"""

import sqlite3


class FinanceTracker:
    def __init__(self):
        self.mydb = sqlite3.connector.connect('Finances.db')
        self.cursor = self.mydb.cursor()
        print('Database initialized')

    def add_expense(id, expense, amount):
        cursor.execute('INSERT INTO Expenses VALUES(id, expense, amount)')
        return 0

    def remove_expense(id):
        cursor.execute('DELETE FROM Expenses WHERE id = id')
        return 0

    def add_income(id, income, amount):
        cursor.execute('INSERT INTO Income VALUES(id, income, amount)')
        return 0

    def remove_income(id):
        cursor.execute('DELETE FROM Income WHERE id = id')
        return 0
