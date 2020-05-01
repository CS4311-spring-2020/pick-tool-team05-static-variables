from Source.Backend.Graph.GraphWindow import GraphWindow

DEBUG = True


""" VectorFacade takes name and description as string parameters and initializes a graph for that individual vector
with the same name provided as parameter for the vector.
"""


class VectorFacade:
    def __init__(self, name="undefined", description="undefined"):

        self.name = name
        self.description = description

        self.graph = GraphWindow(self.name)

        if DEBUG: print("Name of vector: ", self.name, " and description: ", self.description)
        if DEBUG: print(" Graph initialized with it: ", self.graph)
