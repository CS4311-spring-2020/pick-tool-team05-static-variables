from PyQt5.QtWidgets import (QDialog, QDialogButtonBox, QLabel, QLineEdit, QTextEdit, QHBoxLayout, QGroupBox,
                             QFormLayout, QVBoxLayout)
from PyQt5.QtGui import QIcon


class AddVectorPopUp(QDialog):

    def __init__(self):
        super(AddVectorPopUp, self).__init__()

        self.create_horizontal_message()
        self.create_edit_fields()
        self.show()

        button_options = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        button_options.accepted.connect(self.accept)
        button_options.rejected.connect(self.reject)

        main_layout = QVBoxLayout()

        main_layout.addWidget(self.form_edit_field)
        main_layout.addWidget(self.horizontal_message)
        main_layout.addWidget(button_options)
        self.setLayout(main_layout)

        self.setWindowTitle("Add Vector")
        self.setWindowIcon(QIcon("../Resources/Images/add-square.png"))

    def create_horizontal_message(self):
        self.horizontal_message = QGroupBox("Notice")
        layout = QHBoxLayout()

        message = QLabel("Fields with * are necessary in order to continue.")
        layout.addWidget(message)

        self.horizontal_message.setLayout(layout)

    def create_edit_fields(self):
        self.form_edit_field = QGroupBox("New Vector:")
        layout = QFormLayout()
        layout.addRow(QLabel("Name* :"), QLineEdit())
        layout.addRow(QLabel("Description:"), QTextEdit())
        self.form_edit_field.setLayout(layout)

    #(TODO): Read, Save, and process information inputed in the fields and connect button ok