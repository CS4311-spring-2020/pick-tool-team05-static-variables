#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget, QPushButton, QDesktopWidget, QLineEdit, QMessageBox
from PyQt5 import QtWidgets


class ConnectHost(QWidget):

    def __init__(self):
        super(ConnectHost, self).__init__()
        self.ui()

    def connect_error_message(self):
        QMessageBox.about(self, "Error", "The system did not find a host in the network")

    def ui(self):
        self.resize(500, 250)
        self.center()
        self.setWindowTitle('Connect to Host')

        # Label in Window
        name_label = QtWidgets.QLabel(self)
        name_label.setText('Your Name *')
        name_label.move(70, 90)

        # Text Box in Window
        self.textbox = QLineEdit(self)
        self.textbox.move(165, 85)
        self.textbox.resize(200, 30)

        # Buttons in Window
        self.scan_button = QPushButton('Scan for Hosts', self)
        self.scan_button.move(110, 160)

        self.scan_button.clicked.connect(self.connect_error_message)  # Message box

        self.cancel_button = QPushButton('Cancel', self)
        self.cancel_button.move(290,160)
        self.cancel_button.clicked.connect(self.close)

        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    def connect_error_message(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("The system could not connect to a network")

        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Retry)
        msg.setDefaultButton(QMessageBox.Ok)
        # msg.buttonClicked.connect()    TODO: Connect to Main Page of app
        x = msg.exec()



