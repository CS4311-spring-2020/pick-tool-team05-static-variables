from PyQt5.QtWidgets import QWidget, QLineEdit, QMessageBox, QLineEdit, QPushButton, QDesktopWidget, QCheckBox, \
    QFileDialog, QAction
from PyQt5 import QtWidgets
from PyQt5 import QtGui


class ExportGraphImage(QWidget):

    def __init__(self):
        super(ExportGraphImage, self).__init__()
        self.ui()

    def ui(self):
        self.resize(450,330)
        self.center()
        self.setWindowTitle("Export Graph Image")

        # Text in Window
        save_as_label = QtWidgets.QLabel(self)
        save_as_label.setText('Save as :')
        save_as_label.move(70, 60)
        jpeg = QtWidgets.QLabel(self)
        jpeg.setText("JPEG")
        jpeg.move(190,120)
        png = QtWidgets.QLabel(self)
        png.setText("PNG")
        png.move(190,170)

        # Check boxes
        self.j = QCheckBox(self)
        self.j.move(230, 110)
        self.j.resize(320, 40)
        self.p = QCheckBox(self)
        self.p.move(230,171)

        # Input Textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(145, 56)
        self.textbox.resize(200, 30)
        self.show
        self.textbox2 = QLineEdit(self)
        self.textbox2.move(145,220)
        self.textbox2.resize(200,30)
        self.show

        # Buttons
        self.file_button = QPushButton("...", self)
        self.file_button.resize(35,35)
        self.file_button.move(350, 217)
        self.file_button.clicked.connect(self.file_open)

        self.save_button = QPushButton("Save", self)
        self.save_button.move(150, 275)


        self.save_button = QPushButton("Cancel", self)
        self.save_button.move(260, 275)

        # Opening File System
        openFile = QAction('&Open File', self)
        openFile.setStatusTip('Open File')
        openFile.triggered.connect(self.file_open)
        self.save_button.clicked.connect(self.close)

    def file_open(self):
        name, _ = QFileDialog.getOpenFileName(self, 'Open File', options=QFileDialog.DontUseNativeDialog)
        file = open(name, 'r')



    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
