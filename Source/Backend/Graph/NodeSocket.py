from Source.Backend.Graph.GraphicNodeSocket import GraphicsSocket


TOP = 1
BOTTOM = 2

DEBUG = False


class Socket:
    # passing the parent node in order to added to the scene, and index to keep track of position
    def __init__(self, node, socket_x_pos=0, socket_y_pos=TOP):

        self.node = node
        self.socket_x_pos = socket_x_pos
        self.socket_y_pos = socket_y_pos

        if DEBUG: print("Socket: -- creating with: ", self.socket_x_pos, self.socket_y_pos, self.node)
        # create graphical sockets
        self.grSocket = GraphicsSocket(self.node.grNode)

        self.grSocket.setPos(*self.node.getSocketPosition(socket_x_pos, socket_y_pos))

        self.edge = None

    def __str__(self):
        return "<Edge: %s...%s>" % (hex(id(self))[2:5], hex(id(self))[:3])

    # return coordinate: index,position
    def getSocketPosition(self):
        if DEBUG: print(" GSP: ", self.socket_x_pos, self.socket_y_pos, "node: ", self.node)

        result = self.node.getSocketPosition(self.socket_x_pos, self.socket_y_pos)

        if DEBUG: print("  result: ", result)
        return result

    def setConnectedEdge(self, edge=None):
        self.edge = edge

    def hasEdge(self):
        return self.edge is not None
