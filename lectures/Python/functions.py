#always two parts to a function
#1 define
def addTwoNums(a, b):
    c = a + b
    print(c)

# 2 call the function or invoke the function
addTwoNums(4, 5)
addTwoNums(45, 786)
addTwoNums(12, 1991)



def orderTacos(money):
    print("I have your tacos!")

my_tacos = orderTacos(15.98)
print(my_tacos)


print("=" * 80)

# Default Parameters
def greet(name = "", repeat = 2):
    print(f"Good Morning {name} " * repeat)

greet()
greet("Jeremi")
greet("Jeremi", 4)
greet(4)

# Named Arguements
greet(repeat = 5)
greet(name = "Tyler")
greet(name = "Jim", 3)
greet(repeat = 3, name = "Jim")