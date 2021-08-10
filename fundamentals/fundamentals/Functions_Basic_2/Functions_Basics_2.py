# Problem 1

def countdown(num):
    newarr = []
    for count in range(num, 0, -1):
        newarr.append(count)
    return newarr

print(countdown(10))


# Problem 2

def print_and_return(arr):
    print(arr[0])
    return arr[1]

print(print_and_return([1,2]))

# Problem 3

def first_plus_length(arr):
    tempval = arr[0] + arr.first_plus_length
    return tempval

print(first_plus_length([1,2,3,4,5,6]))

# problem 4

def values_greater_than_second(arr):
    newarr = []
    arrsum = 0
    if(len(arr) < 2):
        return False
    for i in range(len(arr)):
        if(arr[i] > arr[1]):
            arrsum += 1
            newarr.append(arr[i])
    print(arrsum)
    return newarr

print(values_greater_than_second([3]))

# problem 5

def length_and_value(size, value):
    newarr = []
    for i in range(size):
        newarr.append(value)
    return newarr

print(length_and_value(6,2))