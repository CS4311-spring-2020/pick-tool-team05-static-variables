from Source.Backend.Data.DBFacade import DBFacade


class EventConfiguration:
    eventConfig = {
        "Event Name": "",
        "Event Start Time ": "HH:MM MM/DD/YY AM/PM",
        "Event End Time": "HH:MM MM/DD/YY AM/PM",
        "Root Directory": 'usr/local/..',
        "Red  Team Folder": "",
        "White Team Folder": "",
        "Lead:": "",
        "Lead IP address": "",
        "Connection Status": ""
    }
    dbCollection = DBFacade("PICKDB", "EventConfiguration", )
    dbCollection.add(eventConfig)




