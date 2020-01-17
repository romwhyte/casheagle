
__author__ = "Romayne Whyte, http://ijasoft.com/"
__version__ = "$Revision: 1.0 $"
__date__ = "$Date: 2019/12/31 $"
__copyright__ = "Copyright 2019 Ijasoft, Inc."


from PyQt5.QtWidgets import QMdiSubWindow, QWidget, QInputDialog, QMessageBox, QDockWidget,QWizard
from PyQt5.QtCore import pyqtProperty, QDate, QDateTime, Qt, QRegExp
from PyQt5.QtGui import QIcon, QRegExpValidator
from ui_action.ui.applicant_ui import *

class ApplicantForm(QWizard):
    def __init__(self):
        """[summary]
        """
        super().__init__()
        self.ui = Ui_Wizard()
        self.ui.setupUi(self)
        self.setWindowTitle("Applicant")