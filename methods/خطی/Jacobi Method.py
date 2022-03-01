'''روش تکراری ژاکوبی'''
#|A| =! 0

x1=[0]
x2=[0]
#x3=[0]

epsilon = 0.0001

k=0

def iif(k,epsilon) :
    list_of_si = []
    if not(abs(x1[k]-x1[k-1]) <= epsilon) :
        list_of_si.append(False)
    elif not(abs(x2[k]-x2[k-1]) <= epsilon) :
        list_of_si.append(False)
    #elif not(abs(x3[k]-x3[k-1]) <= epsilon) :
     #   list_of_si.append(False)
    if k>1 :
        if False in list_of_si :
            return False
        else :
            return True
    

while not(iif(k,epsilon)) :
    x1.append(1-2*x2[k])
    x2.append((3+2*10**(-15)-3*x1[k])/(6+2*10**(-15)))
    #x3.append((18+x1[k]-x2[k])/10)
    k+=1

print ('x1 :',x1)
print ('x2 :',x2)
#print ('x3 :',x3)

print ('x1[k+1]-x1[k] :',abs(x1[k]-x1[k-1]))
print ('x2[k+1]-x2[k] :',abs(x2[k]-x2[k-1]))
#print ('x3[k+1]-x3[k] :',abs(x3[k]-x3[k-1]))