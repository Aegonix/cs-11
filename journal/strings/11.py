
#? Write a program to input a line of text and capitalize the first character of each word.

string = input("Enter a line of text: ")
output = ""

for i in range(len(string)):
    if string[i - 1] == " " or i == 0:
        output += string[i].upper()

    else:
        output += string[i]

print(output)
