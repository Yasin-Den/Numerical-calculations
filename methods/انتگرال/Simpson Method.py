'''انتگرال گیری با روش سیمپسون مرکب'''
#a <= x <= b

from math import *

x = [1, 2, 3, 4, 5]
y = [0, -2.718281828459045, -34.99278805264069, -239.09114572975682, -1232.207119124943]

#a and b and n
if len(x) == 0 :
    a = 0.0000000001
    b = 1
    n = 10000000
else :
    a = x[0]
    b = x[-1]
    n = 0.5*len(x)

def f(x) :
    return (x+(1/x))

def append(a, b ,n) :
    h = (b - a) / (2*n)
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
    def sigma1() :
        sigma = 0
        i = 1
        while i <= n-2 :
            sigma += y[2*i]
            i += 1
        return sigma
    def sigma2() :
        sigma = 0
        i = 1
        while i <= n-1 :
            sigma += y[2*i - 1]
            i += 1
        return sigma
    h = abs(x[0]-x[1])
    return (h/3) * (y[0] + y[-1] + 2 * sigma1() + 4 * sigma2())

print ('integration of f :' ,integration())