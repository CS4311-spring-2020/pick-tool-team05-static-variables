from PyQt5.QtWidgets import *

from Source.Backend.Graph.Node import Node
from Source.Backend.Graph.GraphicsView import GraphicsView
from Source.Backend.Graph.Scene import Scene


class GraphWindow(QWidget):
    def __init__(self, name=None, description=None, parent=None):
        super().__init__(parent)

        self.data = {
            "Graph Name": name,
            "Graph Description": description,
            "Nodes": [],
            "Relationships": []
        }
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 800, 600)

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        # create graphics scene
        self.scene = Scene()

        self.addNode()

        # create graphics view
        self.view = GraphicsView(self.scene.grScene, self)
        self.layout.addWidget(self.view)

    def addNode(self, **kwargs):
        if kwargs is not None:
            Node(self.scene, **kwargs)
        else:
            pass
