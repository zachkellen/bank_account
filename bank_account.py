class BankAccount:
    # don't forget to add some default values for these parameters!
    accounts = []
    def __init__(self, int_rate, balance = 0): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if (self.balance > amount):
            self.balance -= amount
        else:
            self.balance -= 5
            print("Insufficient funds: Carging a $5 fee")
        return self
    def display_account_info(self):
        print(f"Balance: {self.balance}")
    def yield_interest(self):
        if (self.balance > 0):
            self.balance *= (self.int_rate + 1)
        return self
    @classmethod
    def get_all_info(cls):
        for account in cls.accounts:
            print(f"Your interest rate is: {account.int_rate} Your balance is: {account.balance}")


account1 = BankAccount(.01, 1000)
account2 = BankAccount(.02, 10000)

account1.deposit(500).deposit(500).deposit(100).yield_interest().display_account_info()
account2.deposit(1000).deposit(750).withdraw(150).withdraw(100).withdraw(250).withdraw(500).yield_interest().display_account_info()

BankAccount.get_all_info()