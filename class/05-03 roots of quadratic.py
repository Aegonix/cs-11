
#? WAP to calculate and print the roots of a quadratic equation.
#? Take a, b, and c as input and a != 0.

from math import sqrt

a = float(input("Enter x^2 coefficient (a): "))
b = float(input("Enter x coefficient (b): "))
c = float(input("Enter constant value (c): "))

if a == 0:
    print("Please input a valid x^2 coefficient.")

else:
    x1 = ((-b) + sqrt((b ** 2) - (4 * a * c))) / (2 * a)
    x2 = ((-b) - sqrt((b ** 2) - (4 * a * c))) / (2 * a)

    print("The roots are:", x1, "and", x2)
