from math import log2, ceil
from ..utils.math_funct import *

def abs_stop(a, b, tol):
    """ Stop per l'errore assoluto """
    return max(a, b) - min(a, b) < tol

def rel_stop(a, b, tol):
    """ Stop per l'errore relativo """
    try:
        return (max(a, b) - min(a, b))/min(abs(a), abs(b)) < tol
    except ZeroDivisionError:
        raise ZeroDivisionError("Ho provato a dividere per zero, usare l'errore misto")
    
def mix_stop(a, b, tol):
    """ Stop per l'errore misto """
    return (max(a, b) - min(a, b))/(1 + min(abs(a), abs(b))) < tol

def_error = {"abs": abs_stop, "rel": rel_stop, "mix": mix_stop} # Dizionario delle tipologie di errore disponibili

def zeros(f: float, a: float, b: float, tol: float = 1e-10, itmax: int = 1e4, option: str = "abs") -> float | int:
    """ Calcola lo zero di una funzione utilizzando il metodo delle successive bisezioni
        Keyword arguments:
        f - funzione di cui calcolare lo zero
        a - primo termine dell'intervallo da considerare della funzione
        b - secondo termine dell'intervallo da considerare della funzione
        tol - precisione richiesta (default = 1e-10)
        itmax - numero di iterazioni massime (default = ie4)
        option - tipo di errore da utilizzare (default = "abs")
    """
    # show_plot(f)
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
            raise KeyError(f"Immettere un valore corretto: {def_error.keys()}")
    except KeyError:
        raise
    if option == "abs":
        steps_to_precision = log2((b - a)/tol) 
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
        if option == "abs":
            print(f"Per raggiungere la precisione richiesta sono necessari {ceil(steps_to_precision)} passi")
    return c, it

""" Metodo di Newton """
def newton(f: float, x0: float, tol: float = 1e-10, itmax: int = 10e4):
    it = 0
    arresto = False
    while not(arresto) and it < itmax:
        it += 1
        x1 = x0 - (f(x0)/f(x0, 1))
        arresto = abs(x1 - x0) < tol
        x0 = x1
    if not arresto:
        print("Precisione non raggiunta")
    return x1, it