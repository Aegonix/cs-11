
#? WAP to take any number and check if it is an armstrong. (using while loop)

n = int(input("Enter a number to check if it is armstrong: "))
sum = 0
temp = n

while temp > 0:
    digit = temp % 10
    sum += digit ** len(str(n))
    temp //= 10

if n == sum:
    print("Yes, it is an Armstrong number.")
else:
    print("No, it is not an Armstrong number.")
