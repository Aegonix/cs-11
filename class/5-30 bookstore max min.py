
#? WAP to take n number of books from the user (including type, name, and price)
#? and find the highest and lowest price book name.

n = int(input("Enter the number of books: "))

max = 0
min = max
max_name = 0
min_name = 0

for i in range(n):
    name = input("Enter the name of book " + str(i + 1) + ": ")
    type = input("Enter the type of book " + str(i + 1) + ": ")
    price = int(input("Enter the price of book " + str(i + 1) + ": "))

    if not i:
        max = price
        min = price
        max_name = name
        min_name = name
    
    else:
        if price > max:
            max = price
            max_name = name

        if price < min:
            min = price
            min_name = name

print("The most expensive book is", max_name, "with price", max)
print("The cheapest book is", min_name, "with price", min)
