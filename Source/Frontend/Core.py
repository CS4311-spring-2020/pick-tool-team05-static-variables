from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QDesktopWidget, QMainWindow, QAction, QApplication, QMenu, QWidget,
                             QSizePolicy, QHBoxLayout, QFrame, QSplitter, QVBoxLayout, QTabWidget, QToolBar,
                             QLabel, QCheckBox)

from Source.Frontend.Tables import NodeTable, LogFileTable, LogEntryTable
from Source.Frontend.gui_node_configuration_g import Graph


# (TODO): Reformat vector, graph, node map into attribute of main window, not VectorPages
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.hbox = QHBoxLayout()
        self.menuBar = self.menuBar()
        self.toolBar = self.addToolBar('Toolbar')
        self.pages = TablePages()
        self.vectorPages = VectorPages()
        self.graph = Graph()

        self.main()

    def main(self):
        self.setWindow()

        self.setFileMenu(self.menuBar.addMenu('&File'))
        self.setEditMenu(self.menuBar.addMenu('&Edit'))
        self.setViewMenu(self.menuBar.addMenu('&View'))
        self.setHelpMenu(self.menuBar.addMenu('&Help'))

        self.initToolBar()
        self.show()

    def setWindow(self):
        self.statusBar().showMessage('Ready')
        self.setWindowTitle('PMR Insight Collective Knowledge')
        self.setWindowIcon(QIcon('Resources/Images/icon.png'))

        # Centers window to provide consistent launch of app
        self.resize(1900, 1030)
        r = self.frameGeometry()
        p = QDesktopWidget().availableGeometry().center()
        r.moveCenter(p)
        self.move(r.topLeft())

        # Top side of main window
        splitH = QSplitter(Qt.Horizontal)
        splitH.addWidget(self.vectorPages)
        splitH.addWidget(self.graph)
        splitH.setStretchFactor(1, 1)
        splitH.setSizes([900, 600])

        # Bottom side of main window
        splitV = QSplitter(Qt.Vertical)
        splitV.addWidget(splitH)
        splitV.addWidget(self.pages)
        splitV.setStretchFactor(1, 1)
        splitV.setSizes([600, 280])

        self.hbox.addWidget(splitV)
        self.setCentralWidget(QWidget(self))
        self.centralWidget().setLayout(self.hbox)

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
        orientation_h.triggered.connect(self.graph.toggleGraphView)

        # (TODO): Add triggers
        orientation_v = QAction('&Vertical', self)
        orientation_v.setStatusTip('Position graph vertically')
        orientation_v.setCheckable(True)
        orientation_v.triggered.connect(self.graph.toggleGraphView)

        # (TODO): Add triggers
        seconds_i = QAction('&Seconds', self)
        seconds_i.setStatusTip('Set timeline interval to seconds')
        seconds_i.setCheckable(True)
        seconds_i.triggered.connect(self.graph.zoom)

        # (TODO): Add triggers
        minutes_i = QAction('&Minutes', self)
        minutes_i.setStatusTip('Set timeline interval to minutes')
        minutes_i.setCheckable(True)
        minutes_i.triggered.connect(self.graph.zoom)

        # (TODO): Add triggers
        hours_i = QAction('&Hours', self)
        hours_i.setStatusTip('Set timeline interval to hours')
        hours_i.setCheckable(True)
        hours_i.triggered.connect(self.graph.zoom)

        # (TODO): Add triggers
        days_i = QAction('&Days', self)
        days_i.setStatusTip('Set timeline interval to hours')
        days_i.setCheckable(True)
        days_i.triggered.connect(self.graph.zoom)

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


class TablePages(QFrame):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.tabs = QTabWidget()
        self.log_files = LogFileTable()
        self.log_entries = LogEntryTable()
        self.main()

    def main(self):
        self.setLayout(self.layout)
        self.setFrameShape(QFrame.StyledPanel)
        self.layout.addWidget(self.tabs)

        self.tabs.setTabPosition(QTabWidget.South)
        self.tabs.addTab(self.log_files, "Log Files")
        self.tabs.addTab(self.log_entries, "Log Entries")


class VectorPages(QFrame):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.nodeVisibility = QToolBar('Toolbar')
        self.tabs = QTabWidget()

        # (TODO): Access vector global var, paginate OPEN vectors. Hardcoded for now.
        self.vectors = ["DDoS", "Vector 2", "Reverse Shell", "+"]
        # (TODO): Keep list of nodes = node tables
        self.nodeTables = [NodeTable(), NodeTable(), NodeTable(), NodeTable()]
        # (TODO): Keep list of graphs = graph tables
        self.graphs = ["", "", "", ""]
        # Map Vector -> Graph -> Node list
        self.tabList = zip(self.vectors, self.nodeTables, self.graphs)

        self.main()

    def main(self):
        self.setLayout(self.layout)
        self.setFrameShape(QFrame.StyledPanel)
        self.nodePropertyVisibilityToggles()
        self.layout.addWidget(self.tabs)

        for tab in self.tabList:
            self.tabs.addTab(tab[1], tab[0])

    # (TODO): Add correct buttons
    # (TODO): Add triggers
    def nodePropertyVisibilityToggles(self):
        frame = QFrame()
        frame.setFrameShape(QFrame.StyledPanel)
        layout_frame = QVBoxLayout()
        frame.setLayout(layout_frame)

        header = QLabel("Selected NodeProperty Visibility")
        header.setAlignment(Qt.AlignCenter)
        layout_frame.addWidget(header)
        layout_frame.addWidget(QLabel(""))

        buttons_bar = QToolBar("Buttons")
        buttons_bar.setStyleSheet("""
        QToolBar {
            spacing: 40px;
        }
        """)

        buttons_bar.addWidget(QCheckBox("Node\nID"))
        buttons_bar.addWidget(QCheckBox("Node\nName"))
        buttons_bar.addWidget(QCheckBox("Node\nTimestamp"))
        buttons_bar.addWidget(QCheckBox("Node\nDescription"))
        buttons_bar.addWidget(QCheckBox("Log Entry\nReference"))
        buttons_bar.addWidget(QCheckBox("Log\nCreator"))
        buttons_bar.addWidget(QCheckBox("Event\nType"))
        buttons_bar.addWidget(QCheckBox("Icon\nType"))
        buttons_bar.addWidget(QCheckBox("Source"))
        layout_frame.addWidget(buttons_bar)

        self.layout.addWidget(frame)
