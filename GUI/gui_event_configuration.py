from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout, QDesktopWidget)


class EventConfiguration(QWidget):

    def __init__(self):
        super().__init__()

        self.init_event_configuration()

    def init_event_configuration(self):
        self.setWindowTitle("Event Configuration")
        # self.setWindowIcon()
        self.set_window()
        self.show()

    def set_window(self):
        e_name = QLabel('Event Name*')
        e_description = QLabel("Event Description")
        d_path = QLabel("Directory Path*")
        d_one = QLabel("Directory 1*")
        d_two = QLabel("Directory 2*")
        d_three = QLabel("Directory 3*")
        s_date = QLabel("Start Date*")
        s_time = QLabel("Start Time*")
        e_date = QLabel("End Date*")
        e_time = QLabel("End Time*")

        e_name_edit = QLineEdit()
        e_e_description = QTextEdit()
        e_d_path = QLineEdit()
        e_d_one = QLineEdit()
        e_d_two = QLineEdit()
        e_d_three = QLineEdit()
        e_s_date = QLineEdit()
        e_s_time = QLineEdit()
        e_e_date = QLineEdit()
        e_e_time = QLineEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(e_name, 1, 0)
        grid.addWidget(e_name_edit, 1, 1)

        grid.addWidget(e_description, 2, 0)
        grid.addWidget(e_e_description, 2, 1)

        grid.addWidget(d_path, 3, 0)
        grid.addWidget(e_d_path, 3, 1)

        grid.addWidget(d_one, 4, 0)
        grid.addWidget(e_d_one, 4, 1)

        grid.addWidget(d_two, 5, 0)
        grid.addWidget(e_d_two, 5, 1)

        grid.addWidget(d_three, 6, 0)
        grid.addWidget(e_d_three, 6, 1)

        grid.addWidget(s_date, 7, 0)
        grid.addWidget(e_s_date, 7, 1)

        grid.addWidget(s_time, 8, 0)
        grid.addWidget(e_s_time, 8, 1)

        grid.addWidget(e_date, 9, 0)
        grid.addWidget(e_e_date, 9, 1)

        grid.addWidget(e_time, 10, 0)
        grid.addWidget(e_e_time, 10, 1)

        self.setLayout(grid)
        # sets window relative to desktop and the commented code in the bottom hardcodes the location
        window = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        window.moveCenter(center_point)
        self.move(window.topLeft())

        # self.setGeometry(600, 250, 450, 450)
