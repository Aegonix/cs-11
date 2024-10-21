
#? WAP to find salesman's comission.
#? If his monthly sale is more than 5 lakh, then commission will be 10% of the monthly sale.
#? If it is less than 5 lakh but more than 2 lakh, then commission will be 5% of the monthly sale.
#? If it is under 2 lakh, then no commission.

monthly_sale = int(input("Enter monthly sale: "))

if monthly_sale >= 500000:
    print("You are eligible for 10% commission.")
    print("Your commission is", monthly_sale / 10)

elif monthly_sale >= 200000:
    print("You are eligible for 5% commission.")
    print("Your commission is", monthly_sale / 20)

else:
    print("You are not eligible for a commision.")
