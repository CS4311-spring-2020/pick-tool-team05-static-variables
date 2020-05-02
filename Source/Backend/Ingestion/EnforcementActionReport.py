
import csv
import os
import path
import datetime
from Source.Backend.Ingestion.LogFile import LogFile
from dateutil.parser import parse

#know log file from ingestion
#know the errors of the log file from error cless





class EnforcementActionReport:

    def __init__(self, cpath):
        self.path = cpath
        self.errorList = []
        self.go_through_files(self.path)
        print(self.errorList)




    def go_through_files(self, path):
        print("beginning to go through directory")

        for filename in os.listdir(path):
            file = path + "\\" + filename
            with open(file) as in_file:
                for row in csv.reader(in_file):
                    if self.validate_date(row):
                        LogFile.validationStat = True

        print("finished going through directory")


    def validate_date(self, row, b = False):
        try:
            parse(row, b = b)
            return True

        except Exception as e:
            self.errorList.append(e)
            LogFile.validationStat = False
            return False