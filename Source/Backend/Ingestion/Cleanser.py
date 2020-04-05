import csv
import os

# Making a Facade so the system has the ability to choose different correct cleansers for each log file
# Ingestion facade should read what type of log file it is
# Every type of cleanser should remember to call Splunk Facade to give it the clean output
# All this different class in one are wrong, it was barely on the works. They need to be seperated.
# Dr.Roach email examples the clients provided, study that to formulate a way to make the cleansing configurable and scalable.

class CleanserFacade:
    def __init__(self, path):
        self.path = path

    def chooseCleanser(self):
        pass


class Cleanser:
    # All these paths are hardcoded because it is for demonstration purposes, and because I don't know whether the cleansed log files should be saved or not
    # When you find out whether they need to be saved or not, it will talk with the dbFacade in order to save
    def __init__(self):
        self.path = "C:\\Users\\mdelgado\\Desktop\\Log Examples3" # Example log file that I created in order to test out the cleansing
        self.cpath = self.path + "\\Cleansed"
        self.upath = self.path + "\\unfiltered"

        if not os.path.exists(self.cpath):
            os.mkdir(self.cpath)

    def read(self):
        for filename in os.listdir(self.upath):
            file = self.upath + "\\" + filename

            with open(file) as in_file:
                with open(self.cpath + "\\" + filename, 'w', newline='') as out_file:
                    writer = csv.writer(out_file)
                    for row in csv.reader(in_file):
                        if any(field.strip() for field in row):
                            writer.writerow(row)
            print(filename + " Finished Cleansing")


import re
import unicodedata

# Started to test different functions from re


class TxtCleanser:

    def __init__(self):
        string = re.sub(r'[ \s\t\n]+', ' ', 'The     quick brown                \n\n             \t        fox')
        print(string)

    printable = {'Lu', 'Ll'}

    def filter_non_printable(self, string, pritable):
        return ''.join(c for c in string if unicodedata.category(c) in printable)


class Test:
    pass


c = Cleanser()
n = TxtCleanser()

c.read()
