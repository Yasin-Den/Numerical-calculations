'''روش اولر'''
#f(x,y) = dy/dx
#a <= x <= b
#y(a) = y0 = w0

from math import *
N = 4
a = 0
b = 2
y0 = 0.5
h = (b - a)/N

def f(x, y) :
    return y + 1 - x**2

def Euler(a, b, y0, N) :
    X = [a]
    W = [y0]
    Euler = {}
    i = 1
    Euler[X[0]] = W[0]
    while X[-1] < b :
        W.append( W[i-1] + f(X[i-1], W[i-1]) * h )
        X.append(a + i*h)
        Euler[X[-1]] = W[i-1] + f(X[i-1], W[i-1]) * h
        i += 1
    #print (X, W)
    return (Euler)

print('Euler :' ,Euler(a, b, y0, N))