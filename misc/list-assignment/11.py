
#? WAP to enter 10 names and print all the names starting with "A".

names: list[str] = []

for i in range(10):
    names.append(input("Enter name " + str(i + 1) + ": "))

for name in names:
    if ord(name[0]) == 65 or ord(name[0]) == 97:
        print(name)
