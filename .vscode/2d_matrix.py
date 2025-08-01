

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))


matrix = []

print("Enter the elements row-wise:")

for i in range(1,rows+1):
    row = []
    for j in range(1,cols+1):
        element = int(input(f"Enter element at [{i}][{j}]: "))
        row.append(element)
    matrix.append(row)


print("\nThe 2D Matrix is:")
for row in matrix:
    print(row)

