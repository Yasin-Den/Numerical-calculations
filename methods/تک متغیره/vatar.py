'''روش وتر'''
from math import *

def f(x) :
    return (2*x) - 1 + (e**(-2*x))


def vatar(x0,x1,epsilon) :
    #List of x
    x = [x0,x1]
    #x(n+1)
    n = 1
    while not (abs (f(x[n])) <= epsilon) :
        x.append(x[n] - ( f(x[n]) / ((f(x[n]) - f(x[n-1])) / (x[n] - x[n-1]) )))
        n += 1
    print ('x :', x)
    #print ('x_n :', '%.4f'% x[-1])
    return x[-1]

print (vatar(1,1.5,0.0001))