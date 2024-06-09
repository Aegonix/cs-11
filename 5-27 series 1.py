
#? WAP to print the series:
#* 1, 4, 7, 10, ...

n = int(input("Enter n: "))

for i in range(1, n + 1):
    print(1 + (i - 1) * 3, end=" ")
