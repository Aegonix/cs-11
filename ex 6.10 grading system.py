
#? 10.
#? Write a program to find the grade of a student when  
#? grades are allocated as given in the table below. 

#* Percentage of Marks   Grade
#?* Above 90%            A
#?* 80% to 90%           B
#?* 70% to 80%           C
#?* 60% to 70%           D
#?* Below 60%            E

#? Percentage of the marks obtained by the student is input 
#? to the program.

percent = float(input("Enter your percentage marks: "))

if percent >= 90:
    print("Grade: A")

elif percent >= 80:
    print("Grade: B")

elif percent >= 70:
    print("Grade: C")

elif percent >= 60:
    print("Grade: D")

else:
    print("Grade: E")
