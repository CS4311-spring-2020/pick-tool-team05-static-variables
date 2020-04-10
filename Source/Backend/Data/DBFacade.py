from bson import ObjectId
from pymongo import MongoClient, collection


class DBFacade:
    def __init__(self, dbName=None, collectionName=None):
        self.dbName = dbName
        self.collectionName = collectionName
        self.connection = MongoClient("localhost", 27017, maxPoolSize=20)

        self.db = self.connection[self.dbName]
        self.collection = self.db[self.collectionName]

    # TODO: Enhance to add specific data within a document
    # TODO: Add several objects into a collection: create an array of objects
    # Adds object data into the DB saves the document id for future need
    def add(self, data):
        doc_id = self.collection.insert_one(data)

    # Updates data with a specified ID and the data its going to change it to,
    # if a document already exists with that ID it will create a new doc
    def update(self, doc_id, data):
        document = self.collection.update_one({'_id': ObjectId(doc_id)}, {"$set": data})
        return document.acknowledged

    # Retrieve a document within a collection specifying the ID
    # TODO: Enhance function to retrieve a specific document given other search criteria
    def get_single_doc(self, doc_id):
        data = self.collection.find_one({'_id': ObjectId(doc_id)})
        print(data)







    # Retrieve all the objects inside the collection on a specified criteria
    def get_multiple_docs(self):
        data = self.collection.find()
        print(data)
