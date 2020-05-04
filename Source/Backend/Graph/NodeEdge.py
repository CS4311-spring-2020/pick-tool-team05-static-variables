from Source.Backend.Graph.GraphicEdge import *

EDGE_TYPE_DIRECT = 1

DEBUG = False


class Edge:
    def __init__(self, scene, start_socket, end_socket, label):
        self.scene = scene

        self.label = label

        self.start_socket = start_socket
        self.end_socket = end_socket

        self.start_socket.edge = self
        if self.end_socket is not None:
            self.end_socket.edge = self

        self.grEdge = GraphicsEdgeDirect(self)

        self.updatePositions()

        if DEBUG: print("Edge: ", self.grEdge.posSource, "to", self.grEdge.posDestination)

        self.scene.addEdge(self)

        # adding graphical edge to the scene itself
        self.scene.grScene.addItem(self.grEdge)

        def __str__(self):
            return "<Edge: %s...%s>" % (hex(id(self))[2:5], hex(id(self))[:3])

        # update position receive coordinate point in a list [x,y]
    def updatePositions(self):
        source_pos = self.start_socket.getSocketPosition()
        source_pos[0] += self.start_socket.node.grNode.pos().x()
        source_pos[1] += self.start_socket.node.grNode.pos().y()
        self.grEdge.setSource(*source_pos)
        if self.end_socket is not None:
            end_pos = self.end_socket.getSocketPosition()
            end_pos[0] += self.end_socket.node.grNode.pos().x()
            end_pos[1] += self.end_socket.node.grNode.pos().y()
            self.grEdge.setDestination(*end_pos)
        else:
            self.grEdge.setDestination(*source_pos)
            if DEBUG:
                print(" SS:", self.start_socket)
                print(" ES:", self.end_socket)
        self.grEdge.update()

    def remove_from_sockets(self):
        if self.start_socket is not None:
            self.start_socket = None
        if self.end_socket is not None:
            self.end_socket.edge = None

        self.end_socket = None
        self.start_socket = None

    def remove(self):
        self.remove_from_sockets()
        self.scene.grScene.removeItem(self.grEdge)
        self.grEdge = None
        self.scene.removeEdge(self)
