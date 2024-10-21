
#? WAP to enter 10 numbers (using a loop to take inputs) and find the sum and average.

sum = 0

for i in range(10):
    num = int(input("Enter an integer: "))

    sum += num

avg = sum / 10

print("The sum is:", sum)
print("The average is:", avg)
