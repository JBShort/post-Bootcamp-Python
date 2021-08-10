# create a class and make instances from it
# practice accessing the methods and attributes of different instances

class User():
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
    def make_deposit(self, amount):
        print(f"You have deposited ${amount} into your account.")
        self.amount += amount
        return self
    def make_withdrawal(self, amount):
        self.amount -= amount
        print(f"You have withdrew ${amount} from your account.")
        return self
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.amount}")
        return self
    def transfer_money(self, other_user, amount):
        self.amount -= amount
        other_user.amount += amount
        print(f"First user: {self.name} Balance: ${self.amount} Second user: {other_user.name} Balance: ${other_user.amount}")

user1 = User("Jeremi", 0)
user2 = User("Tom", 0)
user3 = User("Bob", 0)

user1.make_deposit(1000).make_deposit(1000).make_deposit(1000).make_withdrawal(239).display_user_balance()

user2.make_deposit(5345).make_deposit(5345).make_withdrawal(987).make_withdrawal(987).display_user_balance()

user3.make_deposit(901234).make_withdrawal(892).make_withdrawal(8921).make_withdrawal(89254).display_user_balance()

user1.transfer_money(user3, 2500)