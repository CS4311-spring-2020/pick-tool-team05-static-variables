from PyQt5.QtWidgets import QWidget, QDesktopWidget, QPushButton, QLabel
from PyQt5.QtGui import QIcon, QPixmap


class Launcher(QWidget):

    def __init__(self):
        super().__init__()

        self.init_launcher()

    def init_launcher(self):
        self.setWindowTitle("PMR Insight Collective Knowledge Launcher")
        self.setWindowIcon(QIcon("../Resources/Images/view.png"))

        self.set_size()
        self.set_buttons()
        self.show()

    def set_size(self):
        self.resize(450, 500)
        f_window = self.frameGeometry()
        window = QDesktopWidget().availableGeometry().center()
        f_window.moveCenter(window)
        self.move(f_window.topLeft())
        'Sets the background picture found inside resources'
        #set_pic = QLabel(self)
        #background_icon = QPixmap("../Resources/Images/eye_logo.png")
        #set_pic.setPixmap(background_icon)
        #self.resize(background_icon.width(), background_icon.height())

    def set_buttons(self):
        btn_connect = QPushButton("Connect", self)
        btn_connect.move(125, 350)
        'btn_connect.frameGeometry()'

        btn_host = QPushButton("Host", self)
        btn_host.move(275, 350)

        btn_cancel = QPushButton("Cancel", self)
        btn_cancel.move(200, 400)


'''buttons are not are relative to window size, when it opens they are somewhat in the right position but whe the window is set to full screen the lack
    of not having it anchored to a relative position in the window becomes apparent.'''

'''
    This is a way of connecting a button, there for sure are more elegant and better ways.

        btn_cancel.clicked.connect(self.button_clicked)
        btn_host.clicked.connect(self.button_clicked)
        btn_connect.clicked.connect(self.button_clicked)

    def button_clicked(self):

        sender = self.sender()
        self.
'''


