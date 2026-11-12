print("WELCOME TO THE EXAMINATION BOARD")

num = input("Enter the number of students: ").strip()
highscore = -1
lowscore = 101
total_marks = 0 
valid_students = 0
passed = 0
failed =0
student = []
admission = []
mark = []

while True:
    if num == "":
        print("Please enter a value.")
        num = input("Enter the number of students: ")
    elif not num.isdigit():
        print("You have entered an invalid value. Use digits only")
        num = input("Enter the number of students: ")
    else:
        num = int(num)
        if num <= 0:
            print("You have entered an unrealistic value. Enter values above 0.")
            num = input("Enter the number of students: ")
        else:
            break

for students in range(num):
    print("-----GRADES-----")
    adm =  input("Enter student\'s admission number: ").strip()
    name = input("Enter student\'s name: ")
    score =  input("Enter student\'s score: ")

    while True:
        if score == "":
            print("Please enter student\'s score.")
            score = input("Enter student\'s score: ")
        elif not score.isdigit():
            print("You have entered an invalid value. Enter whole numbers between 0 and 100.")
            score = input("Enter student\'s score: ")
        else:
            score = int(score)
            if score < 0 or score > 100:
                print("You can only enter whole numbers between 0 and 100.")
                score = input("Enter student\'s score: ")
            else:
                mark.append(score)
                break

    while True:
        if adm == "":
            print("Please enter student\'s amission number.")
            adm = input("Enter student\'s admission number: ")
        else:
            admission.append(adm)
            break

    while True:
            if name == "":
                print("Please enter student\'s name.")
                name = input("Enter student\'s name: ")
            else:
                student.append(name)
                break

    if score <= 25:
        grade = "Grade E - Fail"
    elif score <= 45:
        grade = "Grade D - Fail"
    elif score <= 65:
        grade =  "Grade C - Pass"
    elif score <=  80:
        grade = "Grade B - Good"
    else:
        grade = "Grade A - Excellent"

    print("---STUDENT---")
    print(f"ADM NO: {adm}")
    print(f"Name: {name}.")
    print(f"Score: {score}.")
    print(f"Grade: {grade}.")
    total_marks += score
    valid_students += 1

    if score <= 45:
        failed += 1
    if score > 45:
        passed  += 1

highest = max(mark)

print(f"The highest score is {highest}")
for i in range(len(mark)):
    if mark[i] == highest:
        print(student[i])
        print(admission[i])

lowest = min(mark)
print(f"The lowest score is {lowest}")
for x in range(len(mark)):
    if mark[x] == lowest:
        print(student[x])
        print(admission[x])

print(admission)
print(student)
print(mark)
overal = 100 * num
average = total_marks/valid_students
print(f"Class total score: {total_marks} out of {overal} marks.")
print(f"Class average: {average:.2f}")
print(f"Valid students: {valid_students}")
print(f"Total failed students: {failed}")
print(f"Total passed students: {passed}")
