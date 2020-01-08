#Rzut ukosny z zaniedbaniem powietrza
from scipy.integrate import solve_ivp
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math as mh
import numpy as np

n=200
x0,y0=0,0
vx0,vy0= 50,50
g=9.81
cw=0.35
p=1.2
A=10
dt = 2.1/n
plt.plot(x0,y0,'ro')
for i in range(n):
     x1 = x0 + vx0*dt
     y1 = y0 + vy0*dt
     vx1  = vx0-((cw*p*A*mh.sqrt(vx0**2+vy0**2)*dt)/(2))
     vy1  = vy0 -((cw*p*A*mh.sqrt(vx0**2+vy0**2)*dt)/(2)-g)
     if y1<0:
          break
     x0,y0,vx0,vy0 = x1,y1,vx1,vy1
     plt.plot(x1,y1,'ro')
     
plt.show()




