from PyQt5.QtWidgets import QMainWindow, QAction
from casheagle.ui.mainwindow_ui import *
from casheagle import borrower

class MainForm(QMainWindow):
    def __init__(self):
        """Initialization for Main Windows

        Arguments:
            QMainWindow {[type]} -- [description]
        """
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.action_Borrower.triggered.connect(self.openBorrower)
        self.ui.action_Loans.triggered.connect(self.openLoan)
        self.ui.actionMake_Payment.triggered.connect(self.makePayment)
        self.ui.actionAbout.triggered.connect(self.openAboutDialog)
        self.show()

    def setPers(self, db):
        """Setup the Persistent object
        Arguments:
            db {Database/Persistance} -- Used to add,update,delete, find, findall
        """
        self.db = db

    def openAboutDialog(self):
        pass

    def openBorrower(self):
        """
            Open the borrowers Screen via GUI
        """
        borrowerform = borrower.BorrowerForm()
        borrowerform.setPers(self.db)
        self.ui.mdiArea.addSubWindow(borrowerform)
        borrowerform.showMaximized()

    def openLoan(self):
        pass

    def makePayment(self):
        pass