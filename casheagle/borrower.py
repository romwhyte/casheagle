from PyQt5.QtWidgets import QMdiSubWindow, QWidget
from casheagle.ui.borrower_ui import *

class BorrowerForm(QMdiSubWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_FormBorrower()
        self.ui.setupUi(self)
        self.setWindowTitle("Borrower")
