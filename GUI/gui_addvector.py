
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QLabel, QDesktopWidget


class addVector(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("New Vector")
        self.setGeometry(400,265,400,300)
        self.UI()

    def UI(self):
        window = self.frameGeometry()
        # adjusts window to center
        adjW = QDesktopWidget().availableGeometry().center()
        window.moveCenter(adjW)

        self.nameBox = QLineEdit(self)
        self.nameBox.move(100,70)
        self.nameBox.resize(200,30)

        self.nameLabel = QLabel(self)
        self.nameLabel.setText("Name ")
        self.nameLabel.move(30,75)

        self.descriptionBox = QLineEdit(self)
        self.descriptionBox.move(100, 110)
        self.descriptionBox.resize(200,100)

        self.descriptionLabel = QLabel(self)
        self.descriptionLabel.setText(" Description ")
        self.descriptionLabel.move(25,120)

        self.addButton = QPushButton("Add", self)
        self.addButton.move(100,250)
        self.addButton.clicked.connect(self.close)

        self.cancelButton = QPushButton("Cancel",self)
        self.cancelButton.move(200, 250)
        self.cancelButton.clicked.connect(self.close)

        self.show()
