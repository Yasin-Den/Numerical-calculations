'''درونیابی با تابع چند جمله ای'''
#f(x) = a0 + a1*x + a2*x**2 + ... + aN*x**N

import numpy as np

dictionery = {-2: 2, 0: 1, 1.0: 2, 2: 2}

x = []
y = []
if len(x) == 0 and len(y) == 0 :
    for i in dictionery :
        x.append(i)
        y.append(dictionery[i])

def zarb(x, y) :
    a = []
    for i in x :
        radif = []
        for j in range(len(x)) :
            radif.append(i**j)
        a.append(radif)
    A = np.array(a)
    #print (A)

    b = []
    for i in y :
        b.append([i])
    B = np.array(b)
    #print (B)

    makoos_A = np.linalg.inv(A)

    return (makoos_A.dot(B))

print (zarb(x, y))
#a0 = 
#a1 = 
#a2 = 
#a3 = 
#a4 = 
#...