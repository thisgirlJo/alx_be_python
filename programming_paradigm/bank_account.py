class BankAccount:
    def __init__(self, account_balance, deposit, withdraw, display_balance):
        self.account_balance = 0
        self.deposit = deposit
        self.withdraw = withdraw
        self.display_balance = display_balance
    
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
    