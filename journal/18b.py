
#? Write a program to input a word and print the following pattern if str="abc".
#* a
#* ab
#* abc

word = input("Enter a word: ")
n = len(word)

for i in range(n):
    print(word[0 : (i + 1)])
