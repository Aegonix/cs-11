
#? WAP that takes n number of students details and stores it in the form of a matrix.
#* [[roll_no, name, mobile_no, [marks of 5 subjects]], [next student], [next student...]]

n = int(input("Enter the number of students: "))

matrix: list[list[object]] = []

for i in range(1, n + 1):
    matrix += [[]]
    matrix[i - 1] += [int(input("Enter the roll number of student " + str(i) + ": "))]
    matrix[i - 1] += [input("Enter the name of student " + str(i) + ": ")]
    matrix[i - 1] += [int(input("Enter the mobile number of student " + str(i) + ": "))]
    marks = []
    for j in range(1, 6):
        marks += [float(input("Enter the marks of student " + str(i) + " for subject " + str(j) + ": "))]
    matrix += [marks]
    print()

print("The matrix is:")
for i in matrix:
    print(i)

#* finding guy with highest average
students_avg = []
for student in matrix:
    sum = 0
    for mark in student[3]:
        sum += mark
    
    avg = sum / 5 #* 5 subjects
    students_avg += [[student[1], avg]]

highest_avg = [0, 0]
for i in students_avg:
    if i[1] > highest_avg[1]:
        highest_avg = i

print(highest_avg[0], "is the topper with an average of:", highest_avg[1])