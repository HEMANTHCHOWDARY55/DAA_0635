import time

def multiply_matrices(A, B):
    m = len(A)
    n = len(A[0])
    p = len(B[0])

    C = [[0] * p for _ in range(m)]

    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

    return C

# Test the program
A = [[1, 2, 3],
     [4, 5, 6]]

B = [[7, 8],
     [9, 10],
     [11, 12]]

start_time = time.time()
result = multiply_matrices(A, B)
end_time = time.time()

print("Resultant Matrix:")
for row in result:
    print(row)

print("Time taken:", end_time - start_time, "seconds")
