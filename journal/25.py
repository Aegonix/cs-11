
#? WAP to input a line of text and count the number of alphabets, numbers and special characters in the text. 

a = 0
n = 0
s = 0
string = input("Enter a string: ")

for i in string:
    if i in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        a += 1
    elif i in "0123456789":
        n += 1
    elif i != " ":
        s += 1

print("Number of alphabets:", a)
print("Number of numbers:", n)
print("Number of special characters:", s)
