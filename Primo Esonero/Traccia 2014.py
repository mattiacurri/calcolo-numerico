print(5 + (1/(4 + 1/(6 + 1/7))))

""" La traccia richiedeva di implementare una funzione che a partire da un vettore x restituisca in output il valore della frazione continua """

x = [3, 4, 12, 4]
x = [5, 4, 6, 7]
i = len(x) - 1
fr = x[i]
print(fr)
while i >= 0:
    fr = x[i] + 1/fr
    i -= 1
    
print(fr)