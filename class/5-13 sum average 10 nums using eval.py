
#? WAP to enter 10 numbers (using eval(...)) and find the sum and average.

nums = eval(input("Enter 10 numbers (separated by commas): "))
sum = 0

for i in nums:
    sum += i

avg = sum / len(nums)

print("The sum is:", sum)
print("The average is:", avg)
