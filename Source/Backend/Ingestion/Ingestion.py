
import csv
import os
import re

from Source.Backend.Ingestion.LogFile import LogFile
from Source.Backend.Ingestion.Cleanser import Cleanser
from Source.Backend.Ingestion.EnforcementActionReport import EnforcementActionReport
from Source.Backend.Ingestion.SplunkFacade import SplunkFacade

#know validation parameters from event config
#know log file directories from even config
#validate log files from event config
#ingest files from splunk & cleanser



class Ingestion:
    #def __init__(self, path):
        #self.path = path
    def __init__(self, path):
        self.path = path
        self.log_file_list = []
        self.populate_LogFiles(self.path)
        print("printing logfile names")
        self.test()

        self.cleanse_LogFiles(self.log_file_list)
        #
    def test(self):
        for log in self.log_file_list:
            print(log.data.get("Filename"))


    def populate_LogFiles(self, path):
        print("populating logfiles...")
        if not os.path.exists(path):
            print("given path: ", path, " doesnt exist")
            return

        for filename in os.listdir(path):
            filepath = path + "/" + filename
            #print("printing filepath", filepath)
            self.log_file_list.append(LogFile(filepath))
            #print(filename)
        print("finished populating log files")
        print(self.log_file_list)

    def cleanse_LogFiles(self, loglist):
        print("starting cleanse")
        for log in loglist:
            print("gonna cleanse ", log.data.get("filepath"))
            Cleanser().cleanse(log)
            log.data["Cleanse_Flag"] = True
        print("finished cleansing")

    def validate_all_files(self, loglist):
        print("Enforcement Action Report Part")

        for log in loglist:
            errorLine = EnforcementActionReport.check_file(log)
            if log.data.get("Validation_Flag") is False:
                print("Invalid, ", log.data.get("Filename"), " Error Line: ", errorLine[0][0],
                      " Error Message: Missing Timestamp/Invalid Timestamp ")
            else:
                print("is valid ", log.data.get("Filename"), log.data.get("Validation_Flag"))

    #def force_validate(self, lofile):



