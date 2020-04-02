import os, csv


class Cleanser:
    def __init__(self, path):
        self.path = "C:\\Users\\mdelgado\\Desktop\\Log Examples3"

        if not os.path.exists(path + "\\Cleansed"):
            os.mkdir(path + "\\Cleansed")

    def Open(self):
        for filename in os.listdir(self.path):

            (self.path + "\\" + filename)
