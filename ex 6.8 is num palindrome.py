
#? 8.
#? Write a function that checks whether an input 
#? number is a palindrome or not.

num = int(input("Enter a number: "))

if num == int(str(num)[::-1]):
    print("The number is a palindrome.")

else:
    print("The number is not a palindrome.")
