from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import math as mh

def f1(t,y):
    return mh.sin(t*y)

y=[2,2.5,3,3.5]
j=1
for i in range(4):
    y0=[y[i]]
    wyn=solve_ivp(f1,[0,6],y0)
    print("t=",wyn.t)
    print("\ny=",wyn.y[0])
    plt.subplot(2,2,j)
    plt.plot(wyn.t,wyn.y[0],'o')
    plt.xlabel('t')
    plt.ylabel('y')
    plt.title("y(0)=%.1f" %(y[i]),loc='center')
    j+=1
plt.show()