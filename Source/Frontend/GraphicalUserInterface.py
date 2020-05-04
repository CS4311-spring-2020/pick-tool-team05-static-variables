import psutil
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, QSize, pyqtSignal
from PyQt5.QtWidgets import (QMainWindow, QHBoxLayout, QVBoxLayout, QDesktopWidget, QSplitter, QSizePolicy, QFrame,
                             QTabWidget, QTableWidget, QAction, QMenu, QApplication, QPushButton, QLineEdit, QWidget,
                             QLabel, QTextEdit, QGridLayout, QToolBar, QListWidget, QTableWidgetItem)


from Source.Backend.Vector.VectorFacade import VectorFacade

DEBUG = True

from Source.Backend.Data.EventConfiguration import EventConfiguration
from Source.Backend.Data.DBFacade import get_vector_list
from Source.Backend.Data.Vector import Vector


class MainWindow(QMainWindow):

    # TODO: Maybe refactor somewhere else?
    def closeEvent(self, event):
        for proc in psutil.process_iter():
            if proc.name() == "mongod.exe":
                proc.kill()

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
        project = QAction('&Event Information', self)
        project.setStatusTip('Event Information')
        file_menu.addAction(project)
        project.triggered.connect(self.__createMainMenu)

        file_menu.addSeparator()

        exit_act = QAction('&Exit', self)
        exit_act.setShortcut('Ctrl+Q')
        exit_act.setStatusTip('Exit application')
        exit_act.triggered.connect(QApplication.quit)
        file_menu.addAction(exit_act)

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

        # (TODO): Add triggers, reimplement
        # undo_act = QAction(QIcon('Resources/Images/undo.png'), '&Undo', self)
        # undo_act.setShortcut('Ctrl+Z')
        # undo_act.setStatusTip('Undo action')
        # self.toolBar.addAction(undo_act)

        # # (TODO): Add triggers, reimplement
        # redo_act = QAction(QIcon('Resources/Images/redo.png'), '&Redo', self)
        # redo_act.setShortcut('Ctrl+Shift+Z')
        # redo_act.setStatusTip('Redo action')
        # self.toolBar.addAction(redo_act)

        # (TODO): Add triggers, reimplement
        # refresh_act = QAction(QIcon('Resources/Images/refresh.png'), '&Sync', self)
        # refresh_act.setShortcut('Ctrl+Shift+S')
        # refresh_act.setStatusTip('Refresh project')
        # self.toolBar.addAction(refresh_act)

        # (TODO): Add triggers, reimplement
        # commit_act = QAction(QIcon('Resources/Images/commit.png'), '&Commit Changes', self)
        # commit_act.setShortcut('Ctrl+Shift+C')
        # commit_act.setStatusTip('Refresh project')
        # self.toolBar.addAction(commit_act)

        # (TODO): Add triggers, reimplement
        # changes = QAction(QIcon('Resources/Images/changes.png'), '&Changelist', self)
        # changes.setShortcut('Ctrl+Shift+L')
        # changes.setStatusTip('See changelist')
        # self.toolBar.addAction(changes)

        # Buttons after this are set to the right side
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.toolBar.addWidget(spacer)

        # (TODO): Add triggers
        push_act = QAction(QIcon('Resources/Images/export.png'), '&Export Graph', self)
        push_act.setShortcut('Ctrl+Shift+X')
        push_act.setStatusTip('Export Graph')
        self.toolBar.addAction(push_act)

    def __createMainMenu(self):
        self.mainMenu = MainMenu()

########################################################################################################################


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
    def __init__(self, layout, name):
        super().__init__()
        self.layout = layout
        self.frameName = name
        self.setLayout(self.layout)

########################################################################################################################


