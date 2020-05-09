from PyQt5.QtCore import QObject, pyqtSignal
from Source.Backend.Data.DBFacade import search_object, add_object, update_object


class Vector(QObject):
    def __init__(self, _id=None, name=None):
        super().__init__()
        self.signal = pyqtSignal()

        if _id is not None:
            self.data = search_object("_id", _id, "Vector")
        elif name is not None:
            self.data = search_object("Name", name, "Vector")
        else:
            self.data = {
                "Name": "untitled",
                "Description": "",
                "Graph ID": "",
                "Significant Log Entries": []
            }
            # self.create_graph()
            self.add()

    def add(self):
        self.check_duplicate()
        add_object(self.data, "Vector")
        self.data = search_object("Name", self.data.get("Name"), "Vector")

    def update(self):
        # TODO: Make sure to update graph name/description when vector is updated
        self.check_duplicate()
        update_object(self.data.get("_id"), self.data, "Vector")

    # TODO:Fix bug where updating only the description triggers appending a number
    def check_duplicate(self):
        # Appends a number if vector with the same name exists
        s = search_object("Name", self.data.get("Name"), "Vector")

        while s is not None:
            if self.data.get("Name").split(' ')[-1].isdigit():
                new = self.data.get("Name").rsplit(' ', 1)
                self.data["Name"] = new[0] + " " + str(int(new[1]) + 1)
            else:
                self.data["Name"] = self.data.get("Name") + " 1"

            s = search_object("Name", self.data.get("Name"), "Vector")


    # def create_graph(self):
    #     # TODO: Create graph with name/description of vector, store Graph ID in vector "GRAPH ID" attribute
    #     g = Graph(self.data.get("Name"), self.data.get("Description"))
    #     self.data["Graph ID"] = g.data.get("_id")