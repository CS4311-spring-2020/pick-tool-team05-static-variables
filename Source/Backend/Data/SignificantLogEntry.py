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
