from Source.Backend.Graph.GraphicNodeSocket import GraphicsSocket
from Source.Backend.Graph.Serializable import Serializable


TOP = 1
BOTTOM = 2


class Socket(Serializable):
    # passing the parent node in order to added to the scene, and index to keep track of position
    def __init__(self, node, socket_x_pos=0, socket_y_pos=TOP):
        super().__init__()

        self.node = node
        self.socket_x_pos = socket_x_pos
        self.socket_y_pos = socket_y_pos

        # create graphical sockets
        self.grSocket = GraphicsSocket(self)
        self.grSocket.setPos(*self.getSocketPosition())

        self.edge = None

    # return coordinate: index,position
    def getSocketPosition(self):
        return self.node.getSocketPosition(self.socket_x_pos, self.socket_y_pos)

    def setConnectedEdge(self, edge=None):
        self.edge = edge

    def hasEdge(self):
        return self.edge is not None

    def serialize(self):
        return {
            "id": id(self),
            "socket_x_pos": self.socket_x_pos,
            "socket_y_pos": self.socket_y_pos
        }
