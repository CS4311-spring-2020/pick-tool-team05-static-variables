class LogEntry:
    def __init__(self):
        self.number
        self.time_stamp
        self.content
        self.host
        self.source
        self.type


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