class MainMenu(GenericWindow):
    def __init__(self):
        super().__init__(QVBoxLayout())
        self.__tabs = QTabWidget()
        self.__buttons = QToolBar("Buttons")
        self.__frames = []

        self.__initUI()

    def __initUI(self):
        self.resize(900, 600)
        self.__initTabs()
        self.__initButtons()

        self.layout.addWidget(self.__tabs)
        self.layout.addWidget(self.__buttons)

        self.show()

    def __initTabs(self):
        self.__frames.append(EventConfigurationFrame())
        self.__frames.append(VectorDatabaseFrame())
        self.__frames.append(LogFileFrame())

        for frame in self.__frames:
            self.__tabs.addTab(frame, frame.frameName)

    def __initButtons(self):
        self.__buttons.setMovable(False)
        self.__buttons.setStyleSheet("""
                    QToolBar {
                        spacing: 6px;
                        padding: 3px;
                    }
                """)

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.__buttons.addWidget(spacer)

        b1 = QPushButton('OK')
        self.__buttons.addWidget(b1)
        b1.clicked.connect(self.__save_input)

        b2 = QPushButton('Cancel')
        self.__buttons.addWidget(b2)
        b2.clicked.connect(self.close)

    def __save_input(self):
        for f in self.__frames:
            f.save_forms()
        self.close()


class EventConfigurationFrame(GenericFrame):
    def __init__(self):
        super().__init__(QGridLayout(), 'Event Configuration')
        self.event_configuration = EventConfiguration()
        self.name_form = QLineEdit()
        self.description_form = QTextEdit()
        self.start_form = QLineEdit()
        self.end_form = QLineEdit()
        self.root_form = QLineEdit()
        self.red_form = QLineEdit()
        self.white_form = QLineEdit()
        self.blue_form = QLineEdit()
        self.lead_label = QLabel()
        self.ip_label = QLabel()
        self.connections_label = QLabel()
        self.__initUI()

        self.event_configuration.eventConfigurationSignal.connect(self.__loadInfo)

    def __loadInfo(self):
        self.name_form.setText(self.event_configuration.data.get("Event Name"))
        self.description_form.setText(self.event_configuration.data.get("Description"))
        self.start_form.setText(self.event_configuration.data.get("Event Start Time"))
        self.end_form.setText(self.event_configuration.data.get("Event End Time"))
        self.root_form.setText(self.event_configuration.data.get("Root Directory"))
        self.red_form.setText(self.event_configuration.data.get("Red Team Folder"))
        self.white_form.setText(self.event_configuration.data.get("White Team Folder"))
        self.blue_form.setText(self.event_configuration.data.get("Blue Team Folder"))
        self.lead_label.setText(self.event_configuration.data.get("Lead Status"))
        self.ip_label.setText(self.event_configuration.data.get("Lead IP Address"))
        self.connections_label.setText(self.event_configuration.data.get("Connections"))

    def save_forms(self):
        self.event_configuration.data['Event Name'] = self.name_form.text()
        self.event_configuration.data['Description'] = self.description_form.toPlainText()
        self.event_configuration.data['Event Start Time'] = self.start_form.text()
        self.event_configuration.data['Event End Time'] = self.end_form.text()
        self.event_configuration.data['Root Directory'] = self.root_form.text()
        self.event_configuration.data['Red Team Folder'] = self.red_form.text()
        self.event_configuration.data['White Team Folder'] = self.white_form.text()
        self.event_configuration.data['Blue Team Folder'] = self.blue_form.text()
        self.event_configuration.update()

    def __initUI(self):
        self.setFrameShape(QFrame.StyledPanel)

        # Labels
        self.layout.addWidget(QLabel('Event Name:'), 1, 0)
        self.layout.addWidget(QLabel('Description:'), 2, 0)
        self.layout.addWidget(QLabel('Event Start Time:'), 4, 0)
        self.layout.addWidget(QLabel('Event End Time:'), 5, 0)
        self.layout.addWidget(QLabel('Root Directory:'), 6, 0)
        self.layout.addWidget(QLabel('Red Team Folder:'), 7, 0)
        self.layout.addWidget(QLabel('White Team Folder:'), 8, 0)
        self.layout.addWidget(QLabel('Blue Team Folder:'), 9, 0)
        self.layout.addWidget(QLabel('Lead Status:'), 10, 0)
        self.layout.addWidget(QLabel("Lead IP Address:"), 11, 0)
        self.layout.addWidget(QLabel('Connections:'), 12, 0)

        # Data
        self.layout.addWidget(self.name_form, 1, 1)
        self.layout.addWidget(self.description_form, 2, 1, 2, 1)
        self.layout.addWidget(self.start_form, 4, 1)
        self.layout.addWidget(self.end_form, 5, 1)
        self.layout.addWidget(self.root_form, 6, 1)
        self.layout.addWidget(self.red_form, 7, 1)
        self.layout.addWidget(self.white_form, 8, 1)
        self.layout.addWidget(self.blue_form, 9, 1)
        self.layout.addWidget(self.lead_label, 10, 1)
        self.layout.addWidget(self.ip_label, 11, 1)
        self.layout.addWidget(self.connections_label, 12, 1)

        self.__loadInfo()


