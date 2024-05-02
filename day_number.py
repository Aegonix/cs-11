days = ["SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"]

n = int(input("Enter day number: "))

if 1 <= n <= 7:
    print(days[n-1])
else:
    print("Invalid day number")