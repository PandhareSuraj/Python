print("Enter elements of 2x2 matrix:")
matrix = []
for i in range(2):
    row = list(map(int, input().split()))
    matrix.append(row)

transpose = []
for i in range(2):
    row = []
    for j in range(2):
        row.append(matrix[j][i])
    transpose.append(row)

print("Transpose of the matrix is:")
for row in transpose:
    print(*row)

