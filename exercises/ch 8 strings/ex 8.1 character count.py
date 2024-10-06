
#? Write a program to input line(s) of text from the user until enter is pressed.
#? Count:
#* the total number of characters in the text (including white spaces), 
#* total number of alphabets,
#* total number of digits, 
#* total number of special symbols
#* and total number of words in the given text.
#? (Assume that each word is separated by one space).

s = input("Enter text: ")
alphabet_count = 0
digit_count = 0
special_count = 0
word_count = 1

if s == "":
    word_count = 0

for i in s:
    if (65 <= ord(i) <= 90) or (95 <= ord(i) <= 122):
        alphabet_count += 1
    elif 48 <= ord(i) <= 57:
        digit_count += 1
    elif i != " ":
        special_count += 1
    else:
        word_count += 1

print("Total number of characters:", len(s))
print("Total number of alphabets:", alphabet_count)
print("Total number of digits:", digit_count)
print("Total number of special symbols:", special_count)
print("Total number of words:", word_count)
