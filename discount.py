bill = float(input("Enter bill amount: "))

print("C - Credit Card\nD - Debit Card\nN - Net Banking\nO - Other")
mode = input("Enter mode: ")

discount = 0

if mode == "C":
    discount = 10/100
elif mode == "D":
    discount = 5/100
elif mode == "N":
    discount = 2/100
elif mode == "O":
    discount = 0
else:
    print("Invalid Mode")
    exit()

print("Payable amount:", bill * (1 - discount))