import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import unittest
from datetime import datetime
import unittest.mock
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
from ui_action.action import borrower
import factories
from db import tables
import logging

logger = logging.getLogger(__name__)

app = QApplication(sys.argv)

class BorrowerTest(unittest.TestCase):
    """[summary]
    Arguments:
        unittest {[type]} -- [description]
    """

    def setUp(self):
        """Create the GUI
        """
        self.session = factories.db.session
        factories.db.reset()
        self.form = borrower.BorrowerForm(factories.db)

    def setfields(self):
        self.borrower = factories.BorrowerFactory.build()
        self.form.ui.lineID.setText(str(self.borrower.id) if self.borrower.id else '')
        self.form.ui.lineEditFirstName.setText(self.borrower.FirstName)
        self.form.ui.lineEditLastName.setText(self.borrower.LastName)
        self.form.ui.lineEditMiddleInit.setText(self.borrower.MiddleName)
        self.form.ui.lineEditTRN.setText(self.borrower.TRN)
        self.form.ui.lineAlias.setText(self.borrower.Alias)
        self.form.ui.cboMaritalStatus.setCurrentText(self.borrower.MaritalStatus)
        self.form.ui.lineAddress1.setText(self.borrower.Address1)
        self.form.ui.lineAddress2.setText(self.borrower.Address2)
        self.form.ui.lineAddress3.setText(self.borrower.Address3)
        self.form.ui.linePrevAddress1.setText(self.borrower.PrevAddr)
        self.form.ui.linePrevAddress2.setText(self.borrower.PrevAddr2)
        self.form.ui.linePrevAddress3.setText(self.borrower.PrevAddr3)
        self.form.ui.linePrevLengthOfStay.setText(self.borrower.Length_reside_prev)
        self.form.ui.lineHomeTel.setText(self.borrower.HomeTel)
        self.form.ui.lineWorkTel.setText(self.borrower.WorkTel)
        self.form.ui.lineCellNo1.setText(self.borrower.digicell)
        self.form.ui.lineCellNo2.setText(self.borrower.digicel2)
        self.form.ui.cbosex.setCurrentText(self.borrower.Sex)
        self.form.ui.cboPaymentPeriod.setCurrentText(self.borrower.PaymentPeriod)
        self.form.ui.linePrevOccupation.setText(self.borrower.PreviousEmployer)
        self.form.ui.linePrevEmployer.setText(self.borrower.PreviousEmployer)
        self.form.ui.linePrevEmpAddress1.setText(self.borrower.PrevEmpAddress1)
        self.form.ui.linePrevEmpAddress2.setText(self.borrower.PrevEmpAddress2)
        self.form.ui.linePrevEmpAddress3.setText(self.borrower.PrevEmpAddress3)
        self.form.ui.datePrevEmpStartDate.setDate(self.borrower.PrevEmpStartDate)
        self.form.ui.linePrevEmpTelNo.setText(self.borrower.Extension)
        self.form.ui.linePrevDepartment.setText(self.borrower.Department)
        self.form.ui.dateDOB.setDate(self.borrower.DOB)
        self.form.ui.lineOccupation.setText(self.borrower.occupation)
        self.form.ui.lineEmployer.setText(self.borrower.Employer1)
        self.form.ui.lineEmpAddress1.setText(self.borrower.EmpAddress1)
        self.form.ui.lineEmpAddress2.setText(self.borrower.EmpAddress2)
        self.form.ui.lineEmpAddress3.setText(self.borrower.EmpAddress3)
        self.form.ui.lineEmpTelNo.setText(self.borrower.EmpAddress3)
        self.form.ui.lineDepartment.setText(self.borrower.Department)
        self.form.ui.dateEmpStartDate.setDate(self.borrower.EmpStartDate)
        self.form.ui.lineEditSalaryAmount.setText(self.borrower.SalaryAmount)
        self.form.ui.lineSpouseEmployer.setText(self.borrower.spouse_employment)
        self.form.ui.lineSpouseFullAddress.setText(self.borrower.spouse_emp_address)
        self.form.ui.lineSpouseFullName.setText(self.borrower.nameofspouse)
        self.form.ui.lineSpouseTRN.setText(self.borrower.SpouseTRN)
        self.form.ui.lineSpouseTelNo.setText(self.borrower.spouse_emp_tel)
        self.form.ui.lineSpouseAlias.setText(self.borrower.SpouseAlias)
        #self.form.ui.dateSpouseDOB.setDate(date.fromisoformat(self.borrower.SpouseDOB) if self.borrower.SpouseDOB else date.today())

    def getfields(self):
        """[summary]
        """
        pass

    def test_something(self):
        """[summary]
        """
        borrower = factories.BorrowerFactory()
        self.assertEqual([borrower], self.session.query(tables.Borrower).all())

    def test_appliedButton(self):
        """[summary]
        """
        self.form.ui.btnApplied.click()
        self.assertEqual(self.form.ui.lineEditGFirstName.text(), "")

    def test_editButton(self):
        """[summary]
        """
        self.setfields()
        testvalue = self.form.ui.lineEditFirstName.text()
        self.form.ui.btnEdit.click()
        self.assertEqual(self.form.ui.lineEditFirstName.text(), testvalue)

    def test_saveButton(self):
        """[summary]
        """
        self.form.ui.btnApplied.click()
        self.setfields()
        testvalue = self.form.ui.lineEditFirstName.text()
        self.form.ui.btnSave.click()
        borrower = self.session.query(tables.Borrower).all()
        #its not empty
        self.assertTrue(borrower)
        #record was actually saved
        self.assertEqual(borrower[0].FirstName,testvalue)


    def test_FindButton(self):
        """[summary]
        """
        isvisible = self.form.ui.dockWidgetFindBorrower.isVisible()
        self.form.ui.btnFind.click()
        self.assertEqual(isvisible,self.form.ui.dockWidgetFindBorrower.isVisible())


    def test_CancelButton(self):
        """[summary]
        """
        self.form.ui.btnApplied.click()
        self.setfields()
        self.form.ui.btnCancel.click()
        self.assertEqual(self.form.ui.lineEditFirstName.isEnabled(),False)


    def test_DeleteButton(self):
        """[summary]
        """
        self.form.ui.btnApplied.click()
        self.setfields()
        self.form.ui.btnSave.click()
        self.form.ui.btnDelete.click()
        borrower = self.session.query(tables.Borrower).all()

        self.assertFalse(borrower) #After deletion data list should be empty

    def test_SearchButton(self):
        """[summary]
        """
        borrower = factories.BorrowerFactory()
        self.form.ui.txtFind.setText(borrower.FirstName)
        self.form.ui.tblFindList.selectRow(0)
        row = self.form.ui.tblFindList.currentRow()

        testvalue = self.form.ui.tblFindList.item(r,0).text()
        self.assertEqual(testvalue,borrower.FirstName) #Test if first row was selected 

        testvalue = self.form.ui.lineEditFirstName.text()
        self.assertEqual(testvalue,borrower.FirstName) # Tested for 


    def test_validation(self):
        """[summary]
        """
        pass

    def tearDown(self):
        """[summary]
        """
        # Rollback the session => no changes to the database
        self.session.rollback()
        # Remove it, so that the next test gets a new Session()
        factories.db.Session.remove()


if __name__=="__main__":
    suite = unittest.TestSuite()
    if len(sys.argv) == 1:
        suite = unittest.TestLoader().loadTestsFromTestCase(BorrowerTest)
    else:
        for test_name in sys.argv[1:]:
            suite.addTest(BorrowerTest(test_name))

    unittest.TextTestRunner(verbosity=2).run(suite)
