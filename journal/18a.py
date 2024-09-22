
#? Write a program to input a word and print the following pattern if str = “abc”.
#* a
#* bb
#* ccc

word = input("Enter a word: ")

n = len(word)
for i in range(1, n + 1):
    print(word[i - 1] * i)
