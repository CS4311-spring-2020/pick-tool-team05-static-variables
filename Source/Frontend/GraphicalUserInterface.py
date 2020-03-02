from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import (QMainWindow, QHBoxLayout, QWidget, QDesktopWidget, QSplitter, QSizePolicy, QFrame,
                             QTabWidget, QTableWidget, QAction, QMenu, QApplication)


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
        self.setLayout(self.layout)
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
        splitV.addWidget(GenericFrame())
        splitV.setStretchFactor(1, 1)
        splitV.setSizes([600, 280])

        self.layout.addWidget(splitV)
        self.setCentralWidget(QWidget(self).setLayout(self.layout))

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
    def __init__(self):
        super().__init__()
        self.r = self.frameGeometry()
        self.p = QDesktopWidget().availableGeometry().center()
        self.layout = QHBoxLayout()
        self.initUI()

    def initUI(self):
        # Centers window to provide consistent launch of app
        self.statusBar().showMessage('Ready')
        self.setWindowTitle('PMR Insight Collective Knowledge')
        self.setWindowIcon(QIcon('Source/Backend/Resources/Images/logo_small.png'))
        self.setLayout(self.layout)
        self.resize(600, 600)
        self.r.moveCenter(self.p)
        self.move(self.r.topLeft())


class GenericFrame(QFrame):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)


class VectorFrame(GenericFrame):
    def __init__(self):
        super().__init__()
        self.tabs = QTabWidget()

        # (TODO): Access vectors in event config, hardcoded for now
        self.vectors = ["DDoS", "Vector 2", "Reverse Shell", "+"]

        self.initUI()

    def initUI(self):
        self.setFrameShape(QFrame.StyledPanel)
        self.layout.addWidget(self.tabs)
        for v in self.vectors:
            self.initTab(v)

    def initTab(self, v):
        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(NodeTableFrame())
        splitter.addWidget(GraphFrame())
        splitter.setStretchFactor(1, 1)
        splitter.setSizes([900, 600])
        t = GenericFrame()
        t.layout.addWidget(splitter)
        # (TODO): Refactor when vectors are pulled from event config
        self.tabs.addTab(t, v)


class NodeTableFrame(GenericFrame):
    def __init__(self):
        super().__init__()
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
        super().__init__()