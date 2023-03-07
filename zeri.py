from math import cos, pi
import time
time_sec = time.time()

def f(x: float) -> float:
    return x - cos(x)

def zeros(f: float, a: float, b: float, tol: float = 1e-10, itmax: int = 1e4) -> float | int:
    fa = f(a)
    fb = f(b)
    it: int = 0
    try:
        if fa * fb > 0:
            raise Exception("La funzione non cambia segno agli estremi dell'intervallo")
    except Exception:
        raise
    while b - a > tol and it < itmax:  
        c: float = (a + b) / 2
        fc = f(c)
        if fc == 0.00:
            break
        if fa * fc < 0:
            b = c
        elif fb * fc < 0:
            a = c
            fa = fc
        it += 1
    if (b - a > tol):
        print("Precisione non raggiunta")
    return c, it

ms = (time.time() - time_sec) * 1000

print(zeros(f, 0, pi/2), "Execution time: " + str(round(ms, 3)) + " ms")