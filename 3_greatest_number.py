a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

if a > b and a > c:
    print(a)
elif b < a and b < c:
    print(b)
elif c > b and c > a:
    print(c)
else:
    print("All are equal")