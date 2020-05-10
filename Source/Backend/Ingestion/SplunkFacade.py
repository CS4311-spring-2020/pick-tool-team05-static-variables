import os
import subprocess
from splunklib import results
import splunklib.client as client

from Source.Backend.Ingestion.Cleanser import Cleanser

import json

# I have not had time to implement everything discussed in the SDD in Splunk.
# I still use this a lot for examples https://dev.splunk.com/enterprise/docs/python/sdk-python/howtousesplunkpython
# Dr.Roach also sent out email regarding Splunk, it might also be helpful
class SplunkFacade:
    def __init__(self):

        # Constants created with log-in information
        self.HOST = "localhost"
        self.PORT = 8089
        #USERNAME = "Minikitteh"
        #PASSWORD = "Mini111~@"

        #self.logList = []
        #self.list2 = self.getLogEntries()
        #print(self.list2)
        #self.get_log_entries()

    def get_credentials(self):
        username = (input("input username: "))
        password = (input("input password: "))
        return username, password


    #def get_log_entries_testing(self):
        #for items in self.getLogEntries():
         #   self.logList.append(items)
        #print(self.logList)
        #return self.logList


    def upload(self, logfile, uname, passwrd):
        #self.service
        # Retrieve the index for the data
        serv = client.connect(host=self.HOST,port=self.PORT, username=uname,password=passwrd)
        current_index = serv.indexes["main"] # indexes are like folders inside Splunk, you can create new indexes with a command not found here, this is to get an index already existing
        #current_index = self.service.indexes["test_index"]
        #for filename in os.listdir(self.path):
        try:
            #current_index.upload(self.path + "\\" + filename)
            current_index.upload(logfile.data.get("Filepath"))
            logfile.data["Ingestion_Flag"] = True
            print(logfile.data.get("Filename"),"uploaded file, ingestion stat now ", logfile.data.get("Ingestion_Flag"))
            #count += 1
        except Exception as e:
            print("Failed to upload, error ", str(e))

    def get_log_entries(self, uname, passwrd):
        serv = client.connect(host=self.HOST,port=self.PORT, username=uname,password=passwrd)
        #Create a job instance and query the first five events(log entries)
        job = serv.jobs.create("search * | head 20")
        rr = results.ResultsReader(job.preview()) # returns a dictionary with the information inside Splunk
        log_entries = [] # Creates a list and just append the information with the right keys from Splunk
        for entry in rr:
            #print(entry)
            log_entries.append([entry['_raw'], entry['_time'], entry['source']])

        return log_entries


