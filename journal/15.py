
#? WAP to find the sum of prime no. between 2 ranges

start = int(input("Enter a number as the start of the range: "))
stop = int(input("Enter a number as the stop of the range (included in the sum): "))
sum = 0

for i in range(start, stop + 1):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break

        else:
            sum += i

print("The sum is:", sum)
