
#? Write a user defined function to convert a string with more than one word into title case string,
#? where string is passed as parameter. (Title case means that the first letter of word is capitalized.)


def title_case(string: str) -> str:
    s = ""
    i = 0

    for char in string:
        if i == 0 or string[i - 1] == " ":
            s += char.upper()
        else:
            s += char

        i += 1

    return s


print(title_case(input("Enter a string: ")))
