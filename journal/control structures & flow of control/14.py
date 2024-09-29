
#? Write a program to calculate sum and average of odd, even and prime no.

ints = eval(input("Enter a list of numbers separated by commas: "))
sum = 0

for i in ints:
    if i % 2 == 0:
        print(i, "is an even number.")

    else:
        print(i, "is an odd number.")

    if i == 1:
        print("1 is neither prime nor composite.")

    elif i > 1:
        for j in range(2, i):
            if i % j == 0:
                print(i, "is a composite number.")
                break

        else:
            print(i, "is a prime number.")

    else:
        print(i, "is a composite number.")

    sum += i

avg = sum / len(ints)

print()
print("The average of the numbers is:", avg)
print("The sum of the numbers is:", sum)
