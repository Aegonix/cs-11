
#? Write a program to input a sentence and count the number of words in the sentence.

string = input("Enter a sentence: ")
word = input("Enter a word to count for: ")
count = 0

for i in range(len(string)):
    if string[i : (len(word) + i)] == word:
        count += 1

print("Number of occurences of '", word, "' is: ", count, sep="")
