
#? WAP to test the divisibility of a number given by the user with another number.

divident = int(input("Enter divident: "))
divisor = int(input("Enter divisor: "))

if divident % divisor == 0:
    print("They are divisible.")

else:
    print("They are not divisible.")
