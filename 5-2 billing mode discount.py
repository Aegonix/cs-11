
#? WAP to enter bill amount and ask the user their payment mode and give discount based on payment mode.
#? Also display the net payable amount.

#? Mode:
#? Credit card - 10% discount
#? Debit card - 5% discount
#? Net banking - 2% discount
#? otherwise - No discount

bill = float(input("Enter billing amount: "))
mode = input("Enter your mode of payment: ")

if mode.lower() == ("credit card"):
    discount = bill / 10
    print("Your payable amount is:", (bill - discount))

elif mode.lower() == ("debit card"):
    discount = bill / 20
    print("Your payable amount is:", (bill - discount))

elif mode.lower() == ("net banking"):
    discount = bill / 50
    print("Your payable amount is:", (bill - discount))

else:
    print("Your payable amount is:", bill)
