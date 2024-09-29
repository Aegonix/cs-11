
#? Write a program to input the value of x and n and print the sum of the following series:
#? 1 + x² + x³ + ... + xⁿ

#* a)
x = float(input("Enter value of x: "))
n = int(input("Enter value of n: "))

sum = 0

for i in range(n + 1):
    if n == 1:
        break
    
    sum += x ** i

print("Sum of the series is:", sum)
