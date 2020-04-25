from Source.Backend.Graph.GraphicNodeSocket import GraphicsSocket

LEFT_TOP = 1
LEFT_BOTTOM = 2
RIGHT_TOP = 3
RIGHT_BOTTOM = 4
BOTTOM = 5
TOP = 6

DEBUG = False


class Socket:
    # passing the parent node in order to added to the scene, and index to keep track of position
    def __init__(self, node, index=0, position=LEFT_TOP):

        self.node = node
        self.index = index
        self.position = position

        if DEBUG: print("Socket: -- creating with: ", self.index, self.position, self.node)
        # create graphical sockets
        self.grSocket = GraphicsSocket(self.node.grNode)

        self.grSocket.setPos(*self.node.getSocketPosition(index, position))

        self.edge = None

    # return coordinate: index,position
    def getSocketPosition(self):
        if DEBUG: print(" GSP: ", self.index, self.position, "node: ", self.node)
        result = self.node.getSocketPosition(self.index, self.position)
        if DEBUG: print("   res: ", result)
        return result

    def setConnectedEdge(self, edge=None):
        self.edge = edge

    def hasEdge(self):
        return self.edge is not None
