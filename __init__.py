import sys
from PyQt5.QtWidgets import QApplication

# To test stuff, call your GUIs here in your branch. If you merge to master, make sure to leave the file like this.
from GUI.Core import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    sys.exit(app.exec_())
