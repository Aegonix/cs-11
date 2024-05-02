
#? WAP to input 3 side lengths of a triangle and classify it into scalene, isosceles and equilateral.

a = float(input("Enter length of side a: "))
b = float(input("Enter length of side b: "))
c = float(input("Enter length of side c: "))

x = {a, b, c}

if len(x) == 3:
    print("Scalene triangle")

elif len(x) == 2:
    print("Isosceles triangle")

elif len(x) == 1:
    print("Equilateral triangle")
