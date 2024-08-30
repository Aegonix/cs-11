
#? WAP to print the following pattern:

#* <------l------->
#* **************** ^
#* *              * |
#* *              * |
#* *              * | b
#* *              * |
#* *              * |
#* **************** v

l = 15
b = 5

for i in range(1, b + 1):
    if i == 1 or i == b:
        print("*" * l)
        continue
    
    print("*", end="")
    print(" " * (l - 2), end="")
    print("*")
