from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import (QMainWindow, QHBoxLayout, QVBoxLayout, QDesktopWidget, QSplitter, QSizePolicy, QFrame,
                             QTabWidget, QTableWidget, QAction, QMenu, QApplication, QPushButton, QLineEdit, QWidget,
                             QLabel, QTextEdit, QGridLayout, QToolBar, QListWidget)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.r = self.frameGeometry()
        self.p = QDesktopWidget().availableGeometry().center()
        self.layout = QHBoxLayout()
        self.menuBar = self.menuBar()
        self.toolBar = self.addToolBar('Toolbar')
        self.vectors = VectorFrame()
        # self.general = TablesFrame()

        self.initUI()

    def initUI(self):
        # Centers window to provide consistent launch of app
        self.statusBar().showMessage('Ready')
        self.setWindowTitle('PMR Insight Collective Knowledge')
        self.setWindowIcon(QIcon('Source/Backend/Resources/Images/logo_small.png'))
        self.resize(1900, 1030)
        self.r.moveCenter(self.p)
        self.move(self.r.topLeft())

        self.__setFileMenu(self.menuBar.addMenu('&File'))
        self.__setEditMenu(self.menuBar.addMenu('&Edit'))
        self.__setViewMenu(self.menuBar.addMenu('&View'))
        self.__initToolBar()

        splitV = QSplitter(Qt.Vertical)
        splitV.addWidget(self.vectors)
        splitV.addWidget(NodeTableFrame())
        splitV.setStretchFactor(1, 1)
        splitV.setSizes([300, 280])

        self.layout.addWidget(splitV)
        self.setCentralWidget(QWidget(self))
        self.centralWidget().setLayout(self.layout)

        self.show()

    def __setFileMenu(self, file_menu):
        # (TODO): Add triggers
        connect_act = QAction('&Connect...', self)
        connect_act.setStatusTip('Connect to host')
        file_menu.addAction(connect_act)

        # (TODO): Add triggers
        disconnect_act = QAction('&Disconnect...', self)
        disconnect_act.setStatusTip('Disconnect from host')
        file_menu.addAction(disconnect_act)

        file_menu.addSeparator()

        # (TODO): Add triggers
        files_act = QAction('&Project', self)
        files_act.setStatusTip('View log files')
        file_menu.addAction(files_act)

        dirs = QAction('&Directories', self)
        dirs.setStatusTip('View Project Directories')
        dirs.triggered.connect(self.__openDIRS)
        file_menu.addAction(dirs)

        file_menu.addSeparator()

        exit_act = QAction('&Exit', self)
        exit_act.setShortcut('Ctrl+Q')
        exit_act.setStatusTip('Exit application')
        exit_act.triggered.connect(QApplication.quit)
        file_menu.addAction(exit_act)

    def __setEditMenu(self, edit_menu):
        vdb = QAction('&Vectors...', self)
        vdb.setStatusTip('Open Vector Database')
        vdb.triggered.connect(self.__openVDB)
        edit_menu.addAction(vdb)

        # (TODO): Add triggers
        lfdb = QAction('Log files...', self)
        lfdb.setStatusTip('Open Log File Database')
        lfdb.triggered.connect(self.__openLFDB)
        edit_menu.addAction(lfdb)

        edit_menu.addSeparator()

        # (TODO): Add triggers
        export_act = QAction('&Export Graph...', self)
        export_act.setStatusTip('Export graph')
        edit_menu.addAction(export_act)

    def __setViewMenu(self, view_menu):
        graph_orientation = QMenu('&Graph Orientation', self)
        timeline = QMenu('Timeline Interval', self)

        # (TODO): Add triggers
        orientation_h = QAction('&Horizontal', self)
        orientation_h.setStatusTip('Position graph horizontally')
        orientation_h.setCheckable(True)

        # (TODO): Add triggers
        orientation_v = QAction('&Vertical', self)
        orientation_v.setStatusTip('Position graph vertically')
        orientation_v.setCheckable(True)

        # (TODO): Add triggers
        seconds_i = QAction('&Seconds', self)
        seconds_i.setStatusTip('Set timeline interval to seconds')
        seconds_i.setCheckable(True)

        # (TODO): Add triggers
        minutes_i = QAction('&Minutes', self)
        minutes_i.setStatusTip('Set timeline interval to minutes')
        minutes_i.setCheckable(True)

        # (TODO): Add triggers
        hours_i = QAction('&Hours', self)
        hours_i.setStatusTip('Set timeline interval to hours')
        hours_i.setCheckable(True)

        # (TODO): Add triggers
        days_i = QAction('&Days', self)
        days_i.setStatusTip('Set timeline interval to hours')
        days_i.setCheckable(True)

        graph_orientation.addAction(orientation_h)
        graph_orientation.addAction(orientation_v)
        timeline.addAction(seconds_i)
        timeline.addAction(minutes_i)
        timeline.addAction(hours_i)
        timeline.addAction(days_i)
        view_menu.addMenu(graph_orientation)
        view_menu.addMenu(timeline)

    # (TODO): Add more buttons according to future developments
    def __initToolBar(self):
        self.toolBar.setMovable(False)
        self.toolBar.setIconSize(QSize(20, 20))
        self.toolBar.setStyleSheet("""
            QToolBar {
                spacing: 6px;
                padding: 3px;
            }
        """)

        # (TODO): Add triggers
        undo_act = QAction(QIcon('Resources/Images/undo.png'), '&Undo', self)
        undo_act.setShortcut('Ctrl+Z')
        undo_act.setStatusTip('Undo action')
        self.toolBar.addAction(undo_act)

        # (TODO): Add triggers
        redo_act = QAction(QIcon('Resources/Images/redo.png'), '&Redo', self)
        redo_act.setShortcut('Ctrl+Shift+Z')
        redo_act.setStatusTip('Redo action')
        self.toolBar.addAction(redo_act)

        # (TODO): Add triggers
        refresh_act = QAction(QIcon('Resources/Images/refresh.png'), '&Sync', self)
        refresh_act.setShortcut('Ctrl+Shift+S')
        refresh_act.setStatusTip('Refresh project')
        self.toolBar.addAction(refresh_act)

        self.toolBar.addSeparator()

        # (TODO): Add triggers
        commit_act = QAction(QIcon('Resources/Images/commit.png'), '&Commit Changes', self)
        commit_act.setShortcut('Ctrl+Shift+C')
        commit_act.setStatusTip('Refresh project')
        self.toolBar.addAction(commit_act)

        # (TODO): Add triggers
        changes = QAction(QIcon('Resources/Images/changes.png'), '&Changelist', self)
        changes.setShortcut('Ctrl+Shift+L')
        changes.setStatusTip('See changelist')
        self.toolBar.addAction(changes)

        # Buttons after this are set to the right side
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.toolBar.addWidget(spacer)

        # (TODO): Add triggers
        push_act = QAction(QIcon('Resources/Images/export.png'), '&Export Graph', self)
        push_act.setShortcut('Ctrl+Shift+X')
        push_act.setStatusTip('Export Graph')
        self.toolBar.addAction(push_act)

    def __openVDB(self):
        self.vdb = VectorDatabase()

    def __openLFDB(self):
        self.lfdb = LogFileDatabase()

    def __openDIRS(self):
        self.dirs = DirectoryFrame()


