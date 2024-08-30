
#? WAP to print the following pattern:
#*     *
#*    * *
#*   *   *
#*  *     *
#* *********

n = 5

for i in range(1, n):
    print(" " * (n - i), end="")
    if i == 1:
        print("*")
        continue

    print("*", end="")
    print(" " * (2 * (i - 1) - 1), end="")
    print("*")

print("*" * (2 * n - 1))
