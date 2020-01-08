from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import math as mh

def f1(t,y):
    return mh.sin(t*y)

y=[2,2.5,3,3.5]
for i in y:
    y0=[i]
    wyn=solve_ivp(f1,[0,6],y0)
    print("t=",wyn.t)
    print("\ny=",wyn.y[0])
    plt.rcParams.update({'font.size':22})
    fig,ax1=plt.subplots(figsize=(12,6))
    ax1.plot(wyn.t,wyn.y[0],'o')
    ax1.set_xlabel('t')
    ax1.set_ylabel('y')
    plt.title("y(0)=%.1f" %(i),loc='center')
    plt.show()