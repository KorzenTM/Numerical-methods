# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 09:19:36 2019

@author: mateu
"""

#Metoda Riddera

import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

def f(x):
    return 2*x**4+24*x**3+61*x**2-16*x+1



d=0.001
a=-8.5
b=0.5

for b in np.arange(-9,1,d):
    if np.sign(f(a))!=np.sign(f(b)):
        prw=optimize.ridder(f,a,b,full_output=True)
        print("%4d   %19.16f" %(prw[1].iterations,prw[0]))
    a=b
xt=np.arange(-10.0,5.0,0.01)
plt.xlim(-9.0,3.0)
plt.ylim(-400.0,200.0)
plt.plot(xt,f(xt))
plt.axhline(y=0,color='red')
plt.xlabel('x')
plt.ylabel('f')

plt.show()