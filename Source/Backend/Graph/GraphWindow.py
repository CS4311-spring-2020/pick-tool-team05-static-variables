from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from Source.Backend.Graph.Node import Node
from Source.Backend.Graph.GraphicsView import GraphicsView
from Source.Backend.Graph.NodeScene import Scene


class GraphWindow(QWidget):
    def __init__(self, parent=None):
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

        # passing the scene reference, the name of the node, inputs and outputs
        # inputs might represent different types of sockets
        node = Node(self.scene, "My Awesome Node", inputs=[1, 2, 3], outputs=[1])

        # create graphics view
        self.view = GraphicsView(self.scene.grScene, self)
        self.layout.addWidget(self.view)

    def loadStyleSheet(self, filename):
        print("Style Loading:", filename)
        file = QFile(filename)
        file.open(QFile.ReadOnly | QFile.Text)
        stylesheet = file.readAll()
        QApplication.instance().setStyleSheet(str(stylesheet, encoding='utf8'))
