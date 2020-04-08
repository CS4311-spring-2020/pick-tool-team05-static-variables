from bson import ObjectId
from pymongo import MongoClient, collection


class DBFacade():
    def __init__(self, dbName=None, collectionName=None):
        self.dbName = dbName
        self.collectionName = collectionName
        self.connection = MongoClient("localhost", 27017, maxPoolSize=20)

        self.db = self.connection[self.dbName]
        self.collection = self.db[self.collectionName]

    def add(self, data):
        # Checking for duplicate data within collections

        # Insert Data
        rec_id1 = self.collection.insert_one(data)
        print("Data inserted with record ids", rec_id1, " ")

        # Printing the data inserted
        cursor = self.collection.find()

    # Updates data with a specified ID and the data its going to change it to,
    # if a document already exists with that ID it will create a new doc
    def update(self, doc_id, data):
        document = collection.update_one({'_id': ObjectId(doc_id)}, {"$set": data}, upset=True)
        return document.acknowledged

    def get_single_data(self, doc_id):
        data = collection.find_one({'_id': ObjectId(doc_id)})
        return data

    # Retrieve all the objects inside the collection on a specified criteria
    def get_multiple_data(self):
        data = collection.find()

    def delete(self, data):
        pass

    def find(self, data):
        pass
