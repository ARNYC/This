'''
class Bankacct:
    def __init__(self, customer_id,acct_no, acct_type ="Savings"):
        self.customer_id = customer_id
        self.acct_no = acct_no
        self.acct_type =acct_type
        self.customer_name = []
        self.beginning_bal = 0.0
        self.credit = 0.0
        self.debit = 0.0
    
    def setCustomer_name(self, customer_name):
        self.customer_name = customer_name

    def enter_debit(self, d_amt):
        self.debit = d_amt

    def enter_credit(self, c_amt):
        self.credit = c_amt

    def get_endingBal(self):
        self.ending_bal = (self.beginning_bal + self.credit - self.debit )
        return self.ending_bal

    def show_acctinfo(self):
        print("Acct no:" + self.acct_no, "Acct Type = " + self.acct_type, "Beg Bal = "+str(self.beginning_bal), 
              "Deposits = "+str(self.credit),"Withdrawals = "+str(self.debit), 
              "Ending Bal = "+str(self.get_endingBal()), sep = '\n')

newCustId = '2348'
new_acct_no ='366425683655'

newcust = Bankacct (newCustId,new_acct_no, acct_type ="Savings")

credit_amt = int(input('Enter a Deposit amount: '))
newcust.enter_credit (credit_amt)

debit_amt = int(input('Enter a withdrawal amount: '))
newcust.enter_debit (debit_amt)

newcust.show_acctinfo()

#-------------------------------------------------------------------------
'''
'''
class Employee:
    def __init__(self,empId):
        self.empId = empId
        self. empName = None
        self.empDept = None
        self.empTitle =''
        self.empSalary = 0

    def setEmpName(self, name):
        self.empName = name

    def setEmpDept (self, dept):
        self.empDept = dept

    def setEmpTitle (self, title):
        self.empTitle = title

    def setEmpSalary (self, salary):
        self.empSalary = salary

    def getEmpSalary (self):
         return (self.empSalary)
    
    def empPrintInfo(self):
        print(self.empId, self.empName, self.empTitle, self.empDept)
 


emp1 = Employee(1001)
emp1.setEmpName("Trump")
emp1.empPrintInfo()
emp1.setEmpSalary(5000)
empSal = emp1.getEmpSalary()
print(empSal)
'''
'''
class Book:
    def __init__(self, title):
        self.title = title
        self.authors = []
        self.price = 0.00

    def setAuthors(self, authors):
        self.authors.extend(authors)

    def setPrice(self, price):
        self.price = price

    def printInfo(self):
        print(self.title, self.authors, self.price)

book1 = Book("This book")
book1.setAuthors(['Arun', 'Tom'])
book1. setPrice(200)
book1.printInfo()
'''
'''
#Comment: The way I did the calc perimeter with print statement first and then return statement 
# came up as an after thought, to fix 'None' Values printed for area and perimeter when I ran
# printinfo. Maybe this is not the best way it needs to be done.

class Rectangle:

    def __init__(self, length, width):
        self. length = length
        self.width = width

    def calcArea(self):
        print("Area of Rectangle:", self.length * self.width)
        return(self.length * self.width)

    def calcPerimeter(self):
        print("Perimeter of Rectangle:",2*(self.length + self.width))
        return(2*(self.length + self.width))

    def printInfo(self):
        print('Length:'+str(self.length), 'Width:'+str(self.width), 'Area:'+str(self.calcArea()),'Perimeter:'+str(self.calcPerimeter()),sep='\n')
        
rec1 = Rectangle(4,3)
rec1.calcArea()
rec1.calcPerimeter()
rec1.printInfo()

'''

 






    
