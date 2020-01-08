#Rzut ukosny z zaniedbaniem powietrza
from scipy.integrate import solve_ivp
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math as mh
import numpy as np

vx=10
vy=10
g=9.81
def f(y,t):
    return [y[2],y[3],0,-g]

y0=[0,0,vx,vy]
t=np.arange(0,((2*y0[3])/(g)),0.1)
sol=odeint(f,y0,t)
#print(sol[:,1:2])
plt.plot(sol[:,0:1],sol[:,1:2],'ro')
plt.show()




