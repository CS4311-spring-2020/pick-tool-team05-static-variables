import sys

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QDesktopWidget, QMainWindow, QAction, QApplication, QMenu, QWidget, QSizePolicy
from PyQt5.QtGui import QIcon


class gui_main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initRoot()

    def initRoot(self):
        self.statusBar().showMessage('Ready')
        self.setWindowTitle('PMR Insight Collective Knowledge')
        self.setWindowIcon(QIcon('Resources/Images/icon.png'))

        self.initSize()
        self.initMenuBar()
        self.initToolBar()
        self.show()

    def initSize(self):
        self.resize(1280, 720)
        r = self.frameGeometry()
        p = QDesktopWidget().availableGeometry().center()
        r.moveCenter(p)
        self.move(r.topLeft())

    def initMenuBar(self):
        menubar = self.menuBar()
        self.setFileMenu(menubar.addMenu('&File'))
        self.setEditMenu(menubar.addMenu('&Edit'))
        self.setViewMenu(menubar.addMenu('&View'))
        self.setHelpMenu(menubar.addMenu('&Help'))

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
        graph_orientation = QMenu('Graph Orientation', self)
        timeline = QMenu('Timeline Interval', self)

        # (TODO): Triggers in toggleGraphView
        orientation_h = QAction('&Horizontal', self)
        orientation_h.setStatusTip('Position graph horizontally')
        orientation_h.setCheckable(True)
        orientation_h.triggered.connect(self.toggleGraphView)

        # (TODO): Triggers in toggleGraphView
        orientation_v = QAction('&Vertical', self)
        orientation_v.setStatusTip('Position graph vertically')
        orientation_v.setCheckable(True)
        orientation_v.triggered.connect(self.toggleGraphView)

        # (TODO): Triggers in zoom
        seconds_i = QAction('&Seconds', self)
        seconds_i.setStatusTip('Set timeline interval to seconds')
        seconds_i.setCheckable(True)
        seconds_i.triggered.connect(self.zoom)

        # (TODO): Triggers in zoom
        minutes_i = QAction('&Minutes', self)
        minutes_i.setStatusTip('Set timeline interval to minutes')
        minutes_i.setCheckable(True)
        minutes_i.triggered.connect(self.zoom)

        # (TODO): Triggers in zoom
        hours_i = QAction('&Hours', self)
        hours_i.setStatusTip('Set timeline interval to hours')
        hours_i.setCheckable(True)
        hours_i.triggered.connect(self.zoom)

        # (TODO): Triggers in zoom
        days_i = QAction('&Days', self)
        days_i.setStatusTip('Set timeline interval to hours')
        days_i.setCheckable(True)
        days_i.triggered.connect(self.zoom)

        graph_orientation.addAction(orientation_h)
        graph_orientation.addAction(orientation_v)
        timeline.addAction(seconds_i)
        timeline.addAction(minutes_i)
        timeline.addAction(hours_i)
        timeline.addAction(days_i)
        view_menu.addMenu(graph_orientation)
        view_menu.addMenu(timeline)

    def setHelpMenu(self, help_menu):
        # About button, missing trigger
        help_act = QAction('&Help', self)
        help_act.setShortcut('f1')
        help_act.setStatusTip('Show Tips')
        help_menu.addAction(help_act)

        help_menu.addSeparator()

        about_act = QAction('&About', self)
        about_act.setStatusTip('About PMR Insight Collective Knowledge Tool')
        help_menu.addAction(about_act)

    # (TODO): Add more buttons according to future developments
    # (TODO): Complete adding basic icons
    def initToolBar(self):
        toolbar = self.addToolBar('Toolbar')
        toolbar.setMovable(False)
        toolbar.setIconSize(QSize(20, 20))

        undo_act = QAction(QIcon('Resources/Images/undo.png'), '&Undo', self)
        undo_act.setShortcut('Ctrl+Z')
        undo_act.setStatusTip('Undo action')
        toolbar.addAction(undo_act)

        redo_act = QAction(QIcon('Resources/Images/redo.png'), '&Redo', self)
        redo_act.setShortcut('Ctrl+Shift+Z')
        redo_act.setStatusTip('Redo action')
        toolbar.addAction(redo_act)

        toolbar.addSeparator()

        refresh_act = QAction(QIcon('Resources/Images/button-refresh-arrows.png'), '&Refresh', self)
        refresh_act.setShortcut('Ctrl+R')
        refresh_act.setStatusTip('Refresh project')
        toolbar.addAction(refresh_act)

        commit_act = QAction(QIcon('Resources/Images/check-1.png'), '&Commit', self)
        commit_act.setShortcut('Ctrl+Shift+C')
        commit_act.setStatusTip('Commit changes')
        toolbar.addAction(commit_act)

        push_act = QAction(QIcon('Resources/Images/share-1.png'), '&Push', self)
        push_act.setShortcut('Ctrl+Shift+P')
        push_act.setStatusTip('Push commit')
        toolbar.addAction(push_act)

        # Buttons after this are set to the right side
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        toolbar.addWidget(spacer)

    #(TODO): Complete
    def toggleGraphView(self):
        print('hi')

    #(TODO): Complete
    def zoom(self):
        print('hello')
