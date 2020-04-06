from Source.Backend.Data.DBFacade import DBFacade


class EventConfiguration:
    def __init__(self, name, description, start_time, end_time, root_directory, red_team_folder, white_team_folder,
                 blue_team_folder, lead, lead_ip_add, connection_status):
        self.name = name
        self.description = description
        self.start_time = start_time
        self.end_time = end_time
        self.root_directory = root_directory
        self.red_team_folder = red_team_folder
        self.white_team_folder = white_team_folder
        self.blue_team_folder = blue_team_folder
        self.lead = False
        self.lead_ip_add = lead_ip_add
        self.connection_status = connection_status

    # Setters for Event Config attributes
    def set_name(self, name):
        self.name = name
        #self.dbCollection.add(self.name)

    def set_start_time(self, start_time):
        self.start_time = start_time
        #self.dbCollection.add(self.start_time)

    def set_end_time(self, end_time):
        self.end_time = end_time
        #self.dbCollection.add(self.end_time)

    def set_root_directory(self, root_directory):
        self.root_directory = root_directory
        #self.dbCollection.add(self.root_directory)

    def set_red_team_folder(self, red_folder):
        self.red_team_folder = red_folder
        #self.dbCollection.add(self.red_folder)

    def set_white_team_folder(self, white_folder):
        self.white_team_folder = white_folder
        #self.dbCollection.add(self.white_folder)

    def set_blue_team_folder(self, blue_folder):
        self.blue_team_folder = blue_folder
        #self.dbCollection.add(self.blue_folder)

    def set_lead(self, lead):
        self.lead = lead
        #self.dbCollection.add(self.lead)

    def set_lead_ip_add(self, lead_ip):
        self.lead_ip_add = lead_ip
        #self.dbCollection.add(self.lead_ip_add)

    def set_connection_status(self, connection_status):
        self.connection_status = connection_status
        #self.dbCollection.add(self.connection_status)

    # Getters For the Event Config Attributes
    def get_name(self):
        return self.name

    def get_start_time(self):
        return self.start_time

    def get_end_time(self):
        return self.end_time

    def get_root_directory(self):
        return self.root_directory

    def get_red_team_folder(self):
        return self.red_team_folder

    def get_white_team_folder(self):
        return self.white_team_folder

    def get_blue_team_folder(self):
        return self.blue_team_folder

    def get_lead(self, lead):
        return self.lead

    def get_lead_ip_add(self):
        return self.lead_ip_add

    def get_lead_ip_add(self):
        return self.lead_ip_add

    def get_connection_status(self):
        return self.connection_status

    # JSON object to test DB
    eventConfig = {
        "Event Name": "",
        "Event Start Time ": "HH:MM MM/DD/YY AM/PM",
        "Event End Time": "HH:MM MM/DD/YY AM/PM",
        "Root Directory": 'usr/local/',
        "Red  Team Folder": "usr/local/red",
        "White Team Folder": "usr/local/white",
        "Blue Team Folder": "usr/local/blue",
        "Lead:": True,
        "Lead IP address": "127.0.0.1",
        "Connection Status": 2
    }
    # Communicating to the Event Config collection through the DB Façade
    dbCollection = DBFacade(dbName="PICKDB", collectionName="EventConfiguration")
    dbCollection.add(eventConfig)
