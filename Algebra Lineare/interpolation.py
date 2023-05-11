from numpy import *
import matplotlib.pyplot as plot

def lagrange(x, y, xx):
    """
    Determina il polinomio interpolante di Lagrange pn(x) nei punti (x(i), y(i)) e lo valuta nei punti xx(i)
    
    Parametri di input
        x: vettore dei nodi
        y: vettore delle ordinate
        xx: vettore di ascisse in cui valutare pn(x)
    
    Parametri di output
        yy: vettore delle valutazioni di pn(x) nelle ascisse xx(i)
    """
    yy = 0
    n = shape(x)[0]
    for k in range(0, n):
        Lk = 1
        for i in range(0, n):
            if i != k:
                Lk *= (xx - x[i])/(x[k]-x[i])
        yy += (Lk * y[k])
    return yy

x = [-1, 0, 1, 2]
y = [2, 1, 3, 0]
xx = linspace(-1, 2, 100)
print(lagrange(x, y, xx))


