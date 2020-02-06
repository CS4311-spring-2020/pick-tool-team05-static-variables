from PyQt5.QtWidgets import (QWidget, QGridLayout, QGroupBox, QVBoxLayout, QTableWidget, QTableWidgetItem,
                             QPushButton, QCheckBox, QDesktopWidget)
from PyQt5.QtGui import QIcon


class VectorConfiguration(QWidget):

    def __init__(self):
        super(VectorConfiguration, self).__init__()

        self.launch_add_vector_btn()
        self.launch_edit_vector_btn()
        self.launch_delete_vector_btn()
        self.create_grid_fields()
        self.show()

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.grid_fields)
        self.setLayout(main_layout)

        self.setWindowTitle("Vector Configuration")
        self.setWindowIcon(QIcon("../Resources/Images/paper-write.png"))

        self.resize(500, 300)
        r = self.frameGeometry()
        p = QDesktopWidget().availableGeometry().center()
        r.moveCenter(p)
        self.move(r.topLeft())

    def create_grid_fields(self):
        self.grid_fields = QGroupBox("Vector Configuration")
        layout = QGridLayout()

        table = QTableWidget(4, 3)
        table.setHorizontalHeaderLabels(["Selected", "Vector Name", "Vector Description"])
        table.verticalHeader().setVisible(False)
        table.horizontalHeader().setStretchLastSection(True)

        # cb = QCheckBox()

        # layout.addWidget(table.setItem(0, 0, cb))
        # table.setItem(0, 0, cb)

        add_vector_btn = QPushButton("Add Vector")
        delete_vector_btn = QPushButton("Delete Vector")
        edit_vector_btn = QPushButton("Edit Vector")

        add_vector_btn.setCheckable(True)
        add_vector_btn.clicked.connect(self.launch_add_vector_btn)

        delete_vector_btn.setCheckable(True)
        delete_vector_btn.clicked.connect(self.launch_delete_vector_btn)

        edit_vector_btn.setCheckable(True)
        edit_vector_btn.clicked.connect(self.launch_edit_vector_btn)

        layout.addWidget(table, 0, 0, 4, 3)
        layout.addWidget(add_vector_btn, 4, 0)
        layout.addWidget(delete_vector_btn, 4, 1)
        layout.addWidget(edit_vector_btn, 4, 2)

        self.grid_fields.setLayout(layout)

    def launch_add_vector_btn(self):
        self.hide()

    def launch_delete_vector_btn(self):
        self.hide()

    def launch_edit_vector_btn(self):
        self.hide()
