from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

""" It is an abstract class that takes an edge as a parameter, sets settings for drawing an edge and makes it selectable
The edge is drawn under the socket. Overwrites original QGraphics paint method. Children classes need to overwrite 
update path.
"""


class GraphicsEdge(QGraphicsPathItem):
    def __init__(self, edge, parent=None):
        super().__init__(parent)

        self.edge = edge

        # settings
        # default pen
        self._color = QColor("#001000")
        self._pen = QPen(self._color)
        self._pen.setWidth(2.0)

        # selected pen
        self._color_selected = QColor("#0ff000")
        self._pen_selected = QPen(self._color_selected)
        self._pen_selected.setWidth(2.0)

        self.setFlag(QGraphicsItem.ItemIsSelectable)

        self.setZValue(-1)

    def setSource(self, x, y):
        self.posSource = [x, y]

    def setDestination(self, x, y):
        self.posDestination = [x, y]

    def paint(self, painter, QStyleOptionGraphicsItem, widget=None):
        self.updatePath()

        painter.setPen(self._pen if not self.isSelected() else self._pen_selected)
        painter.setBrush(Qt.NoBrush)
        painter.drawPath(self.path())

    def updatePath(self):
        """ Will handle drawing QPainterPath from point A to point B """
        raise NotImplemented("This method needs to be overwritten in a child class")


class GraphicsEdgeDirect(GraphicsEdge):
    def updatePath(self):
        path = QPainterPath(QPointF(self.posSource[0], self.posSource[1]))
        path.lineTo(self.posDestination[0], self.posDestination[1])
        self.setPath(path)

