from pymongo import MongoClient

class DBFacade:
    try:
        connection = MongoClient()
        print(" Established Connection")
    except:
        print("Connection not Established")

    # database
    db = connection.PICKDB
    # Collection name
    collection = db.EventConfiguration

    # Info to be stored in Collection
    eventConfig = {
        "Event Name": "",
        "Event Start Time ": 24,
        "Event End Time": 44,
        "Root Directory": 'usr/local/..',
        "Red Team Folder": "",
        "White Team Folder":"",
        "Lead:":"",
        "Lead IP address":"",
        "Connection Satus":""
    }

    # Insert Data
    rec_id1 = collection.insert_one(eventConfig)

    print("Data inserted with record ids", rec_id1, " ")

    # Printing the data inserted
    cursor = collection.find()
    for record in cursor:
        print(record)
