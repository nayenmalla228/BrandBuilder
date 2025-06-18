from bank import bank
customer1 =bank(1001,"nayen",2000)
print(customer1.checkbalance())
customer1.deposit(2000)
print(customer1.checkbalance())
customer1.withdraw(3500)
print(customer1.checkbalance())