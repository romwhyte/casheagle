
__author__ = "Romayne Whyte, http://ijasoft.com/"
__version__ = "$Revision: 1.0 $"
__date__ = "$Date: 2019/12/31 $"
__copyright__ = "Copyright 2019 Ijasoft, Inc."


from PyQt5.QtWidgets import QMdiSubWindow, QWidget, QInputDialog, QMessageBox
from PyQt5.QtCore import QDate, QDateTime, Qt, QRegExp
from PyQt5.QtGui import QIcon, QRegExpValidator

from datetime import datetime,date
from ui_action.ui.borrower_ui import *
from db import tables 
import logging

logger = logging.getLogger(__name__)

class BorrowerForm(QMdiSubWindow):
    #TODO: Add the Garantor, Additional, References fields for CRUD and validation
    #TODO: Add the cancel button

    def __init__(self):
        """Borrowers Sub Windows for the MDI
            Setup for basic actions of the borrowers screen
        Arguments:
            QMdiSubWindow {[type]} -- [description]
        """
        super().__init__()
        self.state = False
        self.ui = Ui_FormBorrower()
        self.ui.setupUi(self)
        self.setWindowTitle("Borrower")
        
        #setup toolbar buttons
        self.ui.btnApplied.clicked.connect(self.applied)
        self.ui.btnEdit.clicked.connect(self.edit)
        self.ui.btnSave.clicked.connect(self.save)
        self.ui.btnFind.clicked.connect(self.find)
        self.ui.btnCancel.clicked.connect(self.cancel)
        self.ui.btnDelete.clicked.connect(self.delete)

        #self.validate()
        self.borrower = tables.Borrower()
        self.BorrowerTextfieldState(False)


    def applied(self):
        """Allow information to be added to the fields
        """
        self.BorrowerTextfieldState(True)
        self.buttonState(True)
        self.setFieldValue()

    def edit(self):
        """Update borrowers information
        """
        self.BorrowerlineState(True)

    def save(self):
        """Save borrowers information
        """
        self.getFieldValues()
        self.db.save(self.borrower)
        self.setFieldValue()
        self.BorrowerTextfieldState(False)
        self.buttonState(False)
        logger.info("insert/update", self.borrower)

    def cancel(self):
        """[summary]
        """
        self.borrower  = tables.Borrower()
        self.setFieldValue()
        self.BorrowerTextfieldState(False)
        self.buttonState(False)

    def delete(self):
        """[summary]
        """
        self.db.delete(self.borrower)
        self.borrower = tables.Borrower()
        self.setFieldValue()

    def find(self):
        """Find the Borrowerer Information
        """
        borrowerid, ok = QInputDialog.getInt(self, 'Find Borrowers Information','Borrower ID:')
        self.borrower = self.db.find(tables.Borrower,borrowerid)
        if not self.borrower:
            self.borrower = tables.Borrower()
            QMessageBox.information(self,"Not Found","The Borrowers ID was not found", QMessageBox.Ok)

        self.setFieldValue()

        self.buttonState(False)
        


    def BorrowerTextfieldState(self, state):
        """Change the edit state of the textfield from enabled to disabled
        Arguments:
            state {boolean} -- parameter for state change true for enable, false for disabled
        """
        self.ui.grpGeneralInfomation.setEnabled(state)
        self.ui.grpPrevAddress.setEnabled(state)
        self.ui.grpAddress.setEnabled(state)
        self.ui.grpContacts.setEnabled(state)
        self.ui.grpPrevEmployment.setEnabled(state)
        self.ui.grpEmployment.setEnabled(state)
        self.ui.grpspouse.setEnabled(state)

        #Gaurantor
        self.ui.grpGGeneralInformation.setEnabled(state)
        self.ui.grpGPrevAddress.setEnabled(state)
        self.ui.grpGAddress.setEnabled(state)
        self.ui.grpGContacts.setEnabled(state)
        self.ui.grpGPrevEmployment.setEnabled(state)
        self.ui.grpGEmployment.setEnabled(state)
        self.ui.grpGspouse.setEnabled(state)
        

    def buttonState(self, state):
        #TODO : Setup a way to enable delete and edit when record is loaded in fields

        
        self.ui.btnApplied.setEnabled(not state)
        
        if self.ui.lineID.text() != "":
            self.ui.btnDelete.setEnabled(not state)
            self.ui.btnEdit.setEnabled(not state)
        
        self.ui.btnFind.setEnabled(not state)
        self.ui.btnSave.setEnabled(state)
        self.ui.btnCancel.setEnabled(state)

    def setFieldValue(self):
        self.setBorrowerFieldValues()
        self.setGuarantorFieldValues()

    def setBorrowerFieldValues(self):
        self.ui.lineID.setText(str(self.borrower.id) if self.borrower.id else '')
        self.ui.lineEditFirstName.setText(self.borrower.FirstName)
        self.ui.lineEditLastName.setText(self.borrower.LastName)
        self.ui.lineEditMiddleInit.setText(self.borrower.MiddleName)
        self.ui.lineEditTRN.setText(self.borrower.TRN)
        self.ui.lineAlias.setText(self.borrower.Alias)
        self.ui.cboMaritalStatus.setCurrentText(self.borrower.MaritalStatus)
        self.ui.lineAddress1.setText(self.borrower.Address1)
        self.ui.lineAddress2.setText(self.borrower.Address2)
        self.ui.lineAddress3.setText(self.borrower.Address3)
        self.ui.linePrevAddress1.setText(self.borrower.PrevAddr)
        self.ui.linePrevAddress2.setText(self.borrower.PrevAddr2)
        self.ui.linePrevAddress3.setText(self.borrower.PrevAddr3)
        self.ui.linePrevLengthOfStay.setText(self.borrower.Length_reside_prev)
        self.ui.lineHomeTel.setText(self.borrower.HomeTel)
        self.ui.lineWorkTel.setText(self.borrower.WorkTel)
        self.ui.lineCellNo1.setText(self.borrower.digicell)
        self.ui.lineCellNo2.setText(self.borrower.digicel2)
        self.ui.cbosex.setCurrentText(self.borrower.Sex)
        self.ui.cboPaymentPeriod.setCurrentText(self.borrower.PaymentPeriod)
        self.ui.linePrevOccupation.setText(self.borrower.PreviousEmployer)
        self.ui.linePrevEmployer.setText(self.borrower.PreviousEmployer)
        self.ui.linePrevEmpAddress1.setText(self.borrower.PrevEmpAddress1)
        self.ui.linePrevEmpAddress2.setText(self.borrower.PrevEmpAddress2)
        self.ui.linePrevEmpAddress3.setText(self.borrower.PrevEmpAddress3)
        self.ui.datePrevEmpStartDate.setDate(date.fromisoformat(self.borrower.PrevEmpStartDate) if self.borrower.PrevEmpStartDate else date.today())
        self.ui.linePrevEmpTelNo.setText(self.borrower.Extension)
        self.ui.linePrevDepartment.setText(self.borrower.Department)
        self.ui.dateDOB.setDate(date.fromisoformat(self.borrower.DOB) if self.borrower.DOB else date.today())
        self.ui.lineOccupation.setText(self.borrower.occupation)
        self.ui.lineEmployer.setText(self.borrower.Employer1)
        self.ui.lineEmpAddress1.setText(self.borrower.EmpAddress1)
        self.ui.lineEmpAddress2.setText(self.borrower.EmpAddress2)
        self.ui.lineEmpAddress3.setText(self.borrower.EmpAddress3)
        self.ui.lineEmpTelNo.setText(self.borrower.EmpAddress3)
        self.ui.lineDepartment.setText(self.borrower.Department)
        self.ui.dateEmpStartDate.setDate(date.fromisoformat(self.borrower.EmpStartDate) if self.borrower.EmpStartDate else date.today())
        self.ui.lineEditSalaryAmount.setText(self.borrower.SalaryAmount)
        self.ui.lineSpouseEmployer.setText(self.borrower.spouse_employment)
        self.ui.lineSpouseFullAddress.setText(self.borrower.spouse_emp_address)
        self.ui.lineSpouseFullName.setText(self.borrower.nameofspouse)
        self.ui.lineSpouseTRN.setText(self.borrower.SpouseTRN)
        self.ui.lineSpouseTelNo.setText(self.borrower.spouse_emp_tel)
        self.ui.lineSpouseAlias.setText(self.borrower.SpouseAlias)
        self.ui.dateSpouseDOB.setDate(date.fromisoformat(self.borrower.SpouseDOB) if self.borrower.SpouseDOB else date.today())

    
    def setGuarantorFieldValues(self):
        """[summary]
        """
        self.ui.lineEditGFirstName.setText(self.borrower.FirstName)
        self.ui.lineEditGLastName.setText(self.borrower.LastName)
        self.ui.lineEditGMiddleInit.setText(self.borrower.MiddleName)
        self.ui.lineEditGTRN.setText(self.borrower.TRN)
        self.ui.lineAlias.setText(self.borrower.Alias)
        self.ui.cboGMaritalStatus.setCurrentText(self.borrower.MaritalStatus)
        self.ui.lineGAddress1.setText(self.borrower.Address1)
        self.ui.lineGAddress2.setText(self.borrower.Address2)
        self.ui.lineGAddress3.setText(self.borrower.Address3)
        self.ui.lineGPrevAddress1.setText(self.borrower.PrevAddr)
        self.ui.lineGPrevAddress2.setText(self.borrower.PrevAddr2)
        self.ui.lineGPrevAddress3.setText(self.borrower.PrevAddr3)
        self.ui.lineGPrevLengthOfStay.setText(self.borrower.Length_reside_prev)
        self.ui.lineGHomeTel.setText(self.borrower.HomeTel)
        self.ui.lineGWorkTel.setText(self.borrower.WorkTel)
        self.ui.lineGCellNo1.setText(self.borrower.digicell)
        self.ui.lineGCellNo2.setText(self.borrower.digicel2)
        self.ui.cboGsex.setCurrentText(self.borrower.Sex)
        self.ui.cboGPaymentPeriod.setCurrentText(self.borrower.PaymentPeriod)
        self.ui.lineGPrevOccupation.setText(self.borrower.PreviousEmployer)
        self.ui.lineGPrevEmployer.setText(self.borrower.PreviousEmployer)
        self.ui.lineGPrevEmpAddress1.setText(self.borrower.PrevEmpAddress1)
        self.ui.lineGPrevEmpAddress2.setText(self.borrower.PrevEmpAddress2)
        self.ui.lineGPrevEmpAddress3.setText(self.borrower.PrevEmpAddress3)
        self.ui.datePrevEmpStartDate.setDate(date.fromisoformat(self.borrower.PrevEmpStartDate) if self.borrower.PrevEmpStartDate else date.today())
        self.ui.lineGPrevEmpTelNo.setText(self.borrower.Extension)
        self.ui.lineGPrevDepartment.setText(self.borrower.Department)
        self.ui.dateGDOB.setDate(date.fromisoformat(self.borrower.DOB) if self.borrower.DOB else date.today())
        self.ui.lineGOccupation.setText(self.borrower.occupation)
        self.ui.lineGEmployer.setText(self.borrower.Employer1)
        self.ui.lineGEmpAddress1.setText(self.borrower.EmpAddress1)
        self.ui.lineGEmpAddress2.setText(self.borrower.EmpAddress2)
        self.ui.lineGEmpAddress3.setText(self.borrower.EmpAddress3)
        self.ui.lineGEmpTelNo.setText(self.borrower.EmpAddress3)
        self.ui.lineGDepartment.setText(self.borrower.Department)
        self.ui.dateGEmpStartDate.setDate(date.fromisoformat(self.borrower.EmpStartDate) if self.borrower.EmpStartDate else date.today())
        self.ui.lineGEditGSalaryAmount.setText(self.borrower.SalaryAmount)
        self.ui.lineGSpouseEmployer.setText(self.borrower.spouse_employment)
        self.ui.lineGSpouseFullAddress.setText(self.borrower.spouse_emp_address)
        self.ui.lineGSpouseFullName.setText(self.borrower.nameofspouse)
        self.ui.lineGSpouseTRN.setText(self.borrower.SpouseTRN)
        self.ui.lineGSpouseTelNo.setText(self.borrower.spouse_emp_tel)
        self.ui.lineGSpouseAlias.setText(self.borrower.SpouseAlias)
        self.ui.dateGSpouseDOB.setDate(date.fromisoformat(self.borrower.SpouseDOB) if self.borrower.SpouseDOB else date.today())




    def getFieldValues(self):
        if self.ui.lineID.text() != '':
            self.borrower.id = self.ui.lineID.text()

        self.borrower.FirstName = self.ui.lineEditFirstName.text()
        self.borrower.LastName = self.ui.lineEditLastName.text()
        self.borrower.MiddleName = self.ui.lineEditMiddleInit.text()
        self.borrower.TRN = self.ui.lineEditTRN.text()
        self.borrower.Alias = self.ui.lineAlias.text()
        self.borrower.MaritalStatus = self.ui.cboMaritalStatus.itemText(self.ui.cboMaritalStatus.currentIndex())
        self.borrower.Address1 = self.ui.lineAddress1.text()
        self.borrower.Address2 =self.ui.lineAddress2.text()
        self.borrower.Address3 = self.ui.lineAddress3.text()
        self.borrower.PrevAddr = self.ui.linePrevAddress1.text() 
        self.borrower.PrevAddr2 = self.ui.linePrevAddress2.text() 
        self.borrower.PrevAddr3 = self.ui.linePrevAddress3.text()
        self.borrower.Length_reside_prev = self.ui.linePrevLengthOfStay.text()
        self.borrower.HomeTel = self.ui.lineHomeTel.text()
        self.borrower.WorkTel = self.ui.lineWorkTel.text()
        self.borrower.digicell = self.ui.lineCellNo1.text()
        self.borrower.digicel2 = self.ui.lineCellNo2.text()
        self.borrower.Sex = self.ui.cbosex.itemText(self.ui.cbosex.currentIndex())
        self.borrower.PaymentPeriod = self.ui.cboPaymentPeriod.itemText(self.ui.cboPaymentPeriod.currentIndex())
        self.borrower.PreviousEmployer = self.ui.linePrevOccupation.text()
        self.borrower.PreviousEmployer = self.ui.linePrevEmployer.text()
        self.borrower.PrevEmpAddress1 = self.ui.linePrevEmpAddress1.text()
        self.borrower.PrevEmpAddress2 = self.ui.linePrevEmpAddress2.text()
        self.borrower.PrevEmpAddress3 = self.ui.linePrevEmpAddress3.text()
        self.borrower.Extension = self.ui.linePrevEmpTelNo.text()
        self.borrower.Department = self.ui.linePrevDepartment.text()
        self.borrower.EmpStartDate = self.ui.datePrevEmpStartDate.date().currentDate().toString(Qt.ISODate)
        self.borrower.occupation = self.ui.lineOccupation.text()
        self.borrower.Employer1 = self.ui.lineEmployer.text()
        self.borrower.addressofemployment = self.ui.lineEmpAddress1.text()
        self.borrower.EmpAddress1 = self.ui.lineEmpAddress2.text()   
        self.borrower.EmpAddress2 = self.ui.lineEmpAddress3.text()
        self.borrower.EmpAddress3 = self.ui.lineEmpTelNo.text()
        self.borrower.Department = self.ui.lineDepartment.text()
        self.borrower.EmpStartDate = self.ui.dateEmpStartDate.date().currentDate().toString(Qt.ISODate)
        self.borrower.SalaryAmount = self.ui.lineEditSalaryAmount.text()
        self.borrower.spouse_employment = self.ui.lineSpouseEmployer.text()
        self.borrower.spouse_emp_address = self.ui.lineSpouseFullAddress.text()
        self.borrower.nameofspouse = self.ui.lineSpouseFullName.text()
        self.borrower.SpouseTRN = self.ui.lineSpouseTRN.text()
        self.borrower.spouse_emp_tel = self.ui.lineSpouseTelNo.text()
        self.borrower.SpouseAlias = self.ui.lineSpouseAlias.text()
        self.borrower.SpouseDOB = self.ui.dateSpouseDOB.date().currentDate().toString(Qt.ISODate)

    def validate(self):
        #TODO: Validate each field and Display error
        reg_ex = QRegExp("[a-z-A-Z_]+")
        name_validator = QRegExpValidator(reg_ex, self.ui.lineEditFirstName)
        self.ui.lineEditFirstName.setValidator(name_validator)

    def setPers(self,db):
        self.db = db
