import numpy

""" Formula di Leibniz per approssimare il pigreco """
def leibniz(tol, itmax):
    a = 0
    npassi = 0
    it = 1
    arresto = 0
    while not arresto and it < itmax:
        if it % 2 == 1 and npassi % 2 == 0:
            a += 1/it
            npassi += 1
        elif it % 2 == 1 and npassi % 2 == 1:
            a -= 1/it
            npassi += 1
        it += 1
        arresto = abs((4 * a) - numpy.pi) < tol
    return (4 * a)

print(leibniz(10e-5, 1000))