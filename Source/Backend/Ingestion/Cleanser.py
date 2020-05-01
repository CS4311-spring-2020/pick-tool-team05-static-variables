import csv
import os
import re


class Cleanser:

    def __init__(self):
        #dir example
        self.path = "C:\\Users\\yamel\\Desktop\\splunk\\tests"
        self.cpath = self.path + "\\Cleansed"
        self.upath = self.path + "\\Uncleansed"

        #creates cleansed dir if not in path
        if not os.path.exists(self.cpath):
            os.mkdir(self.cpath)

        #creates uncleansed dir if not in path
        if not os.path.exists(self.upath):
            os.mkdir(self.upath)

        self.cleanse()

    #gets rid of blank space & need to implement to get rid of non ascii
    def cleanse(self):
        print("starting cleanse")

        for filename in os.listdir(self.upath):
            file = self.upath + "\\" + filename

            with open(file) as in_file:
                with open(self.cpath + "\\" + filename, 'w', newline='') as out_file:
                    writer = csv.writer(out_file)
                    for row in csv.reader(in_file):
                        if (any(field.strip() for field in row)) and self.is_ascii(str(row)):
                            writer.writerow(row)

            print(filename + " finished cleansing")

    def is_ascii(self, s):
        return all(ord(c) < 128 for c in s)




#c = Cleanser()
#c.cleanse()


