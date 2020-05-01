from pymongo import MongoClient

connection = MongoClient("localhost", 27017, maxPoolSize=20)
db = connection['PICKDB']

""" 
    Adds one full object into a collection in the DB 
    data: dic()/JSON object that will be stored 
"""


def add(collection, data):
    collection_name = db[collection]
    status = collection_name.insert_one(data)
    print(status)


"""
    Deletes a full document with provided matching criteria
    @:param field: A String specifying the attribute of the document that will be searched on to find the right doc
    @:param criteria: The String data will be used to find a doc 
"""


def delete(collection,field, criteria):
    collection_name = db[collection]
    status = collection_name.remove({field: criteria})
    print(status)


# TODO: Check why this is not updating the data when given a String rather than the full object with its changes
# Updates specific fields of a document with the provided matching criteria along with the data it will update to.
def update_n(self, field, field_data, data):
    status = self.collection.update_one({field: field_data}, {"$set": data})
    print(status)


# Returns the document from a collection in the DB
def search_n(collection, field, data_field):
    collection_name = db[collection]
    regex_query = {field: {"$regex": data_field}}
    return collection_name.find(regex_query)
