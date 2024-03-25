def split_matrix(matrix):
    n = len(matrix)
    mid = n // 2
    upper_left = [[matrix[i][j] for j in range(mid)] for i in range(mid)]
    upper_right = [[matrix[i][j] for j in range(mid, n)] for i in range(mid)]
    lower_left = [[matrix[i][j] for j in range(mid)] for i in range(mid, n)]
    lower_right = [[matrix[i][j] for j in range(mid, n)] for i in range(mid, n)]
    return upper_left, upper_right, lower_left, lower_right

def add_matrices(A, B):
    n = len(A)
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = A[i][j] + B[i][j]
    return result

def subtract_matrices(A, B):
    n = len(A)
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = A[i][j] - B[i][j]
    return result

def strassen_multiply(A, B):
    n = len(A)
    # Base case: If the matrix size is 1, directly multiply the elements
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    # Divide matrices into submatrices
    A11, A12, A21, A22 = split_matrix(A)
    B11, B12, B21, B22 = split_matrix(B)

    # Calculate Strassen's intermediate matrices
    P1 = strassen_multiply(A11, subtract_matrices(B12, B22))
    P2 = strassen_multiply(add_matrices(A11, A12), B22)
    P3 = strassen_multiply(add_matrices(A21, A22), B11)
    P4 = strassen_multiply(A22, subtract_matrices(B21, B11))
    P5 = strassen_multiply(add_matrices(A11, A22), add_matrices(B11, B22))
    P6 = strassen_multiply(subtract_matrices(A12, A22), add_matrices(B21, B22))
    P7 = strassen_multiply(subtract_matrices(A11, A21), add_matrices(B11, B12))

    # Calculate the resulting submatrices
    C11 = add_matrices(subtract_matrices(add_matrices(P5, P4), P2), P6)
    C12 = add_matrices(P1, P2)
    C21 = add_matrices(P3, P4)
    C22 = subtract_matrices(subtract_matrices(add_matrices(P5, P1), P3), P7)

    # Combine the resulting submatrices into the result matrix
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n // 2):
        for j in range(n // 2):
            result[i][j] = C11[i][j]
            result[i][j + n // 2] = C12[i][j]
            result[i + n // 2][j] = C21[i][j]
            result[i + n // 2][j + n // 2] = C22[i][j]
    return result

# Test the program
A = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]

B = [[17, 18, 19, 20],
     [21, 22, 23, 24],
     [25, 26, 27, 28],
     [29, 30, 31, 32]]

result = strassen_multiply(A, B)
print("Resultant Matrix:")
for row in result:
    print(row)
