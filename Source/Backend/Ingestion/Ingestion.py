
import csv
import os
import re
from dateutil.parser import parse
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
        self.cleanse_LogFiles(self.log_file_list)
        self.validate_all_files(self.log_file_list)
        #self.force_validate(self.log_file_list)

        self.upload_logfiles_to_splunk(self.log_file_list)


        #self.test()



    def test(self):
        for log in self.log_file_list:
            for row in open(log.data.get("Filepath")):
                b = True
                print(EnforcementActionReport().has_date(str(row), b), str(row))


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
            Cleanser().cleanse(log)
            log.data["Cleanse_Flag"] = True
        print("finished cleansing")

    def validate_all_files(self, loglist):
        print("Enforcement Action Report Part")

        for log in loglist:
            errorLine = EnforcementActionReport().check_file(log)
            if log.data.get("Validation_Flag") is False:

                print("Invalid, ", log.data.get("Filename"), " Error Line(s): ", errorLine[0],
                      " Error Message: Missing Timestamp/Invalid Timestamp ")
            else:
                print("is valid ", log.data.get("Filename"), log.data.get("Validation_Flag"))
                log.data["Validation_Flag"] = True

    def force_validate(self, logfile):
        print("force validating...")
        for log in logfile:
            if log.data.get("Validation_Flag") == False:
                log.data["Validation_Flag"] = True
            print(log.data.get("Validation_Flag"))

    def upload_logfiles_to_splunk(self, logfiles):
        #SplunkFacade().service
        uname, pswd = SplunkFacade().get_credentials()
        print(uname, pswd)
        for log in logfiles:
            if log.data.get("Validation_Flag") is not False:
                SplunkFacade().upload(log, uname, pswd)

        entries = SplunkFacade().get_log_entries(uname, pswd)
        for e in entries:
            print(e)
