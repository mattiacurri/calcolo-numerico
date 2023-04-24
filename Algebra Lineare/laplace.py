from numpy import *

def laplace(A):
    [m, n] = shape(A)
    if n == 1:
        detA = A[0][0]
    else:
        detA = 0
        for j in range(0, n):
            A1j = delete(A, 0, axis=0)
            A1j = delete(A1j, j, axis = 1)
            detA += ((-1)**(j) * A[0][j] * laplace(A1j))
    return detA

A = random.rand(3, 3)
print(A)
print("Laplace: " + str(laplace(A)))    
print("Determinante linalg.det(A): " + str(linalg.det(A)))