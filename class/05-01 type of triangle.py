
#? WAP to input 3 side lengths of a triangle and classify it into scalene, isosceles and equilateral.

a = float(input("Enter length of side a: "))
b = float(input("Enter length of side b: "))
c = float(input("Enter length of side c: "))

if a == b == c:
    print("Equilateral triangle")

elif a == b or a == c or b == c:
    print("Isosceles triangle")

else:
    print("Scalene triangle")
