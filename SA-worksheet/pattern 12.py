
#? WAP to print the following pattern:
#*       A
#*     CCC
#*   EEEEE
#* GGGGGGG

n = 4
for i in range(1, n + 1):
    print(" " * ((2 * n) - (2 * i)), end="")
    print(chr(64 + (2 * i - 1)) * (2 * i - 1))
