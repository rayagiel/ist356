'''
Let' write a program to divide up the check among diners in a party.

Write a program to input the amount of a restaurant check, tip %, and number of diners

The program should output the total amount with tip, and the amount each diner owes.
'''


amount = float(input ("Please input the total amount of the check: "))
if amount < 0:
    print("Error: Check amount cannot be less than zero.")
    exit(1)

tip_percent = float(input ("Please input the tip percentage: "))
if tip_percent < 0:
    print("Error: Tip percentage cannot be less than zero.")
    exit(1)

num_diners = int(input ("Please input the number of diners: "))
if num_diners < 0:
    print("Error: Number of diners cannot be less than zero.")
    exit(1)

tip = (tip_percent/100) * amount
total = amount + tip
each_owes = total / num_diners

print(f"Total amount with tip: $ {total:2f}")
print(f"Each diner owes: $ {each_owes:2f}")



