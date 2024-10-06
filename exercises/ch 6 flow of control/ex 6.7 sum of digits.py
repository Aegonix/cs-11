
#? 7.
#? Write a program to find the sum of digits of an 
#? integer number, input by the user.

num = int(input("Enter a number: "))
digits = list(str(num))
sum = 0

for i in digits:
    sum += int(i)

print("Sum:", sum)
