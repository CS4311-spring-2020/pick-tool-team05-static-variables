from PyQt5.QtWidgets import (QWidget, QGridLayout, QGroupBox, QVBoxLayout, QTableWidget, QTableWidgetItem)
from PyQt5.QtGui import QIcon


class VectorConfiguration(QWidget):

    def __init__(self):
        super(VectorConfiguration, self).__init__()

        self.create_grid_fields()
        self.show()

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.grid_fields)
        self.setLayout(main_layout)

        self.setWindowTitle("Vector Configuration")
        self.setWindowIcon(QIcon("../Resources/Images/paper-write.png"))

    def create_grid_fields(self):
        self.grid_fields = QGroupBox("Vector Configuration")
        layout = QGridLayout()

        self.grid_fields.setLayout(layout)

    # (TODO) Finish window, connect buttons and process info.
