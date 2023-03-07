from math import cos, pi

def f(x: float) -> float:
    return x - cos(x)

def abs_stop(a, b, tol):
    return max(a, b) - min(a, b) < tol

def rel_stop(a, b, tol):
    try:
        return (max(a, b) - min(a, b))/min(abs(a), abs(b)) < tol
    except ZeroDivisionError:
        raise ZeroDivisionError("Ho provato a dividere per zero, usare l'errore misto")
    
def mix_stop(a, b, tol):
    return (max(a, b) - min(a, b))/(1 + min(abs(a), abs(b))) < tol

def_error = {"abs": abs_stop, "rel": rel_stop, "mix": mix_stop}

def zeros(f: float, a: float, b: float, tol: float = 1e-10, itmax: int = 1e4, option: str = "abs") -> float | int:
    fa = f(a)
    fb = f(b)
    it: int = 0
    try:
        if fa * fb > 0:
            raise Exception("La funzione non cambia segno agli estremi dell'intervallo")
    except Exception:
        raise
    try:
        if option not in def_error:
            raise KeyError("Immettere un valore corretto: abs, rel o mix")
    except KeyError:
        raise
    while not def_error[option](a, b, tol) and it < itmax:  
        c: float = (a + b) / 2
        fc = f(c)
        if fc == 0.00:
            break
        if fa * fc < 0:
            b = c
        else:
            a = c
            fa = fc
        it += 1
    if (not def_error[option](a, b, tol)):
        print("Precisione non raggiunta")
    return c, it
