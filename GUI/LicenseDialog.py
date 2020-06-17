from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog
from UI.LicenseDialog import Ui_Dialog


class LicenseDialogue(QDialog):
    def __init__(self, parent=None):
        super(LicenseDialogue, self).__init__(parent, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.ExitButton.clicked.connect(self.close)