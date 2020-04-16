from bson import ObjectId
from pymongo import MongoClient, collection


class DBFacade:
    def __init__(self, dbName=None, collectionName=None):
        self.dbName = dbName
        self.collectionName = collectionName
        self.connection = MongoClient("localhost", 27017, maxPoolSize=20)

        self.db = self.connection[self.dbName]
        self.collection = self.db[self.collectionName]

    """ Adds one full object into a collection in the DB 
        data: dic()/JSON object that will be stored 
    """

    # Adds a full document
    def add(self, data):
        return self.collection.insert_one(data)

    # Deletes a full document with provided matching criteria
    def delete(self, field, criteria):
        status = self.collection.remove({field: criteria})
        print(status)

    # Updates all the documents with specified ID within the collection,can update one or many fields in that document.
    def update(self, doc_id, data):
        status = self.collection.update_many({'_id': ObjectId(doc_id)}, {"$set": data})
        print(status)

    # TODO: Check why this is not updating the data when given a String rather than the full object with its changes
    # Updates specific fields of a document with the provided matching criteria along with the data it will update to.
    def update_n(self, field, field_data, data):
        status = self.collection.update_many({field: field_data}, {"$set": data})
        print(status)

    # Returns one documents in a collection
    def search_n(self,field, data_field):
        simple_query = {'_id': ObjectId("5e962ecee3bcf9eb015223b1")}
        regex_query = {field:{"$regex":data_field}}
        logical_query = {""}
        return self.collection.find(regex_query)




    # Method to return a node's content with a specified node ID through the Vector collection
    def find_node(self, node_id):
        self.collectionName = "Vector"
        # traverse the Vector collection's graph to find a node based on its ID
        self.db.self.collection.find({"Graph.Node": node_id})
        self.collectionName = "Node"
        # after it finds the node within the vector return the content of that node
        return self.db.self.collection.find({})
