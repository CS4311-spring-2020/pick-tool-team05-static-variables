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
                "Name": "",
                "Description": "",
                "Graph ID": "",
                "Significant Log Entries": []
            }

        self.init_graph()

    def init_graph(self):
        print('hi')

    def save(self):
        # Appends a number if vector with the same name exists
        if search_object("Name", self.data.get("Name"), "Vector") is not None:
            if self.data.get("Name")[-1].isdigit():
                self.data["Name"] = self.data.get("Name")[:-1] + str(int(self.data.get("Name")[-1]) + 1)
            else:
                self.data["Name"] = self.data.get("Name") + "1"

        add_object(self.data, "Vector")
        self.data = search_object("Name", self.data.get("Name"), "Vector")

    def update(self):
        update_object(self.data.get("_id"), self.data, "Vector")