
#? WAP to find the factorial of a number (using while loop)

n = int(input("Enter a number: "))
i = n
f = 1

while i > 0:
    f *= i
    i -= 1

print(f)