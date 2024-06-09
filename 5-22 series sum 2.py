
#? WAP to print the sum of the series:
#* s = 1 - x + x^2 - x^3 + x^4 +- ... +- x^n

x = int(input("Enter x: "))
n = int(input("Enter n: "))
sum = 0

for i in range(n + 1):
    if i % 2 == 0:
        sum += x ** i
    
    else:
        sum -= x ** i

print("The sum of the series is:", sum)
