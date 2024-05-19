
#? WAP to write a program to print the fibonacci series.

n = int(input("Enter the number of elements: "))
a = 0

if n == 1:
    print(a)

elif n > 1:
    b = 1

    print(a, end=" ")
    print(b, end=" ")

    for i in range(n - 2):
        c = a + b
        a = b
        b = c
        print(c, end=" ")

else:
    print("Please enter a positive integer.")
