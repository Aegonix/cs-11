
#? WAP to enter bill amount and ask the user their payment mode and give discount based on payment mode.
#? Also display the net payable amount.

#? Mode:
#? Credit card - 10% discount
#? Debit card - 5% discount
#? Net banking - 2% discount
#? otherwise - No discount

bill = float(input("Enter billing amount: "))
mode = input("""Enter your mode of payment: 
c/C - Credit Card
d/D - Debit Card
n/N - Net Banking
o/O - Other
> """)

if mode.lower() == "c":
    discount = bill / 10
    print("Your payable amount is:", (bill - discount))

elif mode.lower() == "d":
    discount = bill / 20
    print("Your payable amount is:", (bill - discount))

elif mode.lower() == "n":
    discount = bill / 50
    print("Your payable amount is:", (bill - discount))

elif mode.lower() == "o":
    print("Your payable amount is:", bill)

else:
    print("Please enter a valid payment method.")
