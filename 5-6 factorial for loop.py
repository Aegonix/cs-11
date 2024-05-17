
#? WAP to find the factorial of a number using input.

n = int(input("Enter a number: "))
x = 1

for i in range(n, 0, -1):
    x *= i

print(x)
