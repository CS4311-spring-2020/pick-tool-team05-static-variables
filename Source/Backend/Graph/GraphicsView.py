from PyQt5.QtWidgets import QGraphicsView
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from Source.Backend.Graph.GraphicNodeSocket import GraphicsSocket
from Source.Backend.Graph.NodeEdge import Edge

DEFAULT_MODE = 1
DRAG_MODE = 2

DEBUG = False


class GraphicsView(QGraphicsView):
    def __init__(self, grScene, parent=None):
        super().__init__(parent)
        self.grScene = grScene

        self.initUI()

        # setting scene in view
        self.setScene(self.grScene)

        # mode
        self.mode = DEFAULT_MODE

        # Settings for zooming in wheel event
        self.zoomInFactor = 1.25
        self.zoom = 10
        self.zoomClamp = True
        self.zoomStep = 1
        self.zoomRange = [0, 15]

    def initUI(self):
        # For a smoother look to the items drawn.
        self.setRenderHints(
            QPainter.Antialiasing | QPainter.HighQualityAntialiasing |
            QPainter.TextAntialiasing | QPainter.SmoothPixmapTransform)

        self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)

        # Don't show the scroll bars, but scroll automatically if needed
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.setTransformationAnchor(GraphicsView.AnchorUnderMouse)

    def mousePressEvent(self, event):
        if event.button() == Qt.MiddleButton:
            self.middleMouseButtonPress(event)
        elif event.button() == Qt.LeftButton:
            self.leftMouseButtonPress(event)
        elif event.button() == Qt.RightButton:
            self.rightMouseButtonPress(event)
        else:
            super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MiddleButton:
            self.middleMouseButtonRelease(event)
        elif event.button() == Qt.LeftButton:
            self.leftMouseButtonRelease(event)
        elif event.button() == Qt.RightButton:
            self.rightMouseButtonRelease(event)
        else:
            super().mouseReleaseEvent(event)

    def middleMouseButtonPress(self, event):
        if DEBUG: print("MMB pressed")
        releaseEvent = QMouseEvent(QEvent.MouseButtonRelease, event.localPos(), event.screenPos(),
                                   Qt.LeftButton, Qt.NoButton, event.modifiers())
        super().mouseReleaseEvent(releaseEvent)
        self.setDragMode(QGraphicsView.ScrollHandDrag)
        fakeEvent = QMouseEvent(event.type(), event.localPos(), event.screenPos(), Qt.LeftButton,
                                event.buttons() | Qt.LeftButton, event.modifiers())
        super().mousePressEvent(fakeEvent)

    def middleMouseButtonRelease(self, event):
        if DEBUG: print("MMB release")
        fakeEvent = QMouseEvent(event.type(), event.localPos(), event.screenPos(), Qt.LeftButton, event.buttons() &
                                -Qt.LeftButton, event.modifiers())
        super().mouseReleaseEvent(fakeEvent)
        self.setDragMode(QGraphicsView.NoDrag)

    def leftMouseButtonPress(self, event):

        item = self.getItemAtClicked(event)

        self.last_left_click_scene_pos = self.mapToScene(event.pos())

        # store position of last left click
        if type(item) is GraphicsSocket:
            if self.mode == DEFAULT_MODE:
                self.mode = DRAG_MODE
                self.edgeDragStart(item)
                return

        if self.mode == DRAG_MODE:
            res = self.edgeDragEnd(item)
            if res: return

        return super().mousePressEvent(event)

    def leftMouseButtonRelease(self, event):

        # get item that which was clicked and released on
        item = self.getItemAtClicked(event)

        if self.mode == DRAG_MODE:

            res = self.edgeDragEnd(item)
            if res: return

        return super().mouseReleaseEvent(event)

    def rightMouseButtonPress(self, event):
        # Debugging purposes
        item = self.getItemAtClicked(event)
        if DEBUG: print(item)

        return super().mouseMoveEvent(event)

    def rightMouseButtonRelease(self, event):
        return super().mouseReleaseEvent(event)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_S and event.modifiers() & Qt.ControlModifier:
            self.grScene.scene.loadFromFile("graph.json.txt")
        elif event.key() == Qt.Key_T and event.modifiers() & Qt.ControlModifier:
            self.grScene.scene.saveToFile("graph.json.txt")
        else:
            super().keyPressEvent(event)

    def mouseMoveEvent(self, event):
        # continually feed coordinate position for the "dragging edge" to get drawn
        if self.mode == DRAG_MODE:
            if DEBUG: print("GraphicsView::MouseEvent: DragMode: ", DRAG_MODE)
            pos = self.mapToScene(event.pos())
            if DEBUG: print("GraphicsView::MouseEvent: Pos: ", pos)
            self.dragEdge.grEdge.setDestination(pos.x(), pos.y())
            self.dragEdge.grEdge.update()
        super().mouseMoveEvent(event)

    def getItemAtClicked(self, event):
        pos = event.pos()
        obj = self.itemAt(pos)
        return obj

    def edgeDragStart(self, item):
        if DEBUG: print("In edge drag start")
        self.previousEdge = item.socket.edge
        self.last_start_socket = item.socket

        if DEBUG: print("GraphicsView::EdgeDragStart: previousedge: ", item.socket.edge,
                        " last stat socket: ", self.last_start_socket)

        self.dragEdge = Edge(self.grScene.scene, item.socket, None, "None")
        if DEBUG: print("after dragedge")

    def edgeDragEnd(self,item):
        if DEBUG: print("IN Edge Drag End")
        self.mode = DEFAULT_MODE

        if type(item) is GraphicsSocket:
            self.dragEdge.start_socket = self.last_start_socket
            self.dragEdge.end_socket = item.socket

            self.dragEdge.start_socket.setConnectedEdge(self.dragEdge)
            self.dragEdge.end_socket.setConnectedEdge(self.dragEdge)

            self.dragEdge.updatePositions()
            return True

        self.dragEdge.remove()
        self.dragEdge = None

        if self.previousEdge is not None:
            self.previousEdge.start_socket.edge = self.previousEdge

        return False

    # Implementing zooming in and zooming out with the middle scroll button on a mouse
    def wheelEvent(self, event):
        # calculate our zoom factor
        zoomOutFactor = 1 / self.zoomInFactor

        # calculate zoom
        if event.angleDelta().y() > 0:
            zoomFactor = self.zoomInFactor
            self.zoom += self.zoomStep
        else:
            zoomFactor = zoomOutFactor
            self.zoom -= self.zoomStep

        # set limit to the amount of zoom
        clamped = False
        if self.zoom < self.zoomRange[0]: self.zoom, clamped = self.zoomRange[0], True
        if self.zoom > self.zoomRange[1]: self.zoom, clamped = self.zoomRange[1], True

        # set the scene scale
        if not clamped or self.zoomClamp is False:
            self.scale(zoomFactor, zoomFactor)
