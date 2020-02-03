
from PyQt5.QtWidgets import QWidget, QPushButton, QDesktopWidget, QFileDialog, QTextEdit, QVBoxLayout, QLabel

import PyQt5.QtWidgets

class logIngestion(PyQt5.QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Log Ingestion")
        self.setGeometry(600,600,600,600)
        self.UI()

    def UI(self):
        window = self.frameGeometry()
        adjW = QDesktopWidget().availableGeometry().center()
        window.moveCenter(adjW)

        # NEED TO FIX THIS WINDOW

        self.continueButton = PyQt5.QtWidgets.QPushButton("Continue", self)
        self.validateButton = PyQt5.QtWidgets.QPushButton("Validate", self)
        self.continueButton.move(120, 500)
        self.validateButton.move(350, 500)

        self.show()

    # update screen
    def getFiles(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setFilter("Text files (*.txt)")

        if dlg.exec_():
            filenames = dlg.selectedFiles()
            f = open(filenames[0], 'r')
            with f:
                data = f.read()
                self.contents.setText(data)

