# What is OOP?
    # OBJECT ORIENTED PROGRAMMING
        # Paradigm - other ones like Functional or Procedural Programming
        # it's a way to think about how we use data in our application
        # in OOP we think of data FIRST, then the functions that need to be done with it
        # objects are the combination of data and functions to manipulate and display the things we need to do with the data

# WHY use OOP?
    # 1. Organization. Easier to organize our code
    # 2. Modular. we can use the same piece of code in multiple different areas.
    # 3. Efficiency
    # 4. Models real life things. It helps us to model things we are working with in real life


# The Hard Way
dog1 = {
    "name": "Vicky",
    "age": 3,
    "hair_color": "brown and white"
}

dog2 = {
    "name": "Leia",
    "age": 0,
    "hair_color": "red and white"
}

dog3 = {
    "name": "Shiro",
    "age": 9,
    "hair_color": "dirty white"
}

# The Better Way
    # Class
    # Class = how we make our custom data type
        # it's a blueprint or model 
        # we create instances of a class, Aka objects

# class Dog:
#     pass

# instantiating = making an instance of the class dog or (basically a dog object)
# dog1 = Dog()
# print(dog1)

class Dog:
    # the def init is called the CONSTRUCTOR
    def __init__(self, name, age, hair_color):
        # this needs attributes - the actual data thats part of the object
        self.name = name
        self.age = age
        self.hair_color = hair_color
        # what we are doign here is passing the arguments from the parameters that are being sent from the variables below
        
        # Method - a function that is a part of a class
    def bark(self):
        print(f"BARK BARK my name is {self.name}!")

    def eat_treats(self, num_of_treats):
        print(f"BARK BARK THANK YOU FOR THE {num_of_treats} TREATS!")
    # self needs to be in front and IN THE PARENTHESES ALWAYS NO MATTER THE OTHER PARAMETERS when using a class. it helps to keep passing the same attributes in the constructor

# implicit passing of self. meaning we don't actually state anything but whenever we call the class method it automatically passes the class attributes through self
# self is just a reference to the OBJECT THAT CALLED IT so when you pass self it has access to it's attributes from inside of the methods (functions)
# through self I have access to the attributes inside of the method
dog1 = Dog("Vicky", 3, "browna nd white")
print(dog1.name)
print(dog1.age)
print(dog1.hair_color)

dog2 = Dog("Leia", 0, "red and white")
print(dog1.name)
print(dog1.age)
print(dog1.hair_color)
dog3 = Dog("Shiro", 9, "dirty white")
print(dog1.name)
print(dog2.name)
print(dog3.name)

dog1.bark()
dog2.bark()
dog3.bark()
dog1.eat_treats(3)