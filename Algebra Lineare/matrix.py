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

def is_triang_up(A):
    is_triang = False
    ex = False
    [m, n] = shape(A)
    for i in range(0, m):
        if ex:
            break
        for j in range(0, i):
            if i > j:
                if A[i][j] == 0:
                    is_triang = True
                else:
                    is_triang = False
                    ex = True
                    break
    return is_triang
                    
A = array([[1, 2, 3], [0, 5, 6], [0, 0, 9]])
print(A)
B = random.randint(2, 5, size=(3, 3))
print(B)
print(is_triang_up(A))