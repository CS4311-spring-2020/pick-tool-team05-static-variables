
class NodeVisibility:

    def __init__(self, node_id_visibility, node_name_visibility, node_timestamp_visibility, node_description_visibility,
                 log_entry_reference_visibility, log_creator_visibility, event_type_visibility, icon_visibility,
                 source_visibility,
                 node_visibility):
        self.nodeIdVis = node_id_visibility
        self.nodeNameVis = node_name_visibility
        self.nodeTimestampVis = node_timestamp_visibility
        self.nodeDescriptionVis = node_description_visibility
        self.logEntryVis = log_entry_reference_visibility
        self.logCreatorVis = log_creator_visibility
        self.eventTypeVis = event_type_visibility
        self.iconVis = icon_visibility
        self.sourceVis = source_visibility
        self.nodeVis = node_visibility

        self.node_visibility_ = {
            "Node ID Visibility": self.nodeIdVis,
            "Node Name Visibility": self.nodeNameVis,
            "Node Timestamp Visibility": self.nodeIdVis,
            "Node Description Visibility": self.nodeDescriptionVis,
            "Log Entry Reference Visibility": self.logEntryVis,
            "Log Creator Visibility": self.logCreatorVis,
            "Event Type Visibility": self.eventTypeVis,
            "Icon Visibility ": self.iconVis,
            "Source Visibility": self.sourceVis,
            "Node Visibility": self.nodeVis
        }
