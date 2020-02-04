import sys
from PyQt5.QtWidgets import QFrame


class gui_graph(QFrame):
    def __init__(self):
        super().__init__()

        self.main()

    def main(self):
        self.setFrameShape(QFrame.StyledPanel)

    # (TODO): Complete
    def toggleGraphView(self):
        print('hi')

    # (TODO): Complete
    def zoom(self):
        print('hello')