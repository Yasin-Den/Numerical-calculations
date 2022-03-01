'''روش نقطه ثابت'''
#Shart1 : g(x) peyvaste bashad
#Shart2 : a1 <= g(x)[bord tabea] <= a2
#Shart3 : g(x) moshtagh pazir bashad
#Shart4 : |dg(x)| <= k < 1

from math import cos ,sin

def f(x) :
    return -0.25-x+0.5*sin(x)+cos(0.5*x)


def g(x) :
    return 0.5*cos(x)-0.5*sin(0.5*x)

#argham aashar
ragham_aashar = 6

def constant_point_method(a1,b1,x0,ragham_aashar) :
    a = [x0]
    b = []
    
    i = 0
    while i <= 10000 :
        y = g(a[i])
        b.append(y)
        a.append(y)
        if a[i] == b[i] or i == ragham_aashar :
            y = i
            break
        i += 1
    print ('a :', a)
    print ('b :', b)
    return b[-1]

print (constant_point_method(-2,2,-0.6,ragham_aashar))
