
#? WAP to print the following pattern:
#*    A
#*   BAB
#*  CBABC
#* DCBABCD

n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    print(" " * (n - i), end="")

    for j in range(i - 1, 0, -1):
        print(chr(65 + j), end="")

    for j in range(i):
        print(chr(65 + j), end="")
    
    print()
