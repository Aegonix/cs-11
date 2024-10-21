
#? WAP to find the number of occurences of a digit in a number.

n = int(input("Enter the number: "))
d = int(input("Enter the digit to count for: "))
occurences = 0

for i in str(n):
    if int(i) == d:
        occurences += 1

print(occurences)
