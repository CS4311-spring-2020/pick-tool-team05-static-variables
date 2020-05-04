from Source.Backend.Graph.GraphicNode import GraphicsNode
from Source.Backend.Graph.NodeContentWidget import NodeContentWidget
from Source.Backend.Graph.NodeSocket import *

DEBUG = False


class Node:
    def __init__(self, scene, inputs=[], outputs=[], **kwargs):
        self.scene = scene

        # saves individual information of a node
        self.content_info = kwargs

        self.title = kwargs.pop('name')

        # create a widget for contents of a nodes and add itself to node graphics
        self.content = NodeContentWidget(self)
        self.grNode = GraphicsNode(self)

        # add itself to the scene
        self.scene.addNode(self)
        self.scene.grScene.addItem(self.grNode)

        self.socket_spacing = 1

        self.inputs = []
        self.outputs = []

        # once node is instantiated sockets are created
        # create sockets for input and outputs

        for item in inputs:
            socket = Socket(node=self,  socket_y_pos=TOP)
            self.inputs.append(socket)

        for item in outputs:
            socket = Socket(node=self, socket_y_pos=BOTTOM)
            self.outputs.append(socket)

    def __str__(self):
        return "<Node: %s...%s>" % (hex(id(self))[2:5], hex(id(self))[:3])

    @property
    def pos(self):
        return self.getNode.pos()

    def setPos(self, x, y):
        self.grNode.setPos(x, y)

    # return coordinate position of a socket as a list for updating positions inside NodeEdge
    def getSocketPosition(self, socket_x_position, socket_y_position):
        if socket_y_position == TOP:
            return [socket_x_position, self.grNode.height/2]
        elif socket_y_position == BOTTOM:
            return [socket_x_position, -self.grNode.height/2]
        else:
            pass

    def updateConnectedEdges(self):
        for socket in self.inputs + self.outputs:
            if socket.hasEdge():
                if DEBUG: print("updating")
                socket.edge.updatePositions()
            else:
                if DEBUG: print("no operation")