class GenericWindow(QWidget):
    def __init__(self, layout):
        super().__init__()
        self.r = self.frameGeometry()
        self.p = QDesktopWidget().availableGeometry().center()
        self.r.moveCenter(self.p)
        self.move(self.r.topLeft())

        self.layout = layout
        self.setLayout(self.layout)

        self.setWindowTitle('PMR Insight Collective Knowledge')
        self.setWindowIcon(QIcon('Source/Backend/Resources/Images/logo_small.png'))


class GenericFrame(QFrame):
    def __init__(self, layout):
        super().__init__()
        self.layout = layout
        self.setLayout(self.layout)


class VectorFrame(GenericFrame):
    def __init__(self):
        super().__init__(QHBoxLayout())
        self.tabs = QTabWidget()
        self.__selected = -1

        # (TODO): Access vectors from vector table, hardcoded for now
        self.vectors = ["DDoS", "Vector 2", "Reverse Shell"]

        self.__initUI()

    def __initUI(self):
        self.setFrameShape(QFrame.StyledPanel)
        self.layout.addWidget(self.tabs)

        for v in self.vectors:
            self.__initTab(v, 0)

        self.tabs.addTab(QWidget(), '+')
        self.tabs.tabBarClicked.connect(self.__setSelected)
        self.tabs.currentChanged.connect(self.insertTab)

    def __initTab(self, v, c):
        splitter = QSplitter(Qt.Horizontal)

        splitter.addWidget(NodeTableFrame())
        splitter.addWidget(GraphFrame())

        splitter.setStretchFactor(1, 1)
        splitter.setSizes([900, 600])
        t = GenericFrame(QHBoxLayout())
        t.layout.addWidget(splitter)

        # (TODO): Refactor when vectors are pulled from event config
        if c == 0:
            self.tabs.addTab(t, v)
        else:
            self.tabs.insertTab(c, t, self.vectors[-1])

    def __setSelected(self, s):
        if s == self.tabs.count() - 1:
            self.__selected = -1
        else:
            self.__selected = s

    def insertTab(self, t):
        if t == self.tabs.count() - 1:
            # (TODO): Call to create new vector in DB

            self.__initTab(self.vectors[-1], t)
            self.tabs.setCurrentIndex(t)

    # (TODO): Connect to delete vector & context menu
    def deleteTab(self, t):
        self.tabs.removeTab(t)


