
#? WAP to check if a number is a palindrome or not. (using while loop)

num = int(input("Enter any integer: "))

n = num
digits = len(str(n))

for i in range(1, digits + 1, 2):
    ones_place = n % 10
    first_place = n // (10 ** (digits - i))

    if ones_place != first_place:
        print(n, "is not a palindrome")
        break
    
    else:
        n %= (10) ** (digits - i)
        n //= 10

else:
    print(num, "is a palindrome")
