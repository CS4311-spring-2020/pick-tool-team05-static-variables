from PyQt5.QtWidgets import (QDialog, QVBoxLayout, QDialogButtonBox, QLabel, QLineEdit, QTextEdit, QGridLayout,
                             QGroupBox, QHBoxLayout, QFormLayout, QScrollArea, QPushButton)


class EventConfiguration(QDialog):

    def __init__(self):
        super(EventConfiguration, self).__init__()

        self.create_horizontal_message()
        self.create_field_box()
        self.create_vector_box()
        self.show()

        button_options = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        button_options.accepted.connect(self.accept)
        button_options.rejected.connect(self.reject)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.grid_fields)
        main_layout.addWidget(self.form_vector_box)
        main_layout.addWidget(self.horizontal_message)
        main_layout.addWidget(button_options)
        self.setLayout(main_layout)

        self.setWindowTitle("Event Configuration")
        # self.setWindowIcon()

    def create_horizontal_message(self):
        self.horizontal_message = QGroupBox("Message:")
        layout = QHBoxLayout()

        message = QLabel("Fields with * next to them are required before configuration can begin.")
        layout.addWidget(message)
        self.horizontal_message.setLayout(layout)

    def create_field_box(self):
        self.grid_fields = QGroupBox("Fields:")
        grid = QGridLayout()
        grid.setSpacing(10)

        e_name = QLabel('Event Name* :')
        e_description = QLabel("Event Description:")
        d_path = QLabel("Directory Path* :")
        d_one = QLabel("Directory 1* :")
        d_two = QLabel("Directory 2* :")
        d_three = QLabel("Directory 3* :")
        s_date = QLabel("Start Date* :")
        s_time = QLabel("Start Time* :")
        e_date = QLabel("End Date* :")
        e_time = QLabel("End Time* :")

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

        grid.addWidget(e_name, 1, 0)
        grid.addWidget(e_name_edit, 1, 1, 1, 4)

        grid.addWidget(e_description, 2, 0)
        grid.addWidget(e_e_description, 2, 1, 1, 4)

        grid.addWidget(d_path, 3, 0)
        grid.addWidget(e_d_path, 3, 1, 1, 4)

        grid.addWidget(d_one, 4, 0)
        grid.addWidget(e_d_one, 4, 1, 1, 4)

        grid.addWidget(d_two, 5, 0)
        grid.addWidget(e_d_two, 5, 1, 1, 4)

        grid.addWidget(d_three, 6, 0)
        grid.addWidget(e_d_three, 6, 1, 1, 4)

        grid.addWidget(s_date, 7, 0)
        grid.addWidget(e_s_date, 7, 1)

        grid.addWidget(s_time, 8, 0)
        grid.addWidget(e_s_time, 8, 1)

        grid.addWidget(e_date, 7, 3)
        grid.addWidget(e_e_date, 7, 4)

        grid.addWidget(e_time, 8, 3)
        grid.addWidget(e_e_time, 8, 4)

        grid.setColumnStretch(1, 10)
        self.grid_fields.setLayout(grid)

    def create_vector_box(self):
        self.form_vector_box = QGroupBox("Vectors:")
        layout = QFormLayout()

        vector_scroll = QScrollArea()
        b1 = QPushButton("Add")  # Might want ot resize add button
        # self.b1.clicked.connect(lamda:self.add_vector(self.b1))

        layout.addWidget(vector_scroll)
        layout.addWidget(b1)
        self.form_vector_box.setLayout(layout)

        # (TODO) read,Save, and Process information from fields, Change name ok button and connect it
