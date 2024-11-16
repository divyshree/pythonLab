""""3. Write a program to define a class to represent a bank account, with methods to deposit, withdraw, 
and check the balance."""
# Answer:
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. Current balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. Current balance: {self.balance}")

    def check_balance(self):
        print(f"Current balance: {self.balance}")

# Create an instance of BankAccount
account = BankAccount()

# Perform operations
account.deposit(1000)
account.withdraw(500)
account.check_balance()