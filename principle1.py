import math

print('Thank you for using principle calculator.')
Q = input("what would you want to calculate? if interest enter/'I', if total amount with interest enter /'A', if rate enter /'R', if time enter /'T'")

if Q.lower() == "a":
	principle = float(input("Enter your principle amount: "))
	r = float(input("Enter the rate: "))
	t = float(input("Enter time: "))
	
	A = principle * ((1 + (r/100)) ** t)
	A = round(A, 2)
	
	print(f"Your total amount is KES {A: 2f}.")
	
elif Q.lower() == "i":
	principle = float(input("Enter your principle amount: "))
	r = float(input("Enter the rate: "))
	t = float(input("Enter time: "))
	
	A = principle * ((1 + (r/100)) ** t)
	I = A - principle
	I = round(I, 2)
	print(f"your interest is KES {I: 2f}")
	
elif Q.lower() == "r":
	A = float(input("Enter the total amount after adding the interest to the principle"))
	principle = float(input("Enter your principle amount: "))
	print("The current code works only when time is 2 years")
	#t = float(input("Enter time: "))
	
	r = 100 * ((math.sqrt(A/principle)) - 1)
	r = round(r, 2)
	
	print(f"Your interest is calculated under interest rate of {r: 2f}%")
	