import os
from splunklib import results
import splunklib.client as client


# I have not had time to implement everything discussed in the SDD in Splunk.
# I still use this a lot for examples https://dev.splunk.com/enterprise/docs/python/sdk-python/howtousesplunkpython
# Dr.Roach also sent out email regarding Splunk, it might also be helpful
class SplunkFacade:
    def __init__(self, cpath):
        # Hardcoded path
        #self.path = "C:\\Users\\mdelgado\\Desktop\\Log Examples"
        #this is uncleansed path
        self.path = "C:\\Users\\yamel\\Desktop\\splunk\\tests"

        #cleansed
        self.path = cpath
        #self.path = Cleanser.cpath

        # Constants created with log-in information
        HOST = "localhost"
        PORT = 8089
        #USERNAME = "menny" # Individual information needed by Splunk, was thinking of creating a class in the future that will allow the individual user to set that info
        USERNAME = "Minikitteh"
        #PASSWORD = "Manuel27!"
        PASSWORD = "Mini111~@"

        # Create a Service instance and log in
        self.service = client.connect(
            host=HOST,
            port=PORT,
            username=USERNAME,
            password=PASSWORD)

        self.upload()

        self.logList = []




    def get_log_entries(self):
        for items in self.getLogEntries():
            self.logList.append(items)
        print(self.logList)
        return self.logList


    def upload(self):
        # Retrieve the index for the data
        current_index = self.service.indexes["main"] # indexes are like folders inside Splunk, you can create new indexes with a command not found here, this is to get an index already existing
        for filename in os.listdir(self.path):
            # Upload and index the file
            try:
                current_index.upload(self.path + "\\" + filename)
            except Exception as e:
                print("Failed to upload, error ", str(e))

    def getLogEntries(self):
        # Create a job instance and query the first five events(log entries)
        job = self.service.jobs.create("search * | head 5")
        rr = results.ResultsReader(job.preview()) # returns a dictionary with the information inside Splunk
        log_entries = [] # Creates a list and just append the information with the right keys from Splunk
        for entry in rr:
            log_entries.append([entry['_serial'], entry['_raw'], entry['_time'], entry['source']])
        '''
        for item in log_entries:
            print(*item)
        '''
        ''''
        print(log_entries)
        '''
        return log_entries



#class Test(SplunkFacade): #Just a basic test to make sure information moves correctly.
 #   pass
#s = SplunkFacade()

#for items in s.getLogEntries():
 #   y = json.dumps(items)
  #  print(y)