from numpy import *

"""
Si scriva una function che abbia:
INPUT: A, matrice quadrata;
OUTPUT: B, matrice quadrata ottenuta da A mediante una permutazione delle sue colonne così definita: la prima colonna di B coincide con la colonna di A che contiene il maggior numero di zeri; tra le n - 1 colonne rimanenti di A si seleziona quella che contiene il maggior numero di zeri e la si pone come seconda colonna di B, e così via per la terza, quarta, ..., n-esima colonna di B
"""
a = array([[1, 1, 5, 0], [9, 7, 0, 0], [1, 2, -1, 1], [0, 1, 0, 0]])

# Transpose the matrix
b = transpose(a)
print(b)

# Create an empty list
index = []
# Iterate over the rows of the matrix
for i in range(0, b.shape[0]):
    # Count the number of zeros in the row
    x = (b[i]==0).sum()
    # Append the row index and the number of zeros to the list
    index.append((i, x))

# Sort the list of tuples by the number of zeros in descending order
index.sort(reverse=True, key=lambda a: a[1])
print(index)
