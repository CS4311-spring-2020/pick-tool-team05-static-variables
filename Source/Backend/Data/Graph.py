from PyQt5.QtCore import QObject, pyqtSignal
from Source.Backend.Data.DBFacade import search_object, add_object, update_object


class Graph(QObject):
    def __init__(self, _id=None, name=None, description=None, export_format=None, orientation=None, interval_units=None,
                 interval=None, position_of_nodes=None, position_of_relationships=None):
        super().__init__()
        print("in Graph after parent constructor")
        self.signal = pyqtSignal()

        print(" in Graph creating dictionary")
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
        print("  in Graph inside add function")
        add_object(self.data, "Graph")
        print("   in Graph inside add function after adding")
        self.data = search_object("Name", self.data.get("Name"), "Graph")
        print("    in Graph inside add function after searching for name")

