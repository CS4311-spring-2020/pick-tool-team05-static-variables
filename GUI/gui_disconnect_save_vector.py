from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication, QPushButton
from PyQt5.QtCore import Qt
import sys

class Disconnect_Save_Vector(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        Vector1 = QCheckBox('Attempted security breach', self)
        Vector1.move(20, 20)
        Vector1.toggle()
        Vector1.stateChanged.connect(self.changeTitle)

        Vector2 = QCheckBox('Attempted Virus upload', self)
        Vector2.move(20, 40)
        Vector2.toggle()
        Vector2.stateChanged.connect(self.changeTitle)

        Vector3 = QCheckBox('Attempted System Failure', self)
        Vector3.move(20, 60)
        Vector3.toggle()
        Vector3.stateChanged.connect(self.changeTitle)

        Cancel = QPushButton('Cancel', self)
        Cancel.clicked.connect(QApplication.instance().quit)
        Cancel.resize(Cancel.sizeHint())
        Cancel.move(280, 350)

        Confirm = QPushButton('Save Selected Vectors and Disconnect', self)
        Confirm.clicked.connect(QApplication.instance().quit)
        Confirm.resize(Confirm.sizeHint())
        Confirm.move(50, 350)

        self.setGeometry(400, 400, 400, 400)
        self.setWindowTitle('Save Vectors before Disconnecting?')
        self.show()


    def changeTitle(self, state):

        if state == Qt.Checked:
            self.setWindowTitle('Save selected Vectors before Disconnecting?')
        else:
            self.setWindowTitle('Save selected Vectors before Disconnecting?')