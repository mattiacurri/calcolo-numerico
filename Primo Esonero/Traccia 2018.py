from numpy import array, transpose
"""
    Traccia: Scrivere una funzione che abbia in input una matrice A con elementi interi compresi tra 0 e 9 e un vettore x la cui lunghezza non superi ciascuna delle dimensioni di A.
    La funzione dovrà restituire in output una variabile logica s che assuma valore True se il vettore x lo si ritrova all'interno di una riga o di una colonna di A, False altrimenti
"""

def contenuto(A, x):
    found = False
    if len(x) <= A.shape[0] and len(x) <= A.shape[1]:
        for i in range(0, A.shape[0]):
            if found:
                break
            for z in range(0, A.shape[1]-len(x)):
                if found:
                    break
                for y in range(0, len(x)):
                    if A[i][z] == x[y]:
                        found = True
                        z += 1
                    else:
                        found = False
                        break    
    return found

def contenuto_a(A, x):
    return contenuto(A, x) or contenuto(transpose(A), x)

A = array([[7, 5, 9, 2, 3, 1, 6, 1, 4, 1], 
           [2, 7, 8, 3, 2, 8, 9, 9, 8, 4], 
           [6, 9, 8, 8, 3, 9, 4, 1, 1, 2], 
           [6, 1, 4, 7, 5, 7, 5, 1, 8, 6], 
           [5, 1, 9, 5, 1, 7, 8, 2, 9, 4], 
           [6, 2, 2, 3, 8, 2, 1, 1, 2, 1], 
           [5, 3, 4, 9, 5, 1, 6, 3, 9, 9], 
           [5, 4, 1, 5, 8, 9, 5, 9, 7, 9],
           [5, 1, 2, 3, 4, 9, 8, 8, 7, 1],
           [7, 9, 7, 9, 2, 8, 1, 1, 7, 4]])

x = [9, 7, 7, 2, 1, 9]
print(contenuto_a(A, x))
x = [9, 7, 9, 2, 8, 1, 1]
print(contenuto_a(A, x))
x = [1, 1, 2, 2, 1]
print(contenuto_a(A, x))
