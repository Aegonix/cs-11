

#? Write a program to input n names and print the names with the least number of characters.

shortest_name = ""
i = 0

while True:
    name = input("Enter a name (type 'stop' to stop entering names): ")

    if name == "stop":
        break

    elif i == 0:
        shortest_name = name

    elif len(name) < len(shortest_name):
        shortest_name = name

    i += 1

print("The shortest name is:", shortest_name)
