import sys
from PyQt5.QtWidgets import QApplication

# To test stuff, call your GUIs here in your branch. If you merge to master, make sure to leave the file like this.
from Source.Frontend.Core import MainWindow
from Source.Frontend.gui_after_action_report import logIngestion
from Source.Frontend.gui_directory_configuration import DirectoryConfiguration
from Source.Frontend.gui_event_configuration import EventConfiguration
from Source.Frontend.gui_export import ExportFormat
from Source.Frontend.gui_icon_configuration import IconConfiguration
from Source.Frontend.gui_launcher import Launcher
from Source.Frontend.gui_node_edit import EditNode
from Source.Frontend.gui_relationship_edit import nodeCorrelation
from Source.Frontend.gui_team_configuration import TeamConfiguration
from Source.Frontend.gui_vector_configuration_2 import VectorConfiguration2
from Source.Frontend.gui_vector_edit import addVector

if __name__ == '__main__':
    app = QApplication(sys.argv)

    l = Launcher()
    tc = TeamConfiguration()
    dc = DirectoryConfiguration()
    ec = EventConfiguration()

    ic = IconConfiguration()
    n = EditNode()
    nc = nodeCorrelation()
    ef = ExportFormat()

    vc = VectorConfiguration2()
    av = addVector()
    aar = logIngestion()

    main = MainWindow()
    sys.exit(app.exec_())
