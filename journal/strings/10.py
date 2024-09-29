
#? WAP to input a line of text and convert to uppercase if it is in lower and convert to lower case if it is in uppercase.

string = input("Enter a string: ")
output = ""

for i in string:
    if i in "abcdefghijklmnopqrstuvwxyz":
        output += chr(ord(i) - 32)

    elif i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        output += chr(ord(i) + 32)

    else:
        output += i

print(output)
