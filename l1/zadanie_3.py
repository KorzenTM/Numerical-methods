# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 09:56:50 2019

@author: mateu
"""

#dzialania na macierzach i wektorach

import numpy as np
from scipy import linalg
#zdefiniowanie macierzy
A=np.array([[4,-2,1],[-2,4,-2],[1,-2,4]])
B=np.array([[4,2,0],[2,5,2],[0,2,4]])
w=np.array([1,-2,3])

print("Macierz A:\n")
print(A)
print("Macierz B:\n")
print(B)
print("Wektor w:\n")
print(w)
#dzialania
print("A*B=\n",np.dot(A,B))
print("A*w=\n",np.dot(A,w))
print("det(A)=",linalg.det(A))
print("det(B)=",linalg.det(B))
print("inv(A):\n",linalg.inv(A))
print("inv(B):\n",linalg.inv(B))