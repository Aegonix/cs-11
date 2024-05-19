
#? 1.
#? Write a program that takes the name and age of the 
#? user as input and displays a message whether the 
#? user is eligible to apply for a driving license or not. 
#? (the eligible age is 18 years).

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to apply for a driving license.")
else:
    print("You are not eligible to apply for a driving license.")
