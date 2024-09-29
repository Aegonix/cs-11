
#? WAP to write a program to input percentage marks of a student and find the grade as per mark.

percent = float(input("Enter your percentage marks: "))

if percent > 100 or percent < 0:
    print("Please enter a valid percentage.")

elif percent >= 91:
    print("A1 grade")

elif percent >= 81:
    print("A2 grade")

elif percent >= 71:
    print("B1 grade")

elif percent >= 61:
    print("B2 grade")

elif percent >= 51:
    print("C1 grade")

elif percent >= 41:
    print("C2 grade")

elif percent >= 33:
    print("D grade")

else:
    print("E grade")
