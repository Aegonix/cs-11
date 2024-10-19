
#? WAP to print the following pattern:

#*     1
#*    1 1
#*   1 2 1
#*  1 3 3 1
#* 1 4 6 4 1
#* ...

rows = 5

for i in range(rows):
    print(" " * (rows - (i + 1)), end="")

    #* using combinations (nCr)
    for j in range(i + 1):

        n = 1
        for k in range(1, i + 1): #* finding n!
            n *= k

        r = 1
        for k in range(1, j + 1): #* finding r!
            r *= k

        n_minus_r = 1
        for k in range(1, ((i - j) + 1)): #* finding (n-r)!
            n_minus_r *= k

        print(int(n / (r * n_minus_r)), end=" ")

    print()
