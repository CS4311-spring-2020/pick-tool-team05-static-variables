import sys
import subprocess
import psutil
from PyQt5.QtWidgets import QApplication

from Source.Backend.Data.EventConfiguration import EventConfiguration
from Source.Frontend.GraphicalUserInterface import MainWindow


if __name__ == '__main__':
    db = subprocess.Popen(['C:/Program Files/MongoDB/Server/4.2/bin/mongod.exe', '--dbpath', '../Source/Database'], shell=True)

    event_configuration = EventConfiguration("SQL Attack", "This is an SQL attack", "12:49 04/18/20 PM",
                                                  "11:49 04/18/20 PM", 'usr/local/', "usr/local/red",
                                                  "usr/local/white", "usr/local/blue", "True", "127.0.0.1", "4")

    app = QApplication(sys.argv)
    g = MainWindow()
    sys.exit(app.exec_())
