#Understand the fundamentals of OOP in Python by 
#implementing a BankAccount class that encapsulates banking operations.
#Use command line arguments to interact with instances of this class.

class BankAccount:
    def __init__(self):
        self.account_balance = 0 #Default Attribute Value
    
    def deposit(self, amount):
        amount = float(input("Enter Amount to be Deposited: "))
        self.account_balance += amount
        return self.account_balance

    def withdraw(self, amount):
        amount = float(input("Enter Amount to be Deposited: "))
        self.account_balance -= amount
        return self.account_balance

    def display_balance(self):
        return f"Current Balance: $", {self.account_balance}
    
