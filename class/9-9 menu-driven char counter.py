
#? Write a menu driven program to count number of:
#* 1) vowels
#* 2) consonants
#* 3) digits
#* 4) spaces
#* 5) special characters
#? in a string given by the user.

string = input("Enter the string: ")

while True:
    option = input("""Options: (enter any number)
(1) Count vowels
(2) Count consonants
(3) Count digits
(4) Count spaces
(5) Count special characters
(6) Exit""")

    if option == "1":
        vowel_count = 0
        for i in string:
            if i in "aeiou" or i in "AEIOU":
                vowel_count += 1
               
        print("The number of vowels is:", vowel_count, "\n\n")

    elif option == "2":
        consonant_count = 0
        for i in string:
            if i in "bcdfghjklmnpqrstvwxyz" or i in "BCDFGHJKLMNPQRSTVWXYZ":
                consonant_count += 1
        
        print("The number of consonants is:", consonant_count, "\n\n")

    elif option == "3":
        digit_count = 0
        for i in string:
            if i in "0123456789":
                digit_count += 1

        print("The number of digits is:", digit_count, "\n\n")

    elif option == "4":
        spaces_count = 0
        for i in string:
            if i == " ":
                spaces_count += 1
        
        print("The number of spaces is:", spaces_count, "\n\n")

    elif option == "5":
        special_chars_count = 0
        for i in string:
            if i not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ":
                special_chars_count += 1

        print("The number of special characters is:", special_chars_count, "\n\n")

    elif option == "6":
        print("Exiting...")
        break

    else:
        print("Unrecognized option. Please try again.\n\n")
