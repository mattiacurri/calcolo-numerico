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

def dot_matrix(A: array, B: array):
    [m, n] = shape(A)
    [r, c] = shape(B)
    if n != r:
        raise ValueError("Dimensioni non compatibili")
    C = zeros(shape = (n, r))
    for i in range(0, m):
        for j in range(0, c):
            for k in range(0, n):
                C[i][j] += A[i][k] * B[k][j]
    return C

A = random.randint(2, 5, size=(3, 3))
print(A)
B = random.randint(2, 5, size=(3, 3))
print(B)
print(sum_matrix(A, B))
print(dot_matrix(A, B))