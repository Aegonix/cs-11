
#? Write a program to input a number and check if the number is a prime or composite number.

n = int(input("Enter a number: "))

if n == 1:
    print("1 is neither prime nor composite.")

else:
    for i in range(2, n):
        if n % i == 0:
            print(n, "is a composite number.")
            break

    else:
        print(n, "is a prime number.")
