
#? 19.
#? Write a to enter program their that asks the user name and age.  
#? Print a message addressed to the user that tells the user 
#? the year in which they will turn 100 years old.

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(name, "will be 100 years old in the year", 2024 + (100 - age))
