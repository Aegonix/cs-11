
#? Write a program to input the value of x and n and print the sum of the following series:
#? x - x^2/2! + x^3/3! - x^4/4! + x^5/5! - x^6/6!

x = float(input("Enter value of x: "))
n = int(input("Enter value of n: "))
sum = 0

for i in range(1, n + 1):
    #* factorial

    f = 1
    for j in range(i, 0, -1):
        f *= j

    if i % 2 != 0:
        sum += (x ** i) / f
    else:
        sum -= (x ** i) / f

print("Sum of the series is:", sum)
