from PyQt5.QtWidgets import (QWidget, QDesktopWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
                             QPushButton, QCheckBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon


class VectorConfiguration2(QWidget):
    def __init__(self):
        super(VectorConfiguration2, self).__init__()
        self.ui()

    def ui(self):
        self.resize(500, 230)
        self.setWindowTitle("Vector Configuration")
        self.setWindowIcon(QIcon("../Resources/Images/paper-write.png"))

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        self.create_table()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.table)
        self.layout.setAlignment(Qt.AlignCenter)
        self.setLayout(self.layout)

        # Buttons
        add_button = QPushButton("Add", self)
        add_button.clicked.connect(self.launch_add_btn)
        add_button.move(75, 170)

        delete_button = QPushButton('Delete', self)
        delete_button.clicked.connect(self.launch_delete_btn)
        delete_button.move(195, 170)

        edit_button = QPushButton('Edit', self)
        edit_button.clicked.connect(self.launch_edit_btn)
        edit_button.move(320, 170)
        self.show()

    def create_table(self):
        self.table = QTableWidget(3, 3)
        self.table.setHorizontalHeaderLabels(["Selected", "Vector Name", "Vector Description"])
        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setStretchLastSection(True)

        for columns in range(1):
            self.pWidget = QWidget()
            self.pCheckbox = QCheckBox()
            self.pLayout = QVBoxLayout(self.pWidget)
            self.pLayout.addWidget(self.pCheckbox)
            self.pLayout.setAlignment(Qt.AlignCenter)
            self.pLayout.setContentsMargins(0, 0, 0, 0)
            self.pWidget.setLayout(self.pLayout)
            self.table.insertRow(0)
            self.table.setCellWidget(0, 0, self.pWidget)

    def launch_add_btn(self):
        self.hide()

    def launch_delete_btn(self):
        self.hide()

    def launch_edit_btn(self):
        self.hide()