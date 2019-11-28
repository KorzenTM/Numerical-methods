# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 10:02:47 2019

@author: mateu
"""

#obliczanie całek z wykorzystaniem rekurencji

import numpy as np
from scipy.integrate import quad

def fpodcalk(x,n):
    return x**n*np.exp(x)
y=1
for n in range(2,21):
    y=np.e-(n+1)*y
    I=quad(fpodcalk,0,1,args=(n))
    print(" %2d   %20.10f" %(n,y-I[0]))
    
y=np.e/100
n=99

"""
while n>0:
    y=np.e-n*y
    n=n-1
    if n<99:
        I=I=quad(fpodcalk,0,1,args=(n))
        print(" %2d  %10.5f  %10.6e" %(n,y,y-I[0]))
 """