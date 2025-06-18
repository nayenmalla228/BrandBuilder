#Create a bank account class with:
#attribute: account number,account holder name,balance
# methods: deposit,withdraw,checkbalance
class bank:
    def __init__(self,accNum,accName,balance):
     self.accName=accName
     self.accNum=accNum
     self.balance=balance
     
    def checkbalance(self):
         return self.balance
    def deposit(self,depositamt):
          self.balance=depositamt+self.balance
    def withdraw(self,withdrawamt):
          self.balance=self.balance - withdrawamt
     


    