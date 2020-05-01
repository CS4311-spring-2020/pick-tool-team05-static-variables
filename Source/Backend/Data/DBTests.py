import sys
import unittest

from PyQt5.QtWidgets import QApplication

from Source.Backend.Data.EventConfiguration import EventConfiguration
from Source.Backend.Data.Vector import Vector
from Source.Frontend.GraphicalUserInterface import MainWindow


class DBTests(unittest.TestCase):

    # Test Case to Add a Event Configuration object in the DB
    # def test_ec_add(self):
    #   EventConfiguration("AA Attack", "This is an AA attack", "12:49 04/18/20 PM", "11:49 04/18/20 PM",
    #                     'usr/local/', "usr/local/red", "usr/local/white", "usr/local/blue", "False",
    #                    "127.0.0.1",
    #                   "4")

    # Test Case to Update a Event Configuration object in the DB
    # def test_ec_update(self):
    #   EventConfiguration("Changed Name", "This is not an AA attack", "12:49 04/18/20 PM", "11:49 04/18/20 PM",
    #                     'usr/local/', "usr/local/red", "usr/local/white", "usr/local/blue", "False",
    #                    "127.0.0.1",
    #                   "4")
    # EventConfiguration.update(EventConfiguration,"Name","A")
    # i = EventConfiguration.get_name(EventConfiguration)

    # Test Case to Pull an Event Configuration Object from the DB with specified searching parameters
    #def test_ec_pull(self,att,val):
     #   EventConfiguration.pull_object(EventConfiguration, att, val)
      #  i = EventConfiguration.get_name(EventConfiguration)
       # print(i)

    # Test Case to Add a Vector object in the DB
    #def test_vector_add(self):
     #   Vector("Ddos", "An attack")

    #def test_vector_delete(self):
        #Vector.delete(Vector,"Name","Ddos")

    if __name__ == '__main__':
        # test_ec_add()
        # test_ec_delete()
        # test_ec_update()
        #test_ec_pull("Event Name", "A")



         #test_vector_add()
         #test_vector_delete()
        # test_vector_update()
        # test_vector_pull()

        # runs all the tests at the same time
        unittest.main()
