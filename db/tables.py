from sqlalchemy import Table, Sequence, MetaData,create_engine, Column, Integer, String 
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Borrower(Base):
    __tablename__ = 'tblborrowers'
    id = Column(Integer, Sequence('borrowers_id_seq'), primary_key=True)
    appid = Column(String)
    ApplicationDate = Column(String)
    FirstName = Column(String)
    LastName = Column(String)
    MiddleName = Column(String)
    Alias = Column(String)
    Sex = Column(String)
    MaritalStatus = Column(String)
    Age = Column(String)
    Address = Column(String)
    Length_reside = Column(String)
    PrevAddr = Column(String)
    PrevAddr2 = Column(String)
    PrevAddr3 = Column(String)
    Length_reside_prev = Column(String)
    HomeTel = Column(String)
    WorkTel = Column(String)
    OwnHome = Column(String)
    Rent = Column(String)
    Amt_Rent = Column(String)
    Other = Column(String)
    Morgage_monthly = Column(String)
    occupation = Column(String)
    nameofemployer = Column(String)
    EmpAddress1 = Column(String)
    EmpAddress2 = Column(String)
    EmpAddress3 = Column(String)
    EmpStartDate  = Column(String)
    Department = Column(String)
    PrevEmpAddress1 = Column(String)
    PrevEmpAddress2 = Column(String)
    PrevEmpAddress3 = Column(String)
    PrevEmpStartDate = Column(String)
    Extension = Column(String)
    PostionHeld = Column(String)
    PaymentPeriod = Column(String)
    PreviousEmployer = Column(String)
    otherIncomeSource = Column(String)
    nameofspouse = Column(String)
    addressofspouse = Column(String)
    spouse_employment = Column(String)
    spouse_emp_address = Column(String)
    spouse_emp_tel = Column(String)
    SpouseAlias = Column(String)
    SpouseTRN = Column(String)
    SpouseDOB = Column(String)
    Dependent = Column(String)
    LoanAmtNeed = Column(String)
    PurposeOfLoan = Column(String)
    DurationOfLoan = Column(String)
    ReturningCustomer = Column(String)
    YesAmount = Column(String)
    OutstandingDebtName = Column(String)
    OutstandingDebtAmount = Column(String)
    SalaryAmount = Column(String)
    ProcessDate = Column(String)
    Name1 = Column(String)
    Address1 = Column(String)
    WorkNum1 = Column(String)
    HomeNum1 = Column(String)
    Relations1 = Column(String)
    Name2 = Column(String)
    Address2 = Column(String)
    WorkNum2 = Column(String)
    HomeNum2 = Column(String)
    Relations2 = Column(String)
    Employer2 = Column(String)
    Name3 = Column(String)
    Address3 = Column(String)
    WorkNum3 = Column(String)
    HomeNum3 = Column(String)
    Relation3 = Column(String)
    Employer3 = Column(String)
    Name4 = Column(String)
    Address4 = Column(String)
    WorkNum4 = Column(String)
    HomeNum4 = Column(String)
    Relations4 = Column(String)
    Employer4 = Column(String)
    Employer1 = Column(String)
    Picture = Column(String)
    incomeid = Column(String)
    filename = Column(String)
    Comment = Column(String)
    TRN = Column(String)
    digicell = Column(String)
    digicel2 = Column(String)
    branch= Column(String)
    branchname = Column(String)
    stamp = Column(String)
    validateby = Column(String)
    validatedate = Column(String)

class Guarantors(Base):
    __tablename__ = 'tblGuarantors'
    id = Column(Integer, Sequence('guarantors_id_seq'), primary_key=True)
    appid = Column(String)
    ApplicationDate = Column(String)
    FirstName = Column(String)
    LastName = Column(String)
    MiddleName = Column(String)
    Alias = Column(String)
    Sex = Column(String)
    MaritalStatus = Column(String)
    Age = Column(String)
    Address = Column(String)
    Length_reside = Column(String)
    PrevAddr = Column(String)
    PrevAddr2 = Column(String)
    PrevAddr3 = Column(String)
    Length_reside_prev = Column(String)
    HomeTel = Column(String)
    WorkTel = Column(String)
    OwnHome = Column(String)
    Rent = Column(String)
    Amt_Rent = Column(String)
    Other = Column(String)
    Morgage_monthly = Column(String)
    occupation = Column(String)
    nameofemployer = Column(String)
    EmpAddress1 = Column(String)
    EmpAddress2 = Column(String)
    EmpAddress3 = Column(String)
    EmpStartDate  = Column(String)
    Department = Column(String)
    PrevEmpAddress1 = Column(String)
    PrevEmpAddress2 = Column(String)
    PrevEmpAddress3 = Column(String)
    PrevEmpStartDate = Column(String)
    Extension = Column(String)
    PostionHeld = Column(String)
    PaymentPeriod = Column(String)
    PreviousEmployer = Column(String)
    otherIncomeSource = Column(String)
    nameofspouse = Column(String)
    addressofspouse = Column(String)
    spouse_employment = Column(String)
    spouse_emp_address = Column(String)
    spouse_emp_tel = Column(String)
    SpouseAlias = Column(String)
    SpouseTRN = Column(String)
    SpouseDOB = Column(String)
    Dependent = Column(String)
    LoanAmtNeed = Column(String)
    PurposeOfLoan = Column(String)
    DurationOfLoan = Column(String)
    ReturningCustomer = Column(String)
    YesAmount = Column(String)
    OutstandingDebtName = Column(String)
    OutstandingDebtAmount = Column(String)
    SalaryAmount = Column(String)
    ProcessDate = Column(String)
    Name1 = Column(String)
    Address1 = Column(String)
    WorkNum1 = Column(String)
    HomeNum1 = Column(String)
    Relations1 = Column(String)
    Name2 = Column(String)
    Address2 = Column(String)
    WorkNum2 = Column(String)
    HomeNum2 = Column(String)
    Relations2 = Column(String)
    Employer2 = Column(String)
    Name3 = Column(String)
    Address3 = Column(String)
    WorkNum3 = Column(String)
    HomeNum3 = Column(String)
    Relation3 = Column(String)
    Employer3 = Column(String)
    Name4 = Column(String)
    Address4 = Column(String)
    WorkNum4 = Column(String)
    HomeNum4 = Column(String)
    Relations4 = Column(String)
    Employer4 = Column(String)
    Employer1 = Column(String)
    Picture = Column(String)
    incomeid = Column(String)
    filename = Column(String)
    Comment = Column(String)
    TRN = Column(String)
    digicell = Column(String)
    digicel2 = Column(String)
    branch= Column(String)
    branchname = Column(String)
    stamp = Column(String)
    validateby = Column(String)
    validatedate = Column(String)