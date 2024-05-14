
#? Case-based questions
#? Write a menu driven program that has options to
#? accept the marks of the student in five major 
#? subjects in Class X and display the same.
#? Calculate the sum of the marks of all subjects. 
#? Divide the total marks by number of subjects 
#? (i.e. 5), calculate percentage = total marks/5 
#? and display the percentage. 

#? Find the grade of the student as per the 
#? following criteria:
#* Criteria                                    Grade
#* percentage > 85                             A
#* percentage < 85 && percentage >= 75         B
#* percentage < 75 && percentage >= 50         C
#* percentage > 30 && percentage <= 50         D
#* percentage < 30                             Reappear

sum = 0
marks = {
    "Mathematics": int(input("Please enter marks of Mathematics: ")),
    "Science": int(input("Please enter marks of Science: ")),
    "English": int(input("Please enter marks of English: ")),
    "SST": int(input("Please enter marks of SST: ")),
    "Hindi/French": int(input("Please enter marks of Hindi/French: ")),
}

print("\nYour marks are: ")

for i in marks:
    print(i, "-", marks[i])

    sum += marks[i]

print("\nSum of your marks is:", sum, "out of 500.")
avg = sum / len(marks)
print("Average percentage is:", avg, end="\n\n")

if avg > 85:
    print("Grade: A")
elif avg >= 75:
    print("Grade: B")
elif avg >= 50:
    print("Grade: C")
elif avg >= 30:
    print("Grade: D")
else:
    print("Grade: Reappear")
