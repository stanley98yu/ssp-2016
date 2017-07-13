from math import *

#uses Newton's method to solve numerically for the eccentric anomaly E
def newton(M,e,guess):
    Ei = 0
    E = guess
    while abs(Ei - E) >= 1e-10:
        Ei = E
        E = E - (M - E + e*sin(E))/(-1+e*cos(E))
    return E
