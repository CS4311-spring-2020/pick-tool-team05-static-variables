from PyQt5.QtWidgets import QWidget, QLineEdit, QMessageBox, QLineEdit, QPushButton, QDesktopWidget, QCheckBox, \
    QFileDialog, QAction, QComboBox
from PyQt5 import QtWidgets
from PyQt5 import QtGui


class ExportFormat(QWidget):

    def __init__(self):
        super(ExportFormat, self).__init__()
        self.ui()

    def ui(self):
        self.resize(280, 120)
        self.center()
        self.setWindowTitle("Export Configuration")

        # Label
        name_label = QtWidgets.QLabel(self)
        name_label.setText('Export Format : ')
        name_label.move(40, 40)

        # Drop-Down Box
        combo = QComboBox(self)
        combo.move(135,1)
        combo.resize(100,100)
        combo.addItems(["PNG", "JPG"])
        combo.show()

        # Buttons
        export_button = QPushButton("Export", self)
        export_button.move(48,75)
        

        cancel_button = QPushButton('Cancel', self)
        cancel_button.move(145, 75)
        cancel_button.clicked.connect(self.close)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
