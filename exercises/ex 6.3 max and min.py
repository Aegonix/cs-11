
#? 3.
#? Write a program that prints minimum and maximum 
#? of five numbers entered by the user. (without using built-in functions)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))
e = int(input("Enter fifth number: "))

x = [a, b, c, d, e]
max = x[0]
min = x[0]

for i in x[1:]:
    if i >= max:
        max = i

for j in x[1:]:
    if j <= min:
        min = j

print("The maximum number is:", max)
print("The minimum number is:", min)
