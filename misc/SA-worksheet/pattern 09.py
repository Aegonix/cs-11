
#? WAP to print the pattern:
#*       4
#*     4 3 4
#*   4 3 2 3 4
#* 4 3 2 1 2 3 4
#*   4 3 2 3 4
#*     4 3 4
#*       4

n = 7
m = n // 2 + 1

for i in range(1, m + 1):
    print(" " * (2 * (m - i)), end="")

    for j in range(m, m - i, -1):
        print(j, end=" ")

    for j in range(m - i + 2, m + 1):
        print(j, end=" ")

    print()

for i in range(1, m):
    print(" " * (2 * i), end="")

    for j in range(m, i, -1):
        print(j, end=" ")

    for j in range(i + 2, m + 1):
        print(j, end=" ")

    print()
