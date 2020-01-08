# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 20:52:15 2019

@author: mateu
"""
import numpy as np


def gauss(A,b):
    #funkcja hstack laczy dwie macierze horyzontalnie
    #funkcja reshape ustawia kształt tablicy zgodnie z parametrami(rzad,kolumna)
    Ab = np.hstack([A,b.reshape(-1,1)])
    print(Ab,"\n\n")
    n = len(b) #ilosc elementow macierzy b

    for i in range(n):
        a = Ab[i]
        
        for j in range(i+1,n):
            b=Ab[j]
            m = a[i]/b[i]
            print(a[i],"/",b[i],"=",m)
            print(a,b)
            Ab[j]=a-m*b
            print(Ab,"\n\n")
       
    for i in range(n-1,-1,-1):
        Ab[i]=Ab[i]/Ab[i,i]
        a=Ab[i]
        
        for j in range(i-1,-1,-1):
            b=Ab[j]

            m=a[i]/b[i]
            print(a[i],"/",b[i],"=",m)
            print(a,b)
            Ab[j]=a-m*b
            print(Ab,"\n\n")
    print(Ab)        
    x=Ab[:,3]
    print(x)

A = np.array([[8, -6, 2], [-4,11,-7], [4,-7,6]], dtype='float')
b = np.array([28,-40,33])

#A = np.array([[-1,1,-4], [2,2,0], [3,3,2]], dtype='float')
#b = np.array([0,1,1/2])
    
#A = np.array([[2,-3,-1], [3,2,-5], [1,4,-1]], dtype='float')
#b = np.array([1,-1,2])

#A = np.array([[0,0,2,1,2], [0,1,0,2,-1], [1,2,0,-2,0],[0,0,0,-1,1],[0,1,-1,1,-1]], dtype='float')
#b = np.array([1,1,-4.-2.-1])
"""
A=np.array([[1,0,0**2,0**3,0**4],
            [1,1,1**2,1**3,1**4],
            [1,3,3**2,3**3,3**4],
            [1,5,5**2,5**3,5**4],
            [1,6,6**2,6**3,6**4]],dtype='float')
b=np.array([-1,1,3,2,-2])
"""
gauss(A,b)


