
#? Write a program to input a word and print the following pattern if str="abc".
#* cba
#* cb
#* c

word = input("Enter a word: ")
n = len(word)

for i in range(n):
    print(word[::-1][: (n - i)])
