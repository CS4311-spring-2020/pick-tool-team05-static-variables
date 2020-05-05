from PyQt5.QtWidgets import *

from Source.Backend.Graph.Node import Node
from Source.Backend.Graph.GraphicsView import GraphicsView
from Source.Backend.Graph.Scene import Scene


class GraphWindow(QWidget):
    def __init__(self, graph_name="Undefined Vector", parent=None):
        vector = graph_name
        super().__init__(parent)

        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 800, 600)

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        # create graphics scene
        self.scene = Scene()

        # create graphics view
        self.view = GraphicsView(self.scene.grScene, self)
        self.layout.addWidget(self.view)

    def __str__(self):
        return "<Graph Window: %s...%s>" % (hex(id(self))[2:5], hex(id(self))[:3])

    def addNode(self, **kwargs):
        if kwargs is not None:
            Node(self.scene, inputs=[1], outputs=[1], **kwargs)
        else:
            pass
