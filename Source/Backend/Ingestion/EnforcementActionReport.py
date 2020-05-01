
import csv
import os
import path
import datetime

#know log file from ingestion
#know the errors of the log file from error cless





class EnforcementActionReport:

    def __init__(self, cpath):
        self.path = cpath
        self.errorList = []



    def validate_date(self, file):
        #pass
        try:


