from PyQt5.QtCore import QObject, pyqtSignal
from Source.Backend.Data.DBFacade import search_object, add_object, update_object


class Graph(QObject):
    def __init__(self, _id=None, name=None, description=None, export_format=None, orientation=None, interval_units=None,
                 interval=None, position_of_nodes=None, position_of_relationships=None):
        super().__init__()
        self.signal = pyqtSignal()

        self.data = {
            "Name": name,
            "Description": description,
            "Export Format": export_format,
            "Orientation": orientation,
            "Interval Units": interval_units,
            "Interval": interval,
            "Nodes": [],
            "Relationships": []
        }
        self.add()

    def add(self):
        add_object(self.data, "Graph")
        self.data = search_object("Name", self.data.get("Name"), "Graph")


