from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton, QCheckBox
from PyQt5 import QtWidgets
from PyQt5.uic.properties import QtCore, QtGui


class IconConfiguration(QWidget):
    def __init__(self, rows, columns):
        super(IconConfiguration, self).__init__()
        self.ui()

    def ui(self):
        self.resize(500, 230)
        self.center()
        self.setWindowTitle("Icon Configuration")

        # Creating Table along with the layout to display in window
        self.createTable()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.table)
        self.setLayout(self.layout)

        # Buttons
        add_button = QPushButton("Add", self)
        add_button.move(75, 180)

        delete_button = QPushButton('Delete', self)
        delete_button.move(195, 180)

        edit_button = QPushButton('Edit', self)
        edit_button.move(320, 180)

        self.show()

    def createTable(self):
        # Table
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setRowCount(4)
        self.table.setHorizontalHeaderLabels(['', 'Icon Name ', 'Icon Source', 'Image Preview'])
        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.move(5,5)
        self.table.resize(5,5)

        # Checkboxes


    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())