# guido.make_deposit(100)
# guido.make_deposit(200)
# guido.make_deposit(300)
# guido.make_withdrawal(50)
# guido.display_user_balance()

# this was from the last assignment and it took up a lot of space to repeat the call many times to make a deposit. So lets refactor this
# 
# guido.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(50).display_user_balance()
# 
#  this is called chaining. In order for this to work, each method must return self. By returning self, if we recall how functions work, each method call will now be equal to the instance that called it.


# class User:
    # def make_deposit(self, amount):
    #     # your code goes here...
    #     return self

# the return self statement at the end is what makes this possible.

# you must be aware that the return self statement at the end is only going to return the initial statement. In guido.make_deposit(100) it's going to return "guido" not the value that's being passed through.
