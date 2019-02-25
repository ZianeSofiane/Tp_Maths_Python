### Author : BETOURNE Aurélien, ZIANE Sofiane // Tp1_Interpolation polynomiale ###

import numpy as np
from numpy import sqrt  # importation fonction racine carré (sqrt)

import matplotlib.pyplot as plt # import fonctions de graphes

from math import cos # import cosinus
from math import pi  # import 3.14....
from math import sin # import sinus

##
## EXERCICE N°1 ##

# Polynôme d'interpolation de Lagrange vérifiant les points donnés
def foncP(x):
    return ( 2*(sqrt(2)-sqrt(6)+1)*(x**2) + (-sqrt(2) - 3 + 2*sqrt(6))*x + 1 )

# fonction f(x) = racine de (1+x) #
def foncF(x):
    i=0
    res=0
    while i != x:
        i=i+1
        res=res+i
    return res

#def foncF(x):
#    return foncF2(x)
N= 10


vectabs = np.linspace(0 , 10 , N+10) # tableau des j/N avec j de 0 à N
vectord = foncF(vectabs) # tableau des images de f des vectabs
vectord2 = foncP(vectabs) # tableau des images de P des vectabs
vecp = np.array([0.0 , 0.5 , 1.0]) # tableau des points donnés

plt.figure(1) # création d'une figure
# traçage graphe de la fonction f, vectabs en abcisse, ses images en ordonnée
plt.plot(vectabs,foncF(vectabs()), '-' , color = 'green')
# traçage sur le même graphe du polynôme P, vectabs en abcisse, ses images en ordonnée
plt.plot(vectabs,foncP(vectabs), '-' , color = 'blue')

plt.figure(2) # nouvelle figure
# graphe différence f(x) - P(x)
plt.plot(vectabs, vectord-vectord2)

plt.show()  # faire apparaitre les graphes


##
## EXERCICE N°2 ##


## a)

# renvoie tab des différences divisés
def diffdiv(xp,yp):
    n=np.size(xp)
    dd=yp.copy()
    for i in range(n):
        for j in range(n-1,i,-1):
            dd[j]=(dd[j]-dd[j-1])/(xp[j]-xp[j-i-1])
    return dd

## b)

# Calcul de (x-X[0])(x-X[1])...(x-X[n])
def horner(X,x,n):
    res = 1
    for i in range(n):
        res = res*(x-X[i])
    return res

# Calcul valeur du polynome pour un x donné
def poly(dd,X,x):
    res = X[0]
    for i in range(0,len(dd)):
        res=res+(dd[i]*horner(X,x,i))
    return res

# Calcul tableau des polynomes pour un tableau de x
def myhorner(dd,xp,x):
    n=np.size(x)
    tab=x.copy()
    for i in range(n):
        tab[i]=poly(dd,xp,x[i])
    return tab

## c)

# Calcul tableau des points équirépartis
def ptsEqui(a,b,n):
    vectabs = np.linspace(a , b , n)
    for i in range(n-1):
        vectabs[i]= a + ((i-1)-1)*(b-a)/(n-1)
    return vectabs

# Calcul tableau des points de Tchebychev
def ptsTchebychev(a,b,n):
    vectabs = np.linspace(a , b , n)
    for i in range(n-1):
        vectabs[i]= ((a+b)/2) + ((b-a)/2)*cos(((2*(i-1))-1)*(pi/2*n))
    return vectabs

# Création graph avec les deux méthodes
def comparaison(f,a,b,n):
    plt.figure(3)
    plt.plot(ptsEqui(a,b,n),myhorner(diffdiv(ptsEqui(a,b,n),f(ptsEqui(a,b,n))),ptsEqui(a,b,n),ptsEqui(a,b,n)), '-' , color = 'green')
    plt.plot(ptsTchebychev(a,b,n),myhorner(diffdiv(ptsEqui(a,b,n),f(ptsTchebychev(a,b,n))),ptsTchebychev(a,b,n),ptsTchebychev(a,b,n)), '-' , color = 'blue')
    plt.show()

## d) e)

def f1(x): # fonction d)
    res = 1/(1+x**2)
    return res
    
def f2(x): # fonction e)
    res = 2*pi*x
    return res

comparaison(f1,-5,5,25)
comparaison(f2,-2,2,5)
    
