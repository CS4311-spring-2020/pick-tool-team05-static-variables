
import csv
import os
import re


from Source.Backend.Ingestion.SplunkFacade import SplunkFacade


#know log file directories from even config
#ingest files from splunk & cleanser
#attempt to scan for changes from splunk facade

class ingestion:
    def __init__(self):

        self.teamDir = []
        self.get_team_directories()
        self.entriesToStore = []


    def get_team_directories(self):
        for dir in self.getDirectories():
            self.teamDir.append(dir)
        print(self.teamDir)
        return self.teamDir

    def getDirectories(self):
        #get from event config
        pass

    def store_entries(self):
        entriesToStore = SplunkFacade.get_log_entries()
        return entriesToStore




    def total_files(self, path):
        file_count = len(path(os.getcwd()))
        return file_count


