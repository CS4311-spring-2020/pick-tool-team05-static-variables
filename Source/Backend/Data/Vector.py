from PyQt5.QtWidgets import QWidget

from Source.Backend.Data.SignificantLogEntry import SignificantLogEntry


class Vector(QWidget):
    def __init__(self, name=None, description=None):
        super().__init__()
        self.__name = name
        self.__description = description
        self.__associatedLogs = []

    def getName(self):
        return self.__name

    def getDescription(self):
        return self.__description

    def setName(self, name):
        self.__name = name

    def setDescription(self, description):
        self.__description = description

    def getAssociatedLogCount(self):
        return self.__associatedLogs.count(SignificantLogEntry)
