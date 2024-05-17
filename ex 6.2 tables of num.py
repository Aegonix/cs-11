
#? 2.
#? Write a function to print the table of a given number. 
#? The number has to be entered by the user.

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)
