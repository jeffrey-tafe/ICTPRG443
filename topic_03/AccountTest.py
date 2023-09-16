from Account import Account

print("Test account creation")
ac = Account(1122, 20000, 4.5)
print(ac)

print("Test withdraw 2500")
ac.withdraw(2500)
print(ac)

print("Test deposit 3000")
ac.deposit(3000)
print(ac)
