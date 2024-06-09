
#? WAP to take any number and check if it is an armstrong. (using while loop)

n = input("Enter a number: ")
i = 0
sum = 0

while i < len(n):
    sum += int(n[i]) ** len(n)    
    i += 1

if sum == int(n):
    print("Yes, it is an armstrong number.")

else:
    print("No, it is not an armstrong number.")
