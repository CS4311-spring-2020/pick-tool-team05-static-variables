import sys
from PyQt5.QtWidgets import QApplication

#To test stuff, call your GUIs here in your branch. If you merge to master, make sure to leave the file like this.
from GUI.gui_connect_initial import ConnectHost
from GUI.gui_export_image import ExportGraphImage
from GUI.gui_eventconfig_error import EventConfigError
from GUI.gui_local_warning import LocalCopyWarning

if __name__ == '__main__':
    app = QApplication(sys.argv)

    connect_host = ConnectHost()
    connect_host.show()

    local_copy_warning = LocalCopyWarning()
    local_copy_warning.show()

    event_config_window = EventConfigError()
    event_config_window.show()

    export_image = ExportGraphImage()
    export_image.show()

    sys.exit(app.exec_())
