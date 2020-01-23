import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy import optimize
import math as mh
import numpy as np

def fur1(t,y):
    return(y[1],-mh.sin(y[0])-1)

y_a=0
t_k=mh.pi
y_b=0

def g(u):
    y0=[y_a,u]
    woh=solve_ivp(fur1,[0,t_k],y0,atol=1e-10,rtol=1e-8)
    return woh.y[0,-1]-y_b

vg=np.vectorize(g)
zu=np.arange(-mh.pi,mh.pi,0.1)
plt.plot(zu,vg(zu))
plt.axhline(y=0,color='k')
plt.xlabel('u')
plt.ylabel('g')
plt.show()

u0=2.0
u_p=optimize.newton(g,u0,tol=1e-12,maxiter=150)
print('u_p=',u_p,'g(u_p)=',g(u_p))
y0=[y_a,u_p]
wms1=solve_ivp(fur1,[0,t_k],y0,atol=1e-10,rtol=1e-8)
plt.rcParams.update({'font.size': 16})
fig,ax1=plt.subplots(figsize=(12, 6))

ax1.plot(wms1.t,wms1.y[0],linewidth=4,label='y(t)')
ax1.plot(wms1.t,wms1.y[1],linewidth=4,label="y'(t)")
ax1.plot([0,t_k],[y_a,y_b],'o',label='war. brzeg.')
ax1.set_xlabel('t')
ax1.set_ylabel('y')
ax1.legend()
plt.show()