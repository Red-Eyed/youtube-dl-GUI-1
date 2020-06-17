from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog
from UI.AboutDialog import Ui_Dialog


class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super(AboutDialog, self).__init__(parent, Qt.WindowSystemMenuHint | Qt.WindowTitleHint)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
