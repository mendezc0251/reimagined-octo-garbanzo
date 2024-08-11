"""
Class that will take care of the backend of the finance tracker.
"""

import sqlite3

class FinanceTrackerBackend:
    mydb = sqlite3.connector.connect('Finances.db')
    cursor = mydb.cursor()
    print('Database initialized')
    def add_expense(id, expense, amount):
        cursor.execute('INSERT INTO Expenses VALUES(id, expense, amount)')
        return 0
    def remove_expense(id):
        cursor.execute('DELETE FROM Expenses WHERE id = id')
        return 0
    def add_income():
        cursor.
        return 0
    def remove_income():
        return 0