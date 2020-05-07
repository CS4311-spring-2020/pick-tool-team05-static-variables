
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

    def __init__(self):
        testing = []


    def has_date(self, row, fuzzy= False):
        try:
            parse(row, fuzzy=fuzzy)
            return True

        except ValueError:
            return False

    def check_file(self, file):
        errorList = []
        for row in open(file.data.get("Filepath")):
            lineNum = 1
            b = True
            dateBool =  self.has_date(str(row), b)
            if dateBool == False:
                errorMsg = "Timestamp doesn't exist"
                if errorMsg:
                    errorList.append(lineNum)
                    file.data["Validation_Flag"] = False
                else:
                    file.data["Validation_Flag"] = True
            lineNum += 1

        return errorList