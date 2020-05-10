import sys
import subprocess
from PyQt5.QtWidgets import QApplication

from Source.Backend.Data.EventConfiguration import EventConfiguration
from Source.Backend.Data.Vector import Vector
from Source.Frontend.GraphicalUserInterface import MainWindow
from Source.Backend.Ingestion.Ingestion import Ingestion
import threading


if __name__ == '__main__':
    db = subprocess.Popen(['C:/Program Files/MongoDB/Server/4.2/bin/mongod.exe', '--dbpath', '../Source/Database'], shell=True)

    # event_configuration = EventConfiguration("SQL Attack", "This is an SQL attack", "12:49 04/18/20 PM",
    #                                               "11:49 04/18/20 PM", 'usr/local/', "usr/local/red",
    #                                               "usr/local/white", "usr/local/blue", "True", "127.0.0.1", "4")

    event_configuration = EventConfiguration("SQL Attack", "This is an SQL attack", "12:49 04/18/20 PM",
                                            "11:49 04/18/20 PM", 'usr/local/', "C:\\Users\\theli\\Desktop\\a",
                                            "usr/local/white", "usr/local/blue", "True", "127.0.0.1", "4")
    app = QApplication(sys.argv)
    g = MainWindow()

    #test = Ingestion("C:\\Users\\yamel\\Desktop\\splunk\\tests\\Uncleansed")
    print(event_configuration.data.get("Red Team Folder"))
    splunk = threading.Thread(target=Ingestion.init_thread)
    splunk.start()
    sys.exit(app.exec_())
