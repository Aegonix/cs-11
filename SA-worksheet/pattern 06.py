
#? WAP to print the pattern:
#*     A
#*    ABA
#*   ABCBA
#*  ABCDCBA
#*   ABCBA
#*    ABA
#*     A

n = 5  # * must be odd number
m = n // 2 + 1

for i in range(1, m + 1):
    print(" " * (m - i), end="")

    for j in range(1, i):
        print(chr(64 + j), end="")

    for j in range(i, 0, -1):
        print(chr(64 + j), end="")

    print()

for i in range(1, (n - m + 1)):
    print(" " * i, end="")

    for j in range(1, (m - i)):
        print(chr(64 + j), end="")

    for j in range(m - i, 0, -1):
        print(chr(64 + j), end="")

    print()
