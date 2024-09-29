
#? Write a program to input a line of text and replace the word with a new word.

string = input("Enter a line of text: ")
word_to_replace = input("Enter the word to be replaced: ")
new_word = input("Enter the new word: ")

words = string.split()
i = 0

for word in words:
    if word == word_to_replace:
        words[i] = new_word

    i += 1

for i in words:
    print(i, end=" ")
