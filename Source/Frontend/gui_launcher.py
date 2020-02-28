from PyQt5.QtWidgets import (QWidget, QGridLayout, QGroupBox, QDesktopWidget,
                             QLabel, QPushButton, QVBoxLayout)
from PyQt5.QtGui import QIcon, QPixmap
from Source.Frontend.gui_team_configuration import TeamConfiguration


class Launcher(QWidget):

    def __init__(self):
        super(Launcher, self).__init__()

        self.launch_team_configuration_btn()
        self.launch_cancel_btn()
        self.create_grid_buttons()
        self.show()

        label = QLabel()
        logo = QPixmap('../Resources/Images/logo_large.png')
        label.setPixmap(logo)

        main_layout = QVBoxLayout()
        main_layout.addWidget(label)
        main_layout.addWidget(self.button_grid)
        self.setLayout(main_layout)

        self.setWindowTitle("PMR Insight Collective Knowledge Launcher")
        self.setWindowIcon(QIcon("../Resources/Images/logo_small.png"))

        self.resize(400, 400)
        r = self.frameGeometry()
        p = QDesktopWidget().availableGeometry().center()
        r.moveCenter(p)
        self.move(r.topLeft())

    def create_grid_buttons(self):
        self.button_grid = QGroupBox()
        layout = QGridLayout()

        btn_connect = QPushButton("Connect", self)
        layout.addWidget(btn_connect, 0, 2)
        btn_connect.setCheckable(True)
        btn_connect.clicked.connect(self.launch_team_configuration_btn)
        # btn_connect.setDefault(True)
        # btn_connect.clicked(btn)

        # btn_host = QPushButton("Host", self)
        # layout.addWidget(btn_host, 0, 2)

        btn_cancel = QPushButton("Cancel", self)
        layout.addWidget(btn_cancel, 0, 0)
        btn_cancel.setCheckable(True)
        btn_cancel.clicked.connect(self.launch_cancel_btn)

        self.button_grid.setLayout(layout)

    def launch_team_configuration_btn(self):
        self.hide()
        launch_window = TeamConfiguration()
        launch_window.show()

    def launch_cancel_btn(self):
        self.hide()
