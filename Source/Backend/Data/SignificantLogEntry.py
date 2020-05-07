from PyQt5.QtWidgets import QTableWidgetItem
# from Source.Backend.Data.DBFacade import add


class SignificantLogEntry(QTableWidgetItem):
    def __init__(self, **kwargs):

        self.logEntryNumber = kwargs.get("key")
        self.logEntryTimestamp = kwargs.get("key")
        self.logEntryContent = kwargs.get("key")
        self.host = kwargs.get("key")
        self.source = kwargs.get("key")
        self.sourceType = kwargs.get("key")

        self.significant_log_entry = {
            "Log Entry Number": self.logEntryNumber,
            "Log Entry Timestamp": self.logEntryTimestamp,
            "Log Entry Content": self.logEntryContent,
            "Host": self.host,
            "Source": self.source,
            "Source Type": self.sourceType
        }

    def getSignificantLogEntry(self):
        return self.significant_log_entry
