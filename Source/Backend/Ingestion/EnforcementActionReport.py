
import csv
import os
import path
import re
import datetime

from Source.Backend.Ingestion.LogFile import LogFile
from dateutil.parser import parse
from dateparser.search import search_dates

#know log file for ingestion
#know the errors of the log file


class EnforcementActionReport:

    def __init__(self, cpath):
        self.path = cpath
        self.errors = []
        self.log_file_list = []

        #populate logFile obj
        self.populate_LogFiles(cpath)

        self.logs = self.log_file_list[:]

        #print(self.log_file_list.name)
        for log in self .log_file_list:
            self.validate_file(log)
            print("lets goooo", log.name)

        for log in self.log_file_list:
            print("mffff")
            #print(self.validate_file(logs))

            if log.getInvalidStat is False:
                print("sfjkdbj")
                log.setIngestionStat()
                log.setValidationStat()
                print(log.get_name)
                print(log.getValidationStat)


    def populate_LogFiles(self, path):
        print("beginning to go through directory")
        for filename in os.listdir(path):
            filepath = path + "\\" + filename
            self.log_file_list.append(LogFile(filename, filepath))
        print("finished going through directory")


    def has_date(self, row, fuzzy= False):
        try:
            parse(row, fuzzy=fuzzy)
            return True

        except ValueError:
            return False

    def validate_file(self, logfile):
        errorList = []
        for row in open(logfile.get_path()):
            lineNum = 1
            b = True
            dateBool = self.has_date(str(row), b)
            #print("reading")
            if not dateBool:
                errorMsg = "Invalid Timestamp/Timestamp doesn't exit"
                #print(errorMsg)
                if errorMsg:
                    # errorList.append(filename)
                    #print(errorMsg)
                    errorList.append(lineNum)
                    errorList.append(errorMsg)
                    logfile.insert_errors(errorList)
                    #logfile.setValidationStat()
                    logfile.setInvalidStat()
                    #print("in false")
            lineNum += 1
        return logfile