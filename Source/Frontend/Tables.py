from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFrame, QTableWidget, QVBoxLayout, QAbstractScrollArea, QTableWidgetItem, QPushButton, \
    QToolBar, QLineEdit, QComboBox, QCheckBox


class LogFileTable(QFrame):
    def __init__(self):
        super().__init__()
        self.table = QTableWidget()
        self.layout = QVBoxLayout()
        self.main()

    def main(self):
        self.setLayout(self.layout)
        self.setStyleSheet("""
        QTableWidget {
            border: none;
        }
        """)
        self.initTable()

    # (TODO): Add way of getting column # based on log entries in DB, hard coded for now based on SRS 1.7
    def initTable(self):
        self.table.setRowCount(5)
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(['Filename', 'Cleansing Status', 'Validation Status',
                                              'Ingestion Status', 'Action Report', 'Source'])
        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.updateTable()
        self.layout.addWidget(self.table)

    def updateTable(self):
        # (TODO): Actually feed in data from log files, make log file global variable (fill from DB)
        self.table.setStyleSheet("""
            QPushButton {
                margin: 6px;
            }
        """)
        self.table.insertRow(0)
        self.table.setItem(0, 0, QTableWidgetItem("1391.log"))
        self.table.setItem(0, 1, QTableWidgetItem("Cleansed"))
        self.table.setItem(0, 2, QTableWidgetItem("Validated"))
        self.table.setItem(0, 3, QTableWidgetItem("Ingested"))
        self.table.setCellWidget(0, 4, QPushButton("View"))
        self.table.setItem(0, 5, QTableWidgetItem("C:/Users/x/Documents/Ev/Red/1391.log"))

        self.table.insertRow(1)
        self.table.setItem(1, 0, QTableWidgetItem("139w.log"))
        self.table.setItem(1, 1, QTableWidgetItem("Uncleansed"))
        self.table.setItem(1, 2, QTableWidgetItem("Not Validated"))
        self.table.setItem(1, 3, QTableWidgetItem("Not Ingested"))
        self.table.setCellWidget(1, 4, QPushButton("View"))
        self.table.setItem(1, 5, QTableWidgetItem("C:/Users/x/Documents/Ev/Blue/139w.log"))

        self.table.insertRow(2)
        self.table.setItem(2, 0, QTableWidgetItem("13333w.log"))
        self.table.setItem(2, 1, QTableWidgetItem("Uncleansed"))
        self.table.setItem(2, 2, QTableWidgetItem("Invalid"))
        self.table.setItem(2, 3, QTableWidgetItem("Not Ingested"))
        self.table.setCellWidget(2, 4, QPushButton("View"))
        self.table.setItem(2, 5, QTableWidgetItem("C:/Users/x/Documents/Ev/Blue/13333w.log"))


class LogEntryTable(QFrame):
    def __init__(self):
        super().__init__()
        self.table = QTableWidget()
        self.layout = QVBoxLayout()
        self.menu = QToolBar('Toolbar')
        self.main()

    def main(self):
        self.setLayout(self.layout)
        self.setStyleSheet("""
        QTableWidget {
            border: none;
        }
        QCellWidget {
            text-align: center;
        }
        """)
        self.initMenu()
        self.initTable()

    def initMenu(self):
        self.layout.addWidget(self.menu)
        self.menu.setMovable(False)
        self.menu.setStyleSheet("""
        QToolBar {
            spacing: 6px;
            margin-bottom: 39px;
        }
        """)

        add_to_vectors = QPushButton("Correlate Entries")
        add_to_vectors.setStatusTip('Add selected log entries to specified vectors')
        self.menu.addWidget(add_to_vectors)

        self.menu.addSeparator()

        search_box = QLineEdit()
        search_button = QPushButton("Search")
        search_button.clicked.connect(self.search)
        self.menu.addWidget(search_box)
        self.menu.addWidget(search_button)

        self.menu.addSeparator()

        # (TODO): Add dropdown for sub-filters
        filters = QComboBox()
        combo_options = ["Creator", "Event Type", "Start Timestamp", "End TimeStamp"]
        for x in combo_options:
            filters.addItem(x)
        filter_button = QPushButton("Apply Filter")
        filter_button.clicked.connect(self.filter)
        self.menu.addWidget(filters)
        self.menu.addWidget(filter_button)

    # (TODO): Save complete table, formulate new table with search results and replace table displayed
    def search(self):
        items = self.table.findItems(self.edit.text(), Qt.MatchExactly)

    # (TODO): Apply filters by using the same process as search
    def filter(self):
        return

    # (TODO): Add way of getting column # based on log entries in DB, hard coded for now based on SRS 1.7
    def initTable(self):
        self.table.setStyleSheet("""
            QComboBox {
                margin: 6px;
            }
        """)
        self.table.setRowCount(4)
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(
            ['Select\nTo Add', 'Vector', 'List Number', 'Timestamp', 'Log Entry Event'])
        self.updateTable()
        self.table.verticalHeader().setVisible(False)
        self.table.verticalHeader().setDefaultSectionSize(47)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setWordWrap(True)
        self.layout.addWidget(self.table)

    # (TODO): Add way of getting # of rows from log entries in DB
    def updateTable(self):
        # (TODO): Actually feed in data from log files
        for i in range(0, 4):
            self.table.insertRow(i)

            box = QCheckBox()
            box.blockSignals(True)

            # (TODO): Get options from actual vectors. Declare vectors global variable
            combo = QComboBox()
            combo_options = ["", "DDoS", "Vector 2"]
            for x in combo_options:
                combo.addItem(x)

            self.table.setCellWidget(i, 0, box)
            self.table.setCellWidget(i, 1, combo)
            self.table.setItem(i, 2, QTableWidgetItem(i.__str__()))
            self.table.setItem(i, 3, QTableWidgetItem("12:39pm 2/3/2020"))
            self.table.setItem(i, 4, QTableWidgetItem("""
            Host: Blue, Source: Red, Sourcetype: .txt, 
            Content: We did a thing.
            """))