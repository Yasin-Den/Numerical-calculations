'''روش رانگ کوتای مرتبه 2'''
#f(x,y) = dy/dx
#a <= x <= b
#y(a) = y0 = w0

from math import *
N = 2
a = 1
b = 2
y0 = 0
h = (b - a)/N

def f(x, y) :
    return ((y**2)/x) + (1/x)

def w(x, w) :
    w_h = w + f(x, w) * h
    return w + 0.5 * h * (f(x, w) + f(x+h, w_h))

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

print ('Rung kuta 2nd :' ,Rung())