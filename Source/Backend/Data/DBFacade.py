from bson import ObjectId

from pymongo import MongoClient

mongo_client = MongoClient("localhost", 27017, maxPoolSize=20)
database = mongo_client["PICKDB"]

""" 
    Adds one full object into a collection in the DB 
    @:param data: dic()/JSON object that will be stored
    @:param collection_name: A string specifying which collection to search in
"""


def add_object(data, collection_name):
    print(database[collection_name].insert_one(data))


"""
    Deletes a full document with provided matching criteria
    @:param key: A String specifying the attribute of the document that will be searched on to find the right doc
    @:param value: The String data will be used to find a doc 
    @:param collection_name: A string specifying which collection to search in
"""


def del_object(key, value, collection_name):
    print(database[collection_name].remove({key: value}))


"""
    Searches for an object with provided mathcing criteria
    @:param key: A String specifying the attribute of the document that will be searched on to find the right doc
    @:param value: The String data will be used to find a doc 
    @:param collection_name: A string specifying which collection to search in
"""


def search_object(key, value, collection_name):
    if value == "event configuration":
        result = database[collection_name].find_one()
    else:
        result = database[collection_name].find_one({key: value})
    return result


def update_object(key, value, collection_name):
    print(database[collection_name].update_one(key, value))
