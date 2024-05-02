name = input("Enter a name: ")
p = int(input("Enter physics: "))
c = int(input("Enter chem: "))
m = int(input("Enter maths: "))
cs = int(input("Enter CS: "))
e = int(input("Enter eng: "))

total = p + c + m + cs + e
print("Total is", total)
print("Percentage: ", total/500 * 100)