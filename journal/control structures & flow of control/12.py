
#? WAP to check the validity of a date.

year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
day = int(input("Enter the day: "))

false_date = False

if year < 0:
    print("This date is not valid.")
    false_date = True

if not false_date and (month > 12 or month < 1):
    print("This date is not valid.")
    false_date = True

if not false_date and ((day > 31 or day < 0) or (day > 30 and (month == 4 or month == 6 or month == 9 or month == 11))):
    print("This date is not valid.")
    false_date = True

if not false_date:
    print("This date is valid.")
