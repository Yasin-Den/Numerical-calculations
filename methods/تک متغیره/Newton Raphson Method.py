'''روش نیوتن رافسون'''
#ekhtar : dar extermom mahali javab nemide

from math import e

def f(x) :
    return (2*x) - 1 + (e**(-2*x))

def df(x) :
    return 2 + (e**(-2*x)) * (-2*x)


#Newton Raphson Method
def Newton_Raphson(x0,epsilon) :
    #List of x
    x = [x0]
    #x(n+1)
    n = 0
    while not (abs (f(x[n])) <= epsilon) :
        c = x[n] - ( f(x[n]) / df(x[n]) )
        #c = float ('%.4f'% c)
        x.append(c)
        n += 1
    print ('x :', x)
    #print ('x_n :','%.4f'% x[-1])
    return x[-1] 

print (Newton_Raphson(1,0.0001))