from PyQt5.QtWidgets import QMainWindow, QAction
from casheagle.ui.mainwindow_ui import *
from casheagle import borrower

class MainForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.action_Borrower.triggered.connect(self.openBorrower)
        self.ui.action_Loans.triggered.connect(self.openLoan)
        self.ui.actionMake_Payment.triggered.connect(self.makePayment)
        self.ui.actionAbout.triggered.connect(self.openAboutDialog)
        #self.ui.mdiArea
        self.show()

    def openAboutDialog(self):
        pass

    def openBorrower(self):
        borrowerform = borrower.BorrowerForm()
        self.ui.mdiArea.addSubWindow(borrowerform)
        borrowerform.showMaximized()

    def openLoan(self):
        pass

    def makePayment(self):
        pass