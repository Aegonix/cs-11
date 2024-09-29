
#? Write a program to input a sentence and a word and check whether the word is present in the sentence.

string = input("Enter a sentence: ")
word = input("Enter a word: ")

if word in string:
    print("Yes, the word is present in the sentence.")
else:
    print("No, the word is not present in the sentence.")
