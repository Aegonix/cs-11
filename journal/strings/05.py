
#? Write a program to input a word and check whether the word is a palindrome.

word = input("Enter a word: ")

if word == word[::-1]:
    print("Yes, '", word, "' is a palindrome.", sep="")

else:
    print("No, '", word, "' is not a palindrome.", sep="")
