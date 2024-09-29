
#? Write a program to input a line of text and extract all numbers from it and find the sum.

string = input("Enter a line of text: ")
sum = 0
output = ""
print("The numbers are: ", end="")

for i in string:
    if i in "0123456789":
        output += i + ", "
        sum += int(i)
    
print(output[:-2])
print("The sum is:", sum)
