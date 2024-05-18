class BankAccount:
    def __init__(self, account_number, owner, balance=0.0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            fee = amount * 0.01
            self.balance += (amount - fee)
            print(f"Deposited: {amount}, Fee: {fee}, New Balance: {self.balance:.2f}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount > 0 and (amount + amount * 0.01) <= self.balance:
            fee = amount * 0.01
            self.balance -= (amount + fee)
            print(f"Withdrew: {amount}, Fee: {fee}, New Balance: {self.balance:.2f}")
        else:
            print("Invalid withdraw amount or insufficient funds")

    def check_balance(self):
        print(f"Current Balance: {self.balance:.2f}")
        return self.balance

account1 = BankAccount("229922990", "Lion", 8282)
account2 = BankAccount("229922991", "Heck")

account1.deposit(555)
account2.deposit(1001)

account1.withdraw(210)
account2.withdraw(1330)

account1.check_balance()
account2.check_balance()