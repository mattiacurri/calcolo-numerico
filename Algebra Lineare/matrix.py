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
    if m != n:
        raise ValueError("La matrice non e' quadrata")
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

def solve_triup(A, b):
    if not is_triang_up(A):
        raise ValueError("La matrice non e' triangolare superiore")
    n = len(A)
    x = zeros(shape=(n, 1))
    for i in range(n - 1, -1, -1):
        if abs(A[i][i]) < 1e-15:
            raise ValueError("Matrice singolare")
        part_sum = 0
        for j in range(i + 1, n):
            part_sum += (A[i][j] * x[j])
        x[i] = (b[i] - part_sum)/A[i][i]
    return x

def fattLU(A):
    [m, n] = shape(A)
    if m != n:
        raise ValueError("Matrice non quadrata")
    A = copy(A)
    L = identity(n)
    for k in range(0, n - 1):
        for i in range(k + 1, n):
            if abs(A[k][k]) < 1e-15:
                raise ZeroDivisionError("Divisione per zero")
            mik = - A[i][k]/A[k][k]
            for j in range(k + 1, n):
                A[i][j] = A[i][j] + (mik * A[k][j])
            L[i][k] = -mik
    U = triu(A)
    return L, U

def gauss_elim(A, b):
    [m, n] = shape(A)
    if m != n:
        raise ValueError("Matrice non quadrata")
    A = copy(A)
    b = copy(b)
    L = identity(n)
    for k in range(0, n - 1):
        for i in range(k + 1, n):
            if abs(A[k][k]) < 1e-15:
                raise ZeroDivisionError("Divisione per zero")
            mik = - A[i][k]/A[k][k]
            b[i] = b[i] + (mik * b[k])
            for j in range(k + 1, n):
                A[i][j] = A[i][j] + (mik * A[k][j])
            L[i][k] = -mik
    U = triu(A)
    return solve_triup(U,b)

def gauss_elim_pivot(A, b):
    [m, n] = shape(A)
    if m != n:
        raise ValueError("Matrice non quadrata")
    A = copy(A)
    b = copy(b)
    L = identity(n)
    for k in range(0, n - 1):
        for i in range(k + 1, n):
            if abs(A[k][k]) < 1e-15:
                raise ZeroDivisionError("Divisione per zero")
            s = k
            piv = abs(A[k][k])
            if (abs(A[i][k] > piv)):
                s = i
                piv = abs(A[i][k])
            if s != k:
                A[[k][s]] = A[[s][k]]
                b[k], b[s] = b[s], b[k]
            mik = - A[i][k]/A[k][k]
            b[i] = b[i] + (mik * b[k])
            for j in range(k + 1, n):
                A[i][j] = A[i][j] + (mik * A[k][j])
            L[i][k] = -mik
    U = triu(A)
    return solve_triup(U,b)

# gauss, gauss con pivot, inversa con LU, riduzione a scalini, calcolo rank
"""A = array([[1, 2, 3, 4], [0, 3, 1, 3], [0, 0, 9, 4], [0, 0, 0, 4]])
B = array([[2, -1, -3], [-4, 4, -4], [-1, -4, -5]])
print(is_triang_up(A))
b = array([4, 5, 6, 7])
print(solve_triup(A, b))
print(B)
[L, U] = fattLU(B)
print(L)
print(U)"""
A = array([[1, -2, 0, 1],[0, -1, 2, 1], [0, 1, 0, 0], [0, 0, 0, -1]])
b = array([-1, -1, 3, 1])
print(gauss_elim(A, b))
print(gauss_elim_pivot(A, b))