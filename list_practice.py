std = []
num = input("Enter number of students: ")
stdnum = 0

while True:
    if num == "":
        print("Please enter a value.")
        num = input("Enter number of students: ")
    elif not num.isdigit():
        print("Enter digits only, enter values above 0.")
        num = input("Enter number of students: ")
    else:
        num = int(num)
        break
    
for i in range(num):
    name = input("Enter the name of student: ")
    std.append(name)

print()
if len(std) > 0:
    print("REGISTERED STUDENTS")
    for student in std:
        print(student)
else:
    print("The class have no students")

stdnum = len(std)
print()
print(f"Total students:  {stdnum}")

if stdnum > 0:
    quiz =  input("Would you like to remove any student? ")
    if quiz.lower() == "yes":
        rname = input("Enter the name of student you\'d want to remove: ")
        if rname in std:
            std.remove(rname)
            print()
            print("UPDATED STUDENT LIST")

            for student in std:
                print(student)
            
            print()
            print(f"Remaining students: {len(std)}")
        else:
            print("Student not found in the list.")