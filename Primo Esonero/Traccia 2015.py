from numpy import array, transpose, all
A = array([[-2, -1, 2], [9, -1, 3], [-1, -1, -1]])
A = array([[1, 1, 1], [1, 2, 3], [1, 4, 5]])

""" 
Si scriva una funzione che abbia in input una matrice A quadrata a coefficienti interi, e in output una variabile logica s così definita:
    s = True se A possiede una riga e una colonna uguali 
    s = False altrimenti
"""
# [1,1,1][1,2,3][1,4,5]
def check(A, B):
    x = False
    for i in range(A.shape[0]):
        for z in range(B.shape[0]):
            if x:
                break
            for j in range(B.shape[0]):
                if A[i][j] == B[z][j]:
                    x = True
                else:
                    x = False
                    break
    return x

def find(A):
    B = transpose(A)
    print(A)
    print(B)
    s = False
    if check(A, B):
        s = True
    """In alternativa dovrebbe funzionare anche questo:
    for i in range(A.shape[0]):
        for j in range(B.shape[0]):
            if all(A[i] == B[j]):
                s = True
                break"""
    return s

print(find(A))

