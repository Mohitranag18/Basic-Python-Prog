# Function to take matrix input from the user
def input_matrix(rows, cols):
    matrix = []
    print(f"Enter the elements of {rows}x{cols} matrix:")
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(int(input(f"Element [{i+1}][{j+1}]: ")))
        matrix.append(row)
    return matrix

# Function to print a matrix
def print_matrix(matrix):
    for row in matrix:
        print(row)

# Function for matrix addition
def add_matrices(matrix1, matrix2, rows, cols):
    result = [[matrix1[i][j] + matrix2[i][j] for j in range(cols)] for i in range(rows)]
    return result

# Function for matrix multiplication
def multiply_matrices(matrix1, matrix2, rows1, cols1, rows2, cols2):
    if cols1 != rows2:
        return "Matrix multiplication is not possible due to incompatible dimensions."
    
    result = [[sum(matrix1[i][k] * matrix2[k][j] for k in range(cols1)) for j in range(cols2)] for i in range(rows1)]
    return result

# Main function
def main():
    # Taking input for the first matrix
    rows1 = int(input("Enter number of rows for the first matrix: "))
    cols1 = int(input("Enter number of columns for the first matrix: "))
    matrix1 = input_matrix(rows1, cols1)

    # Taking input for the second matrix
    rows2 = int(input("Enter number of rows for the second matrix: "))
    cols2 = int(input("Enter number of columns for the second matrix: "))
    matrix2 = input_matrix(rows2, cols2)

    # Matrix addition
    if rows1 == rows2 and cols1 == cols2:
        added_matrix = add_matrices(matrix1, matrix2, rows1, cols1)
        print("\nMatrix Addition Result:")
        print_matrix(added_matrix)
    else:
        print("\nMatrix addition is not possible due to incompatible dimensions.")

    # Matrix multiplication
    multiplied_matrix = multiply_matrices(matrix1, matrix2, rows1, cols1, rows2, cols2)
    print("\nMatrix Multiplication Result:")
    if isinstance(multiplied_matrix, str):  # In case of incompatible dimensions
        print(multiplied_matrix)
    else:
        print_matrix(multiplied_matrix)

if __name__ == "__main__":
    main()
