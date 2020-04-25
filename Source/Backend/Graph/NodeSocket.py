from Source.Backend.Graph.GraphicNodeSocket import GraphicsSocket

LEFT_TOP = 1
LEFT_BOTTOM = 2
RIGHT_TOP = 3
RIGHT_BOTTOM = 4
BOTTOM = 5
TOP = 6


class Socket:
    # passing the parent node in order to added to the scene, and index to keep track of position
    def __init__(self, node, index=0, position=LEFT_TOP):

        self.node = node
        self.index = index
        self.position = LEFT_TOP

        # create graphical sockets
        self.grSocket = GraphicsSocket(self.node.grNode)

        self.grSocket.setPos(*self.node.getSocketPosition(index, position))
