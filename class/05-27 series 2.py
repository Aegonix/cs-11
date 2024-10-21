
#? WAP to print the series:
#* 5, -10, 15, -20, 25, ...

pos = True
n = int(input("Enter n: "))

for i in range(1, n + 1):
    if pos:
        print(i * 5, end=" ")
        pos = False

    else:
        print(i * -5, end=" ")
        pos = True