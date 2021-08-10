class Bankaccount:
    bank_name = "Ninja Banking"
    all_accounts = []
    def __init__(self, int_rate, balance):
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


# User has been updated
class User():
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = Bankaccount(int_rate=0.02, balance=0)
    def make_deposit(self, amount):
        print(f"You have deposited ${amount} into your account.")
        self.account.balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account.balance -= amount
        print(f"You have withdrew ${amount} from your account.")
        return self
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account.balance}")
        return self
    # cut out the transfer money function since it's not part of this assignment
    # def transfer_money(self, other_user, amount):
    #     self.amount -= amount
    #     other_user.amount += amount
    #     print(f"First user: {self.name} Balance: ${self.amount} Second user: {other_user.name} Balance: ${other_user.amount}")