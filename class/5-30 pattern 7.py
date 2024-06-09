
#? WAP to print the following pattern:
#* 5
#* 44
#* 333
#* 2222
#* 11111

n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):
    print(str(n + 1 - i) * i)
