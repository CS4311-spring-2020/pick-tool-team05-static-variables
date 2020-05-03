from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from Source.Backend.Graph.Node import Node
from Source.Backend.Graph.GraphicsView import GraphicsView
from Source.Backend.Graph.Scene import Scene
from Source.Backend.Graph.NodeEdge import Edge


class GraphWindow(QWidget):
    def __init__(self, vector_name="Undefined Vector", parent=None):
        vector = vector_name
        super().__init__(parent)

        self.styleSheet_filename = 'qss/nodestyle.qss'
        self.loadStyleSheet(self.styleSheet_filename)

        self.info1 = {"name": "something1",
                      "time_stamp": "something2",
                      "description": "something3",
                      "log_entry_reference": "something4",
                      "log_creator": "something5",
                      "event_type": "something6",
                      "icon_type": "something7",
                      "source": "something8"}

        self.info2 = {"name": "info2",
                      "time_stamp": "info2",
                      "description": "info2",
                      "log_entry_reference": "info2",
                      "log_creator": "info2",
                      "event_type": "info2",
                      "icon_type": "info2",
                      "source": "info2"}

        self.info3 = {"name": "info3",
                      "time_stamp": "info3",
                      "description": "info3",
                      "log_entry_reference": "info3",
                      "log_creator": "info3",
                      "event_type": "info3",
                      "icon_type": "info3",
                      "source": "info3"}

        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 800, 600)

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        # create graphics scene
        self.scene = Scene()

        # create a node
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

    def loadStyleSheet(self, filename):
        print("Style Loading:", filename)
        file = QFile(filename)
        file.open(QFile.ReadOnly | QFile.Text)
        stylesheet = file.readAll()
        QApplication.instance().setStyleSheet(str(stylesheet, encoding='utf8'))
