#polymorphism overrides the data in the child class from the parent class
"""
Task : Bank Account System (Basic Version)
Create a simple bank account system that demonstrates inheritance and polymorphism.
Base Class: BankAccount
Create a BankAccount base class with:
Attributes:

account_number (string)
owner_name (string)
balance (float, starts at 0) """
# Bank account system


class Bankaccount:
    def __init__(self,acc_num,owner_name,balance):
        self.acc_num=acc_num
        self.owner_name=owner_name
        self.balance=0 #balance 0 suruma 
        
    def deposit(self,deposit_amt):
        self.balance+=deposit_amt
    def withdraw(self,withdrawamt):
        if(self.balance<50):
            print("balance is too low")
        else:
            self.balance=self.balance-withdrawamt
            
class SavingAccount(Bankaccount):
    def __init__(self,acc_num,owner_name,balance):
        super().__init__(acc_num,owner_name,balance)
        self.interest_rate=3.0
        
    def calculate_interest(self):
        print(self.balance*self.interest_rate/100)
        
    def checkbalance(self):
        print(f"The total amount in your account is {self.balance}")
        
class checkingaccount(Bankaccount):
    def __init__(self,acc_num,owner_name,balance,overdraft_limit):
        super().__init__(acc_num,owner_name,balance)
        self.overdraft_limit=overdraft_limit
        self.overdraft_limit=200
        
    def withdraw_amt(self,amount):
        if(self.balance+self.overdraft_limit<amount):
            self.balance=self.balance-amount
        else:
            ("amount cannot be withdraw")
            
customer1=SavingAccount(1234,"Ram",2000)
customer1.deposit(5000)
customer1.checkbalance()
customer1.withdraw(3000)
customer1.checkbalance()
customer1.calculate_interest()
    
            
