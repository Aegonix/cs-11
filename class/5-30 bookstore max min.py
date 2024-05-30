
#? WAP to take n number of books from the user (including type, name, and price)
#? and find the highest and lowest price book name.

n = int(input("Enter the number of books: "))

max = 0
min = 999999999999999999999999999999999999999999999999999999999999999999999999999
max_name = 0
min_name = 0
i = 0

while i < n:
    type = input("Enter the type of book: ")
    name = input("Enter the name of book: ")
    price = int(input("Enter the price of book: "))

    if price > max:
        max = price
        max_name = name

    if price < min:
        min = price
        min_name = name

    i += 1


print("The highest price book is", max_name, "with price", max)
print("The lowest price book is", min_name, "with price", min)
