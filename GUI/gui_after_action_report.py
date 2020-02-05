from PyQt5.QtCore import QBasicTimer
from PyQt5.QtWidgets import QWidget, QPushButton, QDesktopWidget, QFileDialog, QTextEdit, QVBoxLayout, QLabel, \
    QLineEdit, QProgressBar

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
        self.statusBox.resize(400, 250)

        # text in window, need to fix so it reads from PATH
        self.wordLabel = QLabel(self)
        self.wordLabel.setText(">Reading files.....")
        self.wordLabel.move(55, 35)
        self.wordLabel1 = QLabel(self)
        self.wordLabel1.setText(">(3) Errors found. ")
        self.wordLabel1.move(55, 55)
        self.wordLabel2 = QLabel(self)
        self.wordLabel2.setText(">ERROR: File C://Users/dir/red/1239 could not be cleansed")
        self.wordLabel2.move(55, 75)
        self.wordLabel2 = QLabel(self)
        self.wordLabel2.setText(">ERROR LINE 12: INVALID DATE FORMAT: 5/50/20")
        self.wordLabel2.move(55, 95)
        self.wordLabel3 = QLabel(self)
        self.wordLabel3.setText(">ERROR: C://Users/dir/blue/save could not be cleansed")
        self.wordLabel3.move(55, 115)
        self.wordLabel4 = QLabel(self)
        self.wordLabel4.setText(">ERROR LINE 11: START DATE 5/10/19 IS AFTER END DATE 5/1/19")
        self.wordLabel4.move(55, 135)
        self.wordLabel4 = QLabel(self)
        self.wordLabel4.setText(">...")
        self.wordLabel4.move(55, 155)

        # progress bar attempt
        self.progressBar = QProgressBar(self)
        self.progressBar.setGeometry(150, 300, 200, 25)

        self.timer = QBasicTimer()
        self.step = 0
        self.completed = 0
        while self.completed < 100:
            self.completed += 0.0001
            self.progressBar.setValue(self.completed)


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

