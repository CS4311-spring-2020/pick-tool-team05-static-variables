from Source.Backend.Graph.GraphicNode import GraphicsNode
from Source.Backend.Graph.NodeContentWidget import NodeContentWidget
from Source.Backend.Graph.NodeSocket import *

DEBUG = False


class Node:
    def __init__(self, scene, title="Undefined Node", inputs=[], outputs=[], **content_info):
        self.scene = scene

        self.title = title

        # saves individual information of a node
        self.content_info = content_info

        # create a widget for contents of a nodes and add itself to node graphics
        self.content = NodeContentWidget()
        self.grNode = GraphicsNode(self)

        # add itself to the scene
        self.scene.addNode(self)
        self.scene.grScene.addItem(self.grNode)

        # self.grNode.title = "It is now changed"

        self.socket_spacing = 22

        self.inputs = []
        self.outputs = []

        # once node is instantiated sockets are created
        # create sockets for input and outputs
        counter = 0
        for item in inputs:
            socket = Socket(node=self, index=counter, position=LEFT_BOTTOM)
            counter += 1
            self.inputs.append(socket)

        counter = 0
        for item in outputs:
            socket = Socket(node=self, index=counter, position=RIGHT_TOP)
            counter += 1
            self.outputs.append(socket)

    @property
    def pos(self):
        return self.getNode.pos()

    def setPos(self, x, y):
        self.grNode.setPos(x, y)

    # return coordinate position of a socket as a list for updating positions inside NodeEdge
    def getSocketPosition(self, index, position):
        x = 0 if (position in(LEFT_TOP, LEFT_BOTTOM)) else self.grNode.width
        # y = index * 20
        '''
        y = (self.grNode.title_height
        + self.grNode._padding
        + self.grNode.edge_size
        + index
        * 20)
        '''
        if position in (LEFT_BOTTOM, RIGHT_BOTTOM):
            # start from bottom
            y = self.grNode.height \
                - self.grNode.edge_size \
                - self.grNode._padding \
                - index * \
                self.socket_spacing
        else:
            # from top
            y = self.grNode.title_height \
                 + self.grNode._padding \
                 + self.grNode.edge_size \
                 + index \
                 * self.socket_spacing

        return [x, y]

    def updateConnectedEdges(self):
        for socket in self.inputs + self.outputs:
            if socket.hasEdge():
                if DEBUG: print("updating")
                socket.edge.updatePositions()
            else:
                if DEBUG: print("no operation")
