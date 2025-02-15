import sys
import sqlite3
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.pushButton.clicked.connect(self.table)

    def table(self):
        self.con = sqlite3.connect('coffee.sqlite')
        self.cursor = self.con.cursor()
        self.tableWidget.verticalHeader().setVisible(False)
        self.data = self.cursor.execute('SELECT * FROM coffee').fetchall()
        self.tableWidget.setColumnCount(len(self.data[0]))
        names = [el[0] for el in self.cursor.description]
        self.tableWidget.setHorizontalHeaderLabels(names)
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(self.data):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, el in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(el)))
        self.tableWidget.resizeColumnsToContents()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Coffee()
    window.show()
    sys.exit(app.exec())
