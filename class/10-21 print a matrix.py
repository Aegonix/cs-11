
#? WAP to create a matrix (of n dimensions) and print it, using values from the user.
#*[[1, 2], [1, 2]] === [1, 2]
#*                     [1, 2]

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

matrix: list[list[object]] = []

for i in range(1, rows + 1):
    matrix += [[]]
    for j in range(1, cols + 1):
        matrix[i - 1] += [input("Enter a value for row " + str(i) + ", column " + str(j) + ": ")]
    
    print()

print("The matrix is:")
for i in matrix:
    print(i)
