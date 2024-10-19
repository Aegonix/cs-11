
#? WAP to print the pattern:
#*    *
#*   * *
#*  *   *
#* *     *
#*  *   *
#*   * *
#*    *

n = 7
m = n // 2 + 1

for i in range(1, m + 1):
    print(" " * (m - i), end="")

    if i == 1:
        print("*")
        continue

    print("*", end="")
    print(" " * (2 * (i - 1) - 1), end="")
    print("*")

for i in range(1, (n - m + 1)):
    print(" " * i, end="")

    if (n - m - i) == 0:
        print("*")
        continue

    print("*", end="")
    print(" " * (2 * (n - m - i) - 1), end="")
    print("*")
