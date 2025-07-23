rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("\nEnter elements for Matrix 1:")
m1 = [[int(input(f"Element [{i+1}][{j+1}]: ")) for j in range(cols)] for i in range(rows)]

print("\nEnter elements for Matrix 2:")
m2 = [[int(input(f"Element [{i+1}][{j+1}]: ")) for j in range(cols)] for i in range(rows)]

result = [[m1[i][j] + m2[i][j] for j in range(cols)] for i in range(rows)]

print("\nResultant Matrix:")
for row in result:
    print(row)

