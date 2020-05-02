from PyQt5.QtWidgets import QTableWidgetItem
from Source.Backend.Data.DBFacade import add


class SignificantLogEntry(QTableWidgetItem):
    def __init__(self, log_entry_number, log_entry_timestamp, log_entry_content, host, source, source_type):
        self.logEntryNumber = log_entry_number
        self.logEntryTimestamp = log_entry_timestamp
        self.logEntryContent = log_entry_content
        self.host = host
        self.source = source
        self.sourceType = source_type

        self.significant_log_entry = {
            "Log Entry Number": self.logEntryNumber,
            "Log Entry Timestamp": self.logEntryTimestamp,
            "Log Entry Content": self.logEntryContent,
            "Host": self.host,
            "Source": self.source,
            "Source Type": self.sourceType
        }
# Not sure who wrote the code and not sure how it will affect the removal of reason for comment
"""
import inspect

from PyQt5.QtWidgets import QTableWidgetItem


class SignificantLogEntry(QTableWidgetItem):
    def __init__(self):
        super().__init__()

        self.main()

    def main(self):
        print('hi')

    def returnAttributes(self):
        att = inspect.getmembers(self, lambda i: not (inspect.isroutine(list)))
        return [i for i in att if not (i[0].endswith('__') and i[0].startswith('__'))]
"""
