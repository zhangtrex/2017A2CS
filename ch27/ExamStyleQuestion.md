chapter 27 exam style questions
1.
(a)
BankAccount ---> PersonalAccount
BankAccount ---> SavingsAccount


(b)
```python
class BankAccount(object):
    def __init__(self,n,iban):
        self.AccountHolderName = n;
        self.IBAN = iban;
    def SetAccountHolderName(self,n):
        self.AccountHolderName = n;
    def GetAccountHolderName(self):
        return self.AccountHolderName
    def GetIBAN(self):
        return self.IBAN
```

(c)
(i)
PersonalAccount
Attributes: MonthlyFee OverdrawLimit
Methods: 
SetMonthlyFee() 
SetOverdrawLimit() 
GetMonthlyFee()
GetOverdrawLimit()
Pay()
(ii)
SavingsAccount
Attributes: Balance InterestRate
Methods:
SetBalance()
GetBalance()
SetInterestRate()
GetInterestRate()
Pay()
(iii)
The design is that the class's attributes can be automatically passed into its functions.




2.
a.
SeasonTicketHolder:
TicketHolderEmail: STRING
AddNewHolder()
GetHolderName()
GetHolderEmail()

Pay-As-You-GoTicketHolder:
Account: INTEGER
Price: INTEGER
Constructor()
SetPrice()
GetPrice()
PayFare()
PrintHolderDetails()

ContractTicketHolder:
Account: INTEGER
Fee: INTEGER
SetFee()
GetFee()
PayFee()
PrintHolderDetails()

b.
(i)
Because in that case, attributes can not been modified or called outside the class.
It is easier to debug and ensure data integraty
(ii)
Because functions need to be called outside the class, public methods allows users 
to call functions while they are using.

c.
c = ContractTicketHolder('A. Smith','xyz@abc.xx',10);

3.
a. Containment
b.
```python
class NodeClass(object):
    def __init__(self):
	self.__data = '';
	self.__pointer = -1;
    def SetData(self,d):
	self.__data = d;
    def SetPointer(self,p):
	self.__pointer = p;
    def GetData(self):
	return self.__data
    def GetPointer(self):
	return self.__pointer
```
c.
```python
class QueueClass(object):
    def __init__(self):
	self.__queue = [NodeClass() for i in range(50)];
	self.__head = -1;
	self.__tail = -1;
```
d.











