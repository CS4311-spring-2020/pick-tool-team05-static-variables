from PyQt5.QtCore import QObject, pyqtSignal
from Source.Backend.Data.DBFacade import search_object, add_object, update_object
from Source.Backend.Data.Graph import Graph


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

            self.add()

    def add(self):
        self.create_graph()
        self.check_duplicate()
        add_object(self.data, "Vector")
        self.data = search_object("Name", self.data.get("Name"), "Vector")

    def update(self):
        g = search_object("_id", self.data.get("Graph ID"), "Graph")
        # g.data["Name"] = self.data.get("Name")
        # g.data["Description"] = self.data.get("Description")
        # g.update()
        self.check_duplicate()
        update_object(self.data.get("_id"), self.data, "Vector")

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

    def create_graph(self):
        g = Graph(self.data.get("Name"), self.data.get("Description"))
        self.data["Graph ID"] = g.data.get("_id")
