class ATM:
    def __init__(self, cardNumber, pinNumber):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber
        

    def showCardNumber(self):
        print("hello pls enter your card number "+ self.cardNumber)
    def showpinNumber(self):
        print("Pin number is  ", self.pinNumber)
    def withdrawl(self):
        print("this is the withdrawl function")
    def deposit(self):
        print("this is the depoit function")
    def balanceEnquiry(self):
        print("this is the balance enquiry function")

account1 =ATM("987654321",5216)
account1.showCardNumber()
account1.showPinNumber()
account1.Withdrawl()
account1.desposit()
account1.balanceEnquiry()

account2=ATM(123456789,1234)
account2.showCardNumber()
account2.ShowPinMunber()
account2.withdrawl()
account2.desposit()
account2.balanceEnquiry()