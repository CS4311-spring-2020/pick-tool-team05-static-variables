
import csv
import os
import re


from Source.Backend.Ingestion.SplunkFacade import SplunkFacade

#know validation parameters from event config
#know log file directories from even config
#validate log files from event config
#ingest files from splunk & cleanser
#attempt to scan for changes from splunk facade
#know log file format



class ingestion:
    def __init__(self):

        self.teamDir = []
        self.get_team_directories()
        self.entriesToStore = []

    def validation(self):
        pass


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

    def knowFormat(self):
        pass






    def total_files(self, path):
        file_count = len(path(os.getcwd()))
        return file_count

    #this function recognizes unsupported file types
    #& gets rid of them from the dire
    def unsupported_file_type(self):
        d = self.path
        #yeilds only to files of type from directory
        type = d.walkfiles("*.txt")
        #ocr
        type1 = d.walkfiles("*.jpg")
        type2 = d.walkfile("*.png")
        type3 = d.walkfile("*.pdf")
        #audio
        type4 = d.walkfiles("*.mp3")
        type5 = d.walkfile("*.mp4")
        type6 = d.walkfile("*.wav")

        if not type:
            for file in type1:
                file.remove()
                print("Removed {} file".format(file))

