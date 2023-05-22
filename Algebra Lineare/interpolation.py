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

#plot.plot(xx, lagrange(x, y, xx), 'b', x, y, 'ro') 
#plot.show()

def interpolation(f, apx, n):
    """
    Interpolazione polinomiale di una funzione
    Parametri di input
    f: funzione (eventualmente inline)
    apx: intervallo di approssimazione
    n: numero di nodi equidistanti che ricoprono l'intervallo apx
    """
    a = apx[0]
    b = apx[1]
    x = linspace(a, b, n)
    y = f(x) # vettore delle ordinate
    xx = linspace(a, b, 100)
    yy = lagrange(x, y, xx)
    fxx = f(xx)
    # plot the interpolating polynomial
    plot.plot(x, y, 'ro', xx, fxx, xx, yy)
    plot.legend(['nodi', 'f(x)', 'p(x)'])
    plot.grid(True)
    plot.title('Interpolazione polinomiale di Lagrange')
    plot.xlabel('x')
    plot.ylabel('y')
    plot.show()

def f(x):
    return e**(-x)*sin(x)

apx = [0, pi]
n = 5
interpolation(f, apx, n)
 