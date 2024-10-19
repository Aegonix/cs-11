
#? WAP to print the second largest element in a list, without using any functions.

nums = eval(input("Enter list of numbers: "))
largest_element = nums[0]

for i in nums:
    if i > largest_element:
        largest_element = i

nums_without_largest: list[int] = []

for i in nums:
    if i != largest_element:
        nums_without_largest.append(i)

second_largest_element = nums_without_largest[0]

for i in nums_without_largest:
    if i > second_largest_element:
        second_largest_element = i

print("The second largest element is:", second_largest_element)
