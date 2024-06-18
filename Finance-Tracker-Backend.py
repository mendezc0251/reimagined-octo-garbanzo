import csv

with open('Finance-Data.csv', 'w', newline='') as csvfile:
    fieldnames = ['Income', 'Expenses']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)