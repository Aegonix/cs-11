
#? 4.
#? Write a program to check if the year entered by the 
#? user is a leap year or not.

year = int(input("Enter year: "))

if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
    print("It is a leap year.")

else:
    print("It is not a leap year.")
