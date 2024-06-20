"""
Class that will take care of the backend of the finance tracker.
"""

import csv
import pandas as pd

colnames = ['ID','Income','Expense','Amount']
df = pd.read_csv('Finance-Data.csv', names=colnames, header=None, index_col='ID')
print(df.head)
def add_expense(id, expense, amount):
    data = {
        'ID': [id],
        'Income': ['N/A'],
        'Expense': [expense],
        'Amount': [amount]
    }
    df = pd.DataFrame(data)
    df.to_csv('Finance-Data.csv', mode='a', header=False, index=False) 
def remove_expense(id):
    global df
    df.drop(index=pd.int(id))
def add_income():
    return 0
def remove_income():
    return 0
remove_expense('01')