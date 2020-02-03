from PyQt5.QtWidgets import (QWidget, QGridLayout, QGroupBox,
                             QLabel, QPushButton, QVBoxLayout)
from PyQt5.QtGui import QIcon, QPixmap


class Launcher(QWidget):

    def __init__(self):
        super(Launcher, self).__init__()

        self.create_grid_buttons()
        self.show()

        label = QLabel()
        logo = QPixmap('../Resources/Images/eye_logo450.png')
        label.setPixmap(logo)
        # (TODO) Change logo position
        main_layout = QVBoxLayout()
        main_layout.addWidget(label)
        main_layout.addWidget(self.button_grid)
        self.setLayout(main_layout)

        self.setWindowTitle("PMR Insight Collective Knowledge Launcher")
        self.setWindowIcon(QIcon("../Resources/Images/view.png"))

    def create_grid_buttons(self):
        self.button_grid = QGroupBox()
        layout = QGridLayout()

        btn_connect = QPushButton("Connect", self)
        layout.addWidget(btn_connect, 0, 0)

        btn_host = QPushButton("Host", self)
        layout.addWidget(btn_host, 0, 2)

        btn_cancel = QPushButton("Cancel", self)
        layout.addWidget(btn_cancel, 2, 1)

        self.button_grid.setLayout(layout)
        # (TODO) Connect functionality to buttons.
    '''
    This is a way of connecting a button, there for sure are more elegant and better ways.

        btn_cancel.clicked.connect(self.button_clicked)
        btn_host.clicked.connect(self.button_clicked)
        btn_connect.clicked.connect(self.button_clicked)

    def button_clicked(self):

        sender = self.sender()
        self.
    '''
