import os
from splunklib import results
import splunklib.client as client

class SplunkFacade:
    def __init__(self):
        # Hardcoded path
        self.path = "C:\\Users\\mdelgado\\Desktop\\Log Examples"

        # Constants created with log-in information
        HOST = "localhost"
        PORT = 8089
        USERNAME = "menny"
        PASSWORD = "Manuel27!"

        # Create a Service instance and log in
        self.service = client.connect(
            host=HOST,
            port=PORT,
            username=USERNAME,
            password=PASSWORD)

    def upload(self):
        # Retrieve the index for the data
        current_index = self.service.indexes["main"]

        for filename in os.listdir(self.path):
            # Upload and index the file
            current_index.upload(self.path + "\\" + filename)

    def getLogEntries(self):
        # Create a job instance and query the first five events(log entries)
        job = self.service.jobs.create("search * | head 5")
        rr = results.ResultsReader(job.preview())

        log_entries = []

        for entry in rr:
            log_entries.append([entry['_serial'], entry['_raw'], entry['_time'], entry['source']])

        return log_entries


class test(SplunkFacade):
    pass


s = SplunkFacade()

print(s.getLogEntries())
