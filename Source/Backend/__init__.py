import sys
import threading
from PyQt5.QtWidgets import QApplication
from Source.Frontend.GraphicalUserInterface import MainWindow
from Source.Frontend.gui_team_configuration import TeamConfiguration

if __name__ == '__main__':
    app = QApplication(sys.argv)
    g = MainWindow()
    # t1 = threading.Thread(target=TeamConfiguration, args=())
    # t2 = threading.Thread(target=MainWindow, args=())
    # t1.start()
    # t2.start()
    # t1.join()

    sys.exit(app.exec_())
