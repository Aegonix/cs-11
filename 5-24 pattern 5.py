
#? WAP to print the following pattern:
#!    *
#!   * *
#!  * * *
#! * * * *
#!  * * *
#!   * *
#!    *

n = int(input("Please enter number of rows (odd number): "))

for j in range(n // 2, -1, -1):
    print((" " * j) + ("* " * ((n // 2 + 1) - j)))

for j in range(1, n // 2 + 1):
    print((" " * j) + ("* " * ((n // 2 + 1) - j)))
