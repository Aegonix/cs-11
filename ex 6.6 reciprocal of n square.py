
#? 6.
#? Write a program to find the sum of 1 + 1/8 + 
#? 1/27......1/n^3, where n is the number input by the 
#? user.

n = int(input("Enter a number: "))
sum = 0

for i in range(1, n + 1):
    sum += 1 / (i ** 3)

print("The sum is:", sum)
