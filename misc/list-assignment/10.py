
#? To input 10 names into a list, and search for a name.

names: list[str] = []

for i in range(10):
    names.append(input("Enter name " + str(i + 1) + ": "))

name = input("Enter name to search: ")

for i in names:
    if i == name:
        print("Yes, '", name, "' is in the list.", sep="")
        break
else:
    print("No, '", name, "' is not in the list.", sep="")
