
#? WAP to input a string and count the number of times 'a' and 'A' appear in the string.

string = input("Enter a string: ")
a, A = 0, 0

for i in string:
    if i == "a":
        a += 1
    elif i == "A":
        A += 1

print("Number of 'a':", a)
print("Number of 'A':", A)
