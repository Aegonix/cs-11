
#? 8.
#? Write a function that checks whether an input 
#? number is a palindrome or not.

n = input("Enter a number: ")
i = len(n) - 1
reverse = ""

while i >= 0:
    reverse += n[i]
    i -= 1

if reverse == n:
    print("Yes,", n, "is a palindrome.")
else:
    print("No,", n, "is not a palindrome.")
