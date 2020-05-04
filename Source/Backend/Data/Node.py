from Source.Backend.Data.SignificantLogEntry import SignificantLogEntry
from Source.Backend.Data.NodeVisibility import NodeVisibility



class Node:
    def __init__(self, node_id, node_name, node_timestamp, node_description, log_creator, event_type, icon_type, source,):
        self.nodeID = node_id
        self.nodeName = node_name
        self.nodeTimestamp = node_timestamp
        self.nodeDescription = node_description
        self.logCreator = log_creator
        self.eventType = event_type
        self.iconType = icon_type
        self.source = source

        s = SignificantLogEntry("8","8","ll","","","")
        n = NodeVisibility(True,True,True,True,True,True,True,True,True,True)
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
