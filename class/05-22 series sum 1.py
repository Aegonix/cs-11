
#? WAP to print the sum of the following series:
# * s = 1 + x + x^2 + x^3 + x^4 + ... + x^n

x = int(input("Enter value of x: "))
n = int(input("Enter value of n: "))
sum = 0

for i in range(n + 1):
    sum += x ** i

print("Sum of the series is:", sum)
