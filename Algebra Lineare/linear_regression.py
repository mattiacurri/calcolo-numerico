# approssimazione polinomiale e calcolo dell'indice di determinazione
from numpy import *
from matplotlib.pyplot import *
import warnings

def regression(x, y, yp, index):
    if index > 1 or index < 0:
        print("L'indice di determinazione deve essere compreso tra 0 e 1")
        return
    index_found = 0
    i = 0
    while index_found < index:
        xx = linspace(-100, 100, 1000000)
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
    legend(['Polinomio di grado ' + str(i - 1)])
    title('Approssimazione polinomiale di grado ' + str(i - 1) + ' con indice di determinazione ' + str(index_found))
    resize = get_current_fig_manager()
    resize.resize(1000, 600)
    show()
    return i - 1
    
    
m = 50 # numero di punti
x = linspace(-100, 100, m) # vettore delle ascisse
y = -x**3 + 2 * x**2 - 1 + x
yp = y + 0.021 * random.randn(m) # simulo la distorsione dei dati con un rumore gaussiano di media 0 e varianza 0.021
print(regression(x, y, yp, 0.9))