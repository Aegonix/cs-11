
#? WAP to display the sum of elements row wise and column wise of an n x n matrix.

#* Consider matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range(len(matrix)):
    row_sum = 0
    cols_sum = 0

    for j in matrix[i]:
        row_sum += j

    for j in matrix:
        cols_sum += j[i]

    print("The sum of row", (i + 1), "is:", row_sum)
    print("The sum of column", (i + 1), "is:", cols_sum)
