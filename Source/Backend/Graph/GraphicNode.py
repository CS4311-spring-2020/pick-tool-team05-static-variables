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
        # self.title_height = 24.0

        self._pen_default = QPen(QColor("#7f000000"))
        self._pen_selected = QPen(QColor("#FFFFA637"))


        self.initUI()

        # Give selectable and movable ability to the bounds given to the node
    def initUI(self):
        self.setFlag(QGraphicsItem.ItemIsSelectable)
        self.setFlag(QGraphicsItem.ItemIsMovable)

    def boundingRect(self):
        return QRectF(
            0,
            0,
            2 * self.edge_size + self.width,
            2 * self.edge_size + self.height
        ).normalized()

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

        # Highlights selected node
        painter.setPen(self._pen_default if not self.isSelected() else self._pen_selected)
        painter.setBrush(Qt.NoBrush)
        painter.drawPath(path_outline.simplified())
