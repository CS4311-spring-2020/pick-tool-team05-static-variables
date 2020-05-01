from Source.Backend.Data.Node import Node
from Source.Backend.Data.Relationship import Relationship


class Graph:

    def __init__(self, export_format, orientation, interval_units, interval, position_of_nodes,
                 position_of_relationships):
        self.exportFormat = export_format
        self.orientation = orientation
        self.interval_units = interval_units
        self.interval = interval
        self.positionOfNodes = position_of_nodes
        self.positionOfRelationships = position_of_relationships

        self.n = Node(1, 2, 3, 4, 5, 5, 6, 7)
        self.r = Relationship(1, 2, 3)

        self.graph = {
            "Export Format": self.exportFormat,
            "Orientation": self.orientation,
            "Interval Units": self.interval_units,
            "Interval": self.interval,
            "Position of Nodes": [self.n.node],
            "Position of Relationships": [self.r.relationships]
        }
