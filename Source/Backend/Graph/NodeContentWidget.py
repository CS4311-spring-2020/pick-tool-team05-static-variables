from PyQt5.QtWidgets import *
from Source.Backend.Graph.Serializable import Serializable


# widget that will be extend to all corners that displays Qlabels and Qline edits with the information from the node
class NodeContentWidget(QWidget, Serializable):
    def __init__(self, node, parent=None):
        self.node_info = node.content_info
        super().__init__(parent)

        self.initUI()

    # adds basic layout and "hardcoded" contents
    def initUI(self):

        self.layout = QGridLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        posx = 0
        posy = 1
        labelPosy = 0

        for key in self.node_info.keys():
            newKey = key + ":"
            self.key = QLabel(newKey)
            # self.key.setStyleSheet("QLabel {background-color:grey;}")
            self.info = QLineEdit(self.node_info[key])
            self.layout.addWidget(self.key, posx, labelPosy)
            self.layout.addWidget(self.info, posx, posy)
            posx += 1

    def serialize(self):
        return {
            "Node Visibility": self.node_info.get("Node Visibility"),
            "Node ID": self.node_info.get("Node ID"),
            "Node Time Stamp": self.node_info.get("Node Time Stamp"),
            "log_entry_reference": self.node_info.get("log_entry_reference"),
            "log_creator": self.node_info.get("log_creator"),
            "event_type": self.node_info.get("event_type"),
            "icon_type": self.node_info.get("icon_type"),
            "source": self.node_info.get("source"),
            "Node Description": self.node_info.get("Node Description")
        }


