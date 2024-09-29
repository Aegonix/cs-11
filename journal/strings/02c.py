
#? Write a program to input a word and print the following pattern if str="abc".
#* abc
#* ab
#* a

word = input("Enter a word: ")
n = len(word)

for i in range(n):
    print(word[: (n - i)])
