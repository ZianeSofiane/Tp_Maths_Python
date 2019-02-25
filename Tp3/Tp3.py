from math import pi
import numpy as np
from numpy import tan
import matplotlib.pyplot as plt

def zeropardicho(f,a,b,eps,nitermax):
    m = (a+b)/2
    niter=0
    while(abs(f(m))>eps and niter!=nitermax):
        m = (a+b)/2
        if(f(a)*f(m) > 0):
            a=m
        else:
            b=m
        niter = niter+1
    return [m,niter]

x = np.linspace(0.1, (pi/2)-0.1 , 100)
x2 = np.linspace(pi, 3*(pi/2)-0.1 , 100)
x3 = np.linspace(2*pi, 5*(pi/2)-0.1 , 100)

y = tan(x)
y2 = x**(-1)
plt.figure(1)
plt.plot(x,y)
plt.plot(x,y2)
y = tan(x2)
y2 = x2**(-1)
plt.plot(x2,y)
plt.plot(x2,y2)
y = tan(x3)
y2 = x3**(-1)
plt.plot(x3,y)
plt.plot(x3,y2)
plt.show()
    
def f1(x):
    return (x*tan(x)-1)
    
print(zeropardicho(f1,0.8,1,10**(-8),100))
print(zeropardicho(f1,3.4,3.6,10**(-8),100))
print(zeropardicho(f1,6.4,6.6,10**(-8),100))

for i in range(2,10,1):
    print()
    print(zeropardicho(f1,0.8,1,10**(-i),1000))
    print(zeropardicho(f1,3.4,3.6,10**(-i),1000))
    print(zeropardicho(f1,6.4,6.6,10**(-i),1000))
