
#? WAP to print the sum of the series:
#* x - (x^2 / 3!) + (x^3 / 5!) - (x^4 / 7!) +- ... +- (x^n / (2n-1)!)

x = int(input("Enter x: "))
n = int(input("Enter n: "))
sum = 0

for i in range(1, n + 1):
    f = 1

    for j in range(1, 2 * i):
        f *= j
    
    if i % 2 != 0:
        sum += (x ** i) / f
    else:
        sum -= (x ** i) / f

print("The sum of the series is:", sum)
