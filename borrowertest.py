
__author__ = "Romayne Whyte, http://ijasoft.com/"
__version__ = "$Revision: 1.0 $"
__date__ = "$Date: 2019/12/31 $"
__copyright__ = "Copyright 2019 Ijasoft, Inc."

import sys, os
import unittest
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
from casheagle.borrower import BorrowerForm
from datetime import datetime
import unittest.mock
import factory # From "factory_boy"
from db import tables, database

app = QApplication(sys.argv)

class BorrowerTest(unittest.TestCase):
    """[summary]
    """

    class BorrowerFactory(factory.Factory):
        class Meta:
           model = tables.Borrower
        
        FirstName = "Romayne"
        LastName = "Whyte"
        MiddleName = "A"
        TRN= ""
        Alias = ""
        MaritalStatus = ""
        Address1= ""
        Address2 = ""
        Address3 = ""
        PrevAddr = ""
        PrevAddr2= ""
        PrevAddr3 = ""
        Length_reside_prev = ""
        HomeTel = ""
        WorkTel = ""
        digicell = ""
        digicel2 = ""
        Sex = ""
        PerForthnight = ""
        PreviousEmployer = ""
        PreviousEmployer = ""
        PrevEmpAddress1 = ""
        PrevEmpAddress2 = ""
        PrevEmpAddress3 = ""
        PrevEmpTelNo = ""
        PrevDepartment = ""
        datePrevEmpStartDate= ""
        occupation = ""
        Employer1 = ""
        addressofemployment = ""
        #FirstName = ""
        #FirstName = ""
        #FirstName = ""lineEmpTelNo.text()
        #FirstName = ""lineDepartment.text()
        #FirstName = ""dateEmpStartDate.text()
        # = ""lineEditSalaryAmount.text()
        #so = ""lineSpouseAlias.text()
        #FirstName = ""cboSpouseSex.text()
        #sp = ""dateSpouseDOB.text()
        spouse_employment = ""
        spouse_emp_address = ""
        nameofspouse = ""
        SpouseTRN = ""
        spouse_emp_tel = ""
    
    @unittest.mock.patch("database.Borrower")
    def test_that_correct_users_are_returned_from_the_endpoint(self, mocked_view_users):
        borrower1 = self.BorrowerFactory.build(firstname="Romayne",lastname= "Whyte")
        mocked_view_users.query.all.return_value = [user1, user2]

    def setUp(self):
        """Create the GUI
        """
        
        self.form = BorrowerForm()

    def setValues(self):
        """[summary]
        """
        self.form.ui.lineEditFirstName.setText("1")
        self.form.ui.lineEditLastName.setText("")
        self.form.ui.lineEditMiddleInit.setText("")
        self.form.ui.lineEditTRN.setText("")
        self.form.ui.lineAlias.setText("")
        self.form.ui.cboMaritalStatus.setCurrentText("")
        self.form.ui.lineAddress1.setText("")
        self.form.ui.lineAddress2.setText("")
        self.form.ui.lineAddress3.setText("")
        self.form.ui.linePrevAddress1.setText("") 
        self.form.ui.linePrevAddress2.setText("") 
        self.form.ui.linePrevAddress3.setText("")
        self.form.ui.linePrevLengthOfStay.setText("")
        self.form.ui.lineHomeTel.setText("")
        self.form.ui.lineWorkTel.setText("")
        self.form.ui.lineCellNo1.setText("")
        self.form.ui.lineCellNo2.setText("")
        self.form.ui.cbosex.setCurrentText("")
        self.form.ui.cboPaymentPeriod.setCurrentText("")
        self.form.ui.linePrevOccupation.setText("")
        self.form.ui.linePrevEmployer.setText("")
        self.form.ui.linePrevEmpAddress1.setText("")
        self.form.ui.linePrevEmpAddress2.setText("")
        self.form.ui.linePrevEmpAddress3.setText("")
        self.form.ui.linePrevEmpTelNo.setText("")
        self.form.ui.linePrevDepartment.setText("")
        self.form.ui.datePrevEmpStartDate.setDate(datetime.today()) 
        self.form.ui.lineOccupation.setText("")
        self.form.ui.lineEmployer.setText("")
        self.form.ui.lineEmpAddress1.setText("")
        self.form.ui.lineEmpAddress2.setText("")
        self.form.ui.lineEmpAddress3.setText("")
        self.form.ui.lineEmpTelNo.setText("")
        self.form.ui.lineDepartment.setText("")
        self.form.ui.dateEmpStartDate.setDate(datetime.today())
        self.form.ui.lineEditSalaryAmount.setText("")
        self.form.ui.lineSpouseAlias.setText("")
        self.form.ui.cboSpouseSex.setCurrentText("")
        self.form.ui.dateSpouseDOB.setDate(datetime.today())
        self.form.ui.lineSpouseEmployer.setText("")
        self.form.ui.lineSpouseFullAddress.setText("")
        self.form.ui.lineSpouseFullName.setText("")
        self.form.ui.lineSpouseTRN.setText("")
        self.form.ui.lineSpouseTelNo.setText("")

    def test_Add(self):
        self.form.ui.btnApplied.click()
        self.setValues()
        
    def test_Delete(self):
        self.form.ui.btnDelete.click()
        
    def test_Modify(self):
        pass

    @unittest.mock.patch("table.Borrower")
    def test_Save(self):
        self.setValues() 
        self.form.ui.btnSave.click()

if __name__ == '__main__':
    unittest.main()