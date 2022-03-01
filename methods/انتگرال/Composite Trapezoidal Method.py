'''انتگرال گیری با روش ذوزنقه ای مرکب'''
#a <= x <= b

from math import *

n = 2
x = []
y = []

#a and b
if len(x) == 0 :
    a = 1
    b = 2
else :
    a = x[0]
    b = x[-1]

def f(x) :
    return log(x)

def append(a, b ,n) :
    h = (b - a) / n
    if len(x) == 0 :
        while a <= b :
            x.append(a)
            a += h
    if len(y) == 0 :
        for i in x :
            y.append(f(i))
append(a, b, n)
#print (x, y)

def integration() :
    def sigma() :
        sigma = 0
        i = 1
        while i <= n-2 :
            sigma += y[i]
            i += 1
        return sigma
    h = (b - a) / n
    return (h/2) * (f(a) + f(b) + 2 * sigma())
print ('integration of f :' ,integration())
