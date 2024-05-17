
#? WAP to print fibonacci series using while loop.

n = int(input("Enter a number: "))

a = 0
b = 1

print(a, end=" ")
print(b, end=" ")

i = 0

while i < (n - 2):
    c = a + b
    a, b = b, c
    print(c, end=" ")

    i += 1
