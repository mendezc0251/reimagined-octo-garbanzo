"""
Class that will take care of the backend of the finance tracker.
"""

import csv
import pandas as pd

colnames = ['ID','Income','Expense','Amount']
df = pd.read_csv('Finance-Data.csv', names=colnames, header=None, index_col='ID')

def add_expense(id, expense, amount):
    data = {
        'ID': id,
        'Income': 'N/A',
        'Expense': expense,
        'Amount': amount
    }
    df = pd.DataFrame(data)
    df.to_csv('Finance-Data.csv', mode='a') 
def remove_expense():
    return 0
def add_income():
    return 0
def remove_income():
    return 0
add_expense('01','Dining',10.00)