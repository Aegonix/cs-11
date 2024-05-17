
#? WAP to find the number of occurences of a digit in a number.

n = input("Enter the number: ")
d = input("Enter the digit to count for: ")

x = 0
i = 0

while i < len(n):
    if n[i] == d:
        x += 1

    i += 1

print(x)
