# so we're gonna need 3 keys and 3 lists for sure. One for each subject (Math, Science and History)
# another key for the grade that they have.
# another key for the name of the student
# need a loop to go through the process of adding a student
# in the beginning ask if you need to add another student and use that yes answer to lead to the next statement of inputting their name grade and class

nameAndGrade = {
    "Name": [],
    "Grade": [],
    "Class": []
    }
schoolclass = ["Math", "Science", "History"]

def addStudent(numStudents):
    for num in range(numStudents):
        check = False
        while(check == False):
            tempcheck = input("Students Name: ")
            tempcheck = (int)tempcheck
            if(isinstance(tempcheck, str) == True ):
                nameAndGrade["Name"].append(tempcheck)
                check = True
            else:
                print("Invalid name, try again....")
        check = False
        while(check == False):
            tempcheck = int(input("Students Grade: "))
            if(isinstance(tempcheck, str) == False):
                nameAndGrade["Grade"].append(tempcheck)
                check = True
            else:
                print("Invalid grade, try again....")
        check = False
        while(check == False):
            tempclass = int(input("Select a Course: 1 - Math, 2 - Science, 3 - History "))
            if(tempclass < 4):
                nameAndGrade["Class"].append(schoolclass[tempclass - 1])
                check = True
            else:
                print("Invalid Class, try again....")

totalStudents = int(input("How many students do you have? "))
addStudent(totalStudents)
for place in range(len(nameAndGrade) - 1):
    print(f"Name: {nameAndGrade['Name'][place]}, Grade: {nameAndGrade['Grade'][place]}. Course: {nameAndGrade['Class'][place]}")