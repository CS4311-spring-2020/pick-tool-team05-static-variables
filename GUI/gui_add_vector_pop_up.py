from PyQt5.QtWidgets import (QWidget, QDesktopWidget, QLabel, QLineEdit, QTextEdit, QGridLayout)
from PyQt5.QtGui import QIcon


class AddVectorPopUp(QWidget):

    def __init__(self):
        super().__init__()

        self.init_add_vector_pop_up()

    def init_add_vector_pop_up(self):
        self.setWindowTitle("Add Vector")
        self.setWindowIcon(QIcon("../Resources/Images/add-square.png"))
        self.set_window()
        self.show()

    def set_window(self):
        v_name = QLabel("Name*")
        v_description = QLabel("Description")

        e_v_name = QLineEdit()
        e_v_description = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(v_name, 1, 0)
        grid.addWidget(e_v_name, 1, 1)

        grid.addWidget(v_description, 2, 0)
        grid.addWidget(e_v_description, 2, 1)

        self.setLayout(grid)

        window = self.frameGeometry()
        win_center = QDesktopWidget().availableGeometry().center()
        window.moveCenter(win_center)
        self.move(window.topLeft())
