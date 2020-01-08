# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 09:21:47 2019

@author: mateu
"""
#wyznaczanie współczynniku wielomianu

import numpy as np
A=np.array([[1,0,0**2,0**3,0**4],
            [1,1,1**2,1**3,1**4],
            [1,3,3**2,3**3,3**4],
            [1,5,5**2,5**3,5**4],
            [1,6,6**2,6**3,6**4]])
b=np.array([-1,1,3,2,-2])
x=np.linalg.solve(A,b)
print("x=",x)

check=np.allclose(np.dot(A,x),b) #sprawdzenie czy wynik jest prawidłowy
print("Sprawdzenie wyniku:",check)