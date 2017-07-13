from math import *

#evaluates a definite integral using midpoint Riemann sum
def integral(a, b, exp,n):
    #takes the sum of the areas of n rectangles
    intv = (b-a)/float(n)
    sum = 0
    x = a + intv/2.
    while x < b:
        sum += eval(exp)*intv
        x += intv
    return sum
