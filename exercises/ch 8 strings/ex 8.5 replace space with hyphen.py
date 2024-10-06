
#? Write a function that takes a sentence as an input 
#? parameter where each word in the sentence is 
#? separated by a space. The function should replace 
#? each blank with a hyphen and then return the 
#? modified sentence.


def replace_space_with_hyphen(sentence: str) -> str:
    s = ""

    for i in sentence:
        if i == " ":
            s += "-"
        else:
            s += i

    return s


print(replace_space_with_hyphen(input("Enter a sentence: ")))
