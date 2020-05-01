from Source.Backend.Data.DBFacade import add
from Source.Backend.Data.DBFacade import delete
from Source.Backend.Data.DBFacade import search_n
from Source.Backend.Data.Graph import Graph


class Vector:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        g = Graph("or", 88, 88, "sg", "Node1", "Relationship 2")

        vector = {
            "Name": self.name,
            "Description": self.description,
            "Graph": g.graph
        }

        add("Vector", vector)       # adds vector when its created

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def set_name(self, name):
        self.name = name

    def set_description(self, description):
        self.description = description

    """
    Function to delete a full vector along its content in the Vector collection in the DB  with
    specified search values
    """

    def delete(self, attribute, value):
        delete("Vector", attribute, value)

    # TODO: Pull object ot
    def pull_objectv(self):
        pass
