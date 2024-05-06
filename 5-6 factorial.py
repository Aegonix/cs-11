
#? WAP to find the factorial of a number using input.

n = int(input("Enter a number: "))
x = 1

for i in range(1, n + 1):
    x *= i

print(x)
