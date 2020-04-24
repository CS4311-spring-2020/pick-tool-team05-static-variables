from PyQt5.QtWidgets import QGraphicsScene

from Source.Backend.Graph.GraphicsScene import GraphicsScene


class Scene(GraphicsScene):
    def __init__(self):
        self.nodes = []
        self.edges = []

        self.scene_width = 6400
        self.scene_height = 6400

        self.initUI()

    def initUI(self):
        self.grScene = GraphicsScene(self)
        # self.grScene = QDMGraphicsScene(self)
        # self.grScene.setScene(self.scene_width, self.scene_height)

    def addNode(self, node):
        self.nodes.append(node)

    def addEdge(self, edge):
        self.addEdge.append(edge)

    def removeNode(self, node):
        self.node.remove(node)

    def removeEdge(self, edge):
        self.edges.remove(edge)
