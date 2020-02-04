from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
                             QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
                             QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
                             QVBoxLayout)
import sys

from GUI.gui_approve_changes import Approve_Changes

if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = Approve_Changes()
    sys.exit(test.exec_())



#original
#if __name__ == '__main__':
 #   app = QApplication(sys.argv)
  #  sys.exit(app.exec_())