x = [[5,2,3], [10,8,9]]
students = [
    {'first_name': 'Michael', 'last_name' : 'Jordan'},
    {'first_name': 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

z = [{'x': 10, 'y': 20}]

def changex(x):
    x[1][0] = 15
    return x

print(changex(x))

def changelast_name(newname):
    students[0]["last_name"] = f"{newname}"
    return students[0]["last_name"]

print(students)

sports_directory['soccer'][0] = 'Andres'
print(sports_directory['soccer'][0])

z[0]['y'] = 30
print(z[0]['y'])

#######################################################################################
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(students):
    for i in range(len(students)):
        print(f"first_name - {students[i]['first_name']}, last_name - {students[i]['last_name']}")
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

iterateDictionary(students)

#######################################################################################

def iterateDictionary2(key_name, some_list):
    # for i in range(len(students)):
    #     print(students[i][f'{key_name}'])
    for some_dict in some_list:
        if key_name in some_dict:
            print(some_dict[key_name])
        else:
            print(f"key name: {key_name} is not found!")

iterateDictionary2('first_name', students)

#######################################################################################
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    # print(len(some_dict) + f" {some_dict}")
    for key in some_dict:
        print(f"{len(some_dict[key])} {key.upper()}")
        for item in some_dict[key]:
            print(item)
        print()

printInfo(dojo)

# I need to realize that I don't need for i in range(len(students)): I can instead use for key in some_dict in order to loop through the entire dictionary and if there is an array (list) inside the key for the dictionary then I can use another for loop to go through the list
