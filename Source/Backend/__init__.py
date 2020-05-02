import sys
from PyQt5.QtWidgets import QApplication

# from Source.Backend.Ingestion.SplunkFacade import SplunkFacade
# from Source.Backend.Ingestion.Cleanser import Cleanser
# from Source.Backend.Ingestion.SplunkFacade import Test
from Source.Backend.Data.EventConfiguration import EventConfiguration
from Source.Frontend.GraphicalUserInterface import MainWindow
# from Source.Backend.Data.EventConfiguration import EventConfiguration
from Source.Backend.Data.Vector import Vector

if __name__ == '__main__':
    app = QApplication(sys.argv)
    g = MainWindow()
    sys.exit(app.exec_())
    # test2 = Cleanser()
    # test = SplunkFacade(test2.cpath)
