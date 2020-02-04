from PyQt5.QtWidgets import QWidget, QLineEdit, QMessageBox, QLineEdit, QPushButton, QDesktopWidget, QLabel


class EventConfigError(QWidget):

    def __init__(self):
        super(EventConfigError, self).__init__()
        self.ui()

    def ui(self):
        self.resize(525, 250)
        self.center()
        self.setWindowTitle("Directories not Found : Event Configuration Error")

        # Textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(70, 40)
        self.textbox.resize(400, 90)

        # Hardcoded Output
        wordLabel = QLabel(self)
        wordLabel.setText(" Directory: Purple : Not found in the Directory Path provided")
        wordLabel.move(80, 60)
        wordLabel2 = QLabel(self)
        wordLabel2.setText(" Directories: Blue, White : Found")
        wordLabel2.move(80, 80)

        # Buttons
        scan_button = QPushButton('Close', self)
        scan_button.move(220, 160)
        scan_button.clicked.connect(self.close)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

