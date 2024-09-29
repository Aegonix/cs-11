
#? Write a program to input a line of text and a word and count the number of times the word appears in the text.

string = input("Enter a line of text: ")
word = input("Enter a word: ")
count = 0

for i in string.split():
    if i == word:
        count += 1

print("The number of occurrences of '", word, "' is: ", count, sep="")
