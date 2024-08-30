
#? Write a python program to input three numbers and display the largest / smallest number.

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a > b and a > c:
    print(a, "is greatest")

    if b > c:
        print(c, "is smallest")

    else:
        print(b, "is smallest")

elif b > a and b > c:
    print(b, "is greatest")

    if a > c:
        print(c, "is smallest")

    else:
        print(a, "is smallest")

elif c > a and c > b:
    print(c, "is greatest")

    if a > b:
        print(b, "is smallest")
    
    else:
        print(a, "is smallest")

else:
    print("The three numbers are equal")
