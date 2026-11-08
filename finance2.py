income = input("Please enter your income: $ ")
note = input("Pleas enter what you have spent on: ")
spending = input(f"Please enter how much {note} cost: $ ")

if income.isalpha():
	print('Please enter digits only')
	while income.isalpha():
		income = input("Please enter your income: $ ")
else:
	income = float(income)
		
if spending.isalpha():
	print('Please enter digits only')
	while spending.isalpha():
		spending = input("Please enter how mush {note} cost: $ ")
else:
	spending = float(spending)

rem = income - spending
print(f"Your income is $ {income}")
print(f"Your spending is $ {spending}")