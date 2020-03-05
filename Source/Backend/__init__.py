import sys
from PyQt5.QtWidgets import QApplication
from Source.Frontend.GraphicalUserInterface import MainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    g = MainWindow()

    sys.exit(app.exec_())