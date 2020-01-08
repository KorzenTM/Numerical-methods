# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 13:05:27 2019

@author: mateu
"""
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize


def f_1(x,y):
    return x+np.exp(-x)+y**3
def f_2(x,y):
    return x**2+2*x*y-y**2+np.tan(x)
def fdz(x):
     return (x[0]+np.exp(-x[0])+x[1]**3,
     x[0]**2+2*x[0]*x[1]-x[1]**2+np.tan(x[0]))
"""
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
u = np.linspace(0, 2 * np.pi)
v = np.linspace(0, np.pi)
u1 = np.linspace(-2*np.pi, 2 * np.pi)
v1 = np.linspace(-2*np.pi, 2*np.pi)
x1 =np.outer(np.cos(u1), np.sin(v1))
y1 =np.outer(np.sin(u1), np.sin(v1))
x = 2 * np.outer(np.cos(u), np.sin(v))
y = 2 * np.outer(np.sin(u), np.sin(v))
z = 2 * np.outer(np.ones(np.size(u)), np.cos(v))
Z1=x1+np.exp(-x1)+y1**3
Z2=x1**2+2*x1*y1-y1**2+np.tan(x1)
ax.plot_wireframe(x1,y1,Z1,color='r')
ax.plot_wireframe(x1,y1,Z2,color='g')
ax.plot_wireframe(x, y, z, color='b')
ax.set_xlim3d(-2,2)
ax.set_ylim3d(-2,2)
ax.set_zlim3d(-2,2)
"""

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

angle=np.arange(-(np.pi),np.pi,0.01)
x=2*np.cos(angle)
y=2*np.sin(angle)
sol=[]

for i in np.arange(-2,2,0.1):
    for j in np.arange(-2,2,0.1):
        r=optimize.root(fdz,[j,i])
        if r.success and i**2+j**2<=2:
           if not ([round(r.x[0], 2), round(r.x[1], 2)] in sol):
                sol.append([round(r.x[0], 2), round(r.x[1], 2)])
print(sol)

    



