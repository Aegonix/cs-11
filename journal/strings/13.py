
#? Write a program to input a line of text and print each word in a new line.

string = input("Enter a line of text: ")

for word in string.split():
    print(word)
