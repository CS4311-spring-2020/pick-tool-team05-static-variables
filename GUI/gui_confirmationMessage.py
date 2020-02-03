from PyQt5.QtWidgets import QWidget, QDesktopWidget, QPushButton, QLabel


class confirmation(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Timed Confirmation Message")
        self.setGeometry(200, 200, 300, 200)
        self.UI()

    def UI(self):
        window = self.frameGeometry()
        # adjusts window to center
        adjW = QDesktopWidget().availableGeometry().center()
        window.moveCenter(adjW)

        self.messageLabel = QLabel(self)
        self.messageLabel.setText("No validation errors found. ")
        self.messageLabel.move(30, 75)

        self.messageLabel2 = QLabel(self)
        self.messageLabel2.setText("All log entries imported successfully. ")
        self.messageLabel2.move(30, 100)

        self.show()