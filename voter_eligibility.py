age_str = input("Age: ")

if age_str.isdigit():
    age = int(age_str)
    if age >= 18:
        print("Eligible to vote")
    else:
        print("Not eligible to vote")

else:
    print("Input a valid age")