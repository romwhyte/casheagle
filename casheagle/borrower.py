
__author__ = "Romayne Whyte, http://ijasoft.com/"
__version__ = "$Revision: 1.0 $"
__date__ = "$Date: 2019/12/31 $"
__copyright__ = "Copyright 2019 Ijasoft, Inc."


from PyQt5.QtWidgets import QMdiSubWindow, QWidget, QInputDialog, QMessageBox
from PyQt5.QtGui import QIcon
from datetime import datetime
from casheagle.ui.borrower_ui import *
from db import tables 

class BorrowerForm(QMdiSubWindow):
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
        self.ui.btnApplied.clicked.connect(self.applied)
        self.ui.btnEdit.clicked.connect(self.edit)
        self.ui.btnSave.clicked.connect(self.save)
        self.ui.btnFind.clicked.connect(self.find)

        self.borrower = tables.Borrower()


    def applied(self):
        """Allow information to be added to the fields
        """
        self.BorrowerTextfieldState(True)
        self.buttonState(True)
        self.setFieldValue()

    def edit(self):
        self.BorrowerlineState(True)

    def save(self):
        """[summary]
        """
        self.getFieldValues()
        self.db.save(self.borrower)
        self.setFieldValue()
        self.BorrowerTextfieldState(False)
        self.buttonState(False)


    def find(self):
        """Find the Borrowerer Information
        """
        borrowerid, ok = QInputDialog.getInt(self, 'Find Borrowers Information','Borrower ID:')
        self.borrower = self.db.find(tables.Borrower,borrowerid)
        if not self.borrower:
            self.borrower = tables.Borrower()
            QMessageBox.information(self,"Not Found","The Borrowers ID was not found", QMessageBox.Ok)

        self.setFieldValue()


    def BorrowerTextfieldState(self, state):
        """Change the edit state of the textfield from enabled to disabled

        Arguments:
            state {boolean} -- parameter for state change true for enable, false for disabled
        """

        self.ui.lineEditFirstName.setEnabled(state)
        self.ui.lineEditLastName.setEnabled(state)
        self.ui.lineEditMiddleInit.setEnabled(state)
        self.ui.lineEditTRN.setEnabled(state)
        self.ui.lineAlias.setEnabled(state)
        self.ui.cboMaritalStatus.setEnabled(state)
        self.ui.lineAddress1.setEnabled(state)
        self.ui.lineAddress2.setEnabled(state)
        self.ui.lineAddress3.setEnabled(state)
        self.ui.lineLengthOfStay.setEnabled(state)
        self.ui.linePrevAddress1.setEnabled(state)
        self.ui.linePrevAddress2.setEnabled(state)
        self.ui.linePrevAddress3.setEnabled(state)
        self.ui.linePrevLengthOfStay.setEnabled(state)
        self.ui.lineHomeTel.setEnabled(state)
        self.ui.lineWorkTel.setEnabled(state)
        self.ui.lineCellNo1.setEnabled(state)
        self.ui.lineCellNo2.setEnabled(state)
        self.ui.dateDOB.setEnabled(state)
        self.ui.cbosex.setEnabled(state)
        self.ui.cboPaymentPeriod.setEnabled(state)
        self.ui.linePrevOccupation.setEnabled(state)
        self.ui.linePrevEmployer.setEnabled(state)
        self.ui.linePrevEmpAddress1.setEnabled(state)
        self.ui.linePrevEmpAddress2.setEnabled(state)
        self.ui.linePrevEmpAddress3.setEnabled(state)
        self.ui.linePrevEmpTelNo.setEnabled(state)
        self.ui.linePrevDepartment.setEnabled(state)
        self.ui.datePrevEmpStartDate.setEnabled(state)
        self.ui.lineOccupation.setEnabled(state)
        self.ui.lineEmployer.setEnabled(state)
        self.ui.lineEmpAddress1.setEnabled(state)
        self.ui.lineEmpAddress2.setEnabled(state)
        self.ui.lineEmpAddress3.setEnabled(state)
        self.ui.lineEmpTelNo.setEnabled(state)
        self.ui.lineDepartment.setEnabled(state)
        self.ui.dateEmpStartDate.setEnabled(state)
        self.ui.lineEditSalaryAmount.setEnabled(state)
        self.ui.lineSpouseAlias.setEnabled(state)
        self.ui.cboSpouseSex.setEnabled(state)
        self.ui.dateSpouseDOB.setEnabled(state)
        self.ui.lineSpouseEmployer.setEnabled(state)
        self.ui.lineSpouseFullAddress.setEnabled(state)
        self.ui.lineSpouseFullName.setEnabled(state)
        self.ui.lineSpouseTRN.setEnabled(state)
        self.ui.lineSpouseTelNo.setEnabled(state)


    def buttonState(self, state):
        self.ui.btnApplied.setEnabled(not state)
        #self.ui.btnDelete.setEnabled(not state)
        #self.ui.btnEdit.setEnabled(not state)
        self.ui.btnFind.setEnabled(not state)
        self.ui.btnSave.setEnabled(state)

    def setFieldValue(self):
        self.ui.lineEditFirstName.setText(""+self.borrower.id)
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
        self.ui.linePrevEmpTelNo.setText(self.borrower.Extension)
        self.ui.linePrevDepartment.setText(self.borrower.Department)
        self.ui.datePrevEmpStartDate.setDate(datetime.strptime(self.borrower.EmpStartDate, '%m/%d/%y %H:%M:%S') if self.borrower.EmpStartDate else datetime.today()) 
        self.ui.lineOccupation.setText(self.borrower.occupation)
        self.ui.lineEmployer.setText(self.borrower.Employer1)
        self.ui.lineEmpAddress1.setText(self.borrower.addressofemployment)
        #self.borrower.FirstName =  self.ui.lineEmpAddress2.setText()
        #self.borrower.FirstName =  self.ui.lineEmpAddress3.setText()
        #self.borrower.FirstName =  self.ui.lineEmpTelNo.setText()
        #self.borrower.FirstName =  self.ui.lineDepartment.setText()
        #self.borrower.FirstName =  self.ui.dateEmpStartDate.setText()
        #self.borrower. =  self.ui.lineEditSalaryAmount.setText()
        #self.borrower.so =  self.ui.lineSpouseAlias.setText()
        #self.borrower.FirstName =  self.ui.cboSpouseSex.setText()
        #self.borrower.sp =  self.ui.dateSpouseDOB.setText()
        self.ui.lineSpouseEmployer.setText(self.borrower.spouse_employment)
        self.ui.lineSpouseFullAddress.setText(self.borrower.spouse_emp_address)
        self.ui.lineSpouseFullName.setText(self.borrower.nameofspouse)
        self.ui.lineSpouseTRN.setText(self.borrower.SpouseTRN)
        self.ui.lineSpouseTelNo.setText(self.borrower.spouse_emp_tel)



    def getFieldValues(self):
        self.borrower.FirstName =  self.ui.lineEditFirstName.text()
        self.borrower.LastName =  self.ui.lineEditLastName.text()
        self.borrower.MiddleName =  self.ui.lineEditMiddleInit.text()
        self.borrower.TRN=  self.ui.lineEditTRN.text()
        self.borrower.Alias =  self.ui.lineAlias.text()
        self.borrower.MaritalStatus =  self.ui.cboMaritalStatus.itemText(self.ui.cboMaritalStatus.currentIndex())
        self.borrower.Address1=  self.ui.lineAddress1.text()
        self.borrower.Address2 =  self.ui.lineAddress2.text()
        self.borrower.Address3 =  self.ui.lineAddress3.text()
        self.borrower.PrevAddr =  self.ui.linePrevAddress1.text() 
        self.borrower.PrevAddr2= self.ui.linePrevAddress2.text() 
        self.borrower.PrevAddr3 = self.ui.linePrevAddress3.text()
        self.borrower.Length_reside_prev =  self.ui.linePrevLengthOfStay.text()
        self.borrower.HomeTel =  self.ui.lineHomeTel.text()
        self.borrower.WorkTel =  self.ui.lineWorkTel.text()
        self.borrower.digicell =  self.ui.lineCellNo1.text()
        self.borrower.digicel2 =  self.ui.lineCellNo2.text()
        self.borrower.Sex =  self.ui.cbosex.itemText(self.ui.cbosex.currentIndex())
        self.borrower.PerForthnight =  self.ui.cboPaymentPeriod.itemText(self.ui.cboPaymentPeriod.currentIndex())
        self.borrower.PreviousEmployer =  self.ui.linePrevOccupation.text()
        self.borrower.PreviousEmployer =  self.ui.linePrevEmployer.text()
        self.borrower.PrevEmpAddress1 =  self.ui.linePrevEmpAddress1.text()
        self.borrower.PrevEmpAddress2 =  self.ui.linePrevEmpAddress2.text()
        self.borrower.PrevEmpAddress3 =  self.ui.linePrevEmpAddress3.text()
        self.borrower.PrevEmpTelNo =  self.ui.linePrevEmpTelNo.text()
        self.borrower.PrevDepartment =  self.ui.linePrevDepartment.text()
        self.borrower.datePrevEmpStartDate=  self.ui.datePrevEmpStartDate.date().toString('%m/%d/%y %H:%M:%S')
        self.borrower.occupation =  self.ui.lineOccupation.text()
        self.borrower.Employer1 =  self.ui.lineEmployer.text()
        self.borrower.addressofemployment =  self.ui.lineEmpAddress1.text()
        #self.borrower.FirstName =  self.ui.lineEmpAddress2.text()
        #self.borrower.FirstName =  self.ui.lineEmpAddress3.text()
        #self.borrower.FirstName =  self.ui.lineEmpTelNo.text()
        #self.borrower.FirstName =  self.ui.lineDepartment.text()
        #self.borrower.FirstName =  self.ui.dateEmpStartDate.text()
        #self.borrower. =  self.ui.lineEditSalaryAmount.text()
        #self.borrower.so =  self.ui.lineSpouseAlias.text()
        #self.borrower.FirstName =  self.ui.cboSpouseSex.text()
        #self.borrower.sp =  self.ui.dateSpouseDOB.text()
        self.borrower.spouse_employment =  self.ui.lineSpouseEmployer.text()
        self.borrower.spouse_emp_address =  self.ui.lineSpouseFullAddress.text()
        self.borrower.nameofspouse =  self.ui.lineSpouseFullName.text()
        self.borrower.SpouseTRN =  self.ui.lineSpouseTRN.text()
        self.borrower.spouse_emp_tel =  self.ui.lineSpouseTelNo.text()

    def validate(self):
        pass

    def setPers(self,db):
        self.db = db
