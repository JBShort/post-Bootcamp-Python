# NAMING CONVENTION FOR CLASS NAMES
# Should be Pascal Case    - every word is capitalized
# class names should always be singular, NOT plural

# how does python tell the difference between a variable and a function
# the parentheses
# def clean_up_poop():
#     pass
# dog = "Vicky"
# clean_up_poop()

# def bank_account():
#     pass

# class bankAccount:
#     pass

# bank_account()
# bankAccount()

# FOLLOW PROPER NAMING CONVENTIONS FOR CLASSES AND FUNCTIONS so that when we look at the code we will know without having to look through it and search for when it was defined



class BankAccount:
    # Class Variables = belong to the class and not any specific object
    bank_name = "Bank of Ninjas"
    all_accounts = []
    def __init__(self, int_rate = 0.2, balance = 0):
        # here are the attributes that belond to a single method
        self.int_rate = int_rate
        self.balance = balance
        # we need to add accounts in the constructor to make the all_balances function work
        BankAccount.all_accounts.append(self)

    # these are called INSTANCE METHODS - belong to the individual object (we talking about the specific instance that are calling these methods. There are others however)   
    # belongs to each individual object 
    def withdraw(self, amount):
        if BankAccount.can_withdraw(self.balance, amount):
            self.balance -= amount
        else:
            print("Insufficient funds.")

    def deposit(self, amount):
        self.balance += amount

    # CLASS METHOD - belong to the class itself. 
    @classmethod
    def change_bank_name(cls, name):
        # cls is a variable that holds the entire class itself
        cls.bank_name = name

    @classmethod
    def all_balances(cls):
        sum = 0
        for account in cls.all_accounts:
            sum += account.balance
        return sum
    
    # STATIC METHOD - belongs to nothing. They are a stand alone method in a class. they do NOT have access to either instance or class attributes
    # a static method is like a function that is bare and outside of a class.
    # we put it in the class so that it helps us organize our code when it deals with the banking stuff. It may not work with the objects or class itself. but if it has some associate with the class then it'll go inside the class in order to keep our code organized
    @staticmethod
    def can_withdraw(balance, amount):
        if(balance - amount) < 0:
            return False
        else:
            return True
        # this can function can be called elsewhere in the User

BankAccount.change_bank_name("Popcorn Bank")


# ASSOCIATION BETWEEN CLASSES
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount()
        self.accounts = []
        # this is the IMPORTANT connection (link) between the above class and this class
        # we do this so that they can be linked together and we can just call different functions that do these things. We don't want to be repeating code too often. It helps you save time and be more efficient in your coding
    def withdraw(self, amount):
        self.account.withdraw(amount)
    def deposit(self, amount):
        self.account.deposit(amount)

user1 = User("Shawn", "shawn@email.com")
user2 = User("Jim", "jim@email.com")

user1.account.balance
user1.account.int_rate
user1.account.withdraw

# what this is doing is allowing you to access the account balance int rate and withdraw functions through just the user1 in class User



# FOUR PILLARS of OOP

#  it's located in the learning platform. But basically it should be 