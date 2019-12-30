from PyQt5.QtWidgets import QMdiSubWindow, QWidget
from casheagle.ui.borrower_ui import *
from db import models 
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


    def applied(self):
        """Allow information to be added to the fields
        """
        self.BorrowerTextfieldState(True)
        self.clear()
        self.buttonstate(True)

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
        self.ui.linePrevAddress1.setEnabled(state)
        self.ui.linePrevAddress2.setEnabled(state)
        self.ui.linePrevAddress3.setEnabled(state)
        self.ui.linePrevLengthOfStay.setEnabled(state)
        self.ui.lineHomeTel.setEnabled(state)
        self.ui.lineWorkTel.setEnabled(state)
        self.ui.lineCellNo1.setEnabled(state)
        self.ui.lineCellNo2.setEnabled(state)
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


    def buttonstate(self, state):
        self.ui.btnApplied.setEnabled(not state)
        #self.ui.btnDelete.setEnabled(not state)
        #self.ui.btnEdit.setEnabled(not state)
        self.ui.btnFind.setEnabled(not state)
        self.ui.btnSave.setEnabled(state)



    def edit(self):
        self.BorrowerlineState(True)

    def clear(self):
        self.ui.lineEditFirstName.setText("")
        self.ui.lineEditLastName.setText("")
        self.ui.lineEditMiddleInit.setText("")
        self.ui.lineAddress1.setText("")
        self.ui.lineAddress2.setText("")
        self.ui.lineAddress3.setText("")
        self.ui.lineLengthOfStay.setText("")
        self.ui.lineHomeTel.setText("")
        self.ui.lineWorkTel.setText("")
        self.ui.lineCellNo1.setText("")
        self.ui.lineCellNo1_2.setText("")
        self.ui.lineEditFirstName.setFocus()

    def setValues(self):
        borrower = models.Borrower()
        borrower.FirstName =  self.ui.lineEditFirstName.text()
        borrower.LastName =  self.ui.lineEditLastName.text()
        borrower.MiddleName =  self.ui.lineEditMiddleInit.text()
        borrower.TRN=  self.ui.lineEditTRN.text()
        borrower.Alias =  self.ui.lineAlias.text()
        borrower.MaritalStatus =  self.ui.cboMaritalStatus.text()
        borrower.Address1=  self.ui.lineAddress1.text()
        borrower.Address2 =  self.ui.lineAddress2.text()
        borrower.Address3 =  self.ui.lineAddress3.text()
        borrower.PrevAddr =  self.ui.linePrevAddress1.text() 
        #borrower.PrevAddr2= self.ui.linePrevAddress2.text() 
        #borrower.PrevAddr3 = self.ui.linePrevAddress3.text()
        borrower.Length_reside_prev =  self.ui.linePrevLengthOfStay.text()
        borrower.HomeTel =  self.ui.lineHomeTel.text()
        borrower.WorkTel =  self.ui.lineWorkTel.text()
        borrower.digicell =  self.ui.lineCellNo1.text()
        #borrower.digicel2 =  self.ui.lineCellNo2.text()
        borrower.Sex =  self.ui.cbosex.itemText(self.ui.cbosex.currentIndex())
        borrower.PerForthnight =  self.ui.cboPaymentPeriod.itemText(self.ui.cboPaymentPeriod.currentIndex())
        #borrower.PreviousEmployer =  self.ui.linePrevOccupation.text()
        borrower.PreviousEmployer =  self.ui.linePrevEmployer.text()
        #borrower.em =  self.ui.linePrevEmpAddress1.text()
        #borrower.PrevAddr =  self.ui.linePrevEmpAddress2.text()
        #borrower.FirstName =  self.ui.linePrevEmpAddress3.text()
        borrower.Extension =  self.ui.linePrevEmpTelNo.text()
        borrower.Department =  self.ui.linePrevDepartment.text()
        #borrower.dat =  self.ui.datePrevEmpStartDate.text()
        borrower.occupation =  self.ui.lineOccupation.text()
        borrower.Employer1 =  self.ui.lineEmployer.text()
        borrower.addressofemployment =  self.ui.lineEmpAddress1.text()
        #borrower.FirstName =  self.ui.lineEmpAddress2.text()
        #borrower.FirstName =  self.ui.lineEmpAddress3.text()
        #borrower.FirstName =  self.ui.lineEmpTelNo.text()
        #borrower.FirstName =  self.ui.lineDepartment.text()
        #borrower.FirstName =  self.ui.dateEmpStartDate.text()
        #borrower. =  self.ui.lineEditSalaryAmount.text()
        #borrower.so =  self.ui.lineSpouseAlias.text()
        #borrower.FirstName =  self.ui.cboSpouseSex.text()
        #borrower.sp =  self.ui.dateSpouseDOB.text()
        borrower.spouse_employment =  self.ui.lineSpouseEmployer.text()
        borrower.spouse_emp_address =  self.ui.lineSpouseFullAddress.text()
        borrower.nameofspouse =  self.ui.lineSpouseFullName.text()
        #borrower.s =  self.ui.lineSpouseTRN.text()
        borrower.spouse_emp_tel =  self.ui.lineSpouseTelNo.text()


    def setPers(self,db):
        self.db = db

    
