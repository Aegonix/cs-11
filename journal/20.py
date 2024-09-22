
#? Write a program to input a word and count the number of vowels in the word.

word = input("Enter a word: ")
count = 0

for i in word:
    if i in "aeiouAEIOU":
        count += 1

print("The number of vowels in '", word, "' is: ", count, sep="")
