# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 09:17:27 2019

@author: mateu
"""

#rownowazne matematycznie rownania
import numpy as np

def u_1(x):
    return np.sqrt(np.float32(x**2+1))-1

def u_2(x):
    return x**2/(np.sqrt(np.float32(x**2+1))+1)

print("%4s  %16s  %16s"%('x','u1','u2'))
for n in range(2,26,2):
    x=2**(-n)
#    print(n,"\t",x)
    print("%3.1e  %16.12e  %16.12e" %(x,u_1(x),u_2(x)))

