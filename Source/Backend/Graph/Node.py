from Source.Backend.Graph.GraphicNode import GraphicsNode


class Node:
    def __init__(self, scene, title="Undefined Node"):
        self.scene = scene

        self.title = title

        self.grNode = GraphicsNode(self, title)

        # add itself to the scene
        self.scene.addNode(self)
        self.scene.grScene.addItem(self.grNode)

        # self.grNode.title = "It is now changed"

        self.inputs = []
        self.outputs = []