class NodeTableFrame(GenericFrame):
    def __init__(self):
        super().__init__(QHBoxLayout())
        self.table = QTableWidget()
        self.initTable()

    # (TODO): Add way of getting column # based on nodes in DB, hard coded for now based on SRS 1.7
    # (TODO): Set columns to node attributes
    def initTable(self):
        self.table.setRowCount(4)
        self.table.setColumnCount(10)
        self.table.setHorizontalHeaderLabels(['Node\nVisibility', 'Node ID', 'Node\nName', 'Node\nTimestamp',
                                              'Log Entry\nReference', 'Log\nCreator', 'Event\nType', 'Icon\nType',
                                              'Source', 'Node\nDescription'])
        self.table.setColumnWidth(0, 60)
        self.table.setColumnWidth(1, 70)
        self.table.setColumnWidth(4, 70)
        self.table.setColumnWidth(5, 60)
        self.table.setColumnWidth(6, 60)
        self.table.setColumnWidth(7, 60)
        self.table.setColumnWidth(8, 60)
        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.layout.addWidget(self.table)


class GraphFrame(GenericFrame):
    def __init__(self):
        super().__init__(QHBoxLayout())
        self.initImage()

    def initImage(self):
        picture = QLabel()
        pixmap = QPixmap('../Backend/Resources/Images/story.png')
        picture.setPixmap(pixmap)
        self.layout.addWidget(picture)


class VectorDatabase(GenericWindow):
    def __init__(self):
        super().__init__(QVBoxLayout())
        self.__tabs = QTabWidget()
        self.__buttons = QToolBar('Toolbar')

        # (TODO): Access vectors from vector table, hardcoded for now
        self.__vectors = ["DDoS", "Vector 2", "Reverse Shell"]

        self.__initUI()
        self.show()

    def __initUI(self):
        self.resize(600, 400)
        self.__initToolBar()

        for v in self.__vectors:
            self.__initTab(v)

        self.layout.addWidget(self.__tabs)
        self.layout.addWidget(self.__buttons)

    def __initToolBar(self):
        self.__buttons.setMovable(False)
        self.__buttons.setStyleSheet("""
                    QToolBar {
                        spacing: 6px;
                        padding: 3px;
                    }
                """)

        # (TODO): Add triggers
        b1 = QPushButton('Add Vector')
        self.__buttons.addWidget(b1)

        # (TODO): Add triggers
        b2 = QPushButton('Delete Vector')
        self.__buttons.addWidget(b2)

        # Buttons after this are set to the right side
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.__buttons.addWidget(spacer)

        # (TODO): Add triggers
        b3 = QPushButton('OK')
        self.__buttons.addWidget(b3)

        # (TODO): Add triggers
        b4 = QPushButton('Cancel')
        self.__buttons.addWidget(b4)

    def __initTab(self, v):
        frame = GenericFrame(QGridLayout())
        frame.layout.addWidget(QLabel('Name:'), 1, 0)
        frame.layout.addWidget(QLineEdit(v), 1, 1)
        frame.layout.addWidget(QLabel('Description:'), 2, 0)
        frame.layout.addWidget(QTextEdit(), 2, 1, 2, 1)
        frame.layout.addWidget(QLabel('Associated Log Entries:'), 4, 0)
        frame.layout.addWidget(QLabel('10'), 4, 1)
        self.__tabs.addTab(frame, v)

    # (TODO): Connect to delete vector, delete vector from DB
    def deleteTab(self, t):
        self.tabs.removeTab(t)

    def insertTab(self, t):
        # (TODO): Call to create new vector in DB

        self.__initTab(self.vectors[-1], t)
        self.tabs.setCurrentIndex(t)


