import sys
from PyQt5.QtWidgets import QApplication

# from Source.Backend.Ingestion.SplunkFacade import SplunkFacade
# from Source.Backend.Ingestion.Cleanser import Cleanser
# from Source.Backend.Ingestion.SplunkFacade import Test
from Source.Backend.Data.EventConfiguration import EventConfiguration
from Source.Frontend.GraphicalUserInterface import MainWindow
# from Source.Backend.Data.EventConfiguration import EventConfiguration
from Source.Backend.Data.Vector import Vector
from Source.Backend.Data.mongo_setup import global_init


# Database Testing
def db_ec_tests():
    # This information will be coming from the EC window, for testing reasons the dummy data is given here
    # Every time a new Object is created it will be inserted into the DB.
    EventConfiguration("SQL Attack", "This is an SQL attack", "12:49 04/18/20 PM", "11:49 04/18/20 PM",
                       'usr/local/', "usr/local/red", "usr/local/white", "usr/local/blue", "False", "127.0.0.1",
                       "4")
    EventConfiguration.get_name(EventConfiguration)

    # Pulling an object from the DB and loading it into the system with specified search criteria


# EventConfiguration.pull_object(EventConfiguration, "Event Name", "S")


# i = EventConfiguration.get_name(EventConfiguration)
# print(i)


# Vector Database Testing
def db_vector_tests():
    vdb = Vector("Sss", "attack")


if __name__ == '__main__':
    # app = QApplication(sys.argv)
    # g = MainWindow()
    # sys.exit(app.exec_())
    # test2 = Cleanser()
    # test = SplunkFacade(test2.cpath)

    db_ec_tests()

# global_init('PICKDB')
# db_vector_tests()
# EventConfiguration.pull_object(EventConfiguration,"Event Name", "A")
# s = EventConfiguration.get_start_time(EventConfiguration)
# print (s)
