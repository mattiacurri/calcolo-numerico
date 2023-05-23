# approssimazione polinomiale e calcolo dell'indice di determinazione
from numpy import *
from matplotlib.pyplot import *
import warnings

def regression(x, y, yp, index):
    index_found = 0
    i = 0
    while index_found < index:
        xx = linspace(-10, 10, 10000)
        with warnings.catch_warnings():
            warnings.filterwarnings('error')
            try:
                p = polyfit(x, yp, i) # polinomio di migliore appossimazione di grado i
            except RankWarning:
                print("Non è possibile approssimare correttamente con un polinomio di grado", i)
                print("Diminuire l'indice di determinazione")
                return i - 1
        pxx = polyval(p, xx) # valuto il polinomio nei punti del vettore xx
        index_found = var(polyval(p, x)) / var(yp)
        i += 1
    plot(xx, pxx)
    plot(x, y, 'ro', x, yp, 'bo', markersize=4)
    show()
    return i
    
    
m = 11 # numero di punti
x = linspace(-10, 10, m) # vettore delle ascisse
y = 1/(1 + x**2) # funzione di Runge 
yp = y + 0.021 * random.randn(m) # simulo la distorsione dei dati con un rumore gaussiano di media 0 e varianza 0.021
print(regression(x, y, yp, 0.7))