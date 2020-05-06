# Cleansing, validation should be through before the ingestion process should begin and after sent to Splunk Ingestion should be set to true

class LogFile:
    def __init__(self, name, path):       # Constructor of a Log File requires a name and sets flags to false
        self.name = name
        self.path = path
        #self.objectID = objectID
        self.errors = []
        self.cleansingStat = True
        self.validationStat = True
        self.ingestionStat = False
        self.acknowledgementStat = False


# Class  functions to change the status of the attributes of any log file
    #def set_objectid(self, objectID):
    #    self.objectID = objectID

    def setCleansingStat(self):
        self.cleansingStat = False

    def setIngestionStat(self):
        self.ingestionStat = True

    def setInvalidStat(self):
        self.invalidStat = True


# Getters for all the Log File attributes
    #def get_objectID(self):
    #    return self.objectID

    def get_path(self):
        return self.path

    def get_name(self):
        return self.name

    def getCleansingStat(self):
        return self.cleansingStat

    def getValidationStat(self):
        return self.validationStat

    def makeInvalid(self):
        self.validationStat = False

    def isInvalid(self):
        self.validationStat is False

    def isValid(self):
        self.validationStat is True

    def makeInvalid(self):
        self.validationStat = False

    def makeValid(self):
        self.validationStat = True

    def isInvalid(self):
        self.validationStat is False

    def isValid(self):
        self.validationStat is True

    def getIngestionStat(self):
        return self.ingestionStat

    def getAcknowledgementStatus(self):
        if self.cleansingStat and self.validationStat and self.ingestionStat:
            self.acknowledgementStat = True

    def insert_errors(self, e):
        self.errors.append(e)

    def getAcknowledgementStatus(self):
        if self.cleansingStat and self.validationStat and self.ingestionStat:
            self.acknowledgementStat = True

    def insert_errors(self, e):
        self.errors.append(e)
