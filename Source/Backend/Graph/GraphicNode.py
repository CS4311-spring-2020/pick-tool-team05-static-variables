from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import math


class GraphicsNode(QGraphicsItem):
    def __init__(self, node, parent=None):
        super().__init__(parent)

        self.node = node
        self.content = self.node.content

        # settings
        self.radius = 150
        self.innerRectangleSize = self.radius * math.sin(45)
        self.edge_size = 10.0

        self.width = (self.innerRectangleSize * 2) - (self.edge_size * 2)
        self.height = (self.innerRectangleSize * 2) - (self.edge_size * 2)

        self.title_height = 24.0

        # offset from left side
        self._padding = 10.0

        self._pen_default = QPen(QColor("#7f000000"))
        self._pen_selected = QPen(QColor("#FFFFA637"))

        self._brush_title = QBrush(QColor("#FF515151"))
        self._brush_background = QBrush(QColor("#E3212121"))

        # init content
        self.initContent()

        self.initUI()

    # update and redraw edges connected to a socket when a node is moved by the mouse
    def mouseMoveEvent(self, event):
        super().mouseMoveEvent(event)
        self.node.updateConnectedEdges()

    # Give selectable and movable ability to the bounds given to the node
    def initUI(self):
        self.setFlag(QGraphicsItem.ItemIsSelectable)
        self.setFlag(QGraphicsItem.ItemIsMovable)

    def boundingRect(self):
        """ defines draggable surface of a node """
        return QRectF(-self.innerRectangleSize + self.edge_size,
                      -self.innerRectangleSize + self.edge_size,
                      (self.innerRectangleSize * 2) - (self.edge_size * 2),
                      (self.innerRectangleSize * 2) - (self.edge_size * 2)).normalized()

    def initContent(self):
        self.grContent = QGraphicsProxyWidget(self)

        self.content.setGeometry(-self.innerRectangleSize + (self.edge_size * 2.5),
                                 -self.innerRectangleSize + (self.edge_size * 2.5),
                                 (self.innerRectangleSize * 2) - (self.edge_size * 5),
                                 self.innerRectangleSize - (self.edge_size * 5) + self.title_height)

        self.grContent.setWidget(self.content)

    def paint(self, painter, QStyleOptionGraphicsItem, widget=None):
        # outline
        path_outline = QPainterPath()
        path_outline.addEllipse(-self.radius, -self.radius, self.radius * 2, self.radius * 2)

        # Highlights selected node
        painter.setPen(self._pen_default if not self.isSelected() else self._pen_selected)
        painter.setBrush(Qt.NoBrush)
        painter.drawPath(path_outline.simplified())