class VectorDatabaseFrame(GenericFrame):
    def __init__(self):
        super().__init__(QHBoxLayout(), 'Vector Database')
        self.vectors = get_vector_list()
        self.vectorInfo = VectorInformationFrame()

        self.buttons = QToolBar('Buttons')
        self.list = QListWidget()

        self.initList()
        self.initUI()

    def initUI(self):
        self.setFrameShape(QFrame.StyledPanel)
        self.initButtons()

        self.layout.addWidget(self.list)
        self.layout.addWidget(self.vectorInfo)
        self.layout.addWidget(self.buttons)
        self.setMinimumSize(600, 400)

    def initButtons(self):
        self.buttons.setOrientation(Qt.Vertical)
        self.buttons.setMovable(False)
        self.buttons.setStyleSheet("""
                    QToolBar {
                        spacing: 6px;
                        padding: 3px;
                    }
                """)

        # Buttons after this are set to the right side
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.buttons.addWidget(spacer)

        # (TODO): Create new vector, vector sends signal to update list, switch to new vector in list
        b1 = QPushButton('Add Vector')
        self.buttons.addWidget(b1)

        # (TODO): Open confirm window, if yes in confirm, delete vector object in database then refresh list
        b2 = QPushButton('Delete Vector')
        self.buttons.addWidget(b2)
        b2.clicked.connect(self.close)

    def initList(self):
        for vector in self.vectors:
            self.list.addItem(vector.get("Name"))

        self.list.setCurrentItem(self.list.itemAt(0, 0))
        self.vectorInfo.update(self.list.currentItem())
        self.list.itemClicked.connect(self.vectorInfo.update)

    def save_forms(self):
        print('saved')


class VectorInformationFrame(GenericFrame):
    def __init__(self):
        super().__init__(QGridLayout(), 'Vector Information')
        self.currentVector = None
        self.name_form = QLineEdit()
        self.description_form = QTextEdit()
        self.save_changes = QPushButton("Save Changes")

        self.initFrame()

    def initFrame(self):
        self.setFrameShape(QFrame.StyledPanel)
        self.layout.addWidget(QLabel('Name:'), 1, 0)
        self.layout.addWidget(self.name_form, 1, 1)
        self.layout.addWidget(QLabel('Description:'), 2, 0)
        self.layout.addWidget(self.description_form, 2, 1, 2, 1)
        self.layout.addWidget(self.save_changes, 3, 0)

        self.save_changes.clicked.connect(self.update_vector)
        self.name_form.textChanged.connect(self.toggle_save_disabled)
        self.description_form.textChanged.connect(self.toggle_save_disabled)
        self.save_changes.setDisabled(True)

    def toggle_save_disabled(self):
        self.save_changes.setDisabled(False)

    def update(self, vector):
        self.currentVector = Vector(None, vector.text())
        self.name_form.setText(self.currentVector.data.get("Name"))
        self.description_form.setText(self.currentVector.data.get("Description"))
        self.save_changes.setDisabled(True)

    def update_vector(self):
        self.currentVector.data["Name"] = self.name_form.text()
        self.currentVector.data["Description"] = self.description_form.toPlainText()
        self.currentVector.update()
        self.save_changes.setDisabled(True)


