import sys
from PyQt5.QtWidgets import QApplication

#from Source.Backend.Ingestion.SplunkFacade import SplunkFacade
#from Source.Backend.Ingestion.Cleanser import Cleanser
# from Source.Backend.Ingestion.SplunkFacade import Test
from Source.Frontend.GraphicalUserInterface import MainWindow
from Source.Backend.Data.EventConfiguration import EventConfiguration


if __name__ == '__main__':
   app = QApplication(sys.argv)
   g = MainWindow()
   sys.exit(app.exec_())

    #test2 = Cleanser()
    #test = SplunkFacade(test2.cpath)

    # Database Testing
    #ec = EventConfiguration("SQL..", "", "HH:MM MM/DD/YY AM/PM", "HH:MM MM/DD/YY AM/PM", 'usr/local/', "usr/local/red",
                            #"usr/locaffl/white", "usr/qfflocal/blue", False, "127.0.0.1", 4)


