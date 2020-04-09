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
        self.lead = lead
        self.lead_ip_add = lead_ip_add
        self.connection_status = connection_status

        event_config = {
            "Event Name": self.name,
            "Event Start Time ": self.start_time,
            "Event End Time": self.end_time,
            "Root Directory": self.root_directory,
            "Red Team Folder": self.red_team_folder,
            "White Team Folder": self.white_team_folder,
            "Blue Team Folder": self.blue_team_folder,
            "Lead:": self.lead,
            "Lead IP address": self.lead_ip_add,
            "Connection Status": self.connection_status
        }
        # Communicating with Event Config collection through the DB Façade
        db_collection = DBFacade(dbName="PICKDB", collectionName="EventConfiguration")
        db_collection.add(event_config)

    # Setters for Event Config attributes
    def set_name(self, name):
        self.name = name

    def set_start_time(self, start_time):
        self.start_time = start_time

    def set_end_time(self, end_time):
        self.end_time = end_time

    def set_root_directory(self, root_directory):
        self.root_directory = root_directory

    def set_red_team_folder(self, red_folder):
        self.red_team_folder = red_folder

    def set_white_team_folder(self, white_folder):
        self.white_team_folder = white_folder

    def set_blue_team_folder(self, blue_folder):
        self.blue_team_folder = blue_folder

    def set_lead(self, lead):
        self.lead = lead

    def set_lead_ip_add(self, lead_ip):
        self.lead_ip_add = lead_ip

    def set_connection_status(self, connection_status):
        self.connection_status = connection_status

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