class LogFileFrame(GenericFrame):
    def __init__(self):
        super().__init__(QHBoxLayout(), 'Log Files')
        self.__logFiles = {"Readme.txt": "Readme.txt",
                           "20193019_101559.jpg": "20193019_101559.jpg",
                           "20190220_161043.log": "20190220_161043.log"}
        self.__buttons = QToolBar('Buttons')
        self.__list = QListWidget()
        self.__logFileInfo = LogFileInformationFrame()

        self.__initFrame()

    def __initFrame(self):
        self.setFrameShape(QFrame.StyledPanel)
        self.__initList()
        self.__initButtons()

        self.layout.addWidget(self.__list)
        self.layout.addWidget(self.__logFileInfo)
        self.layout.addWidget(self.__buttons)
        self.setMinimumSize(600, 400)

    def __initList(self):
        for f in self.__logFiles:
            self.__list.addItem(f)

        self.__list.setCurrentItem(self.__list.itemAt(0, 0))
        self.__logFileInfo.update(self.__list.itemAt(0, 0))
        self.__list.itemClicked.connect(self.__logFileInfo.update)
        self.__list.setMaximumWidth(200)

    def __initButtons(self):
        self.__buttons.setOrientation(Qt.Vertical)
        self.__buttons.setMovable(False)
        self.__buttons.setStyleSheet("""
                    QToolBar {
                        spacing: 6px;
                        padding: 3px;
                    }
                """)

        # Buttons after this are set to the right side
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.__buttons.addWidget(spacer)

        # (TODO): Add triggers
        b1 = QPushButton('Accept File...')
        self.__buttons.addWidget(b1)

        # (TODO): Add triggers
        b2 = QPushButton('Reject File...')
        self.__buttons.addWidget(b2)

    def save_forms(self):
        print('saved')


class LogFileInformationFrame(GenericFrame):
    def __init__(self):
        super().__init__(QGridLayout(), 'Log File Information')
        self.__currentLog = None
        self.__initFrame()

    def __initFrame(self):
        self.setFrameShape(QFrame.StyledPanel)

    def __loadInfo(self):
        # (TODO): Add after action report for file and status
        self.layout.addWidget(QLabel('Name:'), 1, 0)
        self.layout.addWidget(QLabel('Cleansing Status:'), 2, 0)
        self.layout.addWidget(QLabel('Validation Status:'), 3, 0)
        self.layout.addWidget(QLabel('Ingestion Status:'), 4, 0)
        self.layout.addWidget(QLabel('Acknowledgement Status:'), 5, 0)
        self.layout.addWidget(QLabel('Enforcement Action Report'), 6, 1, Qt.AlignCenter)

        spacer = QLabel()
        self.layout.addWidget(spacer, 6, 2)

        self.layout.addWidget(QLabel(self.__currentLog), 1, 1, Qt.AlignLeft)
        self.layout.addWidget(QLabel('Cleansed'), 2, 1)
        self.layout.addWidget(QLabel('Validated'), 3, 1)
        self.layout.addWidget(QLabel('Ingested'), 4, 1)
        self.layout.addWidget(QLabel('Accepted'), 5, 1)

        self.layout.addWidget(QTextEdit('No problems found'), 8, 0, 8, 3)

    def update(self, logfile):
        for i in reversed(range(self.layout.count())):
            self.layout.itemAt(i).widget().setParent(None)

        self.__currentLog = logfile.text()
        self.__loadInfo()

########################################################################################################################


class VectorFrame(GenericFrame):
    def __init__(self):
        super().__init__(QHBoxLayout(), 'Vector Frame')
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
        t = GenericFrame(QHBoxLayout(), 'vector tab')
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
        super().__init__(QHBoxLayout(), 'Node Table Frame')
        self.info1 = {"Node Visibility": "something0",
                      "Node ID": "something1",
                      "Node Name": "something2",
                      "Node Time Stamp": "something3",
                      "log_entry_reference": "something4",
                      "log_creator": "something5",
                      "event_type": "something6",
                      "icon_type": "something7",
                      "source": "something8",
                      "Node Description": "something9 has to be very long because I am testing how the table will "
                                          "handle it and make sure it doesn't crash "}

        self.table = QTableWidget()
        #self.table.cellChanged().connect(self.c_current)
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

        # little example on how to add a node dictionary to the vector frame table
        self.addNodes()

        self.layout.addWidget(self.table)

    def addNodes(self):
        loop = 1
        rowCount = 1
        colCount = 0

        if loop == 1:
            self.table.setColumnCount(len(self.info1))
            self.table.setRowCount(rowCount)
            self.table.insertRow(1)

            for key in self.info1.keys():
                item = QTableWidgetItem(self.info1[key])
                self.table.setItem(1, colCount, item)
                colCount += 1

            loop = 2


class GraphFrame(GenericFrame):
    def __init__(self):
        super().__init__(QVBoxLayout(), 'Graph Frame')
        self.graphInit()

    def graphInit(self):
        vector = VectorFacade("name", "description")
        self.layout.addWidget(vector.graph)
