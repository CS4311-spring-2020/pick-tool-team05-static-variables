class Relationship:

    def __init__(self, relationship_id, parent_id, child_id, label):
        self.relationshipId = relationship_id
        self.parentId = parent_id
        self.childId = child_id
        self.label = label

        self.relationships = {
            "Relationship ID": self.relationshipId,
            "Parent ID": self.parentId,
            "Child ID": self.childId,
            "Label": self.label
        }