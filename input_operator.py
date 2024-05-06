# 2/5/24 Thursday

a = float(input("Enter a: "))
b = float(input("Enter b: "))

operator = input("Enter operator: ")

if operator == "+":
    print(a, operator, b, "=", a + b)
elif operator == "-":
    print(a, operator, b, "=", a - b)
elif operator == "*":
    print(a, operator, b, "=", a * b)
elif operator == "/":
    print(a, operator, b, "=", a / b)