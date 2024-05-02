temp = float(input("Enter temp: "))

if temp >= 100:
    print("Gas")
elif temp <= 0:
    print("Solid")
else:
    print("Liquid")