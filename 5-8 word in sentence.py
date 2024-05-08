
#? WAP to take a sentence from a user and a word.
#? Check if the word is a part of that sentence.

sentence = input("Enter a sentence: ")
word = input("Enter a word: ")

if word in sentence:
    print("Yes,", "\"" + word + "\"", "is in", "\"" + sentence + "\"")

else:
    print("No,", "\"" + word + "\"", "is not in", "\"" + sentence + "\"")
