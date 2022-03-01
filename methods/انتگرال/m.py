
def f(x) :
    return x


def pishro(x, h, z) :
    return (f(x+h) - f(x)) / h

def pasro(x, h) :
    return (f(x) - f(x-h)) / h

def pishro(x, h) :
    return (f(x+h) - f(x-h)) / 2*h

