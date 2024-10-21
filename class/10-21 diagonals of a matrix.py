
#? WAP to print the diagonals of a matrix.

matrix = [[1, 2], [3, 4]] #* example
for i in range(len(matrix)):
    print(" " * i + str(matrix[i][i]))

for i in range(len(matrix)):
    print(" " * (len(matrix) - i - 1) + str(matrix[i][len(matrix) - i - 1]))