from pymongo import MongoClient

class DBFacade():
    def __init__(self, dbName=None, collectionName=None):
        self.dbName = dbName
        self.collectionName = collectionName
        self.connection = MongoClient("localhost", 27017, maxPoolSize=20)

        self.db = self.connection[self.dbName]
        self.collection = self.db[self.collectionName]

    def add(self, data):
         # Insert Data
        rec_id1 = self.collection.insert_one(data)
        print("Data inserted with record ids", rec_id1, " ")

        # Printing the data inserted
        cursor = self.collection.find()
        for record in cursor:
            print(record)

    def delete(self,data):
        pass
    def find(self,data):
        pass
