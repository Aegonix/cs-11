
#? Write a program to input a word and print the following pattern if str="abc".
#* a
#* abab
#* abcabcabc

word = input("Enter a word: ")
n = len(word)

for i in range(n):
    print(word[: i + 1] * (i + 1))
