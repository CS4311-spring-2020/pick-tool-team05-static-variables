from PyQt5.QtWidgets import (QWidget, QGridLayout, QGroupBox,
                             QLabel, QLineEdit, QPushButton,
                             QVBoxLayout, QCheckBox, QDesktopWidget)
from PyQt5.QtGui import QIcon


class TeamConfiguration(QWidget):

    def __init__(self):
        super(TeamConfiguration, self).__init__()

        self.launch_connect_btn()
        self.create_grid_fields()
        self.show()

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.grid_fields)
        self.setLayout(main_layout)

        self.setWindowTitle("Team Configuration")
        self.setWindowIcon(QIcon("../Resources/Images/paper-write.png"))

        self.resize(400, 300)
        r = self.frameGeometry()
        p = QDesktopWidget().availableGeometry().center()
        r.moveCenter(p)
        self.move(r.topLeft())

    def create_grid_fields(self):
        self.grid_fields = QGroupBox("Team Configuration")
        layout = QGridLayout()

        check_box_lead = QCheckBox("Lead")

        lead_ip = QLabel("Lead IP address:")
        e_lead_ip = QLineEdit()

        established_connections = QLabel("No. of established connections to the lead's IP address:")

        connect_btn = QPushButton("Connect")
        connect_btn.setCheckable(True)
        connect_btn.clicked.connect(self.launch_connect_btn)

        layout.addWidget(check_box_lead, 0, 1)
        layout.addWidget(lead_ip, 0, 2)
        layout.addWidget(e_lead_ip, 0, 3)
        layout.addWidget(established_connections, 1, 1)

        layout.addWidget(connect_btn, 2, 2)

        self.grid_fields.setLayout(layout)

    def launch_connect_btn(self):
        self.hide()
