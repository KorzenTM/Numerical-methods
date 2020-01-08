# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 09:10:53 2019

@author: mateu
"""
#rozwiazywanie rownania Ax=b
import numpy as np

A=[[0,0,2,1,2],[0,1,0,2,-1],[1,2,0,-2,0],[0,0,0,-1,1],[0,1,-1,1,-1]]
b=[[1],[1],[-4],[-2],[-1]]
x=np.linalg.solve(A,b) #funkcja rozwiazujaca rowniania macierzowe
print(x)

check=np.allclose(np.dot(A,x),b) #sprawdzenie czy wynik jest prawidłowy
print("Sprawdzenie wyniku:",check)