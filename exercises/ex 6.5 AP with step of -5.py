
#? 5.
#? Write a program to generate the sequence: –5, 10, –15, 20, –25... upto n,
#? where n is an integer input by the user.

print(list(range(-5, int(input("Enter a number less than -5: ")) - 1, -5)))
