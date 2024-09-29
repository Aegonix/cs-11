
#? Write a program to input a sentence and count the number of words in the sentence.

string = input("Enter a sentence: ")
spaces_count = 1

for i in string:
    if i == " ":
        spaces_count += 1

print("The number of words is:", spaces_count)
