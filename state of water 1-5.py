temp = float(input("Enter temperature of water: "))

if temp <= 0:
    print("Solid (Ice)")

elif temp < 100:
    print("Liquid")

else:
    print("Gas")