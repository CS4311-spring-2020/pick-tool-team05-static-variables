
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QLabel, QDesktopWidget, QComboBox


class editNode(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Edit Node")
        self.setGeometry(400, 400, 400, 400)
        self.UI()


    def UI(self):
        window = self.frameGeometry()
        adjW = QDesktopWidget().availableGeometry().center()
        window.moveCenter(adjW)

        nodeID = "1-004"
        self.idLabel = QLabel(self)
        self.idLabel.setText("ID " + nodeID)
        self.idLabel.move(30, 30)

        artifactID = "none"
        self.artifactLabel = QLabel(self)
        self.artifactLabel.setText("Artifact:  " + artifactID)
        self.artifactLabel.move(30, 60)

        logID = "none"
        self.logLabel = QLabel(self)
        self.logLabel.setText("Artifact:  " + logID)
        self.logLabel.move(30, 90)

        artifactID = "none"
        self.artifactLabel = QLabel(self)
        self.artifactLabel.setText("Artifact:  " + artifactID)
        self.artifactLabel.move(30, 60)

        self.iconLabel = QLabel(self)
        self.iconLabel.setText("Icon")
        self.iconLabel.move(30, 150)
        combo = QComboBox(self)

        combo.addItem("iconA")
        combo.addItem("iconB")
        combo.addItem("iconC")
        combo.addItem("iconD")
        combo.move(90, 150)
        combo.activated[str].connect(self.onActivated)


        self.descriptionBox = QLineEdit(self)
        self.descriptionBox.move(100,290)
        self.descriptionBox.resize(200,60)

        self.descriptionLabel = QLabel(self)
        self.descriptionLabel.setText("Description")
        self.descriptionLabel.move(30,300)

        self.saveButton = QPushButton("Save Changes", self)
        self.cancelButton = QPushButton("Cancel", self)
        self.saveButton.move(100, 360)
        self.cancelButton.move(200, 360)

        self.show()

    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()
        # self.show()