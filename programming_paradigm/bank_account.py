#Simple Bank Account Class

class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = 0

    def deposit(self, amount):
        self.account_balance = self.account_balance + amount
        return self.account_balance

    def withdraw(self, amount):
        if self.account_balance >= amount:
            return True
        else:
            return False

    def display_balance(self):
        print("Current Balance: $",self.account_balance)
    
