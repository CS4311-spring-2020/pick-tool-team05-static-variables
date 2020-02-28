from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QLabel, QDesktopWidget, QComboBox, QFileDialog, QSplitter, \
    QHBoxLayout, QListWidget, QGridLayout, QMessageBox, QTableWidget, QVBoxLayout, QGroupBox, QFrame
from PyQt5.uic.properties import QtGui


class EditNode(QFrame):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout()
        self.relationships = RelationshipsTable()
        self.node_info = NodeInfo()
        self.main()

    def main(self):
        self.setWindow()
        self.setLayout(self.layout)

        splitH = QSplitter(Qt.Horizontal)
        splitH.addWidget(self.node_info)
        splitH.addWidget(self.relationships)
        splitH.setStretchFactor(1, 1)
        splitH.setSizes([300, 300])

        self.layout.addWidget(splitH)
        self.show()

    def setWindow(self):
        self.setWindowTitle('Edit Node')
        self.resize(800, 300)
        r = self.frameGeometry()
        p = QDesktopWidget().availableGeometry().center()
        r.moveCenter(p)
        self.move(r.topLeft())


class RelationshipsTable(QFrame):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout()
        self.table = QTableWidget()
        self.main()

    def main(self):
        self.setLayout(self.layout)
        self.initTable()

    def initTable(self):
        self.table.setRowCount(5)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Relationship ID", "Child", "Label"])
        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.layout.addWidget(self.table)


class NodeInfo(QFrame):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout()
        self.main()
        self.show()

    def main(self):
        self.setLayout(self.layout)
        self.nodeInfo()

    def nodeInfo(self):
        self.grid = QGridLayout()
        self.layout.addLayout(self.grid)
        # has the node info
        nodeID = "1-004"
        self.grid.addWidget(QLabel("Node ID: " + nodeID),0,0)

        #row, col
        # hard coded need to combine with others code
        self.grid.addWidget(QLabel("Log Entry"),1,0)
        combo = QComboBox(self)
        self.grid.addWidget((combo),1,1)
        combo.addItem("sigA")
        combo.addItem("sigB")
        combo.addItem("sigC")
        combo.activated[str].connect(self.onActivated)

        # hard coded need to combine w/ others code
        nameID = "Detection"
        self.grid.addWidget(QLabel("Name: "),2,0)
        self.grid.addWidget(QLineEdit(nameID),2,1)

        # hardcoded need to combine w/ others code
        timeID = " 05:23    09/10/19"
        self.grid.addWidget(QLabel("Timestamp :"),3,0)
        self.grid.addWidget(QLineEdit(timeID),3,1)

        # hard coded need to combine with others code
        eventID = "Blue"
        self.grid.addWidget(QLabel("Event Type: "),4,0)
        self.grid.addWidget(QLineEdit(eventID),4,1)

        # hard coded need to combine with others code
        creatorID = "White"
        self.grid.addWidget(QLabel("Creator: "),5,0)
        self.grid.addWidget(QLineEdit(creatorID),5,1)

        # hard coded need to combine with others code
        self.grid.addWidget(QLabel("Icon "),6,0)
        combo2 = QComboBox(self)
        self.grid.addWidget((combo2),6,1)
        combo2.addItem("iconA")
        combo2.addItem("iconB")
        combo2.addItem("iconC")
        combo2.addItem("iconD")
        combo2.activated[str].connect(self.onActivated)

        self.importButton = QPushButton("Import",self)
        self.grid.addWidget((self.importButton),6,2)
        self.importButton.clicked.connect(self.file_open)

        self.grid.addWidget(QLabel("Description"),7,0)
        self.grid.addWidget(QLineEdit(self),7,1)

        self.saveButton = QPushButton("Save", self)
        self.grid.addWidget((self.saveButton),8,0)
        self.saveButton.clicked.connect(self.close)

        self.cancelButton = QPushButton("Cancel", self)
        self.grid.addWidget((self.cancelButton),8,1)
        self.cancelButton.clicked.connect(self.close)


    def file_open(self):
        name, _ = QFileDialog.getOpenFileName(self, 'Open File', options=QFileDialog.DontUseNativeDialog)
        file = open(name, 'r')

    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()