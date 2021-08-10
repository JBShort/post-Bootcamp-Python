num1 = 42  #variable declaration
num2 = 2.3  #variable declaration
boolean = True  #variable declaration
string = 'Hello World'  #variable declaration
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']  #variable declaration array
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}  #variable declaration object
fruit = ('blueberry', 'strawberry', 'banana')  #variable declaration tuples
print(type(fruit))  #log statement
print(pizza_toppings[1])  #log statement
pizza_toppings.append('Mushrooms')  #log statement
print(person['name'])  #log statement
person['name'] = 'George'  #log statement
person['eye_color'] = 'blue'  #log statement
print(fruit[2])  #log statement

if num1 > 45:   #conditional if
    print("It's greater")
else: #conditional else
    print("It's lower")

if len(string) < 5:  #conditional if
    print("It's a short word!")
elif len(string) > 15: #conditional else if
    print("It's a long word!")
else: #conditional else
    print("Just right!")

for x in range(5):  #for loop and for increment up 5
    print(x)
for x in range(2,5): #for loop and set x = 2 and increment up to 5
    print(x)
for x in range(2,10,3): #for loop and set x = 2 and increment up to 10 by adding 3 each loop
    print(x)
x = 0
while(x < 5): #while loop and set x = 0 and print then increment x by 1
    print(x)
    x += 1

pizza_toppings.pop() #pop a value out of the array 
pizza_toppings.pop(1) #pop index of 1 out of the array

print(person) #log statement
person.pop('eye_color') #pop eye color out of the array
print(person) # log statement

for topping in pizza_toppings: #for loop incrementing through an array called "pizza_toppings" and setting each if statement to evaluate each section of the array and if topping == pepperoni to continue through the array but if topping == olives then it breaks the for loop
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times(): #def = function. Here we are creating our own function
    for num in range(10): #for loop 
        print('Hello') # log statement

print_hello_ten_times() #calling the function

def print_hello_x_times(x): # defining another function
    for num in range(x): #for loop
        print('Hello')# log statement

print_hello_x_times(4) #calling the function and passing 4

def print_hello_x_or_ten_times(x = 10): #define function and setting x = 10
    for num in range(x): #for loop
        print('Hello')

print_hello_x_or_ten_times() #calling the function
print_hello_x_or_ten_times(4) #calling the function and passing 4


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)