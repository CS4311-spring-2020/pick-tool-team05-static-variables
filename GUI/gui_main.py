import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QDesktopWidget, QMainWindow, QAction, QApplication, QMenu, QWidget,
                             QSizePolicy, QHBoxLayout, QFrame, QSplitter, QTableWidget,
                             QTableWidgetItem, QVBoxLayout, QAbstractScrollArea, QHeaderView, QToolBar, QPushButton)

from GUI.gui_graph import gui_graph


class gui_main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.hbox = QHBoxLayout()
        self.menuBar = self.menuBar()
        self.toolBar = self.addToolBar('Toolbar')
        self.nodeTable = node_table()
        self.logTable = log_table()
        self.graph = gui_grap

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
        self.resize(1280, 720)
        r = self.frameGeometry()
        p = QDesktopWidget().availableGeometry().center()
        r.moveCenter(p)
        self.move(r.topLeft())

        splitH = QSplitter(Qt.Horizontal)
        splitH.addWidget(self.nodeTable)
        splitH.addWidget(self.graph)
        splitH.setStretchFactor(1, 1)
        splitH.setSizes([500, 600])

        splitV = QSplitter(Qt.Vertical)
        splitV.addWidget(splitH)
        splitV.addWidget(self.logTable)
        splitV.setStretchFactor(1, 1)
        splitV.setSizes([450, 280])

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

        self.toolBar.addSeparator()

        # (TODO): Add triggers
        refresh_act = QAction(QIcon('Resources/Images/button-refresh-arrows.png'), '&Refresh', self)
        refresh_act.setShortcut('Ctrl+R')
        refresh_act.setStatusTip('Refresh project')
        self.toolBar.addAction(refresh_act)

        # (TODO): Add triggers
        commit_act = QAction(QIcon('Resources/Images/check-1.png'), '&Commit', self)
        commit_act.setShortcut('Ctrl+Shift+C')
        commit_act.setStatusTip('Commit changes')
        self.toolBar.addAction(commit_act)

        # (TODO): Add triggers
        push_act = QAction(QIcon('Resources/Images/share-1.png'), '&Push', self)
        push_act.setShortcut('Ctrl+Shift+P')
        push_act.setStatusTip('Push commit')
        self.toolBar.addAction(push_act)

        # Buttons after this are set to the right side
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.toolBar.addWidget(spacer)


class node_table(QFrame):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.table = QTableWidget()
        self.menu = QToolBar()
        self.main()

    def main(self):
        self.setFrameShape(QFrame.StyledPanel)
        self.setLayout(self.layout)
        self.initMenu()
        self.initTable()

    # (TODO): Apply stylesheet to buttons correctly
    # (TODO): Add correct buttons
    # (TODO): Add triggers
    def initMenu(self):
        self.layout.setMenuBar(self.menu)
        self.menu.setMovable(False)
        self.menu.setStyleSheet("""
        QPushButton {
         margin: 6px; 
         padding: 6px; 
         margin-bottom: 0px;
         }
        """)

        btn_add_vector = QPushButton("Add Vector...", self)
        self.menu.addWidget(btn_add_vector)
        btn_edit_vector = QPushButton("Edit Vector...", self)
        self.menu.addWidget(btn_edit_vector)
        btn_delete_vector = QPushButton("Delete Vector...", self)
        self.menu.addWidget(btn_delete_vector)

    # (TODO): Add way of getting column # based on nodes in DB, hard coded for now based on SRS 1.7
    # (TODO): Set columns to node attributes
    def initTable(self):
        self.table.setRowCount(4)
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(['ID', 'Host', 'Source', 'Source Type', 'Content'])
        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.layout.addWidget(self.table)


class log_table(QFrame):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.table = QTableWidget()
        self.menu = QToolBar()
        self.main()

    def main(self):
        self.setFrameShape(QFrame.StyledPanel)
        self.setLayout(self.layout)
        self.initMenu()
        self.initTable()

    # (TODO): Apply stylesheet to buttons correctly
    # (TODO): Add correct buttons
    # (TODO): Add triggers
    def initMenu(self):
        self.layout.setMenuBar(self.menu)
        self.menu.setMovable(False)
        self.menu.setStyleSheet("""
        QPushButton {
         margin: 6px; 
         padding: 6px; 
         margin-bottom: 0px;
         }
        """)

        btn_log_files = QPushButton("Log Files...", self)
        self.menu.addWidget(btn_log_files)
        btn_edit_log = QPushButton("Edit Log...", self)
        self.menu.addWidget(btn_edit_log)

    # (TODO): Add way of getting column # based on log entries in DB, hard coded for now based on SRS 1.7
    def initTable(self):
        self.table.setRowCount(5)
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(['ID', 'Timestamp', 'Host', 'Source', 'Source Type', 'Content'])
        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.layout.addWidget(self.table)