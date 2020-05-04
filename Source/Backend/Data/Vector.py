from Source.Backend.Graph.GraphWindow import GraphWindow

DEBUG = True


class Vector:
    def __init__(self, name=None, description=None):
        self.name = name
        self.description = description

        self.graph = GraphWindow(self.name)

        if DEBUG: print("Name of vector: ", self.name, " and description: ", self.description)
        if DEBUG: print(" Graph initialized with it: ", self.graph)

        self.vector = {
            "Name": self.name,
            "Description": self.description,
            "Graph": self.graph
        }

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def set_name(self, name):
        self.name = name

    def set_description(self, description):
        self.description = description

    def getVector(self):
        return self.vector

