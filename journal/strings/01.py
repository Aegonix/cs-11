
#? Write a program to input a sentence and count the number of times “a” appears.

string = input("Enter a sentence: ")
count = 0

for i in string:
    if i == "a":
        count += 1

print("Number of occurrences of 'a' is:", count)
