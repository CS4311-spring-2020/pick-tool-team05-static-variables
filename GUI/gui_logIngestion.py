
from PyQt5.QtWidgets import QWidget, QPushButton, QDesktopWidget, QFileDialog, QTextEdit, QVBoxLayout, QLabel, QLineEdit

import PyQt5.QtWidgets

class logIngestion(PyQt5.QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Log Ingestion")
        self.setGeometry(500,500,500,500)
        self.UI()

    def UI(self):
        # will implement centering window in a bit...
        window = self.frameGeometry()
        adjW = QDesktopWidget().availableGeometry().center()
        window.moveCenter(adjW)

        # will fix box edit when combined later
        # for box....
        self.statusBox = QLineEdit(self)
        self.statusBox.move(50, 30)
        self.statusBox.resize(400, 300)

        # text in window, need to fix so it reads from PATH
        self.wordLabel = QLabel(self)
        self.wordLabel.setText(">Searching for files.....")
        self.wordLabel.move(55, 35)
        self.wordLabel1 = QLabel(self)
        self.wordLabel1.setText(">(98) Files found. ")
        self.wordLabel1.move(55, 55)
        self.wordLabel2 = QLabel(self)
        self.wordLabel2.setText(">Cleansing files.....")
        self.wordLabel2.move(55, 75)
        self.wordLabel2 = QLabel(self)
        self.wordLabel2.setText(">ERROR: File C://Users/dir/red/1239.log could not be cleansed")
        self.wordLabel2.move(55, 95)
        self.wordLabel3 = QLabel(self)
        self.wordLabel3.setText("due to corruption. ")
        self.wordLabel3.move(55, 115)
        self.wordLabel4 = QLabel(self)
        self.wordLabel4.setText(">ERROR: C://Users/dir/blue/save.JPEG could not be cleansed")
        self.wordLabel4.move(55, 135)
        self.wordLabel4 = QLabel(self)
        self.wordLabel4.setText("due to unknown format.")
        self.wordLabel4.move(55, 155)




        self.continueButton = PyQt5.QtWidgets.QPushButton("Continue", self)
        self.continueButton.move(100, 400)
        self.continueButton.clicked.connect(self.close)

        self.validateButton = PyQt5.QtWidgets.QPushButton("Validate", self)
        self.validateButton.move(280, 400)
        self.validateButton.clicked.connect(self.close)

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

