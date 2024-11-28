row = int(input("Enter no. of Rows: "))
col = int(input("Enter no. of Columns: "))

matrix = [[],[]]
for i in range(row):
    for j in range(col):
        matrix[i][j] = int(input("Enter value: ",))

