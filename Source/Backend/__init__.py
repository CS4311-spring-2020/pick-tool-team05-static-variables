import sys
import subprocess
from PyQt5.QtWidgets import QApplication

from Source.Backend.Ingestion.SplunkFacade import SplunkFacade
from Source.Backend.Ingestion.Cleanser import Cleanser
from Source.Backend.Ingestion.EnforcementActionReport import EnforcementActionReport
from Source.Frontend.GraphicalUserInterface import MainWindow


if __name__ == '__main__':

    db = subprocess.Popen(['C:Program Files/MongoDB/Server/4.2/bin/mongod.exe', '--dbpath', '../Source/Database'], shell=True)
    ##splunk = subprocess.Popen(['C:Program Files/Splunk/bin/splunk.exe', ''])


    app = QApplication(sys.argv)
    #g = MainWindow()
    test2 = Cleanser()
    test3 = EnforcementActionReport(test2.cpath)
    test = SplunkFacade(test2.cpath)

    sys.exit(app.exec_())