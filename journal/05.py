
#? Write a program to determine whether a number is a perfect number, an Armstrong number or a palindrome.

n = int(input("Enter a number: "))

#* perfect number

factors_sum = 0
for i in range(1, n):
    if n % i == 0:
        factors_sum += i

if factors_sum == n:
    print(n, "is a perfect number.")

#* armstrong number

digits = len(str(n))
armstrong_sum = 0
a = n

for i in range(digits):
    armstrong_sum += (a % 10) ** digits
    a //= 10

if armstrong_sum == n:
    print(n, "is an armstrong number.")

#* palindrome

rev = 0
x = n
while x > 0:
    rem = x % 10
    rev = rev * 10 + rem
    x //= 10

if rev == n:
    print(n, "is a palindrome.")
