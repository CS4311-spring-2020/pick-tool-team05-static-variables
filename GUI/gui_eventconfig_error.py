from PyQt5.QtWidgets import QWidget, QLineEdit, QMessageBox, QLineEdit, QPushButton, QDesktopWidget


class EventConfigError(QWidget):

    def __init__(self):
        super(EventConfigError, self).__init__()
        self.ui()

    def ui(self):

        self.resize(550, 300)
        self.textbox = QLineEdit(self)
        self.textbox.move(76, 40)
        self.textbox.resize(400, 90)
        self.setWindowTitle('Directories not Found: Event Configuration Error ')
        self.textbox.setText("Directory: Purple : Not found in the Directory Path provided \n Directories: Blue, White : Found ")

        self.scan_button = QPushButton('Close', self)
        self.scan_button.move(225, 160)
        self.scan_button.clicked.connect(self.close)
