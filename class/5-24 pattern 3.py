
#? WAP to print the following pattern:
#!    *
#!   **
#!  ***
#! ****

n = 4 #* number of rows
for i in range(1, n + 1):
    print(" " * (n - i) + i * "*")
