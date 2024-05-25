
#? WAP to print the following pattern:
#* 4321
#* 432
#* 43
#* 4

x = 0
for i in range(1, 5):
    for j in range(4, x, -1):
        print(j, end="")

    print()
    x += 1
