from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import math as mh

def f1(t,y,a,c,d):
    return [y[1],a*(c*mh.cos(t*2)-mh.sin(y[1]))]
a=2 #Q
#b=2/3 #w^
c=[0.5,0.5,1.35] #A
d=0 #Q*
y0=[[0,0.01],[0,0.3],[0,0.3]] #Q0


for i in range(0,3):
    wyn=solve_ivp(lambda t,Q:f1(t,Q,a,c[i],d),[0,50],y0[i])
    #print(wyn.t)
    #print(wyn.y[0])
    #print(wyn.y[1])
    plt.subplot(2,1,1)
    plt.plot(wyn.t,wyn.y[0],'o',label='y')
 #   plt.plot(wyn.t,wyn.y[1],'o',label="y'")
    plt.xlabel('t')
    plt.ylabel("y")
    plt.legend()
    plt.grid()
    plt.title("θ(t)-%d condition" %(i+1),loc='center')
    
    plt.subplot(2,1,2)
    plt.plot(wyn.t,wyn.y[0],label='y')
    plt.plot(wyn.t,wyn.y[1],label="y'")
    plt.xlabel('t')
    plt.ylabel("y,y'")
    plt.legend()
    plt.grid()
    plt.title("Trajectory")
    plt.xlim(y0[i])
    
    plt.show()
