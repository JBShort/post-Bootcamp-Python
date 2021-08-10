for num in range(151):
    print(num)

for num in range(5, 1001, 5):
    print(num)

for num in range(1, 101, 1):
    if(num % 10 == 0):
        print("Coding Dojo")
    elif(num % 5 == 0):
        print("Coding")
    else:
        print(num)


sumvalue = 0

for num in range(500001):
    if(num % 2 != 0):
        sumvalue += num

print(sumvalue)



for num in range(2018, 0, -4):
    print(num)


lowNum = 2
highNum = 9
mult = 3
for num in range(lowNum,highNum+1, 1):
    if(num % mult == 0):
        print(num)

