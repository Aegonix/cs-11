
#? WAP to enter n numbers as many as the user wishes.
#? Find the sum, highest, and, lowest digit of the numbers entered.

n = int(input("How many numbers? "))

max = 0
min = max
sum = 0

for i in str(n):
    num = int(input("Enter num " + str(i + 1) + ": "))
    sum += num
    
    if not int(i):
        max = num
        min = num
    
    else:
        if num > max:
            max = num
        if num < min:
            min = num
        
print("The sum of digits of", n, "is:", sum)
print("The highest digit of", n, "is:", max)
print("The lowest digit of", n, "is:", min)
