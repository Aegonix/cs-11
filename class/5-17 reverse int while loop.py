
#? WAP to enter any number and find its reverse.

n = input("Enter a number: ")
i = len(n) - 1
x = ""

while i >= 0:
    x += n[i]
    i -= 1

print(int(x))
