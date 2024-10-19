
#? WAP to input a list and an element, and remove all occurences of the given element from the list.

l = eval(input("Enter list: "))
e = eval(input("Enter element to remove: "))
o: list[object] = [] #* output

for i in l:
    if i != e:
        o.append(i)

print(o)
