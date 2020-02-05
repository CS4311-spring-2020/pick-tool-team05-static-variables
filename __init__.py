import sys
from PyQt5.QtWidgets import QApplication

#To test stuff, call your GUIs here in your branch. If you merge to master, make sure to leave the file like this.
from GUI.gui_addvector import addVector
from GUI.gui_confirmationMessage import confirmation
from GUI.gui_connect_initial import ConnectHost
from GUI.gui_editNode import editNode

from GUI.gui_eventconfig_error import EventConfigError
from GUI.gui_local_warning import LocalCopyWarning
from GUI.gui_logIngestion import logIngestion
from GUI.gui_nodeCorr import nodeCorrelation

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # test = addVector()
    # test = logIngestion()
    # test = nodeCorrelation()
    # test = confirmation()
    test = editNode()
    sys.exit(app.exec_())
