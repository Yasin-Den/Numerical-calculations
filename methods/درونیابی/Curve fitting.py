import numpy as np
#برازش با تابع چند جمله ای
#f(x) = a0 + a1*x + a2*x**2 + ... + an*x**n
n = 1

#---------------------
dictionery = {-2: 2, 0: 1, 1.0: 2, 2: 2}
#or
x = []
y = []
#---------------------
if len(x) == 0 and len(y) == 0 :
    for i in dictionery :
        x.append(i)
        y.append(dictionery[i])

def sigma_x(n) :
    sigma = []
    for i in x :
        sigma.append(i**n)
    return sum(sigma)

def sigma_xy(n) :
    sigma_x = []
    sigma_xy = []
    for i in x :
        sigma_x.append(i**n)
    i = 0
    while i+1 <= len(y) :
        sigma_xy.append(y[i]*sigma_x[i])    
        i += 1
    return sum(sigma_xy)

def A() :
    a = []
    i = 0
    q = 0
    while i <= n : 
        radif = []
        j = q
        z = q + n
        while j <= z :
            if j == 0 :
                radif.append(len(x))
            else :
                radif.append(sigma_x(j))
            j += 1
        a.append(radif)
        q += 1
        i += 1
    A = np.array(a)
    return (A)

def B() :
    b = []
    for i in range(n+1) :
        b.append([sigma_xy(i)])
    B = np.array(b)
    return (B)

#x = (A**-1)*B
print (np.linalg.inv(A()).dot(B()))
#a0
#a1
#a2
#a3
#...