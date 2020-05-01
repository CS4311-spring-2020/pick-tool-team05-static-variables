import sys
from PyQt5.QtWidgets import QApplication

from Source.Backend.Ingestion.SplunkFacade import SplunkFacade
from Source.Backend.Ingestion.Cleanser import Cleanser
from Source.Backend.Ingestion.EnforcementActionReport import EnforcementActionReport
from Source.Frontend.GraphicalUserInterface import MainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    #g = MainWindow()

    #test2 = Cleanser()
    #test = SplunkFacade(test2.cpath)
    #test3 = EnforcementActionReport()

    sys.exit(app.exec_())