
#? WAP to enter two numbers and ask the operator (+ - * /) from the user.
#? Display the result by applying the given operator on the two numbers.

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operator = input("Enter operator (+ - * /): ")

if operator == "+":
    print(a + b)

elif operator == "-":
    print(a - b)

elif operator == "*":
    print(a * b)

elif operator == "/":
    print(a / b)

else:
    print("Please input a valid operator.")
