

class Serializable:
    def __init__(self):
        self.id = id(self)

    def getSid(self):
        return id(self)

    def serialize(self):
        raise NotImplemented
