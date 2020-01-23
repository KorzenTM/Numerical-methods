#Trajectory 
import numpy as np  
from scipy import optimize
import matplotlib.pyplot as plt


g = 9.81
akon = 45
xk = 10



def uklad(arr): #arr[0] = start velocity, arr[1] = angle
    t = 10/(arr[0]*np.cos(arr[1]))    
    return [arr[0]*np.sin(arr[1])*t-g/2*t**2-1,\
            arr[0]*(np.sin(arr[1])+np.cos(arr[1]))-g*t] 

x0 = np.array([15,np.pi/8]) #start angle 

z= optimize.root(uklad,x0)
if z.success:
    print(z.x[0], '            kat:', z.x[1]*180/np.pi)
    vo = z.x[0]
    kat = z.x[1]
t = xk/(vo*np.cos(kat))
print(t)

#def x(t):
#    return vo*cos(kat)*t
def y(t):
    return 2+vo*np.sin(kat)*t-(g/2*t**2)
print(y(t))
x = np.linspace(0,t,100)
#print(y(x))
plt.plot(x,np.zeros(len(x))+3)
plt.plot(x,np.zeros(len(x))+2)
plt.plot(x,y(x))
plt.show()






