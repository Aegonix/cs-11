
#? WAP to print the following pattern:
#* EDCBA
#* DCBA
#* CBA
#* BA
#* A

n = 26

for i in range(n):
    for j in range(n - i, 0, -1):
        print(chr(64 + j), end="")

    print()
