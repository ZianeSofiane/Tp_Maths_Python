from math import log

def f(x):
    return (1/(1+x))
    
print(f(1))
    
def rectg(a,b,g,n):
    h=((b-a)/n)
    res=0
    for i in range(n):
        res = res + h*f(a+i*h)
    return res
    
def rectd(a,b,g,n):
    h=((b-a)/n)
    res=0
    for i in range(1,n+1,1):
        res = res + h*f(a+i*h)
    return res

def milieu(a,b,g,n):
    h=((b-a)/n)
    res=0
    for i in range(n):
        res = res + h*f((a+h/2) + i*h)
    return res

def trapeze(a,b,g,n):
    h=((b-a)/n)
    res= (h/2)*(g(a)+g(b))
    for i in range(1,n,1):
        res = res + (h/2)*(2*f(a+i*h))
    return res

def simpson(a,b,g,n):
    h=((b-a)/n)
    res = (h/6)*(g(a)+g(b)) + (h/6)*(4*f((a+h/2)))
    for i in range(1,n,1):
        res = res + (h/6)*( (2*f(a+i*h)) + (4*f((a+h/2)+i*h)) )
    return res

def deterRectg(a,b,g):
    i=1
    while (abs((log(2)-rectg(a,b,g,i))) >= 0.00001):
        i=i+1
    return i

def deterRectd(a,b,g):
    i=1
    while (abs((log(2)-rectg(a,b,g,i))) >= 0.00001):
        i=i+1
    return i

def deterRectm(a,b,g):
    i=1
    while (abs((log(2)-rectg(a,b,g,i))) >= 0.00001):
        i=i+1
    return i
    
def deterTrapeze(a,b,g):
    i=1
    while (abs((log(2)-rectg(a,b,g,i))) >= 0.00001):
        i=i+1
    return i

def deterSimpson(a,b,g):
    i=1
    while (abs((log(2)-rectg(a,b,g,i))) >= 0.00001):
        i=i+1
    return i

print(log(2))
print(rectg(0,1,f,100))
print(rectd(0,1,f,100))
print(milieu(0,1,f,100))
print(trapeze(0,1,f,100))
print(simpson(0,1,f,100))

print(deterRectg(0,1,f))
        