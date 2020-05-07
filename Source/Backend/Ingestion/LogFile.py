from PyQt5.QtCore import pyqtSignal, QObject
from Source.Backend.Data.DBFacade import search_object, add_object, update_object


# Cleansing, validation should be through before the ingestion process should begin and after sent to Splunk Ingestion should be set to true
# All this information should be saved in the database, where I believe it is through the ingestion facade where it should make the call.


class LogFile(QObject):
    def __init__(self, filepath, _id=None):
        super().__init__()
        self.signal = pyqtSignal()

        if _id is not None:
            self.data = search_object("_id", _id, "LogFile")
        else:
            s = search_object("Filepath", filepath, "LogFile")
            if s is not None:
                self.data = s
            else:
                self.data = {
                    "Filename": filepath.split('/'[-1]),
                    "Filepath": filepath,
                    "Cleanse_Flag": False,
                    "Validation_Flag": False,
                    "Ingestion_Flag": False,
                    "Acknowledgement_Flag": False,
                }

                self.add()

    def add(self):
        add_object(self.data, "LogFile")
        self.data = search_object("Name", self.data.get("Filename"), "LogFile")

    def update(self):
        update_object(self.data.get("_id"), self.data, "LogFile")

# Class function that will force validate, changing all the log file attributes to true
    def setAcknowledgementStatus(self):
        if self.cleansingStat and self.validationStat and self.ingestionStat:
            return True
        else:
            return False
