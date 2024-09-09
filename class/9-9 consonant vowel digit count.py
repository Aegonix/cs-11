
#? WAP to count the number of vowels, consonants and digits in an inputted string, and display the count.

string = input("Enter a string: ")
digit_count = 0
vowel_count = 0
consonant_count = 0

for i in range(string):
    if i in "0123456789":
        digit_count += 1

    elif i in "aeiou" or i in "AEIOU":
        vowel_count += 1

    elif i in "bcdfghjklmnpqrstvwxyz" or i in "BCDFGHJKLMNPQRSTUVWXYZ":
        consonant_count += 1
 
print("The number of vowels is:", vowel_count)
print("The number of consonants is:", consonant_count)
print("The number of digits is:", digit_count)
