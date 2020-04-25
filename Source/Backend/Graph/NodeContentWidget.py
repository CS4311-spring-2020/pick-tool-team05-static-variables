from PyQt5.QtWidgets import *


# widget that will be extend to all corners that has a label and text edit
class NodeContentWidget(QWidget):
    def __init__(self, node_content={}, parent=None):
        super().__init__(parent)

        self.node_content = {"name": "something1",
                        "time_stamp": "something2",
                        "description": "something3",
                        "log_entry_reference": "something4",
                        "log_creator": "something5",
                        "event_type": "something6",
                        "icon_type": "something7",
                        "source": "something8",}

        #self.node_info = node_content.items()

        self.initUI()

    # adds basic layout and "hardcoded" contents
    def initUI(self):
        # self.layout = QVBoxLayout()
        self.layout = QGridLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        posx = 0
        posy = 1
        labelPosy = 0
        for key in self.node_content.keys():
            self.key = QLabel(key)
            self.key.setStyleSheet("QLabel {background-color:grey;  }")
            self.info = QLineEdit(self.node_content[key])
            self.layout.addWidget(self.key, posx, labelPosy)
            self.layout.addWidget(self.info, posx, posy)
            posx += 1



        '''
        self.ID
        self.name
        self.time_stamp
        self.description
        self.log_entry_reference
        self.log_creator
        self.event_type
        self.icon_type
        self.source

        self.wdg_label = QLabel("Some Title")
        self.layout.addWidget(self.wdg_label)
        self.layout.addWidget(QTextEdit("something"))
        '''
