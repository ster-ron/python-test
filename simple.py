#Simple interest calculation
#I = interest earned or paid
#P = principal
#r =  annual interest rate as a decimal
#t = time in years

print("WELCOME YOU MAY START  BY CALCULATING INTEREST")
quiz = input('What would you like to calculate? IF principal enter \"p\", if interst \"i\", time \"t\", rate \"r\": ')

while True:
    if quiz.lower() == "i":
        p = input("Please enter the principal: ")
        r = input("Enter the rate: ")
        t = input("Enter the time or duration in years: ")
        while True:
            if not p.isdigit() or not r.isdigit() or not t.isdigit():
                if not p.isdigit():
                    print("Enter digits only.")
                    p = input("Please enter the principal: ")
                elif not r.isdigit():
                    print("Enter digits only.")
                    r = input("Enter the rate: ")
                elif not t.isdigit():
                    print("Enter digits only.")
                    t = input("Enter the time or duration in years: ")
            else:
                p = float(p)
                r = float(r)
                t = float(t)
                break
        interest = p * r * t
        print(f"Interest: {interest}") 
        break
    elif quiz.lower() == "p":
        i = input("Please enter the interest earned or paid: ")
        r = input("Enter the rate: ")
        t = input("Enter the time or duration in years: ")

        while True:
            if not i.isdigit() or not r.isdigit() or not t.isdigit():
                if not i.isdigit():
                    print("Enter digits only.")
                    i = input("Please enter the interest earned or paid: ")
                elif not r.isdigit():
                    print("Enter digits only.")
                    r = input("Enter the rate: ")
                elif not t.isdigit():
                    print("Enter digits only.")
                    t = input("Enter the time or duration in years: ")
            else:
                i = float(i)
                r = float(r)
                t = float(t)
                break
        principal = i  /  (r * t)
        print(f"Principal: {principal}")
        break
    elif quiz.lower() == "t":
        p = input("Please enter the principal: ")
        r = input("Enter the rate: ")
        i = input("Please enter the interest earned or paid: ")

        while True:
            if not p.isdigit() or not r.isdigit() or not i.isdigit():
                if not p.isdigit():
                    print("Enter digits only.")
                    p = input("Please enter the principal: ")
                elif not r.isdigit():
                    print("Enter digits only.")
                    r = input("Enter the rate: ")
                elif not i.isdigit():
                    print("Enter digits only.")
                    i = input("Please enter the interest earned or paid: ")
            else:
                p = float(p)
                r = float(r)
                i = float(i)
                break
        time = i / (p * r)
        print(f"Time: {time}")
        break
    elif quiz.lower() == "r":
        p = float(input("Please enter the principal: "))
        i = float(input("Please enter the interest earned or paid: "))
        t = float(input("Enter the time or duration in years: "))

        while True:
            if not p.isdigit() or not t.isdigit() or not i.isdigit():
                if not p.isdigit():
                    print("Enter digits only.")
                    p = input("Please enter the principal: ")
                elif not t.isdigit():
                    print("Enter digits only.")
                    t = input("Enter the time or duration in years: ")
                elif not i.isdigit():
                    print("Enter digits only.")
                    i = input("Please enter the interest earned or paid: ")
            else:
                p = float(p)
                t = float(t)
                i = float(i)
                break
        rate = i / (p * t)
        print(f"Rate: {rate}")
        break
    else:
        print(f"Sorry, i could not understand what you ment by {quiz}")
        print("Please give your answer based  on the choises given")
        quiz = input('What would you like to calculate? IF principal enter \"p\", if interst \"i\", time \"t\", rate \"r\": ')