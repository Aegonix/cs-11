
#? Write a program to input a line of text and a word, reverse the word and make a new text.

string = input("Enter a line of text: ")
word_to_reverse = input("Enter the word to be reversed: ")

words = string.split()
i = 0

for word in words:
    if word == word_to_reverse:
        words[i] = word_to_reverse[::-1]

    i += 1

for i in words:
    print(i, end=" ")
