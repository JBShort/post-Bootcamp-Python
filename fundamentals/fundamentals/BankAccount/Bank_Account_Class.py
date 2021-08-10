class Bankaccount:
    bank_name = "Ninja Banking"
    all_accounts = []
    def __init__(self, int_rate = 0.02, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if(self.balance - amount <= 0):
            print("Insufficient funds: Charging a $5 fee")
            amount += 5
        self.balance -= amount
        return self
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    def yield_interest(self):
        if(self.balance > 0):
            self.balance = self.balance + (self.balance * self.int_rate)
        return self
    
    @classmethod
    def print_account_info(cls, user):
        print(f"User Balance: ${user.balance} User Interest Rate: {user.int_rate * 100}%")

account1 = Bankaccount(0.01, 100)
account2 = Bankaccount(0.01, 200)

account1.deposit(300).deposit(300).deposit(300).withdraw(62).yield_interest().display_account_info()

account2.deposit(123).deposit(543).withdraw(76).withdraw(54).withdraw(37).withdraw(18).yield_interest().display_account_info()

Bankaccount.print_account_info(account1)