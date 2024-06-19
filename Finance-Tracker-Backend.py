"""
Class that will take care of the backend of the finance tracker.
"""

import csv
import pandas as pd

# with open('Finance-Data.csv', 'w', newline='') as csvfile:
#     fieldnames = ['Income', 'Expense', 'Amount']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#     writer.writeheader()

def add_expense(name, amount):
    with open('Finance-Data.csv', 'a', newline='') as csvfile:
        fieldnames = ['Income', 'Expense', 'Amount']
        writer = csv.DictWriter(csvfile, fieldnames)
        writer.writerow({'Income': 'N/A', 'Expense': name, 'Amount': amount})
def remove_expense(name, amount):
    data = pd.read_csv('Finance-Data.csv')
    return 0
def add_income():
    return 0
def remove_income():
    return 0
add_expense("Test Expense", 10.00)