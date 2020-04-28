from PyQt5.QtWidgets import *

DEBUG = False


# widget that will be extend to all corners that displays Qlabels and Qline edits with the information from the node
class NodeContentWidget(QWidget):
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
            if DEBUG: print("key: ", key)
            if DEBUG: print(" self.key: ", self.key)
            # self.key.setStyleSheet("QLabel {background-color:grey;}")
            visibleStat = self.key.isVisible()
            if DEBUG: print("  self.key.isVisible: ", visibleStat)
            self.info = QLineEdit(self.node_info[key])
            if DEBUG: print("  self.info: ", self.info)
            self.layout.addWidget(self.key, posx, labelPosy)
            if DEBUG: print("    self.layout.addWidget: ", self.key, " ", posx, " ", labelPosy)
            self.layout.addWidget(self.info, posx, posy)
            if DEBUG: print("    self.layout.addWidget: ", self.info, " ", posx, " ", labelPosy)
            posx += 1


