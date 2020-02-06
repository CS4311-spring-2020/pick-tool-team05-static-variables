import os

from PyQt5.QtCore import Qt, pyqtSlot, QSize
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton, \
    QCheckBox, QAction
from PyQt5 import QtWidgets
from PyQt5.uic.properties import QtCore, QtGui


class IconConfiguration(QWidget):
    def __init__(self):
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
        self.layout.setAlignment(Qt.AlignCenter)
        self.setLayout(self.layout)

        # Buttons
        add_button = QPushButton("Add", self)
        add_button.move(75, 170)
        delete_button = QPushButton('Delete', self)
        delete_button.move(195, 170)
        edit_button = QPushButton('Edit', self)
        edit_button.move(320, 170)
        self.show()

    def createTable(self):
        # Table
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setRowCount(2)
        self.table.setHorizontalHeaderLabels(['', 'Icon Name ', 'Icon Source', 'Image Preview'])
        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setStretchLastSection(True)

        # Iterating through the table,aligning it and adding rows after a checkbox is inserted
        for columns in range(1):
            self.pWidget = QWidget()
            self.pCheckbox = QCheckBox()
            self.pLayout = QVBoxLayout(self.pWidget)
            self.pLayout.addWidget(self.pCheckbox)
            self.pLayout.setAlignment(Qt.AlignCenter)
            self.pLayout.setContentsMargins(0, 0, 0, 0)
            self.pWidget.setLayout(self.pLayout)
            self.table.insertRow(0)
            self.table.setCellWidget(0, 0, self.pWidget)
            # Dummy Data in the table
            self.table.setItem(0, 1, QTableWidgetItem("Shield"))
            self.table.setItem(0, 2, QTableWidgetItem("Resources/Images/shield.png"))

            # Buttons to display the icons
            self.button = QPushButton(self)
            self.button.setFlat(True)
            self.button.setIcon(QIcon("Resources/Images/shield.png"))
            self.button.setEnabled(False)
            self.button.setIconSize(QSize(20,20))
            self.table.setCellWidget(columns, 3, self.button)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())