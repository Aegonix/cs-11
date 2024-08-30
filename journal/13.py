
#? Write a menu driven program to perform the following tasks:
#* 1) Find the factorial of a number 
#* 2) Find the sum of the digits of a number 
#* 3) Check whether a number is palindrome or not 
#* 4) Check whether a number is Armstrong or not 
#* 5) Check whether a number is prime or not 
#* 6) Exit

while True:
    print("What would you like to do?")
    print("""1) Find the factorial of a number 
2) Find the sum of the digits of a number 
3) Check whether a number is palindrome or not 
4) Check whether a number is Armstrong or not 
5) Check whether a number is prime or not 
6) Exit""")

    x = int(input("Input any number (corresponding to the option): "))

    if x == 1:
        n = int(input("Enter a number to find its factorial: "))
        f = 1
        for i in range(n, 0, -1):
            f *= i

        print("The factorial is:", f, end="\n\n")

    elif x == 2:
        n = int(input("Enter a number to find the sum of its digits: "))
        sum = 0
        for i in range(len(str(n))):
            last_digit = n % 10
            sum += last_digit
            n //= 10
        
        print("The sum of digits is:", sum, end="\n\n")

    elif x == 3:
        n = int(input("Enter any number to check if it is a palindrome: "))

        digits = len(str(n))

        for i in range(1, digits + 1, 2):
            ones_place = n % 10
            first_place = n // (10 ** (digits - i))

            if ones_place != first_place:
                print(n, "is not a palindrome", end="\n\n")
                break
            
            else:
                n %= (10) ** (digits - i)
                n //= 10

        else:
            print("Yes, it is a palindrome.", end="\n\n")

    elif x == 4:
        n = int(input("Enter a number to check if it is armstrong: "))
        sum = 0
        temp = n

        while temp > 0:
            digit = temp % 10
            sum += digit ** len(str(n))
            temp //= 10

        if n == sum:
            print("Yes, it is an Armstrong number.", end="\n\n")
        else:
            print("No, it is not an Armstrong number.", end="\n\n")

    elif x == 5:
        n = int(input("Enter a number to check if it is a prime: "))

        if n == 1:
            print("1 is neither prime nor composite.", end="\n\n")

        elif n > 1:
            for i in range(2, n):
                if n % i == 0:
                    print(n, "is a composite number.", end="\n\n")
                    break

            else:
                print(n, "is a prime number.", end="\n\n")

        else:
            print(n, "is a composite number.", end="\n\n")

    elif x == 6:
        print("Exiting...")
        break

    else:
        print("Please input a valid option, e.g: 1", end="\n\n")
