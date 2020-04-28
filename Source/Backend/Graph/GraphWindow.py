from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from Source.Backend.Graph.Node import Node
from Source.Backend.Graph.GraphicsView import GraphicsView
from Source.Backend.Graph.NodeScene import Scene
from Source.Backend.Graph.NodeEdge import Edge


class GraphWindow(QWidget):
    def __init__(self, vector_name="Undifined Vector", parent=None):
        vector = vector_name
        super().__init__(parent)

        self.styleSheet_filename = 'qss/nodestyle.qss'
        self.loadStyleSheet(self.styleSheet_filename)

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

    def addNode(self):
        # passing the scene reference, the name of the node, inputs and outputs

        # inputs might represent different types of sockets
        node1 = Node(self.scene, "My Awesome Node 1", inputs=[1], outputs=[1])
        node2 = Node(self.scene, "My Awesome Node 2", inputs=[1], outputs=[1])
        node3 = Node(self.scene, "My Awesome Node 3", inputs=[1], outputs=[1])

        node4 = Node(self.scene, "My Awesome Node 4", inputs=[1], outputs=[1])
        node5 = Node(self.scene, "My Awesome Node 5", inputs=[1], outputs=[1])
        node6 = Node(self.scene, "My Awesome Node 6", inputs=[1], outputs=[1])

        # set where node is supposed to be drawn from the start
        node1.setPos(-450, -250)
        node2.setPos(-75, 0)
        node3.setPos(-200, -500)
        node4.setPos(800,500)
        node5.setPos(300,600)
        node6.setPos(1000,300)

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
