from PyQt5.QtWidgets import *

from Source.Backend.Graph.Node import Node
from Source.Backend.Graph.GraphicsView import GraphicsView
from Source.Backend.Graph.Scene import Scene
from Source.Backend.Graph.NodeEdge import Edge


class GraphWindow(QWidget):
    def __init__(self, graph_name=None, parent=None):
        self.data = {
            "Graph Name": graph_name,
            "Graph Description": ""
        }
        super().__init__(parent)

        self.info1 = {"Node Visibility": "something0",
                      "Node ID": "something1",
                      "Node Name": "something2 info 1",
                      "Node Time Stamp": "something3",
                      "log_entry_reference": "something4",
                      "log_creator": "something5",
                      "event_type": "something6",
                      "icon_type": "something7",
                      "source": "something8",
                      "Node Description": "something9 has to be very long because I am testing how the table will "
                                          "handle it and make sure it doesn't crash "}

        self.info2 = {"Node Visibility": "something0",
                      "Node ID": "something1",
                      "Node Name": "something2 info 2",
                      "Node Time Stamp": "something3",
                      "log_entry_reference": "something4",
                      "log_creator": "something5",
                      "event_type": "something6",
                      "icon_type": "something7",
                      "source": "something8",
                      "Node Description": "something9 has to be very long because I am testing how the table will "
                                          "handle it and make sure it doesn't crash "}

        self.info3 = {"Node Visibility": "something0",
                      "Node ID": "something1",
                      "Node Name": "something2 info 3",
                      "Node Time Stamp": "something3",
                      "log_entry_reference": "something4",
                      "log_creator": "something5",
                      "event_type": "something6",
                      "icon_type": "something7",
                      "source": "something8",
                      "Node Description": "something9 has to be very long because I am testing how the table will "
                                          "handle it and make sure it doesn't crash "}

        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 800, 600)

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        # create graphics scene
        self.scene = Scene()

        self.addNode()

        # create graphics view
        self.view = GraphicsView(self.scene.grScene, self)
        self.layout.addWidget(self.view)

    def __str__(self):
        return "<Graph Window: %s...%s>" % (hex(id(self))[2:5], hex(id(self))[:3])

    def addNode(self):
        # passing the scene reference, the name of the node, inputs and outputs

        # inputs might represent different types of sockets
        node1 = Node(self.scene, inputs=[1], outputs=[1], **self.info1)
        node2 = Node(self.scene, inputs=[1], outputs=[1], **self.info2)
        node3 = Node(self.scene, inputs=[1], outputs=[1], **self.info3)

        node4 = Node(self.scene, inputs=[1], outputs=[1], **self.info1)
        node5 = Node(self.scene, inputs=[1], outputs=[1], **self.info2)
        node6 = Node(self.scene, inputs=[1], outputs=[1], **self.info3)

        # set where node is supposed to be drawn from the start
        node1.setPos(-450, -250)
        node2.setPos(-75, 0)
        node3.setPos(-200, -500)
        node4.setPos(800, 500)
        node5.setPos(300, 600)
        node6.setPos(1000, 300)

        # creation of edge takes scene, starting pos, ending pos, and type of edge to draw
        edge1 = Edge(self.scene, node1.outputs[0], node2.inputs[0], "something")
        edge2 = Edge(self.scene, node2.outputs[0], node3.inputs[0], "something else")
        edge3 = Edge(self.scene, node5.outputs[0], node6.inputs[0], "something something else")

'''
    def addNode(self, **kwargs):
        if kwargs is not None:
            Node(self.scene, inputs=[1], outputs=[1], **kwargs)
        else:
            pass
'''