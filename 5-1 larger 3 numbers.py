a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

if a > b and a > c:
    print("a is largest")

elif b > a and b > c:
    print("b is largest")

elif c > a and c > b:
    print("c is largest")

else:
    print("They are all equal")
