username = input("Whats your first name? ")

if(username == "Jeremi"):
    print("Hey, that's my name too!")

store10 = []

for num in range(10):
    tempname = input("What's your first name? ")
    store10.append(tempname)

print(store10)
print("it was nice to meet all of you!")

new10 = []
for num in range(10):
    tempname = input("What's your first name? ")
    for num2 in range(10):
        if(tempname == store10[num2]):
            print("That name was already given")
            tempname = input("Please give a new name ")
    print(f"Hello {tempname}")
    new10.append(tempname)

print(new10)