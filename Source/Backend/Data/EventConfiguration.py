from PyQt5.QtCore import pyqtSignal
from Source.Backend.Data.DBFacade import add_object, search_object


class EventConfiguration:
    eventConfigurationSignal = pyqtSignal()

    def __init__(self, name=None, description=None, start_time=None, end_time=None, root_directory=None,
                 red_team_folder=None, white_team_folder=None, blue_team_folder=None, lead_status=None,
                 lead_ip_address=None, connections=None):

        # Search event configuration in Database
        s = search_object("Event Name", "event configuration", "EventConfiguration")

        # If it doesn't exist in database, add it to Database. Else, instantiate object with data from search result
        if s is None:
            self.data = {
                "Event Name": name,
                "Description": description,
                "Event Start Time ": start_time,
                "Event End Time": end_time,
                "Root Directory": root_directory,
                "Red Team Folder": red_team_folder,
                "White Team Folder": white_team_folder,
                "Blue Team Folder": blue_team_folder,
                "Lead Status": lead_status,
                "Lead IP Address": lead_ip_address,
                "Connections": connections
            }

            add_object(self.data, "EventConfiguration")
        else:
            self.data = s
