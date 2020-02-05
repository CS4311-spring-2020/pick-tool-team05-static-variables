from PyQt5.QtWidgets import QWidget, QLineEdit, QMessageBox, QLineEdit, QPushButton, QDesktopWidget
from PyQt5 import QtWidgets


class LocalCopyWarning(QWidget):
    def __init__(self):

        super(LocalCopyWarning, self).__init__()
        self.ui()

    def ui(self):

        self.resize(500, 250)
        self.center()
        self.setWindowTitle('Warning')
        name_label = QtWidgets.QLabel(self)
        name_label.setText('Local files Found. Connecting to a host will override local changes.')
        name_label.move(65, 80)
        self.commit = QPushButton('Commit and Continue', self)
        self.commit.move(160, 125)
        # self.commit.clickek.connect()   #TODO: Connect to corresponding window
        self.continueW = QPushButton('Continue without Committing', self)
        self.continueW.move(135, 160)
        # self.continueW.clicked.connect()  TODO: Connect to corresponding window
        self.cancel = QPushButton("Cancel", self)
        self.cancel.move(200, 195)
        self.cancel.clicked.connect(self.close)


        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
