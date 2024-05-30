
#? WAP to print the sum of the series:
#* s = x + (x^2 / 2) + (x^3 / 3) + ... + (x^n / n)

x = int(input("Enter x: "))
n = int(input("Enter n: "))
sum = 0

for i in range(1, n + 1):
    sum += (x ** i) / i

print("The sum of the series is:", sum)
