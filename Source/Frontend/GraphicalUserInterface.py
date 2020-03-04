from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize, QRect
from PyQt5.QtWidgets import (QMainWindow, QHBoxLayout, QVBoxLayout, QDesktopWidget, QSplitter, QSizePolicy, QFrame,
                             QTabWidget, QTableWidget, QAction, QMenu, QApplication, QPushButton, QLineEdit, QWidget,
                             QLabel, QTextEdit, QGridLayout)


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

        self.setFileMenu(self.menuBar.addMenu('&File'))
        self.setEditMenu(self.menuBar.addMenu('&Edit'))
        self.setViewMenu(self.menuBar.addMenu('&View'))
        self.setHelpMenu(self.menuBar.addMenu('&Help'))
        self.initToolBar()

        splitV = QSplitter(Qt.Vertical)
        splitV.addWidget(self.vectors)
        splitV.addWidget(GenericFrame(QHBoxLayout))
        splitV.setStretchFactor(1, 1)
        splitV.setSizes([600, 280])

        self.layout.addWidget(splitV)
        self.setCentralWidget(QWidget(self))
        self.centralWidget().setLayout(self.layout)

        self.show()

    def setFileMenu(self, file_menu):
        # (TODO): Add triggers
        connect_act = QAction('&Connect...', self)
        connect_act.setShortcut('Ctrl+Shift+C')
        connect_act.setStatusTip('Connect to host')
        file_menu.addAction(connect_act)

        # (TODO): Add triggers
        disconnect_act = QAction('&Disconnect...', self)
        disconnect_act.setShortcut('Ctrl+Shift+D')
        disconnect_act.setStatusTip('Disconnect from host')
        file_menu.addAction(disconnect_act)

        file_menu.addSeparator()

        # (TODO): Add triggers
        files_act = QAction('&View Log Files...', self)
        files_act.setShortcut('Ctrl+Shift+V')
        files_act.setStatusTip('View log files')
        file_menu.addAction(files_act)

        file_menu.addSeparator()

        exit_act = QAction('&Exit', self)
        exit_act.setShortcut('Ctrl+Q')
        exit_act.setStatusTip('Exit application')
        exit_act.triggered.connect(QApplication.quit)
        file_menu.addAction(exit_act)

    def setEditMenu(self, edit_menu):
        # (TODO): Add triggers
        add_act = QAction('&Add Vector...', self)
        add_act.setShortcut('Ctrl+Shift+N')
        add_act.setStatusTip('Add vector')
        edit_menu.addAction(add_act)

        # (TODO): Add triggers
        del_act = QAction('&Delete Vector', self)
        del_act.setShortcut('Ctrl+Shift+D')
        del_act.setStatusTip('Delete vector')
        edit_menu.addAction(del_act)

        edit_menu.addSeparator()

        # (TODO): Add triggers
        export_act = QAction('&Export Graph...', self)
        export_act.setShortcut('Ctrl+Shift+E')
        export_act.setStatusTip('Export graph')
        edit_menu.addAction(export_act)

    def setViewMenu(self, view_menu):
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

    def setHelpMenu(self, help_menu):
        # (TODO): Add triggers
        help_act = QAction('&Help', self)
        help_act.setShortcut('f1')
        help_act.setStatusTip('Show Tips')
        help_menu.addAction(help_act)

        help_menu.addSeparator()

        # (TODO): Add triggers
        about_act = QAction('&About', self)
        about_act.setStatusTip('About PMR Insight Collective Knowledge Tool')
        help_menu.addAction(about_act)

    # (TODO): Add more buttons according to future developments
    def initToolBar(self):
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

        # (TODO): Access vectors from database, hardcoded for now
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

    def insertTab(self, t):
        if t == self.tabs.count() - 1:
            # (TODO): Call vector window to add vector to event config
            self.__initTab(self.vectors[-1], t)
            self.tabs.setCurrentIndex(t)

    # (TODO): Connect to delete vector & context menu
    def deleteTab(self, t):
        self.tabs.removeTab(t)

    def __initTab(self, v, c):
        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(NodeTableFrame())
        splitter.addWidget(GraphFrame())
        splitter.setStretchFactor(1, 1)
        splitter.setSizes([900, 600])
        t = GenericFrame(QHBoxLayout)
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


class VectorDatabase(GenericWindow):
    def __init__(self):
        super().__init__(QHBoxLayout())
        self.resize(900, 600)
        self.nl = QLabel('Name: ')
        self.dl = QLabel('Description: ')
        self.de = QTextEdit()
        self.ne = QLineEdit()

        self.initUI()
        self.show()

    def initUI(self):
        splitter = QSplitter(Qt.Horizontal)
        t = GenericFrame(QGridLayout())
        t.layout.addWidget(self.nl, 1, 0)
        t.layout.addWidget(self.ne, 1, 1)
        t.layout.addWidget(self.dl, 2, 0)
        t.layout.addWidget(self.de, 2, 1, 3, 1)

        # frame = GenericFrame()
        # form = QGridLayout()
        # form.setSpacing(10)
        #
        # form.addWidget(self.nl, 1, 0)
        # form.addWidget(self.ne, 1, 1)
        #
        # form.addWidget(self.dl, 2, 0)
        # form.addWidget(self.de, 2, 1, 3, 1)
        #
        # frame.layout = form
        # frame.setLayout(frame.layout)
        # frame.setGeometry(300, 300, 350, 300)
        #
        # # (TODO): Change to actual vector list
        splitter.addWidget(NodeTableFrame())
        splitter.addWidget(t)
        splitter.setStretchFactor(1, 1)
        splitter.setSizes([400, 200])
        self.layout.addWidget(splitter)
