from Source.Backend.Graph.GraphicsScene import GraphicsScene


class Scene:
    def __init__(self):
        self.nodes = []
        self.edges = []

        self.scene_width = 6400
        self.scene_height = 6400

        self.initUI()

    def initUI(self):
        self.grScene = GraphicsScene(self)

    def addNode(self, node):
        self.nodes.append(node)

    def addEdge(self, edge):
        self.edges.append(edge)

    def removeNode(self, node):
        self.nodes.remove(node)

    def removeEdge(self, edge):
        self.edges.remove(edge)

