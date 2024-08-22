import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QTableView, QTableWidgetItem, QMenuBar, QMenu
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt
from PySide6 import QtSqlite
from Backend import FinanceTracker as FT
import sqlite3

class FinanceTracker(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Frutiger Finance Tracker')
        self.setGeometry(100, 100, 800, 600)

        # Central Widget And Layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Table For Displaying Transactions
        self.transaction_table = QTableView()
        self.transaction_table.horizontalHeader().setStretchLastSection(True)
        layout.addWidget(self.transaction_table)
        self.loadData()

        # Buttons For Adding, Editing, And Deleting Transactions
        self.add_button = QPushButton('Add Transaction')
        self.edit_button = QPushButton('Edit Transaction')
        self.delete_button = QPushButton('Delete Transaction')

        layout.addWidget(self.add_button)
        layout.addWidget(self.edit_button)
        layout.addWidget(self.delete_button)

        # Connect Buttons to Functions
        self.add_button.clicked.connect(self.add_transaction)
        self.add_button.clicked.connect(self.edit_transaction)
        self.add_button.clicked.connect(self.delete_transaction)

    def add_transaction(self):
        pass
    def edit_transaction(self):
        pass
    def delete_transaction(self):
        pass
    def loadData(self):
        db = QtSqlite.QSqlDatabase.addDatabase('Finances.db')
        db.open()
        model = QtSql.QSqlQueryModel()
        model.setQuery("SELECT * FROM Expenses")
        self.transaction_table.setModel(model)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    window = FinanceTracker()
    window.show()
    
    sys.exit(app.exec_())