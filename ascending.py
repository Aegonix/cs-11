a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a >= b:
    if b >= c:
        print(c, b, a)
    else:
        print(b, c, a)

elif b >= a:
    if a >= c:
        print(c, a, b)
    else:
        print(a, c, b)

else:
    if b >= a:
        print(a, b, c)
    else:
        print(b, a, c)
