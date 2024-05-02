monthly_sale = int(input("Enter monthly sale: "))

if monthly_sale >= 500000:
    print("You are eligible for 10% commission.")
    print("Your commission is", monthly_sale / 10)

elif monthly_sale >= 200000:
    print("You are eligible for 5% commission.")
    print("Your commission is", monthly_sale / 20)

else:
    print("You are not eligible for a commision.")
