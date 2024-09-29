
#? Write a program to input n names and print the largest name.

option = ""
i = 0
largest_name = ""

while True:
    name = input("Enter a name (type 'stop' to stop entering names): ")

    if name == "stop":
        break

    elif i == 0:
        largest_name = name

    elif len(name) > len(largest_name):
        largest_name = name

    i += 1

print("The largest name is:", largest_name)
