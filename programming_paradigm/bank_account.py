#Simple Bank Account Class

class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = account_balance #Default Attribute Value
    
    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance = self.account_balance - amount
            return self.account_balance
        else:
            return self.account_balance

    def display_balance(self):
        print("Current Balance: $",self.account_balance)
    
