
#? WAP to check whether the given number is odd or even and also the count the numbers.
#? Take 5 integers from the user and check the above condition.

i = 0

for x in range(5):
    num = int(input("Enter a number: "))
    
    if num % 2 != 0:
        i += 1
        print("Number is odd.")
        continue

    print("Number is even.")

print("Total number of odds are:", i)
