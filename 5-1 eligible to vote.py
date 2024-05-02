age = input("Enter your age: ")

if age.isdigit():
    if int(age) >= 18:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")

else:
    print("Please input a proper digit.")
