import csv
import os
import re

from Source.Backend.Ingestion.LogFile import LogFile

class Cleanser:

    def __init__(self):
        temp = []
        #dir example
        #self.path = "C:\\Users\\yamel\\Desktop\\splunk\\tests"
        #self.path = logfile.data.get("Filepath")
        #self.cpath = self.path + "\\Cleansed"
        #self.upath = self.path

        #creates cleansed dir if not in path
        #if not os.path.exists(self.cpath):
         #   os.mkdir(self.cpath)

    #gets rid of blank space & need to implement to get rid of non ascii
    def cleanse(self, logfile):
        upath = logfile.data.get("Filepath").split('/')[0]
        cpath = upath + "\\Cleansed"

        if not os.path.exists(cpath):
            os.mkdir(cpath)

        file = logfile.data.get("Filepath")
        with open(file) as in_file:
            with open(cpath + "/" + str(logfile.data.get("Filename")), 'w', newline='') as out_file:
                writer = csv.writer(out_file)
                for row in csv.reader(in_file):
                    if (any(field.strip() for field in row)) and self.is_ascii(str(row)):
                        writer.writerow(row)

        #updating filepath for cleansed file
        logfile.data["Filepath"] = cpath+'/'+logfile.data.get("Filename")
        #print(logfile.data.get("Filepath"))

        print(logfile.data.get("Filename"), " finished cleansing")

    def is_ascii(self, s):
        return all(ord(c) < 128 for c in s)



