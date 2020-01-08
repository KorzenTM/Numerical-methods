# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 09:15:46 2019

@author: mateu
"""

#obliczanie elementow ciagu
import matplotlib.pyplot as plt
import numpy as np

x_n=0.1
li=[0.1]

for n in range(1,101):
    f=3.5*x_n*(1-x_n)
    li.append(f)
#    print(li[n])
    x_n=f
    
print(li)
#rysowanie wykresu
x=np.arange(1,102,1)
plt.scatter(x,li, c='r')
plt.xlabel('n')
plt.ylabel('x_n')
plt.grid(True)
plt.show
