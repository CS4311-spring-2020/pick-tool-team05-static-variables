from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class GraphicsNode(QGraphicsItem):
    def __init__(self, node, title="Node Graphics Item", parent=None):
        super().__init__(parent)

        # self.title = title
        self._title_color = Qt.black
        self._title_font = QFont("Times New Roman", 12)

        self.initTitle()
        self.title = title

        self.width = 180
        self.height = 240

        self.edge_size = 10.0

        self._pen_default = QPen(QColor("#7f000000"))

        self.initUI()

    def initUI(self):
        pass

    def initTitle(self):
        self.title_item = QGraphicsTextItem(self)
        self.title_item.setDefaultTextColor(self._title_color)
        self.title_item.setFont(self._title_font)
        # self.title_item.setPlainText(self.title)

    @property
    def title(self): return self._title

    @title.setter
    def title(self, value):
        self._title = value
        self.title_item.setPlainText(self._title)

    def paint(self, painter, QStyleOptionGraphicsItem, widget=None):

        # title

        # contet

        # outline
        path_outline = QPainterPath()
        # path_outline.addEllipse(0, 0, self.width, self.height, self.edge_size, self.edge_size)
        path_outline.addRoundedRect(0, 0, self.width, self.height, self.edge_size, self.edge_size)
        painter.setPen(self._pen_default)
        painter.setBrush(Qt.NoBrush)
        painter.drawPath(path_outline.simplified())
