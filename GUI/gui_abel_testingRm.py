import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

from GUI.gui_approve_changes import Approve_Changes

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Approve_Changes()
    sys.exit(app.exec_())  