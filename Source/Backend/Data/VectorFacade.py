from Source.Backend.Graph.GraphWindow import GraphWindow


class VectorFacade:
    def __init__(self, name=None, description=None):
        self.data = {
            "Name": name,
            "Description": description,
            "nodes": []
        }

        self.graph = GraphWindow(self.data.get("Name"), self.data.get("Description"))

        self.kwargs = {"Node Visibility": "Node1",
                      "Node ID": "Node1",
                      "Node Name": "Node1",
                      "Node Time Stamp": "Node1",
                      "log_entry_reference": "Node1",
                      "log_creator": "Node1",
                      "event_type": "Node1",
                      "icon_type": "Node1",
                      "source": "Node1",
                      "Node Description": "Node1"}

        self.graph.addNode(**self.kwargs)

        self.kwargs = {"Node Visibility": "node2",
                      "Node ID": "node2",
                      "Node Name": "node2",
                      "Node Time Stamp": "node2",
                      "log_entry_reference": "node2",
                      "log_creator": "node2",
                      "event_type": "node2",
                      "icon_type": "node2",
                      "source": "node2",
                      "Node Description": "node2"}

        self.graph.addNode(**self.kwargs)

        self.kwargs = {"Node Visibility": "Node3",
                      "Node ID": "Node3",
                      "Node Name": "Node3",
                      "Node Time Stamp": "Node3",
                      "log_entry_reference": "Node3",
                      "log_creator": "Node3",
                      "event_type": "Node3",
                      "icon_type": "Node3",
                      "source": "Node3",
                      "Node Description": "Node3"}

        self.graph.addNode(**self.kwargs)


