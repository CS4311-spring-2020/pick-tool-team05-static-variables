from pymongo import MongoClient
from pymongo import errors
import os
import subprocess
import platform

mongo_client = MongoClient("localhost", 27017, maxPoolSize=20)
database = mongo_client["PICKDB"]

""" 
    Adds one full object into a collection in the DB 
    @:param data: dic()/JSON object that will be stored
    @:param collection_name: A string specifying which collection to search in to add the data.
"""


def add_object(data, collection_name):
    print(database[collection_name].insert_one(data))


"""
    Deletes a full document with provided matching criteria
    @:param key: A String specifying the attribute of the document that will be searched on to find the right doc
    @:param value: The String data that will be used to find a doc 
    @:param collection_name: A string specifying which collection to search in
"""


def del_object(key, value, collection_name):
    print(database[collection_name].remove({key: value}))


"""
    Searches for an object with provided matching criteria
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


"""
    Updates one or many object's attributes within a document in a specified collection in the DB
    @:param object_id: A String specifying a document's ID to be found in the DB 
    @:param object_data: A dictionary with all the attributes's changes done to the object 
    @:param collection_name: A String specifying the collection in which the doc will be updated 
"""


def update_object(object_id, object_data, collection_name):
    oid = {
        "_id": object_id
    }
    query = {
        "$set": object_data
    }
    print(database[collection_name].update_one(oid, query))


"""
    Retrieves all the vectors in the DB and inserts them into a list to keep track of them in the system. 
"""


def get_vector_list():
    vector_list = []
    for vector in database["Vector"].find({}):
        vector_list.append(vector)

    return vector_list


"""
    Gets the count of the documents inside the collections within the PICKDB and determines whether 
    a PICK project should be continued or start a new one.
"""


def check_db():
    # gets count of all the documents inside the collections within the PICKDB
    try:
        vec_col = mongo_client['PICKDB']['Vector'].count_documents({})
        ec_col = mongo_client['PICKDB']['EventConfiguration'].count_documents({})
        node_col = mongo_client['PICKDB']['Node'].count_documents({})
        graph_col = mongo_client['PICKDB']['Graph'].count_documents({})


    except errors.OperationFailure as err:
        print("PyMongo ERROR:", err, "\n")
    # if all the collections contain zero documents return True
    if vec_col == 0 and ec_col == 0 and node_col == 0 and graph_col == 0:
        return True
    return False


"""
    Detects the user's operating system and provides the Mongo executable path. 
"""


def connect_to_db():
    os = platform.system()
    print(os)
    if os == 'Darwin':
        name = "mongodb-community"
        subprocess.Popen(['/usr/local/Cellar/' + name + '/4.2.3/bin/mongod'], shell=True)
    elif os == 'Windows':
        name = "MongoDB/Server"
        subprocess.Popen(['C:/Program Files/' + name + '/4.2/bin/mongod.exe', '--dbpath', '../Source/Database'],
                         shell=True)
