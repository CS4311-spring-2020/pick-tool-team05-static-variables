
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

        #boi = self.has_date("Sep 11 09:46:33 sys1 crontab[20601]: (root) BEGIN EDIT (root)")
        #print(boi)

        #populate logFile obj
        self.populate_LogFiles(cpath)
        self.log_file_list = self.validate_all_files(self.log_file_list)





###############################################################

    def populate_LogFiles(self, path):
        #print("beginning to go through directory")
        for filename in os.listdir(path):
            filepath = path + "\\" + filename
            self.log_file_list.append(LogFile(filename, filepath))
        #print("finished going through directory")


    def has_date(self, row):
        try:
            parse(row, fuzzy_with_tokens=True)
            return True

        except ValueError as e:
            #print(e)
            return False

    def validate_file(self, logfile):
        errorList = []
        for row in open(logfile.get_path()):
            lineNum = 1
            b = True
            dateBool = self.has_date(str(row))
            #print("reading")
            #print(dateBool)
            if not dateBool:
                errorMsg = "Invalid Timestamp/Timestamp doesn't exit"
                #print(errorMsg)
                if errorMsg:
                    #errorList.append(filename)
                    #print(errorMsg)
                    errorList.append(lineNum)
                    logfile.insert_errors(errorList)
                    #logfile.setValidationStat()
                    logfile.makeInvalid()
                    #print("in false")
            lineNum += 1
        return logfile

    def validate_all_files(self, loglist):
        for log in self.log_file_list:
            #print("mffff")
            self.validate_file(log)

            if log.getValidationStat() is False:
                #print("this bitch")
                print("Invalid, ", log.name, " Error Line: ", log.errors[0][0], " Error Message: Missing Timestamp/Invalid Timestamp ")
            else:
                print("is valid ", log.name, log.getValidationStat())
                log.setIngestionStat()
        return loglist
