sales = int(input("Enter sales: "))

if sales >= 500000:
    print("Commission:", sales / 10)
elif sales >= 200000:
    print("Commission:", sales / 20)
else:
    print("Commission: 0")