'''روش رانگ کوتای مرتبه 3'''
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
    return -(x**2) + y+1

def w(x, w) :
    k1 = f(x, w)
    k2 = f(x+0.5*h, w+0.5*h*k1)
    k3 = f(x+h, w-h*k1+2*h*k2)
    return w + (1/6) * h * (k1 + 4*k2 + k3)

def Rung() :
    X = [a]
    W = [y0]
    Rung = {}
    x = a
    i = 1
    Rung[X[0]] = W[0]
    while X[-1] < b :
        W.append(w(x, W[i-1]))
        X.append(a + i * h)
        Rung[a + i * h] = w(x, W[i-1])
        x = a + i * h
        i += 1
    #print (X, W)
    return (Rung)

print ('Rung kuta 3th :' ,Rung())