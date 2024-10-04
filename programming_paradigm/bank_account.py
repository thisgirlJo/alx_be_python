#Understand the fundamentals of OOP in Python by 
#implementing a BankAccount class that encapsulates banking operations.
#Use command line arguments to interact with instances of this class.

class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = 0 #Default Attribute Value
    
    def deposit(self, amount):
        self.account_balance += amount
        return self.account_balance

    def withdraw(self, amount):
        self.account_balance = self.account_balancd - amount
        return self.account_balance

    def display_balance(self):
        print("Current Balance: $",self.account_balance)
        return
    
