# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 13:05:27 2019

@author: mateu
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize


def f_1(x,y):
    return x+np.exp(-x)+y**3
def f_2(x,y):
    return x**2+2*x*y-y**2+np.tan(x)

x=np.linspace(-2,2,100)
y=np.linspace(-2,2,100)
X, Y=np.meshgrid(x,y)
F=X**2+Y**2-4.0
fig, ax=plt.subplots()
ax.contour(X,Y,F,[0])
ax.set_aspect(1)
plt.xlim(-5,5)
plt.ylim(-5,5)
plt.plot(x,f_1(x,y),x,f_2(x,y))
plt.grid()
plt.show()

fun = lambda x: x[0]+np.e**-x[0]+x[1]**3
fun_2 = lambda x: x[0]**2+2*x[0]*x[1]-x[1]**2+np.tan(x[0])
cons = ({'type':'ineq','fun':lambda x: x[0]**2+x[1]**2-4.0})
bnds=((-2,2),(-2,2))
res_1 = optimize.minimize(fun,(1,1),method='SLSQP',bounds=bnds,constraints=cons)
res_2 = optimize.minimize(fun_2,(1,1),method='SLSQP',bounds=bnds,constraints=cons)
print(res_1)
print(res_2)

    



