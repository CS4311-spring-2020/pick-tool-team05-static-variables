
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QLabel, QDesktopWidget, QComboBox, QFileDialog, QAction


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

        # hard coded need to combine with others code
        nodeID = "1-004"
        self.idLabel = QLabel(self)
        self.idLabel.setText("ID " + nodeID)
        self.idLabel.move(30, 30)

        # hard coded need to combine with others code
        sourceID = "C:\Documents\Teams"
        self.sourceLabel = QLabel(self)
        self.sourceLabel.setText("Source:  ")
        self.sourceLabel.move(30, 60)
        self.sourceBox = QLineEdit(self)
        self.sourceBox.setText(sourceID)
        self.sourceBox.move(100, 55)


        # hard coded need to combine with others code
        self.logLabel = QLabel(self)
        self.logLabel.setText("Log Entry:  ")
        self.logLabel.move(30, 90)
        combo = QComboBox(self)
        combo.addItem("sigA")
        combo.addItem("sigB")
        combo.addItem("sigC")
        combo.move(100, 83)
        combo.activated[str].connect(self.onActivated)

        # hard coded need to combine w/ others code
        nameID = "Detection"
        self.nameLabel = QLabel(self)
        self.nameLabel.setText("Name:  ")
        self.nameLabel.move(30, 120)
        self.nameBox = QLineEdit(self)
        self.nameBox.setText(nameID)
        self.nameBox.move(100, 115)

        # hardcoded need to combine w/ others code
        timeID = "05:23    09/10/19"
        self.timeLabel = QLabel(self)
        self.timeLabel.setText("Timestamp:  ")
        self.timeLabel.move(30, 150)
        self.timeBox = QLineEdit(self)
        self.timeBox.setText(timeID)
        self.timeBox.move(100, 145)


        # hard coded need to combine with others code
        eventID = "Blue"
        self.eventLabel = QLabel(self)
        self.eventLabel.setText("Event Type:  ")
        self.eventLabel.move(30, 180)
        self.eventBox = QLineEdit(self)
        self.eventBox.setText(eventID)
        self.eventBox.move(100, 175)

        # hard coded need to combine with others code
        creatorID = "White"
        self.creatorLabel = QLabel(self)
        self.creatorLabel.setText("Creator:  ")
        self.creatorLabel.move(30, 210)
        self.creatorBox = QLineEdit(self)
        self.creatorBox.setText(creatorID)
        self.creatorBox.move(100, 205)


        # hard coded need to combine with others code
        self.iconLabel = QLabel(self)
        self.iconLabel.setText("Icon")
        self.iconLabel.move(30, 240)
        combo = QComboBox(self)
        combo.addItem("iconA")
        combo.addItem("iconB")
        combo.addItem("iconC")
        combo.addItem("iconD")
        combo.move(90, 240)
        combo.activated[str].connect(self.onActivated)

        self.descriptionBox = QLineEdit(self)
        self.descriptionBox.move(100,290)
        self.descriptionBox.resize(200,60)

        self.descriptionLabel = QLabel(self)
        self.descriptionLabel.setText("Description")
        self.descriptionLabel.move(30,300)

        self.importButton = QPushButton("Import...", self)
        self.importButton.move(190, 238)
        self.importButton.clicked.connect(self.file_open)


        self.saveButton = QPushButton("Save Changes", self)
        self.saveButton.move(100, 360)
        self.saveButton.clicked.connect(self.close)

        self.cancelButton = QPushButton("Cancel", self)
        self.cancelButton.move(200, 360)
        self.cancelButton.clicked.connect(self.close)

        self.show()

    def file_open(self):
        name, _ = QFileDialog.getOpenFileName(self, 'Open File', options=QFileDialog.DontUseNativeDialog)
        file = open(name, 'r')

    # for dropdown menu
    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()
        # self.show()