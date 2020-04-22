from Source.Backend.Graph.GraphicNode import GraphicsNode
from Source.Backend.Graph.NodeContentWidget import NodeContentWidget


class Node:
    def __init__(self, scene, title="Undefined Node"):
        self.scene = scene

        self.title = title

        # create a widget for contents of a nodes and add itself to node graphics
        self.content = NodeContentWidget()
        self.grNode = GraphicsNode(self)

        # add itself to the scene
        self.scene.addNode(self)
        self.scene.grScene.addItem(self.grNode)

        # self.grNode.title = "It is now changed"

        self.inputs = []
        self.outputs = []

