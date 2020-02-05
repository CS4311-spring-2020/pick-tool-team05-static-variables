from PyQt5.QtWidgets import (QWidget, QGridLayout, QGroupBox,
                             QLabel, QLineEdit, QPushButton,
                             QVBoxLayout, QCheckBox)
from PyQt5.QtGui import QIcon


class TeamConfiguration(QWidget):

    def __init__(self):
        super(TeamConfiguration, self).__init__()

        self.create_grid_fields()
        self.show()

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.grid_fields)
        self.setLayout(main_layout)

        self.setWindowTitle("Team Configuration")
        self.setWindowIcon(QIcon("../Resources/Images/paper-write.png"))

    def create_grid_fields(self):
        self.grid_fields = QGroupBox("Team Configuration")
        layout = QGridLayout()

        check_box_lead = QCheckBox("Lead")

        lead_ip = QLabel("Lead IP address:")
        e_lead_ip = QLineEdit()

        established_connections = QLabel("No. of established connections to the lead's IP address:")
        # no_connections = QLabel()

        connect_button = QPushButton("Connect")

        layout.addWidget(check_box_lead, 0, 1)
        layout.addWidget(lead_ip, 0, 2)
        layout.addWidget(e_lead_ip, 0, 3)
        layout.addWidget(established_connections, 1, 1)
        # layout.addWidget(no_connections)
        layout.addWidget(connect_button, 2, 2)

        # layout.setColumnStretch(1, 10)
        # layout.setColumnStretch(2, 20)
        self.grid_fields.setLayout(layout)
        # (TODO) Connect Buttons, Resize to smaller window
