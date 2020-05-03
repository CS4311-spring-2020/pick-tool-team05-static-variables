
import csv
import os
import path
import re
import datetime

from Source.Backend.Ingestion.LogFile import LogFile
from dateutil.parser import parse
from dateparser.search import search_dates

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
                    b=True
                    if self.has_date(str(row), b):
                        #LogFile.validationStat = True
                        print("in if stmt")

        print("finished going through directory")


    def has_date(self, row, fuzzy= False):
        try:
            parse(row, fuzzy=fuzzy)
            return True

        except ValueError:
            #self.errorList.append(e)
            #LogFile.validationStat = False
            return False