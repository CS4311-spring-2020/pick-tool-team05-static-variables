from Source.Backend.Graph.GraphicNode import GraphicsNode
from Source.Backend.Graph.NodeContentWidget import NodeContentWidget
from Source.Backend.Graph.NodeSocket import *
from Source.Backend.Graph.Serializable import Serializable


class Node(Serializable):
    def __init__(self, scene, **kwargs):
        super().__init__()

        self.scene = scene

        # saves individual information of a node
        self.content_info = kwargs

        #self.title = kwargs.pop('name')
        kwargs.pop("Node Visibility")
        kwargs.pop("icon_type")

        # create a widget for contents of a nodes and add itself to node graphics
        self.content = NodeContentWidget(self)
        self.grNode = GraphicsNode(self)

        # add itself to the scene
        self.scene.addNode(self)
        self.scene.grScene.addItem(self.grNode)

        self.socket_spacing = 1

        # once node is instantiated sockets are created
        self.inputs = [Socket(node=self,  socket_y_pos=TOP)]
        self.outputs = [Socket(node=self, socket_y_pos=BOTTOM)]

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

                socket.edge.updatePositions()
            else:
                pass

    def serialize(self):
        inputs, outputs = [], []
        for socket in self.inputs: inputs.append(socket.serialize())
        for socket in self.outputs: outputs.append(socket.serialize())
        print("  In serialize function inside of node")
        res = {
            "id": id(self),
            "name": self.content_info.get("Node Name"),
            "pos x": self.grNode.scenePos().x(),
            "pos y": self.grNode.scenePos().y(),
            "parent": inputs,
            "child": outputs,
            "content": self.content.serialize()
        }
        print(res)
        return res
