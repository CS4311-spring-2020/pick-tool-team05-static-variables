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

        self.socket_spacing = 1

        self.inputs = []
        self.outputs = []

        # once node is instantiated sockets are created
        # create sockets for input and outputs
        counter = 0
        for item in inputs:
            socket = Socket(node=self, index_Socket_xPos=counter, position_Socket_yPos=LEFT_BOTTOM)
            counter += 1
            self.inputs.append(socket)

        counter = 0
        for item in outputs:
            socket = Socket(node=self, index_Socket_xPos=counter, position_Socket_yPos=RIGHT_TOP)
            counter += 1
            self.outputs.append(socket)

    @property
    def pos(self):
        return self.getNode.pos()

    def setPos(self, x, y):
        self.grNode.setPos(x, y)

    # return coordinate position of a socket as a list for updating positions inside NodeEdge
    def getSocketPosition(self, index_xPos, position_yPos):
        x = 0 if (position_yPos in (LEFT_TOP, LEFT_BOTTOM)) else (self.grNode.height/2)


         # start from bottom
        y = self.grNode.height/2

        return [x, y]

    '''        if PARENT:
            return [0, -self.grNode.height/2]
        else:
            return[0, self.grNode.height/2]'''

    def updateConnectedEdges(self):
        for socket in self.inputs + self.outputs:
            if socket.hasEdge():
                if DEBUG: print("updating")
                socket.edge.updatePositions()
            else:
                if DEBUG: print("no operation")