class ReportFrame(GenericFrame):
    def __init__(self):
        super().__init__(QHBoxLayout())
        self.__currentLog = None
        self.__initUI()

    def __initUI(self):
        self.setFrameShape(QFrame.StyledPanel)
        self.layout.addWidget(QLabel())

    def updateReport(self, item):
        for i in range(self.layout.count()):
            self.layout.itemAt(i).widget().setParent(None)

        # (TODO): Get log file after action report using log file name, hardcoded for now
        self.__currentLog = item.text()
        self.layout.addWidget(QLabel(self.__currentLog))


class LogFileDatabase(GenericWindow):
    def __init__(self):
        super().__init__(QVBoxLayout())
        self.__list = QListWidget()
        self.__report = ReportFrame()
        self.__buttons = QToolBar('Toolbar')

        # (TODO): Access log files, hardcoded for now
        self.__logs = ["Readme.txt", "20193019_101559.jpg", "20190220_161043.log"]

        self.__initUI()

    def __initUI(self):
        self.resize(600, 400)
        self.__initToolBar()
        for log in self.__logs:
            self.__list.addItem(log)

        self.__list.itemClicked.connect(self.__report.updateReport)

        splitter = QSplitter(Qt.Horizontal)

        splitter.addWidget(self.__list)
        splitter.addWidget(self.__report)

        splitter.setStretchFactor(1, 1)
        splitter.setSizes([200, 200])

        self.layout.addWidget(splitter)
        self.layout.addWidget(self.__buttons)
        self.show()

    def __initToolBar(self):
        self.__buttons.setMovable(False)
        self.__buttons.setStyleSheet("""
                    QToolBar {
                        spacing: 6px;
                        padding: 3px;
                    }
                """)

        # (TODO): Add triggers
        b1 = QPushButton('Accept File...')
        self.__buttons.addWidget(b1)

        # Buttons after this are set to the right side
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.__buttons.addWidget(spacer)

        # (TODO): Add triggers
        b2 = QPushButton('OK')
        b2.clicked.connect(QApplication.instance().quit)
        self.__buttons.addWidget(b2)

        # (TODO): Add triggers
        b3 = QPushButton('Cancel')
        self.__buttons.addWidget(b3)


class DirectoryFrame(GenericWindow):
    def __init__(self):
        super().__init__(QVBoxLayout())
        # (TODO) Antoine: Connect with the directories from event configuration
        self.__directories = ['C:/Events/20190304', 'C:/Events/20190304/Blue', 'C:/Events/20190304/Red',
                              'C:/Events/20190304/White']
        self.__initUI()

    def __initUI(self):
        self.resize(600, 400)
        frame = GenericFrame(QGridLayout())
        frame.layout.addWidget(QLabel('Root Directory:'), 1, 0)
        frame.layout.addWidget(QLineEdit(self.__directories[0]), 1, 1)
        frame.layout.addWidget(QLabel('Blue Directory:'), 2, 0)
        frame.layout.addWidget(QLineEdit(self.__directories[1]), 2, 1)
        frame.layout.addWidget(QLabel('Red Directory:'), 3, 0)
        frame.layout.addWidget(QLineEdit(self.__directories[2]), 3, 1)
        frame.layout.addWidget(QLabel('White Directory:'), 4, 0)
        frame.layout.addWidget(QLineEdit(self.__directories[3]), 4, 1)
        self.layout.addWidget(frame)
        self.show()

