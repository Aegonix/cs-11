
#? WAP to check whether an odd number is in a given list inputted by the user.
#? If there is no number, do not give any message to the user.

nums = eval(input("Enter some integers (separated by commas): "))

for i in nums:
    if i % 2 != 0:
        print("Yes, there is an odd number in the given list.")
        break
    else:
        pass
        #! This pass statement is useless, it was merely for class demonstration
