from numpy import *

def sum_matrix(A: array, B: array):
    [m, n] = shape(A)
    [r, c] = shape(B)
    if m != r or n != c:
        raise ValueError("Dimensioni non compatibili")
    C = zeros(shape(A))
    for i in range(0, m):
        for j in range(0, n):
            C[i][j] = A[i][j] + B[i][j]
    return C
A = random.randint(20, size=(4, 4))
print(A)
B = random.randint(20, size=(4, 4))
print(B)
print(sum_matrix(A, B))