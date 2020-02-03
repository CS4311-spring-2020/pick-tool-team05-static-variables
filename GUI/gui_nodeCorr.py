
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QLabel, QDesktopWidget, QComboBox


class nodeCorrelation(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("New Correlation")
        self.setGeometry(400, 400, 400, 400)
        self.UI()


    def UI(self):
        window = self.frameGeometry()
        # adjusts window to center
        adjW = QDesktopWidget().availableGeometry().center()
        window.moveCenter(adjW)

        self.parentLabel = QLabel(self)
        self.parentLabel.setText("Parent")
        self.parentLabel.move(30, 50)

        combo = QComboBox(self)
        combo.addItem("n1")
        combo.addItem("n2")
        combo.addItem("n3")
        combo.addItem("n4")
        combo.move(80, 50)
        combo.activated[str].connect(self.onActivated)

        self.childLabel = QLabel(self)
        self.childLabel.setText("Child")
        self.childLabel.move(30, 110)

        combo2 = QComboBox(self)
        combo2.addItem("n1")
        combo2.addItem("n2")
        combo2.addItem("n3")
        combo2.addItem("n4")
        combo2.move(80, 110)
        combo2.activated[str].connect(self.onActivated)

        self.LabelBox = QLineEdit(self)
        self.LabelBox.move(100,190)
        self.LabelBox.resize(200,30)

        self.trueLabel = QLabel(self)
        self.trueLabel.setText("Label")
        self.trueLabel.move(30,200)

        self.createButton = QPushButton("Create", self)
        self.cancelButton = QPushButton("Cancel", self)
        self.createButton.move(100, 300)
        self.cancelButton.move(200, 300)

        self.show()

    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()
        # self.show()