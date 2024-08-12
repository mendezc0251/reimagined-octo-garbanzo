"""
Class that will take care of the backend of the finance tracker.
"""

import sqlite3

class FinanceTrackerBackend:
    mydb = sqlite3.connector.connect('Finances.db')
    cursor = mydb.cursor()
    print('Database initialized')
    def add_expense(id, expense, amount):
        FinanceTrackerBackend.cursor.execute('INSERT INTO Expenses VALUES(id, expense, amount)')
        return 0
    def remove_expense(id):
        FinanceTrackerBackend.cursor.execute('DELETE FROM Expenses WHERE id = id')
        return 0
    def add_income():
        FinanceTrackerBackend.cursor.execute('INSERT INTO Incomes VALUES(id, income, amount)')
        return 0
    def remove_income(self):
        FinanceTrackerBackend.cursor.execute('DELETE FROM Incomes WHERE id = id')
        return 0