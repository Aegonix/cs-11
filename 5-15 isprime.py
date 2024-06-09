
#? WAP to take a number from the user and check if it is prime or not.

n = int(input("Enter a number: "))

if n == 1:
    print("1 is neither prime nor composite.")

elif n > 1:
    for i in range(2, n):
        if n % i == 0:
            print(n, "is a composite number.")
            break

    else:
        print(n, "is a prime number.")

else:
    print(n, "is a composite number.")
