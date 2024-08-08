"""
Class that will take care of the backend of the finance tracker.
"""

import sqlite3

class FinanceTrackerBackend:
    def __init__(self):
        mydb = sqlite3.connector.connect('Finances.db')
        cursor = mydb.cursor()
        print('Database initialized')
    def add_expense(id, expense, amount):
        return 0
    def remove_expense(id):
        return 0
    def add_income():
        return 0
    def remove_income():
        return 0