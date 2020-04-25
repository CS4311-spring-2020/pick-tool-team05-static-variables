
import sys
from PyQt5.QtWidgets import QApplication

# from Source.Backend.Ingestion.SplunkFacade import SplunkFacade
# from Source.Backend.Ingestion.Cleanser import Cleanser
# from Source.Backend.Ingestion.SplunkFacade import Test
from Source.Frontend.GraphicalUserInterface import MainWindow
from Source.Backend.Data.EventConfiguration import EventConfiguration
#from Source.Backend.Data.Vector import Vector


# Database Testing
def db_tests():
    # This information will be coming from the EC window, for testing reasons the dummy data is given here
    ec = EventConfiguration("AA Attackkkkk", "This is an attack", "HH:MM MM/DD/YY AM/PM", "HH:MM MM/DD/YY AM/PM",
                            'usr/local/', "usr/local/red","usr/locaffl/white", "usr/qfflocal/blue", False, "127.0.0.1", 4)
    # Pulling an object from the DB and loading it into the DB.
    ec.pull_object("Event Name", "S")
    i = ec.get_name()
    print(i)


#Vector Database Testing
#vdb = Vector("Ddos", "attack")

if __name__ == '__main__':
    #app = QApplication(sys.argv)
    #g = MainWindow()
    #sys.exit(app.exec_())
    # test2 = Cleanser()
    # test = SplunkFacade(test2.cpath)

    db_tests()







