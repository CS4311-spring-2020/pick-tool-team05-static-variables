from dateutil.parser import parse

#know log file from ingestion
#know the errors of the log file from error cless


class EnforcementActionReport:

    def __init__(self):
        testing = []


    def has_date(self, row, fuzzy= False):
        try:
            parse(row, fuzzy=fuzzy)
            return True

        except ValueError:
            return False

    def check_file(self, logfile):
        errorList = []
        for row in open(logfile.data.get("Filepath")):
            lineNum = 1
            b = True
            dateBool = self.has_date(str(row), b)
            if dateBool == False:
                errorMsg = "no time"
                if errorMsg:
                    errorList.append(lineNum)
                    logfile.data["Validation_Flag"] = False

            lineNum += 1

        if errorList == []:
            logfile.data["Validation_Flag"] = True

        return errorList