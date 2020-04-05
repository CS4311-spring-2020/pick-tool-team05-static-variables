# Cleansing, validation should be through before the ingestion process should begin and after sent to Splunk Ingestion should be set to true
# All this information should be saved in the database, where I believe it is through the ingestion facade where it should make the call.
class LogFile:
    def __init__(self, name):       # Constructor of a Log File requires a name and sets flags to false
        self.cleansingStat = False
        self.validationStat = False
        self.ingestionStat = False
        self.name = name

# Class  functions to change the status of the attributes of any log file
    def setCleansingStat(self, stat):
        self.cleansingStat = stat

    def setValidationStat(self, stat):
        self.validationStat = stat

    def setIngestionStat(self, stat):
        self.ingestionStat = stat

# Class function that will force validate, changing all the log file attributes to true
    def setAcknowledgementStatus(self):
        self.cleansingStat = True
        self.validationStat = True
        self.ingestionStat = True

# Getters for all the Log File attributes
    def getCleansingStat(self):
        return self.cleansingStat

    def getValidationStat(self):
        return self.validationStat

    def getIngestionStat(self):
        return self.ingestionStat
