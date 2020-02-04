from PyQt5.QtWidgets import (QWidget, QGridLayout, QGroupBox, QLabel, QLineEdit, QPushButton, QVBoxLayout)
from PyQt5.QtGui import QIcon


class DirectoryConfiguration(QWidget):

    def __init__(self):
        super(DirectoryConfiguration, self).__init__()

        self.createGridGroupBox()
        self.show()

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.gridGroupBox)
        self.setLayout(main_layout)

        self.setWindowTitle("Directory Configuration")
        # self.setWindowIcon(QIcon("../Resources/Images/"))


    def createGridGroupBox(self):
        self.gridGroupBox = QGroupBox("Directory Configuration")
        layout = QGridLayout()

        d_path = QLabel("Root Directory:")
        d_red = QLabel("Red Team Folder:")
        d_blue = QLabel("Blue Team Folder:")
        d_white = QLabel("White Team Folder:")

        e_d_path = QLineEdit()
        e_d_red = QLineEdit()
        e_d_blue = QLineEdit()
        e_d_white = QLineEdit()

        layout.addWidget(d_path, 1, 0)
        layout.addWidget(e_d_path, 1, 1, 1, 4)

        layout.addWidget(d_red, 2, 0)
        layout.addWidget(e_d_red, 2, 1, 1, 4)

        layout.addWidget(d_blue, 3, 0)
        layout.addWidget(e_d_blue, 3, 1, 1, 4)

        layout.addWidget(d_white, 4, 0)
        layout.addWidget(e_d_white, 4, 1, 1, 4)

        start_ingestion_button = QPushButton("Start data ingestion")
        layout.addWidget(start_ingestion_button, 6, 2)

        self.gridGroupBox.setLayout(layout)

        # (TODO) Connect Button, Read, save process info, maybe change window size
