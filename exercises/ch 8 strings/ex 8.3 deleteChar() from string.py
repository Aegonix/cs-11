
#? Write a function deleteChar() which takes two
#? parameters one is a string and other is a character.
#? The function should create a new string after
#? deleting all occurrences of the character from the
#? string and return the new string.


def deleteChar(string: str, char: str) -> str:
    s = ""

    for i in string:
        if i != char:
            s += i

    return s


print(
    deleteChar(
        input("Enter a string: "),
        input("Enter a character to remove from the string: "),
    )
)
