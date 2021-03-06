from Source.Backend.Graph.GraphicEdge import *
from Source.Backend.Graph.Serializable import Serializable

EDGE_TYPE_DIRECT = 1


class Edge(Serializable):
    def __init__(self, scene, start_socket, end_socket, label):
        super().__init__()

        self.scene = scene

        self.label = label

        self.start_socket = start_socket
        self.end_socket = end_socket

        self.start_socket.edge = self
        if self.end_socket is not None:
            self.end_socket.edge = self

        self.grEdge = GraphicsEdgeDirect(self)

        self.updatePositions()

        self.scene.addEdge(self)

        # adding graphical edge to the scene itself
        self.scene.grScene.addItem(self.grEdge)

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

    def serialize(self):
        return {
            "id": id(self),
            "label": self.label,
            "start": self.start_socket.id,
            "end": self.end_socket.id
        }


