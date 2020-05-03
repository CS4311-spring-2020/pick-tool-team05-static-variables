from Source.Backend.Data.SignificantLogEntry import SignificantLogEntry
from Source.Backend.Data.NodeVisibility import NodeVisibility


class Node:
    def __init__(self, **kwargs):
        self.nodeID = kwargs.get("key")
        self.nodeName = kwargs.get("key")
        self.nodeTimestamp = kwargs.get("key")
        self.nodeDescription = kwargs.get("key")
        self.logCreator = kwargs.get("key")
        self.eventType = kwargs.get("key")
        self.iconType = kwargs.get("key")
        self.source = kwargs.get("key")

        s = SignificantLogEntry("8", "8", "ll", "", "", "")
        n = NodeVisibility(True, True, True, True, True, True, True, True, True, True)
        self.node = {
            "Node_ID": self.nodeID,
            "Node Name": self.nodeName,
            "Node Timestamp": self.nodeTimestamp,
            "Node Description": self.nodeDescription,
            "Log Entry Reference": s.significant_log_entry,
            "Log Creator": self.logCreator,
            "Event Type": self.eventType,
            "Icon Type": self.iconType,
            "Source": self.source,
            "Node Visibility": n.node_visibility_
        }

    def getNode(self):
        return self.node
