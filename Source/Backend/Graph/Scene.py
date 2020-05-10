from Source.Backend.Graph.GraphicsScene import GraphicsScene
from Source.Backend.Graph.Serializable import Serializable


import json


class Scene(Serializable):
    def __init__(self):
        super().__init__()

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

    def clear(self):
        while len(self.nodes) > 0:
            self.nodes[0].remove()

    def saveToFile(self, filename):
        print("In save file function")
        with open(filename, "w") as file:
            print(" Inside openfile")
            file.write(json.dumps(self.serialize(), indent=4))
            print("Saving to", filename, "was successful")

    def serialize(self):
        nodes, edges = [], []
        for node in self.nodes: nodes.append(node.serialize())
        for edge in self.edges: edges.append(edge.serialize())

        return {
            "id": id(self),
            "scene_width": self.scene_width,
            "scene_height": self.scene_height,
            "nodes": nodes,
            "edges": edges
        }