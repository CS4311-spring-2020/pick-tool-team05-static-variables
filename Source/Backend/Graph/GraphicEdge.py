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
        #--- regular pen properties ---#
        self._color = QColor("#001000")
        self._pen = QPen(self._color)
        self._pen.setWidthF(2.0)

        # --- selected pen properties ---#
        self._color_selected = QColor("#0ff000")
        self._pen_selected = QPen(self._color_selected)
        self._pen_selected.setWidthF(2.0)

        # --- dragging pen properties ---#
        self._pen_dragging = QPen(self._color)
        self._pen_dragging.setStyle(Qt.DashDotLine)
        self._pen_dragging.setWidthF(2.0)

        self.setFlag(QGraphicsItem.ItemIsSelectable)

        # sets drawing behind anything else drawn
        self.setZValue(-1)

    def setSource(self, x, y):
        self.posSource = [x, y]

    def setDestination(self, x, y):
        self.posDestination = [x, y]

    def paint(self, painter, QStyleOptionGraphicsItem, widget=None):
        self.updatePath()

        if self.edge.end_socket is None:
            painter.setPen(self._pen_dragging)
        else:
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

