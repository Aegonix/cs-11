
#? WAP to print the sum of the series:
#* x - (x^2 / 2!) + (x^3 / 3!) - (x^4 / 4!) +- ... +- (x^n / n!)

x = int(input("Enter x: "))
n = int(input("Enter n: "))
sum = 0

for i in range(1, n + 1):
    f = 1

    for j in range(1, i + 1):
        f *= j
    
    if i % 2 != 0:
        sum += (x ** i) / f
    else:
        sum -= (x ** i) / f

print("The sum of the series is:", sum)
