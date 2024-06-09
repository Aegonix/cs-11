
#? 3.
#? Write a program that prints minimum and maximum 
#? of five numbers entered by the user. (without using built-in functions)

max = 0
min = max

for i in range(0, 5):
    x = int(input("Enter number " + str(i + 1) + ": ")
    
    if not i:
        max = x
        min = x

    else:
        if x > max:
            max = x

        if x < min:
            min = x

print("The maximum number is:", max)
print("The minimum number is:", min)
