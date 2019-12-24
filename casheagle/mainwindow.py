from PyQt5.QtWidgets import QMainWindow
from casheagle.ui.mainwindow_ui import *

class MainForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
