'''BisectionMethod'''
'''روش نصف کردن'''
#Shart 1 : f(x) peyvaste ast (shart kafi)
#Baghiye sharayet dar code ejra mishavad

from math import sin, cos

def f(x) :
    return -0.25-x+0.5*sin(x)+cos(0.5*x)


def Bisection_Method (a0,b0,epsilon) :
    a = [a0]
    b = [b0]

    if f(a0) < 0 :
        manfi = a
        mosbat = b
    elif f(b0) < 0 :
        manfi = b
        mosbat = a

    while not (abs(f((a[-1] + b[-1])/2)) <= epsilon) :
        c = (a[-1] + b[-1])/2
        #c =float('%.4f'% c )
        #append
        if f(c) < 0 :
            manfi.append(c)
        elif f(c) > 0 :
            mosbat.append(c)
    print ('a :', a)
    print ('b :', b)
    #ragam ashar
    if f(a0)*f(b0) < 0 :
        return ('%.4f'% c) #c

print (Bisection_Method(-1, 4, 0.0005))
