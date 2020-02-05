from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, QLineEdit, QTextEdit, QGridLayout, QGroupBox, QPushButton)
from PyQt5.QtGui import QIcon


class EventConfiguration(QWidget):

    def __init__(self):
        super(EventConfiguration, self).__init__()

        self.create_field_box()
        self.show()

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.grid_fields)

        self.setLayout(main_layout)

        self.setWindowTitle("Event Configuration")
        self.setWindowIcon(QIcon("../Resources/Images/paper-write.png"))


    def create_field_box(self):
        self.grid_fields = QGroupBox("Event Configuration")
        grid = QGridLayout()
        grid.setSpacing(10)

        e_name = QLabel('Event Name:')
        e_description = QLabel("Event Description:")
        s_date = QLabel("Start Date:")
        s_time = QLabel("Start Time:")
        e_date = QLabel("End Date:")
        e_time = QLabel("End Time:")

        e_name_edit = QLineEdit()
        e_e_description = QTextEdit()
        e_s_date = QLineEdit()
        e_s_time = QLineEdit()
        e_e_date = QLineEdit()
        e_e_time = QLineEdit()

        grid.addWidget(e_name, 1, 0)
        grid.addWidget(e_name_edit, 1, 1, 1, 4)

        grid.addWidget(e_description, 2, 0)
        grid.addWidget(e_e_description, 2, 1, 1, 4)

        grid.addWidget(s_date, 4, 0)
        grid.addWidget(e_s_date, 4, 1)

        grid.addWidget(s_time, 5, 0)
        grid.addWidget(e_s_time, 5, 1)

        grid.addWidget(e_date, 5, 3)
        grid.addWidget(e_e_date, 5, 4)

        grid.addWidget(e_time, 4, 3)
        grid.addWidget(e_e_time, 4, 4)

        # grid.setColumnStretch(1, 10)

        save_event_button = QPushButton("Save Event")

        grid.addWidget(save_event_button, 8, 2)

        self.grid_fields.setLayout(grid)

        # (TODO) read,Save, and Process information from fields, Change name ok button and connect it
