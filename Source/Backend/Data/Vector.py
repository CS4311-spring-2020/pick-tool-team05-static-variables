from Source.Backend.Graph.GraphWindow import GraphWindow

DEBUG = True


class Vector:
    def __init__(self, name=None, description=None):
        self.name = name
        self.description = description

        self.graph = GraphWindow(self.name)
        self.kwargs = {"Node Visibility": "something0",
                      "Node ID": "something1",
                      "Node Name": "something2",
                      "Node Time Stamp": "something3",
                      "log_entry_reference": "something4",
                      "log_creator": "something5",
                      "event_type": "something6",
                      "icon_type": "something7",
                      "source": "something8",
                      "Node Description": "something9 has to be very long because I am testing how the table will "
                                          "handle it and make sure it doesn't crash "}

        self.graph.addNode(**self.kwargs)


        if DEBUG: print("Name of vector: ", self.name, " and description: ", self.description)
        if DEBUG: print(" Graph initialized with it: ", self.graph)

        self.vector = {
            "Name": self.name,
            "Description": self.description,
            "Graph": self.graph
        }

        self.kwargs = {"Node Visibility": "something else",
                      "Node ID": "something else",
                      "Node Name": "something else",
                      "Node Time Stamp": "something else",
                      "log_entry_reference": "something else",
                      "log_creator": "something else",
                      "event_type": "something else",
                      "icon_type": "something else",
                      "source": "something else",
                      "Node Description": "something9 has to be very long because I am testing how the table will "
                                          "handle it and make sure it doesn't crash "}

        self.graph.addNode(**self.kwargs)

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

