
#? WAP to input monthly salary of an employee and give bonus of 10% if the salary is more than 50,000.
#? Display the salary and bonus.

s = float(input("Enter salary: "))

if s > 50000:
    print("You are eligible for a bonus.")
    
    bonus = s / 10
    print("Your bonus is:", bonus)
    print("Your salary is:", s)
