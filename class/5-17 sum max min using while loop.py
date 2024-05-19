
#? WAP to enter numbers as long as the user wishes.
#? Find the sum, highest, and, lowest digit of the number entered.

n = int(input("Enter a positive number: "))
max = int(str(n)[0])
min = max
sum = 0
i = 0

#* sum 
while i < len(str(n)):
    sum += int(str(n)[i])
    
    if int(str(n)[i]) > max:
        max = int(str(n)[i])

    if int(str(n)[i]) < min:
        min = int(str(n)[i])

    i += 1

print("The sum of digits of", n, "is:", sum)
print("The highest digit of", n, "is:", max)
print("The lowest digit of", n, "is:", min)
