
#? WAP that takes n number of students details and stores it in the form of a matrix.
#* [[roll_no, name, mobile_no, [marks of 5 subjects]], [next student], [next student...]]

n = int(input("Enter the number of students: "))

matrix: list[list[object]] = []

for i in range(1, n + 1):
    matrix += [[]]
    matrix[i - 1] += [int(input("Enter the roll number of student " + str(i) + ": "))]
    matrix[i - 1] += [input("Enter the name of student " + str(i) + ": ")]
    matrix[i - 1] += [int(input("Enter the mobile number of student " + str(i) + ": "))]
    for j in range(1, 6):
        matrix[i - 1] += [float(input("Enter the marks of student " + str(i) + " for subject " + str(j) + ": "))]

    print()

print("The matrix is:")
for i in matrix:
    print(i)
