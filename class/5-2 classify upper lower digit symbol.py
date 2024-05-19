
#? WAP to enter any character and print if it is upper case, lower case, digit or symbol.

char = input("Enter one character: ")

if len(char) > 1:
    print("Please enter only one character.")

else:
    if char.isupper():
        print("It is upper case.")

    elif char.islower():
        print("It is lower case.")

    elif char.isdigit():
        print("It is a digit.")

    else:
        print("It is a symbol.")
