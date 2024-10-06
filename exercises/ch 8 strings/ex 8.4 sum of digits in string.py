
#? Input a string having some digits. Write a function to return the sum of digits present in this string.

def sum_of_digits(string: str) -> int:
    sum = 0

    for char in string:
        if 48 <= ord(char) <= 57:
            sum += int(char)

    return sum


print(sum_of_digits(input("Enter a string: ")))
