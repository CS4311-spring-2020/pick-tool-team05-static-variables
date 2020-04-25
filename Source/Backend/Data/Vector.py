from pprint import pprint
from Source.Backend.Data.DBFacade import DBFacade
from Source.Backend.Data.Graph import Graph

class Vector:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        g = Graph("or", 88, 88, "sg", "Node1", "Relationship 2")

        vector = {
            "Name": self.name,
            "Description": self.description,
            "Graph": [g.graph]
        }

        db_collection = DBFacade(dbName="PICKDB", collectionName="Vector")
        d = db_collection.add(vector)
        pprint(d)
        #x = db_collection.search_n("Name","Ddos")
        #for i in x:
            #pprint(i)


    def getName(self):
        return self.__name

    def getDescription(self):
        return self.__description

    def setName(self, name):
        self.__name = name

    def setDescription(self, description):
        self.__description = description
