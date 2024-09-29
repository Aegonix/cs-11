
#? Write a python program to input two numbers and display the largest / smallest number.

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if a > b:
    print(a, "is greater and", b, "is smaller")

elif b > a:
    print(b, "is greater and", a, "is smaller")

else:
    print("The two numbers are equal")
