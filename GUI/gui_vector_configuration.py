from PyQt5.QtWidgets import (QWidget, QGridLayout, QGroupBox, QVBoxLayout)
from PyQt5.QtGui import QIcon


class VectorConfiguration(QWidget):

    def __init__(self):
        super(VectorConfiguration, self).__init__()

        self.createGridGroupBox()
        self.show()

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.gridGroupBox)
        self.setLayout(main_layout)

        self.setWindowTitle("Vector Configuration")
        # self.setWindowIcon(QIcon("../Resources/Images/"))

    def createGridGroupBox(self):
        self.gridGroupBox = QGroupBox("Vector Configuration")
        layout = QGridLayout()

        self.gridGroupBox.setLayout(layout)

    # (TODO) Finish window, connect buttons and process info.
