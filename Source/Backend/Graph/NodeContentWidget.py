from PyQt5.QtWidgets import *

DEBUG = False


# widget that will be extend to all corners that has a label and text edit
class NodeContentWidget(QWidget):
    def __init__(self, parent=None):
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
            newKey = key + ":"
            self.key = QLabel(newKey)
            if DEBUG : print("key: ", key)
            if DEBUG : print(" self.key: ", self.key)
            # self.key.setStyleSheet("QLabel {background-color:grey;}")
            visibleStat = self.key.isVisible()
            if DEBUG : print("  self.key.isVisible: ", visibleStat)
            self.info = QLineEdit(self.node_content[key])
            if DEBUG : print("  self.info: ", self.info)
            self.layout.addWidget(self.key, posx, labelPosy)
            if DEBUG : print("    self.layout.addWidget: ", self.key, " ", posx, " ", labelPosy)
            self.layout.addWidget(self.info, posx, posy)
            if DEBUG: print("    self.layout.addWidget: ", self.info, " ", posx, " ", labelPosy)
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
