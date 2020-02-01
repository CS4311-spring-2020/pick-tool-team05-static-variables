import sys
from PyQt5.QtWidgets import QApplication
from GUI.gui_launcher import Launcher
from GUI.gui_event_configuration import EventConfiguration
from GUI.gui_add_vector_pop_up import AddVectorPopUp

if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = Launcher()
    test2 = EventConfiguration()
    test3 = AddVectorPopUp()
    sys.exit(app.exec_())
