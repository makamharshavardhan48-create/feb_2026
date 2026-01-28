#Name:M harshavardhan
#Date:20-1-2026
#project:Atm

class ATM():
    def __init__(self,location,bank,amount=0):
        self.location=location
        self.bank=bank
        self.amount=amount
    def deposite(self,deposite):
        if deposite<=0:
            print("Amount must be greater than zero")
        else:
            self.amount+=deposite
            print(f"{deposite}amount is deposited")
    def withdraw(self,withdraw):
        if withdraw<=0:
            print("Amount must be greather than zero")
        else:
            self.amount-=withdraw
            print(f"{withdraw}amount is withdraw")
    def checkbalance(self,ACN=6302106117,PIN=6117):
        ACN1=int(input("enter the accountnumber:"))
        pin1=int(input("enter the pin to verify:"))
        if ACN==ACN1 and PIN==pin1:
            print(f"balance is fetched {self.amount}")
        else:
            print("invalid details.")
atm = ATM("ALLAGADDA","SBI",78500)
class ATM2(ATM):
    def ministatment(self):
        pass
while True:
    print("\n ATM MENU")
    print("1, withdraw")
    print("2,deposite")
    print("3,checkbalance")
    print("4,exit")
    
    choice=int(input("enter the number only(1-4):"))
    if choice ==1:
        atm.withdraw(int(input("enter amount for withdraw")))
    elif choice ==2:
        atm.deposite(int(input("enter amount for deposit")))
    elif choice ==3:
        atm.checkbalance()
    elif choice ==4:
        print("Thank You...")
        break
    else:
        print("Invalid choice. please try again.")
        