
#? WAP to enter any number and find its reverse.
#! This is not the usual method. Don't memorize.

n = int(input("Enter any integer: "))

#* handling negatives
if n < 0:
    n *= -1
    print("-", end="")

div = n

#* reversing
while True:
    ones_place = n % 10
    print(ones_place, end="")
    rest_of_num = n // 10
    n = rest_of_num

    if 0 < div < 10:
        break
    
    div //= 10
