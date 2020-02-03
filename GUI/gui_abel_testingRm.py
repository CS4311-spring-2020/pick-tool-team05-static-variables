import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
                             QMenu, QPushButton, QRadioButton, QVBoxLayout, QWidget)

from GUI.gui_approve_changes import Approve_Changes

if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = Approve_Changes()
    clock.show()
    sys.exit(app.exec_())

