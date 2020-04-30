from Source.Backend.Data.DBFacade import DBFacade


class EventConfiguration:

    def __init__(self, name, description, start_time, end_time, root_directory, red_team_folder, white_team_folder,
                 blue_team_folder, lead, lead_ip_add, connect_stat):
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
        self.connect_stat = connect_stat

        # Mapping the object to the DB schema
        self.event_config = {
            "Event Name": self.name,
            "Description": self.description,
            "Event Start Time ": self.start_time,
            "Event End Time": self.end_time,
            "Root Directory": self.root_directory,
            "Red Team Folder": self.red_team_folder,
            "White Team Folder": self.white_team_folder,
            "Blue Team Folder": self.blue_team_folder,
            "Lead": self.lead,
            "Lead IP Address": self.lead_ip_add,
            "Connection Status": self.connect_stat
        }

        # Connecting to the EC object to the EC collection in the DB
        self.db_collection = DBFacade(dbName="PICKDB", collectionName="EventConfiguration")
        # Adds the EC object into the DB, the adding of the object will be triggered when "OK" is clicked
        self.id = self.db_collection.add(self.event_config)


    # Setters of the Event Config's attributes
    def set_name(self, name):  # Editable
        self.name = name

    def set_description(self, description):  # Editable
        self.description = description

    def set_start_time(self, start_time):  # Editable
        self.start_time = start_time

    def set_end_time(self, end_time):  # Editable
        self.end_time = end_time

    def set_root_directory(self, root_directory):  # Non Editable
        self.root_directory = root_directory

    def set_red_team_folder(self, red_folder):  # Non Editable
        self.red_team_folder = red_folder

    def set_white_team_folder(self, white_folder):  # Non Editable
        self.white_team_folder = white_folder

    def set_blue_team_folder(self, blue_folder):  # Non Editable
        self.blue_team_folder = blue_folder

    def set_lead(self, lead):  # Editable
        self.lead = lead

    def set_lead_ip_add(self, lead_ip):  # Editable
        self.lead_ip_add = lead_ip

    def set_connection_status(self, connect_stat):  # Non Editable
        self.connect_stat = connect_stat

    # Getters of the Event Config's attributes
    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

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

    def get_lead(self):
        return self.lead

    def get_connect_stat(self):
        return self.connect_stat

    def get_lead_ip_add(self):
        return self.lead_ip_add

    """
        Function to obtain an EC object from the DB specifying search parameters
            - attribute: The EC's attribute that will be searched for in the EC collection
            - value: The attribute's value used as the search criteria
    """

    def pull_object(self, attribute, value):
        db_collection = DBFacade(dbName="PICKDB", collectionName="EventConfiguration")
        cursor1 = db_collection.search_n(attribute, value)
        for cursor in cursor1:
            self.name = cursor.get("Event Name")
            self.description = cursor.get("Description")
            self.start_time = cursor.get("Event Start Time ")
            self.end_time = cursor.get("Event End Time")
            self.root_directory = cursor.get("Root Directory")
            self.red_team_folder = cursor.get("Red Team Folder")
            self.blue_team_folder = cursor.get("Blue Team Folder")
            self.white_team_folder = cursor.get("White Team Folder")
            self.lead = cursor.get("Lead")
            self.lead_ip_add = cursor.get("Lead IP Address")
            self.connect_stat = cursor.get("Connection Status")
        print("Event Configuration pulled from DB with search criteria: ", attribute, "-->", value)
