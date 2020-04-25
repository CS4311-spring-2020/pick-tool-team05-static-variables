from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class GraphicsNode(QGraphicsItem):
    def __init__(self, node, parent=None):
        super().__init__(parent)

        self.node = node
        self.content = self.node.content

        # settings
        # self.title = title
        self._title_color = Qt.black
        self._title_font = QFont("Times New Roman", 12)

        self.width = 180
        self.height = 240
        self.radius = 150

        self.edge_size = 10.0
        self.title_height = 24.0

        # offset from left side
        self._padding = 10.0

        self._pen_default = QPen(QColor("#7f000000"))
        self._pen_selected = QPen(QColor("#FFFFA637"))

        self._brush_title = QBrush(QColor("#FF515151"))
        self._brush_background = QBrush(QColor("#E3212121"))

        # init title
        self.initTitle()
        self.title = self.node.title

        """---------------------------Not Sure if I will be using something similar to this--------------------------"""

        # init sockets
        self.initSockets()

        """----------------------------------------------------------------------------------------------------------"""

        # init content
        self.initContent()

        self.initUI()

    @property
    def title(self): return self._title

    @title.setter
    def title(self, value):
        self._title = value
        self.title_item.setPlainText(self._title)

    # Give selectable and movable ability to the bounds given to the node
    def initUI(self):
        self.setFlag(QGraphicsItem.ItemIsSelectable)
        self.setFlag(QGraphicsItem.ItemIsMovable)

    def boundingRect(self):

        return QRectF(0, 0, self.width, self.height).normalized()
        '''
        return QRectF(
            -self.radius
            - self.edge_size,
            -self.radius
            - self.edge_size,
            2 * self.radius
            + self.edge_size,
            2 * self.radius
            + self.edge_size
        )
        '''
    def initTitle(self):
        self.title_item = QGraphicsTextItem(self)
        self.title_item.setDefaultTextColor(self._title_color)
        self.title_item.setFont(self._title_font)

        # sets padding to the title offset from the left
        self.title_item.setPos(self._padding, 0)
        self.title_item.setTextWidth(
            self.width
            - 2
            * self._padding
        )
        # self.title_item.setPlainText(self.title)

    def initContent(self):
        self.grContent = QGraphicsProxyWidget(self)
        self.content.setGeometry(self.edge_size, self.title_height + self.edge_size,
                                 self.width - 2 * self.edge_size, self.height - 2 * self.edge_size
                                 - self.title_height)
        self.grContent.setWidget(self.content)

    def initSockets(self):
        pass

    def paint(self, painter, QStyleOptionGraphicsItem, widget=None):

        # calculates size of title section and colors the background of the title
        path_title = QPainterPath()
        path_title.setFillRule(Qt.WindingFill)
        path_title.addRoundedRect(0, 0, self.width, self.title_height, self.edge_size, self.edge_size)
        path_title.addRect(0, self.title_height - self.edge_size, self.edge_size, self.edge_size)
        path_title.addRect(self.width - self.edge_size, self.title_height - self.edge_size, self.edge_size,
                           self.edge_size)
        painter.setPen(Qt.NoPen)
        painter.setBrush(self._brush_title)
        painter.drawPath(path_title.simplified())


        # calculates size of body of the node and paints it the background content

        path_content = QPainterPath()
        path_content.setFillRule(Qt.WindingFill)
        path_content.addRoundedRect(0, self.title_height, self.width, self.height - self.title_height, self.edge_size,
                                    self.edge_size)
        path_content.addRect(0, self.title_height, self.edge_size, self.edge_size)
        path_content.addRect(self.width - self.edge_size, self.title_height, self.edge_size, self.edge_size)
        painter.setPen(Qt.NoPen)
        painter.setBrush(self._brush_background)
        painter.drawPath(path_content.simplified())


        # (TODO) Change construction of a node to a circle like figure, might have to change dimensions further in node
        # outline
        path_outline = QPainterPath()
        # path_outline.addEllipse( self.width, self.height, self.edge_size, self.edge_size)
        path_outline.addRoundedRect(0, 0, self.width, self.height, self.edge_size, self.edge_size)
        # path_outline.addEllipse(-self.radius, -self.radius, self.radius * 2, self.radius * 2)

        # Highlights selected node
        painter.setPen(self._pen_default if not self.isSelected() else self._pen_selected)
        painter.setBrush(Qt.NoBrush)
        painter.drawPath(path_outline.simplified())
